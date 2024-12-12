document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('button').forEach(button => {
    button.onclick = () => {
      document.querySelector("#hello").style.color = button.dataset.color;
    }
  });
});