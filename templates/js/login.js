document.getElementById('loginButton').addEventListener('click', function () {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Simples validação para testar preenchimento
  if (username === '' || password === '') {
    alert('Por favor, preencha todos os campos!');
    return;
  }

  // Simula o login e redireciona para a página inicial
  window.location.href = 'principal.html';  // Redireciona para a página principal
});
