
function login() {
    const ra = document.getElementById('ra').value;
    const digito = document.getElementById('digito').value;
    const senha = document.getElementById('senha').value;

    if (ra && digito && senha) {
        // Simulação de login com IA (sem armazenar dados)
        document.getElementById('painel').style.display = 'block';
        alert('Login feito com sucesso!');
    } else {
        alert('Preencha todos os campos.');
    }
}

function fazerTodas() {
    alert('Todas as lições foram resolvidas com sucesso!');
}

function deixarRascunho() {
    alert('Todas as tarefas foram deixadas em rascunho.');
}

function fazerSelecionada() {
    alert('A tarefa selecionada foi concluída!');
}
