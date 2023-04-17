//Arreglos (array)
// Nos permiten almacenar varios valores en una misma estructura

//Arreglos aninados
var listaDeEstudiantes = [["Juan", 20], ["Ana", 19], ["Pedro", 21]];
console.log(listaDeEstudiantes);

//Acceder a un elemento de un arreglo 
var miArreglo = [10, 20, 30];

/**
 * Arreglo: [10 20 30]
 * Índice:   0  1  2
 */

console.log(miArreglo[0]); //10
console.log(miArreglo[1]); //20
console.log(miArreglo[2]); //30

//Suma de los elementos del arreglo
var suma = miArreglo[0] + miArreglo[1] + miArreglo[2];
console.log(suma);

//Modificar elementos de un Arreglo
var miArreglo2 = [10, 20, 30];
miArreglo2[0] = 100;
miArreglo2[1] = 'Hola';
miArreglo2[2] = [1, 2, 3]; //Arreglo anidado
console.log(miArreglo2);

//Acceder a arreglos multidimensionales
var miArreglo3 = [[1, 2], [3, 4], [5, 6]]; 

/**
 * Arreglo: [[1, 2], [3, 4], [5, 6]]
 * Índice:      0       1       2
 * Índice:    0  1    0  1    0  1
 */

console.log(miArreglo3[2][0]); //5

//Agregar elementos a un arreglo
// .push --> significa "empujar". Añadir un elemento al final del arreglo
var estaciones = ["Invierno", "Otoño", "Primavera"];
estaciones.push("Verano");
console.log(estaciones);

// .pop() --> significa "sacar". Eliminar el último elemento del arreglo
// .pop también retorna el elemento eliminado
var estaciones2 = ["Invierno", "Otoño", "Primavera", "Verano"];
estacion = estaciones2.pop();
console.log(estaciones2);
console.log(estacion);

// .shift() --> Elimina el primer elemento del arreglo
var estaciones3 = ["Invierno", "Otoño", "Primavera", "Verano"];
estaciones3.shift();
console.log(estaciones3);

// .unshift() --> Añade un elemento al principio del arreglo
var estaciones4 = ["Invierno", "Otoño", "Primavera"];
estaciones4.unshift("Verano");
console.log(estaciones4);







