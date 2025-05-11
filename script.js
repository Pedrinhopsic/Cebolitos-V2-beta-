// Função para exibir notificações toast
function mostrarToast(mensagem) {
    const toast = document.createElement('div');
    toast.classList.add('toast');
    toast.innerText = mensagem;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// Simulação da resolução das tarefas e envio das notificações
function resolverTarefas() {
    const tarefas = ["Lição 1", "Lição 2", "Lição 3"]; // Exemplo de tarefas
    tarefas.forEach(tarefa => {
        // Exibe a notificação toast para cada lição
        mostrarToast(`Lição resolvida: ${tarefa}`);
    });
    // Notificação de todas as lições concluídas
    mostrarToast("Todas as lições feitas!");
}

// Chama a função para resolver as tarefas e mostrar as notificações
resolverTarefas();
