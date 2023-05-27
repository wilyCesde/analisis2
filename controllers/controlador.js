let button = document.getElementById("generarReporte");

button.addEventListener("click", function (event) {
  event.preventDefault();
  let reporte = document.getElementById("reporte");
  reporte.classList.remove("d-none");

  let nameUser = document.getElementById("nameUser").value;
  let message = document.getElementById("message");

  message.textContent = `Apreciado usuario ${nameUser} el reporte generado es: `;
});