function verificar() {
    const ejecutora = document.getElementById('ejecutor');

    if (ejecutora.value === '1') {
        document.getElementById('dependencia').classList.remove('hidden');
    }
    if (ejecutora.value === 'facultad') {
        document.getElementById('facultad').classList.remove('hidden');
    }
}

function otro() {
     const dependencia = document.getElementById('Dependencia');
     if (dependencia.value === 'otro') {
            document.getElementById('otro').classList.remove('hidden');
     }else if (dependencia.value === 'opciones'){
        document.getElementById('otro').classList.add('hidden')
    }
}







