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



$(function(){
    //oculta al hacer click fuera del elemnto (formulario)
    $(document).on("click",function(e) 
    {
       var container = $("#formulario-nota");       
            if (!container.is(e.target) && container.has(e.target).length === 0) 
            { 
                //Se ha pulsado en cualquier lado fuera de los elementos contenidos en la variable container
                $("#input-titulo-nota").remove();
                $("#input-categoria-nota").remove();
                $("#input-añadir-nota").remove();
                
                $("#contenedor-input-nota").css("height","8%");

            }
     });

    //Muestra elemento (formulario)
    $("#input-descripcion-nota").on("click", function(event)
    {
        if($("#input-titulo-nota").length>0)
        {
            // NO HAGAS NADA
             

        }
        else
        {
            $.ajax({ 
                type: 'POST',
                url: 'obtenerCategorias',
                data: {csrfmiddlewaretoken: token},
                success: function(data)
                {
                    $("#contenedor-input-nota").css("height","auto");
                    $("#formulario-nota").css("height","auto");
    
                    string = "<input type=\"text\" class=\"form-control form-control-sm\" placeholder=\"Titulo\" id=\"input-titulo-nota\" autocomplete=\"off\">";
                    $(string).insertBefore("#input-descripcion-nota")
    
                    string = "<input type=\"button\" class=\"btn btn-sm btn-primary\" value=\"Añadir\" id=\"input-añadir-nota\" autocomplete=\"off\" onclick=\"añadirNota()\">"
                    $(string).insertAfter("#input-descripcion-nota")
    
                    string = "<select name=\"input-categoria-nota\" id=\"input-categoria-nota\" class=\"form-control form-control-sm\">"
                    string += "<option value=\"Todas\" selected>Todas</option>"
                    numero_categorias = data['categorias'].length
                    for(x=0; x<numero_categorias; x++)
                    {
                        string += "<option value=\""+data['categorias'][x]+"\">"+data['categorias'][x]+"</option>"
                    }
                    string+= "</select>"
                    $(string).insertBefore("#input-añadir-nota")
                }
             });
        }
        event.stopImmediatePropagation();
    });
});




// FUNCIONES DEL REGISTRO E INICIO DE USUARIO
function iniciarSesion()
{
    var usuario = $('#usuario').val();
    var contraseña = $('#contraseña').val();
    token = getCookie('csrftoken');

    $.ajax({ 
        type: 'POST',
        url: 'iniciarSesion',
        data: {usuario:usuario, contraseña:contraseña, csrfmiddlewaretoken: token},
        success: function(data)
        {
            if(data=="1")
            {
                window.location.href="Notes";
            }
            else
            {
                alert(data);
            }
        }
     });
}

function registrarUsuario()
{
    token = getCookie('csrftoken');
    var usuario = $('#usuario').val();
    var contraseña = $('#contraseña').val();
    var contraseña2 = $('#contraseña_dos').val();
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    var correo = $('#correo').val();

    if(contraseña==contraseña2)
    {
        arreglo = []
        arreglo.push(usuario);
        arreglo.push(contraseña);
        arreglo.push(nombre);
        arreglo.push(apellido);
        arreglo.push(correo);

        $.ajax({ 
            type: 'POST',
            url: 'registrarUsuario',
            data: {'datosUsuario[]': JSON.stringify(arreglo), csrfmiddlewaretoken: token},
            success: function(data)
            {
                if(data=="Registro exitoso")
                {
                    alert(data);
                    $('#usuario').val("");
                    $('#contraseña').val("");
                    $('#contraseña_dos').val("");
                    $('#nombre').val("");
                    $('#apellido').val("");
                    $('#correo').val("");
                }
                else
                {
                    alert(data);
                }

                
            }
         });
    }
    else
    {
        alert("Las contraseñas no coinciden");
    }
}




// FUNCIONES PROPIAS DE LAS NOTAS
function obtenerNotas(idCategoria)
{
    token = getCookie('csrftoken');

    $.ajax({ 
        type: 'POST',
        url: 'obtenerNotas',

        data: {idCategoria:idCategoria, csrfmiddlewaretoken: token},

        success: function(data)
        {
            contenido = "";
            // console.log(data['notas'].length)

            if(data['notas'].length>0)
            {
                    for(x in data.notas)
                {
                    // console.log(data.notas)
                    idNota = data.notas[x][0]
                    titulo = data.notas[x][1]
                    descripcion = data.notas[x][2]
                    categoria_id = data.notas[x][3]
                    usuario_id = data.notas[x][4]
                    color = data.notas[x][5]
                    fecha = data.notas[x][6]
                    fecha=fecha.substring(0,10)

                    colorFuente = "";

                    if(color=="#444444")
                    {
                        colorFuente = "white";
                    }
                    else
                    {
                        colorFuente = "black"

                    }
                    

                    contenedorColores = "contenedorColores"+idNota+""
                    // console.log(contenedorColores);

                    contenido += 
                    "<div style='background:"+color+"' class='container contenedor-nota' id='nota"+idNota+"'>"+
                        "<div class='container d-flex flex-row justify-content-center align-items-center mt-2 p-0 contendor-titulo'>"+
                                "<input style='color:"+colorFuente+"' type='text' class='titulo' id='titulo"+idNota+"' oninput='cambiarTitulo("+idNota+")' value='"+titulo+"'>"+
                                "<input type='button' class='botonColor' onclick='obtenerColores(\""+contenedorColores+"\")'>"+
                        "</div>"+
                    
                    

                    "<div class='container contenedor-colores-padre p-0' id='contenedorColores"+idNota+"' style='display:none'>"+
                        "<div class='container contenedor-colores p-0 d-flex flex-row justify-content-end'>"+
                            "<input type='button' class='color' id='color-FFF2AB' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-CBF1C4' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-FFCCE5' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-E7CFFF' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-CDE9FF' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-C9C9C9' onclick='cambiarColor("+idNota+",this.id)'>"+
                            "<input type='button' class='color' id='color-444444' onclick='cambiarColor("+idNota+",this.id)'>"+
                        "</div>"+
                    "</div>"+

                    "<textarea style='color:"+colorFuente+"' class='descripcion' id='descripcion"+idNota+"' col='30' oninput='cambiarDescripcion("+idNota+")'>"+descripcion+"</textarea>"+

                    "<div  class='container mt-2 p-0 d-flex flex-row justify-content-between align-items-start'>"+
                        "<p style='color:"+colorFuente+"' class='fecha d-flex flex-column justify-content-start align-items-end'>"+fecha+"</p>"+
                        "<div style='color:"+colorFuente+"' class='container contenedor-botones '>"+
                        "<input style='color:"+colorFuente+"' class='btn btn-primary btn-sm botonEnviarNota p-0' type='button' value='Enviar' onclick='enviarNota("+idNota+")'>"+
                        "<input style='color:"+colorFuente+"' class='btn btn-danger btn-sm botonEliminarNota p-0' type='button' value='Eliminar' onclick=\"eliminarNota("+idNota+")\">"+
                        "</div>"+
                    "</div>"+
                    "</div>";
                }

                 $("#contenedor-notas").html(contenido) 
            }
            else
            {
                $("#contenedor-notas").html("No tienes nota en esta categoria")
            }
        }
     });
}

function obtenerColores(idContenedor)
{
    a = document.getElementById(idContenedor);
    
    if(a.style.display == "none")
    {
        a.style.display = "inline";
    }
    else
    {
        a.style.display = "none";
    }
}

function cambiarColor(idNota, idColor)
{
    arreglo = idColor.split("-");

    id = "#nota"+idNota;
    color = "#"+arreglo[1];

    $.ajax({ 
        type: 'POST',
        url: 'cambiarColor',
        data: {'color':color,'id':idNota, csrfmiddlewaretoken: token},
        success: function(data)
        {
            console.log(data)
        }
     });

    

    if(color=="#444444")
    {
        $(id).css("background-color",color);
        $(id).css("color","white");

        $(id).find("input").css("color", "white")
        $(id).find("textarea").css("color", "white")

    }
    else
    {
        $(id).css("background-color",color);
        $(id).css("color","black");

        $(id).find("input").css("color", "black")
        $(id).find("textarea").css("color", "black")
    }

    
}

function añadirCategoria()
{
    categoria = window.prompt("Añade la categoria","");
    categoria = categoria.trim()

    if(categoria!="")
    {
        $.ajax({
            url:'añadirCategoria',
            type:'POST',
            data:{categoria:categoria, csrfmiddlewaretoken: token },
            success: function(data)
            {
                verificacion = data['verificacion']

                if(verificacion==true)
                {
                    alert("Esa categoria ya existe");
                }
                else if (verificacion==false)
                {
                    id_categoria = data['id']
                    nombre = data['nombre']

                    alert("Categoria agregada correctamente")
                    string = "<div class=\"categoria container d-flex flex-row justify-content-between align-items-center\" id=\""+id_categoria+"\">"
                    string+= "<a onclick=\"obtenerNotas("+id_categoria+")\" href=\"javascript:void(0);\">"+nombre+"</a>"
                    string+= "<input type=\"button\" class=\"btn btn-sm btn-danger botonEliminarCategoria\" value=\"Eliminar\" onclick=\"eliminarCategoria("+id_categoria+ ",'"+nombre+"')\">"
                    string+="</div>"

                    $("#menu-lateral").append(string)
                }
                else
                {
                    alert("Error al agregar la categoria")
                }
            }
        });
    }
    else
    {
        alert("Ingresa el nombre de la categoria");
    }

   
}

function mostrarMenuUsuario()
{

    verificacion = $("#menu-usuario").length;

    if(verificacion>0)
    {
        // console.log("Si existe")
        $("#menu-usuario").remove();
    }
    else
    {
        // console.log("No existe")
        var contenedor = document.createElement("div"); 
        contenedor.setAttribute("id","menu-usuario");

        linkCerrar = document.createElement("a");
        linkCerrar.setAttribute("href","/cerrar_sesion");
        botonCerrarSesion = document.createElement("div");
        textoBoton1 = document.createTextNode("Cerrar Sesion");
        botonCerrarSesion.append(textoBoton1);
        botonCerrarSesion.setAttribute("class","contenedor-boton-usuario");
        linkCerrar.append(botonCerrarSesion);

        contenedor.append(linkCerrar);

        $("body").append(contenedor)
    }
}

function eliminarCategoria(id,nombre)
{
    confirmacion = confirm("¿Deseas eliminar la categoria '"+nombre+"'?")
    // console.log(confirmacion)

    if(confirmacion==false)
    {
        // SI LA CONFIRMACION ES NEGATIVA, NO SE HACE NADA

    }
    else
    {
        $.ajax({ 
            type: 'POST',
            url: 'eliminarCategoria',
            data: {'id': id, csrfmiddlewaretoken: token},
            success: function(data)
            {
                alert(data)
                
                if(data="Categoria eliminada")
                {
                    $("#"+id).remove()
                }

                obtenerNotas(null);
                
            }
         });
    }
}

function eliminarNota(id)
{
    confirmacion = confirm("¿Deseas eliminar esta nota?")
    console.log(confirmacion)


    if(confirmacion==false)
    {

    }
    else
    {
        $.ajax({ 
            type: 'POST',
            url: 'eliminarNota',
            data: {'id': id, csrfmiddlewaretoken: token},
            success: function(data)
            {
                alert(data)
                
                if(data="Nota eliminada")
                {
                    
                    $("#nota"+id).remove()
                }
                
            }
         });

    }
}

function añadirNota()
{
    titulo = $("#input-titulo-nota").val()
    descripcion = $("#input-descripcion-nota").val()
    categoria = $("#input-categoria-nota").val()


    if(titulo=="" || descripcion=="")
    {
        alert("Ni el titulo ni la descripcion pueden estar vacias");
    }
    else
    {
        $.ajax({ 
            type: 'POST',
            url: 'añadirNota',
            data: {'titulo':titulo,'descripcion':descripcion,'categoria':categoria, csrfmiddlewaretoken: token},
            success: function(data)
            {
                alert(data)

                $("#input-titulo-nota").val("")
                $("#input-descripcion-nota").val("")
                obtenerNotas(null);
            }
         });
    }
}

function cambiarTitulo(idNota)
{
    // console.log(idNota)
    token = getCookie('csrftoken');
    titulo = $("#titulo"+idNota).val();

    $.ajax({ 
        type: 'POST',
        url: 'cambiarTitulo',
        data: {'titulo':titulo, 'id':idNota, csrfmiddlewaretoken: token},
        success: function(data)
        {
            if(data=="Error al cambiar el titulo de la nota")
            {
                alert(data)
            }
        }
     });
}

function cambiarDescripcion(idNota)
{
    token = getCookie('csrftoken');
    descripcion = $("#descripcion"+idNota).val()

    $.ajax({ 
        type: 'POST',
        url: 'cambiarDescripcion',
        data: {'descripcion':descripcion, 'id':idNota, csrfmiddlewaretoken: token},
        success: function(data)
        {
            if(data=="Error al cambiar la nota")
            {
                alert(data)
            }
        }
     });


}

function enviarNota(idNota)
{
    token = getCookie('csrftoken');
    usuario = window.prompt("Ingresa el usuario a enviar la nota","");

    $.ajax({ 
        type: 'POST',
        url: 'enviarNota',
        data: {'id':idNota, 'usuario':usuario, csrfmiddlewaretoken: token},
        success: function(data)
        {
            alert(data)

        }
     });

}