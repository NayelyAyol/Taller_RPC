import xmlrpc.client

#Establecer comunicacion con el servidor
cliente = xmlrpc.client.ServerProxy("http://localhost:9000/")

#Invocación de las funciones 
suma = cliente.sumar(2,2)
print("Suma: ", suma)

resta = cliente.restar(2,2)
print("Resta: ", resta)

multiplicacion = cliente.multiplicar(2,2)
print("Multiplicacion: ", multiplicacion)

division = cliente.dividir(2,2)
print("División: ", division)