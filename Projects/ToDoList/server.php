<?php

    $data = file_get_contents("php://input");


       
    $datos = json_decode($data, true);


   
     $archivo = $datos[0];
     $tareas = $datos[1];
   
 
   
    $bytes = file_put_contents("datos/$archivo", json_encode($tareas));
    echo $bytes;
?>