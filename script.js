
function fazerTarefas() {
    const ra = document.getElementById("ra").value;
    const digito = document.getElementById("digito").value;
    const senha = document.getElementById("senha").value;

    if (!ra || !digito || !senha) {
        alert("Preencha todos os campos!");
        return;
    }

    alert("Iniciando a automação para RA: " + ra + "-" + digito);

    // Simulação da automação real (IA/backend deveria estar aqui)
    setTimeout(() => {
        alert("Tarefas feitas com sucesso!");
    }, 2000);
}
