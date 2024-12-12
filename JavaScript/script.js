//Aguardando a página carregar
document.addEventListener('DOMContentLoaded', function() {

  // Selecionando o input e botão a ser usado
  const submit = document.querySelector('#submit');
  const newTask = document.querySelector('#task');

  //Deixando o botão de enviar desativado
  submit.disabled = true;

  //Verificando se o campo foi preenchido para liberar o submit
  newTask.onkeyup = () => {
    if (newTask.value.length > 0) {
      submit.disabled = false;
    }
    else {
      submit.disabled = true;
    }
  }

  //Envio do forms
  document.querySelector('form').onsubmit = () => {

    //Pegando o envio do usuário
    const task = newTask.value;

    // Criando uma lista com a nova tarefa
    const li = document.createElement('li');
    li.innerHTML = task;

    //Adicionando a tarefa do usuário na nossa lista
    document.querySelector('#tasks').append(li);

    // Limpando a variável temporária
    newTask.value = '';

    // Desativando o botão de submit novamente
    submit.disabled = true;

    return false;
  }
})