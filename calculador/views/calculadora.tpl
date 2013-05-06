<html>
    <head>
        <title> Calculadora Sencilla </title>
    </head>
    <body>
        <h1> Calculadora Sencilla </h1>
        <form method='POST' action='/hacer_cuenta'>
            <label> Ingresa la expresion : <input type='text'
name='cuenta' value="{{cuenta}}"> </label>
            
            <br/>
            <label> Resultado: {{total}}</label>
            <br/> 
            <input type='submit' value='Enviar'/>
    </body>
</html>
