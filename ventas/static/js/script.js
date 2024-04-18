let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");

btn.addEventListener('click', (e) => { 
  e.preventDefault();
  sidebar.classList.toggle('active');
});

const openModals = document.querySelectorAll('.btn-abrir');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('#btn-cerrar')


openModals.forEach(openModal => {
    openModal.addEventListener('click', () => {
        modal.classList.add('modal-open');
    });
});

if (closeModal  ){
    closeModal.addEventListener('click', () => {
        modal.classList.remove('modal-open');
    });

}




// VENTA DE ALERTA AL ELIMINAR UN REGISTRO 

// Selecciona el enlace por su ID
var enlaces = document.querySelectorAll('.enlaceDelete');


// Selecciona los botones de la ventana modal
var btnSi = document.getElementById('btnSi');
var btnNo = document.getElementById('btnNo');

// Selecciona la ventana modal
var modalDelete = document.querySelector('.modalDelete');

// Agrega un evento de clic al enlace
enlaces.forEach(enlace => {
    enlace.addEventListener('click', (e) => {
        e.preventDefault(); // Evita que el enlace siga su comportamiento predeterminado (navegar a una nueva página)
        modalDelete.style.display = 'block'; // Muestra la ventana modalDelete
        // Almacena la URL del enlace seleccionado en el botón "Sí"
        btnSi.href = enlace.href;
    
    });
});
// Agrega un evento de clic al botón "No" de la ventana modalDelete
if (btnNo){
    btnNo.addEventListener('click', function() {
        modalDelete.style.display = 'none'; // Oculta la ventana modalDelete
    });
}

// Agrega un evento de clic al botón "Sí" de la ventana modalDelete

if (btnSi){
    btnSi.addEventListener('click', function() {
        modalDelete.style.display = 'none'; // Oculta la ventana modalDelete
        window.location.href = btnSi.href; // Redirige al enlace
    });
}


// // para hacer la seleccion de porductos en la venta 

const creaSeleccion =(id)=>{
    if(id){
        new TomSelect(id,{
        	create: false,
        	sortField: {
        		field: "text",
        		direction: "asc"
        	}});
    }
    
}

const creaSeleccionInabilitada=(id)=>{
    if(id){
        new TomSelect(id);
    }
    
}

try{
    creaSeleccion('#seleccionar-producto')
    creaSeleccion('#select-metodo-venta')
    creaSeleccion('#seleccionar-producto-form2')
    creaSeleccionInabilitada('#select-codigo-fac-disabled')
    creaSeleccionInabilitada('#select-codigo-fac-venta-disabled')
    creaSeleccionInabilitada('#select-total-venta-disabled')
    creaSeleccionInabilitada('#select-codigo-fac-venta-disabled_form2')
}catch (error) {
    
}





