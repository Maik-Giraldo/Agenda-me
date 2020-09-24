var btn = document.getElementById('btn'),
caja = document.getElementById('caja'),
contador=0;

    
function cambio(){
    if(contador == 0){
        caja.classList.add('ocultar');
        contador=1;

    }else{
        caja.classList.remove('ocultar');
        contador=0;
    }
    }

    btn.addEventListener('click',cambio,true)


var btn2 = document.getElementById('btn2'),
caja2 = document.getElementById('caja2'),
contador2 = 0;
    
        
function cambio2(){
    if(contador2 == 0){
        caja2.classList.add('ocultar');
        contador2 = 1;
    
    }else{
        caja2.classList.remove('ocultar');
        contador2 = 0;
    }
    }
    
    btn2.addEventListener('click',cambio2,true)

function muestra_oculta(id){
    if (document.getElementById){ //se obtiene el id
    var el = document.getElementById(id); //se define la variable "el" igual a nuestro div
    el.style.display = (el.style.display == 'none') ? 'block' : 'none'; //damos un atributo display:none que oculta el div
    }
    }
    window.onload = function(){/*hace que se cargue la función lo que predetermina que div estará oculto hasta llamar a la función nuevamente*/
    muestra_oculta('div_flash');/* "contenido_a_mostrar" es el nombre que le dimos al DIV */
    }