
function mostrarToast(mensagem, tipo) {
    const toast = document.getElementById("toast");
    const msg = document.getElementById("toast-msg");
    toast.className = "toast show " + tipo;
    msg.innerText = mensagem;
    setTimeout(() => {
        toast.className = "toast " + tipo;
    }, 3200);
}

function fazerTarefas() {
    const ra = document.getElementById("ra").value;
    const digito = document.getElementById("digito").value;
    const senha = document.getElementById("senha").value;

    if (!ra || !digito || !senha) {
        mostrarToast("Preencha todos os campos!", "warning");
        return;
    }

    fetch("/fazer-tarefas", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ ra, digito, senha })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "ok") {
            mostrarToast("Login feito com sucesso!", "success");
        } else if (data.status === "sem_tarefas") {
            mostrarToast("Nenhuma tarefa SP encontrada!", "warning");
        } else {
            mostrarToast("Erro ao fazer login!", "error");
        }
    }).catch(() => {
        mostrarToast("Erro ao conectar!", "error");
    });
}
