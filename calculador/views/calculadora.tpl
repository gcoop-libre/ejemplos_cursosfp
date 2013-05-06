<html>
    <head>
        <title> Calculadora Sencilla </title>
    </head>
    <body>
        <h1> Calculadora Sencilla </h1>
        <form method='POST' action='/hacer_cuenta/{{nombre}}'>
            <label> Ingresa la expresion : <input type='text'
name='cuenta' value="{{cuenta}}"> </label>
            
            <br/>
            <label> Resultado: {{total}}</label>
            <br/> 
            <input type='submit' value='Enviar'/>
            <h2> Cuentas Anteriores </h2>
            <pre>{{cuentas_anteriores}}</pre>
    </body>
</html>
