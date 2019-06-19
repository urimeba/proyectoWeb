document.addEventListener('DOMContentLoaded', function () {
    if (!Notification) {
        alert('Desktop notifications not available in your browser. Try Chromium.'); 
        return;
    }
  
    if (Notification.permission !== 'granted'){
        Notification.requestPermission();
    }
});

// CAMBIANDO LOS BOTONES A ACTIVE
function cambiandoBotones()
{
    // Get the container element
    var btnContainer = document.getElementById("Derechita");

    // Get all buttons with class="btn" inside the container
    var btns = btnContainer.getElementsByClassName("Categoria");

    // Loop through the buttons and add the active class to the current/clicked button
    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
        });
    }
}


//MANERA DE ENVIAR UN JSON A TRAVES DE AJAX
logIn = () => {
    var user = document.getElementById('userL').value;
    var pass = document.getElementById('passL').value;
    if(user != "" && pass != ""){
        var data = {}
        data['usuario'] = user;
        data['contraseña'] = pass;
        var url = document.getElementById('buttonLogIn').dataset.url;
        var xhttp = new XMLHttpRequest();
        var cookie = getCookie('csrftoken');
        xhttp.open('POST', url, true);
        xhttp.setRequestHeader('X-CSRFToken', cookie);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                console.log(xhttp.responseText)
                if(xhttp.responseText=="True") {
                    alert("Sesion iniciada correctamente");
                    window.location.href="Categorias/obtenerCategorias";
                } else {
                    alert("Favor de verificar tus datos")
                }
                
            }
        };
        datos = "json_name=" + JSON.stringify(data);
        xhttp.send(datos);
    }else{
        alert("No podemos identificarte si no escribes tu usuario y contraseña");
    }
}

signUp = () => {
    var user = document.getElementById('userS').value;
    var name = document.getElementById('nameS').value;
    var last = document.getElementById('lastS').value;
    var mail = document.getElementById('mailS').value;
    var pass = document.getElementById('passS').value;
    var cpass = document.getElementById('cpassS').value;
    var address = document.getElementById('address').value;
    if(user != "" && name != "" && last != "" && pass != "" && cpass != "" && address != "" && mail != ""){
        if(pass.length >= 5){
            if(pass == cpass){
                if(address != 0){
                    var data = {}
                    data['usuario'] = user;
                    data['nombre'] = name;
                    data['apellido'] = last;
                    data['contraseña'] = pass;
                    data['colonia'] = address;
                    data['correo'] = mail;
                    var url = document.getElementById('buttonSignUp').dataset.url;
                    var xhttp = new XMLHttpRequest();
                    var cookie = getCookie('csrftoken');
                    xhttp.open('POST', url, true);
                    xhttp.setRequestHeader('X-CSRFToken', cookie);
                    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    xhttp.onreadystatechange = () => {
                        if (xhttp.readyState == 4 && xhttp.status == 200) {
                            // console.log(xhttp.responseText);
                            // alert(xhttp.responseText);
                            setTimeout(() => {
                                if (Notification.permission !== 'granted'){
                                    Notification.requestPermission();
                                } else {
                                    var notification = new Notification('Bienvenido a nuestra comunidad', {
                                        icon: '/static/img/logo.png',
                                        body: "Registro exitoso",
                                    });
                                    toggle(document.getElementById('reg'));
                                }
                            }, 1000);
                        }
                    };
                    datos = "json_name=" + JSON.stringify(data);
                    xhttp.send(datos);
                }else{
                    alert("Debe escoger una colonia");
                }
            }else{
                alert("Las contraseñas no coinciden");
            }
        }else{
            alert("La contraseña debe de tener mas de 5 caracteres");
        }
    }else{
        alert("No puede haber campos vacios");
    }
}

toggle = (x) => {
    var form = document.getElementById('form');
    var logIn = document.getElementById('logIn');
    var signUp = document.getElementById('signUp');
    if (x.innerHTML === 'Regístrame') {
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
    var addresses = 0;
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            addresses = xhttp.responseText;
            showAddress(addresses);
        }
    };
    xhttp.send();
}

showAddress = (x) => {
    var a = JSON.parse(x);
    var select = document.getElementById('address');
    for(var i = 0; i < a.colonias.length; i++){
        var option = document.createElement('option');
        option.value = a.colonias[i];
        option.innerHTML = a.colonias[i];
        select.appendChild(option);
    }
}

getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

key = (x) => {
    x.value = x.value.replace(" ", "");
}

post = () => {
    var p = 0;
    var padre = document.getElementById('AbajoB');
    var tarjeta = document.createElement('div');
    tarjeta.classList.add('Tarjeta');

    var info = document.createElement('div');
    info.classList.add('info');
    var info2 = document.createElement('div');
    info2.classList.add('info2');
    p = document.createElement('p');
    p.innerHTML = "info";
    info2.appendChild(p);
    var fecha = document.createElement('div');
    fecha.classList.add('fecha');
    p = document.createElement('p');
    p.innerHTML = "fecha";
    fecha.appendChild(p);
    info.appendChild(info2);
    info.appendChild(fecha);

    var titulo = document.createElement('div');
    titulo.classList.add('titulo');
    p = document.createElement('p');
    p.innerHTML = "Titulo";
    titulo.appendChild(p);

    var contenido = document.createElement('div');
    contenido.classList.add('contenido');
    p = document.createElement('p');
    p.innerHTML = "contenido";
    contenido.appendChild(p);

    tarjeta.appendChild(info);
    tarjeta.appendChild(titulo);
    tarjeta.appendChild(contenido);

    padre.appendChild(tarjeta);
}

obtenerPublicaciones = (id, url) => {
    var id = id;
    var url = document.getElementById('cate').dataset.url;

    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = () => {  
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            // console.log(xhttp.responseText)
            document.getElementById("AbajoB").innerHTML = xhttp.responseText;
        }
    };
    datos = "json_name=" + JSON.stringify(id);
    xhttp.send(datos);
}


obtenerPublicacion = (id) => {
    var id = id;
    var url = document.getElementById(id).dataset.url;

    // console.log(id,u)

    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = () => {  
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            // console.log(xhttp.responseText)
            document.getElementById("AbajoB").innerHTML = xhttp.responseText;
        }
    };
    datos = "json_name=" + JSON.stringify(id);
    xhttp.send(datos);
}

comment = () => {
    var comment = document.getElementById('comment').value;
    var padre = document.getElementById('comentarios');  
    if(comment){
        var div1 = document.createElement('div');
        div1.classList.add('comentario');

        var div2 = document.createElement('div');
        div2.classList.add('comentario__head');
        var div3 = document.createElement('div');
        div3.classList.add('comentario__body');

        var div4 = document.createElement('div');
        div4.classList.add('comentario__name');
        var div5 = document.createElement('div');
        div5.classList.add('comentario__date');

        var p1 = document.createElement('p');
        p1.innerHTML = document.getElementById('Username').innerHTML;
        var p2 = document.createElement('p');
        var date = new Date();

        var mes = "";
        switch(date.getMonth()+1)
        {
            case 1:
                mes = "Enero"
                break;
            case 2:
                mes = "Febrero"
                break;
            case 3:
                mes = "Marzo"
                break;
            case 4:
                mes = "Abril"
                break;
            case 5:
                mes = "Mayo"
                break;
            case 6:
                mes = "Junio"
                break;   
            case 7:
                mes = "Julio"
                break; 
            case 8:
                mes = "Agosto"
                break;
            case 9:
                mes = "Septiembre"
                break;
            case 10:
                mes = "Octubre"
                break;
            case 11:
                mes = "Noviembre"
                break;
            case 12:
                mes = "Diciembre"
                break;  

        }
        p2.innerHTML = date.getDate() + " de " + mes + " de " + date.getFullYear();
        var p3 = document.createElement('p');
        p3.innerHTML = comment;

        div4.appendChild(p1);
        div5.appendChild(p2);
        div3.appendChild(p3);

        div2.appendChild(div4);
        div2.appendChild(div5);

        div1.appendChild(div2);
        div1.appendChild(div3);

        padre.insertBefore(div1, document.getElementById('comentar'));

        

        setTimeout(() => {
            if (Notification.permission !== 'granted'){
                Notification.requestPermission();
            } else {
                var notification = new Notification('Comentario', {
                    icon: '/static/img/logo.png',
                    body: "Tu comentario fue publicado",
                });
            }
        }, 0500);
    }else{
        var n = new Notification("LOL");
    }

    document.getElementById('comment').value = ""
}

notificar = () => {
    setTimeout(() => {
        if (Notification.permission !== 'granted'){
            Notification.requestPermission();
        } else {
            var notification = new Notification('Notification title', {
                icon: '/static/img/logo.png',
                body: "Nueva publicación agregada",
            });
        }
    }, 2000);
}


publicarComentario = (boton) => {
    var comentario = document.getElementById('comment').value;
    var id = boton.id;
    var url = document.getElementById('comment').dataset.url;

    data = {};
    data['comentario']=comentario;
    data['id']=id;

    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = () => 
    {  
        if (xhttp.readyState == 4 && xhttp.status == 200) 
        {
            console.log(xhttp.responseText)
            // document.getElementById("AbajoB").innerHTML = xhttp.responseText;
        }
    };
    datos = "json_name=" + JSON.stringify(data);
    xhttp.send(datos);
}

obtenerDatosUsuario = () => {
    var url = document.getElementById('body').dataset.url;

    var xhttp = new XMLHttpRequest();
    var cookie = getCookie('csrftoken');
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader('X-CSRFToken', cookie);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = () => 
    {  
        if (xhttp.readyState == 4 && xhttp.status == 200) 
        {
            datos = JSON.parse(xhttp.responseText);
            // console.log(datos['datos'])

            nombre = datos['datos']['nombre']
            apellido = datos['datos']['apellido']
            correo  = datos['datos']['correo']
            colonia = datos['datos']['colonia']

            document.getElementById("id_nombre").value=nombre
            document.getElementById("id_apellido").value=apellido
            document.getElementById("id_correo").value=correo
            document.getElementById("id_contraseña").value=""
            document.getElementById("id_contraseña2").value=""
        }
    };
    datos = "json_name=" + "";
    xhttp.send(datos);
}