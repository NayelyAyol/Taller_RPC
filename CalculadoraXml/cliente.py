import xmlrpc.client

#Establecer comunicacion con el servidor
cliente = xmlrpc.client.ServerProxy("http://localhost:9000/")

print("Ingrese la operación que desea realizar \n- sumar\n- restar\n- multiplicar\n- dividir")
opcion = input("Ingrese la operacion en letras, tal cual se muestra en el enunciado: ").strip()

a=float(input("Primer número: "))
b=float(input ("Segundo número: "))

resultado = getattr(cliente, opcion)(a, b)
print("Resultado:", resultado)