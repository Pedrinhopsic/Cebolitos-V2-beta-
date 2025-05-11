
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    ra: str
    digito: str
    senha: str

@app.post("/fazer-tarefas")
async def fazer_tarefas(data: LoginData):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://saladofuturo.educacao.sp.gov.br/")

        # Login
        driver.find_element(By.ID, "ra").send_keys(data.ra + data.digito)
        driver.find_element(By.ID, "senha").send_keys(data.senha)
        driver.find_element(By.ID, "botaoEntrar").click()
        time.sleep(2)

        # Verifica se login deu certo (ajustar conforme o sistema real)
        if "login" in driver.current_url.lower():
            driver.quit()
            return { "status": "erro" }

        # Ir até Tarefas SP
        driver.get("https://saladofuturo.educacao.sp.gov.br/tarefasSP")
        time.sleep(2)

        tarefas = driver.find_elements(By.CLASS_NAME, "card-tarefa")
        if not tarefas:
            driver.quit()
            return { "status": "sem_tarefas" }

        for tarefa in tarefas:
            try:
                tarefa.click()
                time.sleep(1)
                botao = driver.find_element(By.XPATH, "//button[contains(text(),'Concluir')]")
                botao.click()
                time.sleep(1)
                driver.back()
                time.sleep(1)
            except:
                continue

        driver.quit()
        return { "status": "ok" }

    except Exception as e:
        print(e)
        return { "status": "erro" }
