<?php
    require './login.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Todo List</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="css/style.css" />
    <link rel="stylesheet" href="css/font-awesome.min.css" />
    <link rel="stylesheet" href="css/bootstrap.min.css" />
    
    <link rel="manifest" href="./manifest.json">
    <script type="module" defer src="./Service_Worker.js"></script>
    <script type="module" defer src="./registro_serviceWorker.js"></script>
    
    <script src='https://cdn.firebase.com/js/client/2.2.1/firebase.js'></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.5/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.5/firebase-messaging-sw.js"></script>


    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="apple-mobile-web-app-status-bar" content="#db4938" />
    <meta name="theme-color" content="#db4938"/>
    
    <!----METAS DE PWA-->
    <meta name="theme-color" content="#2F3BA2">
    <meta name="MobileOptimized" content="width">
    <meta name="HandheldFriendly" content="true">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="shortcut icon" type="image/png" href="./images/icon-512x512.png">
    <link rel="apple-touch-icon" href="./images/icon-512x512.png">
    <link rel="apple-touch-startup-image" href="./images/icon-512x512.png">

    <link rel="apple-touch-icon" href="./images/icon-24x24.png" />
    <link rel="apple-touch-icon" href="./images/icon-42x42.png" />
    <link rel="apple-touch-icon" href="./images/icon-72x72.png" />
    <link rel="apple-touch-icon" href="./images/icon-96x96.png" />
    <link rel="apple-touch-icon" href="./images/icon-128x128.png" />
    <link rel="apple-touch-icon" href="./images/icon-144x144.png" />
    <link rel="apple-touch-icon" href="./images/icon-152x152.png" />
    <link rel="apple-touch-icon" href="./images/icon-192x192.png" />
    <link rel="apple-touch-icon" href="./images/icon-384x384.png" />
    <link rel="apple-touch-icon" href="./images/icon-512x512.png" />
    <meta name="apple-mobile-web-app-status-bar" content="#db4938" />

</head>

<body>
    <script async defer>
        var updateComponent = document.createElement("pwa-update");
        document.body.appendChild(updateComponent);
    </script>
    <header style="background-color: rgb(53, 0, 84); color: #fff;">
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    <nav class="navbar justify-content-between">
                    <a class="navbar-brand">ToDoList</a>
                    <form class="form-inline">
                        <input class="form-control mr-sm-2" type="search" placeholder="Buscar" aria-label="Search"
                        id="searchtextbox" />
                    </form>
                    <a href="./logout.php" style="color: #d3aee2;"><b>Salir</b></a>
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <section class="todo-outer">
        <div class="container">
            <div class="row justify-content-md-center"> <!-- Apartir de aquí añado el botón de refresh -->
                <div class="col-sm-12 col-md-8">
                    <h1><center>Lista de Tareas</center></h1>
                    <?php
                    echo  "Hola ".$atributos["uCorreo"] [0];
                    ?>
                    <div class="container">
                        <br/><br/>
                        <div>
                            <div id="token"></div>
                            <div id="err"></div>
                        </div>
                    </div>
                    <div class="todo-inner">
                        <div class="form-row">
                            <div class="col-9 mr-sm-2">
                                <input type="text" class="form-control" placeholder="Tarea pendiente:" id="addtaskinput" />
                                <input type="hidden" id="saveindex">
                            </div>
                            <button type="button" class="btn" style="background-color: rgb(53, 0, 84); border: none; width: auto; height: auto; color: #fff;" id="addtaskbtn" method="POST">
                            +
                            </button>
                            <button type="button" style="background-color: #fff; border: none; color: #000; margin-left: 18px;" id="refresh"><i class="fa-solid fa-arrow-rotate-right"></i><svg xmlns="http://www.w3.org/2000/svg" width="28" height="33" fill="#000" class="bi bi-arrow-clockwise" viewBox="0 0 15 10">
                            <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2v1z"/>
                            <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466z"/>
                            </svg></button>
                            <button type="button" class="btn btn-success mr-sm-2" id="savetaskbtn" style="display: none;">
                            Guardar
                            </button>
                        </div>
                        <div class="to-do-output">
                            <table class="table table-responsive mt-3 mb-0" id="addedtasklist"></table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <script>
        const persona="<?php echo $atributos["uCorreo"] [0];  ?>";
    </script>
    <script src="./main.js"></script>
</body>

</html>




