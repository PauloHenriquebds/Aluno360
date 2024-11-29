// Exemplo de script para adicionar um evento de clique aos botões
const buttons = document.querySelectorAll('.buttons button');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Aqui você pode adicionar a lógica para cada botão
        console.log('Botão clicado:', button.textContent);
    });
});

function setPlaceholder(type) {
  const inputField = document.getElementById('input-field');
  const formTitle = document.getElementById('form-title');

  if (type === 'turma') {
    inputField.placeholder = 'Digite o nome da turma';
    formTitle.textContent = 'Escreva o nome da turma';
  } else {
    inputField.placeholder = 'Digite o nome do aluno';
    formTitle.textContent = 'Escreva o nome do aluno';
  }
}
