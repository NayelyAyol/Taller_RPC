import xmlrpc.client

#Establecer comunicacion con el servidor
cliente = xmlrpc.client.ServerProxy("http://localhost:9000/")

print("Ingrese la operación que desea realizar \n- CF (Celsius a Fahrenheit )\n- FC (Fahrenheit a Celsius)")
opcion = input("Ingrese la operacion en letras mayúsculas (CF o FC): ").strip()

a=float(input("Grados: "))


resultado = getattr(cliente, opcion)(a)
print("Resultado:", resultado)