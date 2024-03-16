let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");

btn.addEventListener('click', (e) => {
  e.preventDefault();
  sidebar.classList.toggle('active');
});

const openModals = document.querySelectorAll('.btn-abrir');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('#btn-cerrar');

openModals.forEach(openModal => {
    openModal.addEventListener('click', (e) => {
        modal.classList.add('modal-open');
    });
});

closeModal.addEventListener('click', (e) => {
    modal.classList.remove('modal-open');
});

