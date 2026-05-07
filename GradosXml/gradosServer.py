from xmlrpc.server import SimpleXMLRPCServer

#Funciones que van ser llamadas por el cliente

def CF(a):
    return (a*9/5)+32

def FC(a):
    return (a-32)*5/9


#Creacion del servidor, se comunica con loaclhost y el puerto
servidor = SimpleXMLRPCServer(("0.0.0.0",9000))

#Registrar las funciones del cliente para llamarlas en el directorio 
servidor.register_function(CF, "CF")
servidor.register_function(FC, "FC")

# Se inicializa el servidor y siempre se mantiene activo
servidor.serve_forever()
print("Servidor escuchando")