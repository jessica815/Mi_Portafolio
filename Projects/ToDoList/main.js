
showtask(); // Función mostrar la tarea correspondiente
let addtaskinput = document.getElementById("addtaskinput"); // Input para añadir tarea
let addtaskbtn = document.getElementById("addtaskbtn"); // Botón para añadir tarea

addtaskbtn.addEventListener("click", function () {
    addtaskinputval = addtaskinput.value; // Toma el valor del input
    if (addtaskinputval.trim() != 0) { // Si el input no está vacío
        let webtask = localStorage.getItem("localtask"); // GET --> Obtiene información
        if (webtask == null) {
            taskObj = []; //array donde se estarán añadiendo las tareas al momento de dar click en el +
        }
        else {
            taskObj = JSON.parse(webtask); // Convierte el texto en un objeto JavaScript
        }
        taskObj.push({ 'task_name': addtaskinputval, 'completeStatus': false });
        localStorage.setItem("localtask", JSON.stringify(taskObj)); // SET --> Guarda información  ----- JSON.stringify --> Convierte a texto el array, obj o variable
        addtaskinput.value = '';
    }
    showtask(); // Muestra la tarea
    enviodatos(taskObj); // Envía el dato añadido al servidor ------ archivo --> *server.php* 
})

// Esto es para que al dar enter desde el teclado se añada la tarea
addtaskinput.addEventListener("keypress", function (e) {
    addtaskinputval = addtaskinput.value;
    if (e.code === "Enter" && addtaskinputval.trim() != 0) {
        addtaskbtn.click(); // Simula el click del botón
    }
})

// Función para recibir los datos del cliente
refresh.addEventListener("click", function () {
    recibirdatoscliente();
})

// JSON.stringify   -->     función integrada para convertir un objeto en una cadena JSON.
// JSON.parse   -->         función para convertir cadenas JSON en objetos JavaScript.

// Función Mostrar la Tarea
function showtask() {
    let webtask = localStorage.getItem("localtask"); //Toma la información del localstorage y la guarda en la variable webtask
    if (webtask == null) { 
        taskObj = []; // Array donde se estarán añadiendo las tareas al momento de dar click en el +
    }
    else {
        taskObj = JSON.parse(webtask); // Convierte el texto en un objeto JavaScript
    }
    let html = ''; 
    let addedtasklist = document.getElementById("addedtasklist"); // Toma el elemento con el id "addedtasklist" y lo guarda en la variable addedtasklist
    taskObj.forEach((item, index) => { // Devuelve el valor de cada elemento del array

        if (item.completeStatus == true) { 
            taskCompleteValue = `<td class="completed">${item.task_name}</td>`; // Si la tarea está completada, se le añade la clase "completed" para que se vea tachada
        } else {
            taskCompleteValue = `<td>${item.task_name}</td>`;
        }
        // Se añade la tarea a la tabla junto con sus funcionalidades (editar, completar y borrar)
        html += `<tr> 
                    <th scope="row">${index + 1}</th>
                    ${taskCompleteValue}
                    <td><button type="button" onclick="edittask(${index})" class="text-primary"><i class="fa fa-edit"></i>Editar</button></td>
                    <td><button type="button" class="text-success" id=${index}><i class="fa fa-check-square-o"></i>Completada</button></td>
                    <td><button type="button" onclick="deleteitem(${index})" class="text-danger"><i class="fa fa-trash"></i>Borrar</button></td>
                </tr>`;
    });
    addedtasklist.innerHTML = html;
}

// Editar la tarea
function edittask(index) {
    let saveindex = document.getElementById("saveindex");
    let addtaskbtn = document.getElementById("addtaskbtn");
    let savetaskbtn = document.getElementById("savetaskbtn");
    saveindex.value = index;
    let webtask = localStorage.getItem("localtask");
    let taskObj = JSON.parse(webtask);

    addtaskinput.value = taskObj[index]['task_name']; // Toma el valor de la tarea y lo guarda en el input
    addtaskbtn.style.display = "none"; 
    savetaskbtn.style.display = "block"; // Muestra el botón de guardar cambios
    taskObj.push({ 'task_name': addtaskinputval, 'completeStatus': false }); // Añade la tarea al array
}

// Guardar cambios
let savetaskbtn = document.getElementById("savetaskbtn");
savetaskbtn.addEventListener("click", function () {
    let addtaskbtn = document.getElementById("addtaskbtn");
    let webtask = localStorage.getItem("localtask"); 
    let taskObj = JSON.parse(webtask);
    let saveindex = document.getElementById("saveindex").value;

    for (keys in taskObj[saveindex]) { //Atributos de la tarea
        if (keys == 'task_name') {
            taskObj[saveindex].task_name = addtaskinput.value;
        }
    }
    savetaskbtn.style.display = "none";
    addtaskbtn.style.display = "block"; // Muestra el botón de añadir tarea
    localStorage.setItem("localtask", JSON.stringify(taskObj)); //guarda los cambios en localstorage
    addtaskinput.value = ''; // limpia el input
    showtask(); // muestra la tarea
    enviodatos(taskObj);
})

// Función borrar tarea
function deleteitem(index) {
    let webtask = localStorage.getItem("localtask");
    let taskObj = JSON.parse(webtask); //JSON.parse funcion que convierte texto en un objeto JavaScript.
    taskObj.splice(index, 1); //.splice se elimina para eliminar un elemento en especifico, sin dejar espacios vacíos.
    localStorage.setItem("localtask", JSON.stringify(taskObj)); 
    showtask();
    enviodatos(taskObj); // Envía los datos de la tarea al servidor
}

/*  .SPLICE
    * Primer elemento: array.shift()
    * Último elemento: array.pop()
*/

// Completar tarea
function completetask(index) {
    let webtask = localStorage.getItem("localtask");
    let taskObj = JSON.parse(webtask);
    taskObj[index] = '<span style="text-decoration:line-through">' + taskObj[index] + '</span>'; // Tacha la tarea
    let addedtasklist = document.getElementById("addedtasklist");
    addedtasklist.addEventListener("click", function (e) { 
        console.log(addedtasklist)
    });
    localStorage.setItem("localtask", JSON.stringify(taskObj));
    showtask();
    enviodatos(taskObj);
}

// Marcar tarea como completada
let addedtasklist = document.getElementById("addedtasklist");
addedtasklist.addEventListener("click", function (e) {

    let webtask = localStorage.getItem("localtask");
    let taskObj = JSON.parse(webtask);

    let mytarget = e.target; // Toma el elemento que se está clickeando y lo guarda en la variable mytarget
    if (mytarget.classList[0] === 'text-success') {  
        let mytargetid = mytarget.getAttribute("id"); // Toma el id del elemento que se está clickeando y lo guarda en la variable mytargetid


        mytargetpresibling = mytarget.parentElement.previousElementSibling.previousElementSibling; 

        // for para recorrer el objeto y cambiar el estado de la tarea
        for (keys in taskObj[mytargetid]) {
            if (keys == 'completeStatus' && taskObj[mytargetid][keys] == true) {
                taskObj[mytargetid].completeStatus = false;
            } else if (keys == 'completeStatus' && taskObj[mytargetid][keys] == false) {
                taskObj[mytargetid].completeStatus = true;
            }
        }
        localStorage.setItem("localtask", JSON.stringify(taskObj));
        showtask();
        enviodatos(taskObj);
    }
})


// Función para el buscador de tareas
let searchtextbox = document.getElementById("searchtextbox");
searchtextbox.addEventListener("input", function () {
    let trlist = document.querySelectorAll("tr");
    Array.from(trlist).forEach(function (item) {
        let searchedtext = item.getElementsByTagName("td")[0].innerText;
        let searchtextboxval = searchtextbox.value;
        let re = new RegExp(searchtextboxval, 'gi');
        if (searchedtext.match(re)) {
            item.style.display = "table-row";
        }
        else {
            item.style.display = "none";
        }
    })
})



//Método POST para Envío de datos
function enviodatos(taskObj) {

    var cadena = new Array (persona,taskObj);
    //console.log("PERSONA:          ",persona);
    console.log("TAREAS:  ", taskObj);
    console.log('ENVIO AL SERVIDOR',JSON.stringify(cadena));


    fetch("./server.php", //el fetch es un método de búsqueda
        {
            headers: {
                'Accept': 'application/json', //contenido que el cliente puede procesar
                'Content-Type': 'application/json'
            },
            method: "POST", //método para enviar o traer datos
            body: JSON.stringify(cadena)  //JSON.stringify(taskObj)
        })
    .then(function (res) { console.log(res) }) //resuelve la respuesta
    .catch(function (res) { console.log(res) }) //resuleve el error
}

// Función para recibir los datos del servidor
async function recibirdatoscliente() {
    //como mandar una variable en una ruta
    // fetch("datos/?rnd="+Math.random() ,{
    fetch("datos/"+persona+"?rnd="+Math.random() ,{ //modificar la ruta
        headers: {
            'Accept': 'application/json', //contenido que el cliente puede procesar
            'Content-Type': 'application/json'
        },
        method: "POST", //método para enviar o traer datos
        body: persona //correo@ucol.mx se puso solo para que no estuviera vacío
    })
    .then(response => response.json()) //responde en json
    .then(data => construir(data)); //manda data a la función construir
}

recibirdatoscliente();

// Función para construir los datos recibidos del servidor
function construir(data) {
    console.log(data,'datos en construir')

    //checar que la información obtenida es correcta.

    localStorage.setItem("localtask", JSON.stringify(data));
    showtask();
}



