//Funciones
function mostrarMensaje(){
    console.log("Hola, soy una función");
}

mostrarMensaje(); //Ejecutamos la función

//Argumentos
function sumar(a, b){
    var suma = a + b;
    console.log("El resultado de " + a + " + " + b + " es " + suma);
}

//var x = 5;
//var y = 3;

sumar(5, 10); //Ejecutamos la función con argumentos
//sumar(x, y); Esta es otra forma de hacerlo

//Funciones de concatenar cadenas
function concatenarTresCadenas(cadena1, cadena2, cadena3){
    console.log(cadenada1 + " " + cadena2 + " " + cadena3);    
}

concatenarTresCadenas("Hola", "soy", "una función");

//Variable Global vs Variable Local
var miNombre = "Jess";

function mostrarNombre(){
    var miNombre = "Mike"; //Variable local
    console.log(miNombre);
}

mostrarNombre(); //Muestra Mike
console.log(miNombre); //Muestra Jess

// Retorno de Valores
function sumar(a, b){
    return a + b;
}
console.log(sumar(5, 10));

//Asignar un valor retornado a una variable
function sumar2(a, b) {
    return a + b;
    //return "Mi meta es aprender " + lenguajeDeProgramacion;
}
var resultado = sumar2(5, 10);
console.log(resultado);


//Opción 2 con CADENAS
function crearCadenaConMeta(lenguajeDeProgramacion) {
    return "Mi meta es aprender " + lenguajeDeProgramacion;
}
var miMeta = crearCadenaConMeta("JavaScript");
console.log(miMeta);