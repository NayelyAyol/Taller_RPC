from xmlrpc.server import SimpleXMLRPCServer

#Funciones que van ser llamadas por el cliente

def sumar(a, b):
    return a+b

def restar(a,b):
    return a-b

def dividir(a,b):
    return a/b

def multiplicar(a,b):
    return a*b

#Creacion del servidor, se comunica con loaclhost y el puerto
servidor = SimpleXMLRPCServer(("0.0.0.0",9000))

#Registrar las funciones del cliente para llamarlas en el directorio 
servidor.register_function(sumar, "sumar")
servidor.register_function(restar, "restar")
servidor.register_function(dividir, "dividir")
servidor.register_function(multiplicar, "multiplicar")

# Se inicializa el servidor y siempre se mantiene activo
servidor.serve_forever()
print("Servidor escuchando")