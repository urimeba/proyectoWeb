function toggle(x) {
    var form = document.getElementById('form');
    var logIn = document.getElementById('logIn');
    var signUp = document.getElementById('signUp');
    if (x.innerHTML === 'Registrame') {
        // x.innerHTML = 'Iniciar sesión';
        form.classList.add('form__transition');
        logIn.classList.remove('fadeIn');
        logIn.classList.add('fadeOut');
        signUp.classList.remove('fadeOut2');
        signUp.classList.add('fadeIn2');
    } else {
        // x.innerHTML = 'Registrar';
        form.classList.remove('form__transition');
        logIn.classList.remove('fadeOut');
        logIn.classList.add('fadeIn');
        signUp.classList.remove('fadeIn2');
        signUp.classList.add('fadeOut2');
    }
}

getAddress = () => {
    var url = document.getElementById('col').dataset.url
    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            xhttp.responseText
        }
    };
    xhttp.send();
}

logIn = () => {
    var user = document.getElementById('userL').value
    var pass = document.getElementById('passL').value
    var data = {
        usuario: user,
        contraseña: pass
    }
    var url = document.getElementById('buttonLogIn').dataset.url
    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log("Hola");
        }
    };
    xhttp.send('usuario='+user);
    // let fetchData = { 
    //     method: 'POST', 
    //     body: data,
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': cookie,
    //     },
    // }

    // fetch(url, fetchData).then(function() {
    //     console.log("Entra");
    // });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
