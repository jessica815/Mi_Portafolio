<?php    
    require_once('./login.php');
    if($saml->isAuthenticated()) //Si hay sesión iniciada, hacer logout del IDP
		$saml->logout('https://sistemas.cruzperez.com/jessica/ToDoList/index.php');  	// Se puede pasar como parametro a donde redireccionar tras el logout
	else  //Si no tenia sesión iniciada, lo redirecciona a la url configurada. 
		header("https://sistemas.cruzperez.com/jessica/ToDoList/index.php"); 
?>