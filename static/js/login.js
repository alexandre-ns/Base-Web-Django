function entrar() {
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;

    // Lógica de autenticação (pode ser ajustada conforme necessário)
    if (email === 'usuario@example.com' && senha === 'senha123') {
        alert('Login bem-sucedido!');
    } else {
        alert('Email ou senha incorretos. Tente novamente.');
    }
}

function entrar() {
    // Lógica para o botão entrar na página de login
    console.log('Botão Entrar clicado');
}

function redefinirSenha() {
    // Lógica para o botão redefinir senha na página de recuperação de senha
    console.log('Botão Redefinir Senha clicado');
}