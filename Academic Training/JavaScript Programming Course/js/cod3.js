//Escapar Comillas en cadenas de caracteres
var miCadena = "Soy una cadena de caracteres \"con comillas\" dentro";
console.log(miCadena);

//Escapar comillas simples en cadenas de caracteres
var miCadena = 'Se pueden usar comillas dobles "con comillas" dentro de comillas simples o viceversa';
console.log(miCadena);

//Longitud de una cadena de caracteres (.length)
var miCadena;
miCadena = "A B";
console.log(miCadena.length); 

//Notación de Corchetes: Acceder al primer caracter de una cadena de caracteres
var lenguaje = "JavaScript";

/**
 * Cadena: J a v a S c r i p t
 * Índice: 0 1 2 3 4 5 6 7 8 9
 */

console.log(lenguaje[0]); //J

//Acceder al último caracter de una cadena de caracteres
var miCadena;
miCadena = "JavaScript";
console.log(miCadena[miCadena.length - 1]); //t

miCadena = "Python";
n=4;
console.log(miCadena[miCadena.length - n]); 
