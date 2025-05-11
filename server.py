from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Roda o navegador sem abrir a interface
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Função para login
def login(ra, senha):
    driver.get("URL_DO_SALA_DO_FUTURO")  # Substitua pela URL real

    # Identificando os campos de login
    ra_field = driver.find_element(By.NAME, "ra")  # Atualizado para o nome do campo correto
    senha_field = driver.find_element(By.NAME, "senha")  # Atualizado para o nome do campo correto

    ra_field.send_keys(ra)
    senha_field.send_keys(senha)
    senha_field.send_keys(Keys.RETURN)

    time.sleep(2)  # Espera o login ser processado

    # Verificar se o login foi bem-sucedido
    if "Página de Tarefas SP" in driver.title:
        print("Login bem-sucedido!")
        return True
    else:
        print("Erro de login!")
        return False

# Função para navegar até as tarefas e resolver
def resolver_tarefas():
    # Navegar até a seção Tarefas SP
    driver.get("URL_DA_SECAO_TAREFAS_SP")  # Substitua pela URL correta

    # Loop para resolver as lições
    lições = driver.find_elements(By.CLASS_NAME, "classe_da_lição")  # Substitua pela classe certa
    for lição in lições:
        nome_licao = lição.text
        print(f"Resolvendo lição: {nome_licao}")
        lição.click()  # Clica na lição
        time.sleep(1)

        # Ação para resolver a lição (substitua conforme necessário)
        botao_resolver = driver.find_element(By.CLASS_NAME, "classe_do_botao_resolver")  # Substitua pela classe do botão
        botao_resolver.click()

        time.sleep(2)

# Função principal para executar o processo
def main(ra, senha):
    if login(ra, senha):
        resolver_tarefas()
    else:
        print("Falha no login. Verifique suas credenciais.")
    driver.quit()

# Chame a função main com as credenciais (RA e senha)
main("SEU_RA", "SUA_SENHA")
