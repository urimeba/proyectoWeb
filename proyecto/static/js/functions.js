function toggle(x) {
    var form = document.getElementById('form');
    var logIn = document.getElementById('logIn');
    var signUp = document.getElementById('signUp');
    if (x.innerHTML === 'Registrar') {
        x.innerHTML = 'Iniciar sesión';
        form.classList.add('form__transition');
        logIn.classList.remove('fadeIn');
        logIn.classList.add('fadeOut');
        signUp.classList.remove('fadeOut2');
        signUp.classList.add('fadeIn2');
    } else {
        x.innerHTML = 'Registrar';
        form.classList.remove('form__transition');
        logIn.classList.remove('fadeOut');
        logIn.classList.add('fadeIn');
        signUp.classList.remove('fadeIn2');
        signUp.classList.add('fadeOut2');
    }
}