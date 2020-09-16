var btn = document.getElementById('btn'),
caja = document.getElementById('caja'),
contador=0;

    
function cambio(){
    if(contador==0){
        caja.classList.add('ocultar');
        contador=1;

    }else{
        caja.classList.remove('ocultar');
        contador=0;
    }
    }

    btn.addEventListener('click',cambio,true)
