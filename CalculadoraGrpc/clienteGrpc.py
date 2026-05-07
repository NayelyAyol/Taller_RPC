import grpc
import calculadora_pb2
import calculadora_pb2_grpc

# Conectar al servidor gRPC
canal = grpc.insecure_channel('localhost:5000')
stub = calculadora_pb2_grpc.CalculadoraStub(canal)

print("Ingrese la operación que desea realizar:\n- sumar\n- restar\n- multiplicar\n- dividir")
operacion = input("Operación: ").strip().lower()

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

funciones = {
    "sumar": stub.Sumar,
    "restar": stub.Restar,
    "multiplicar": stub.Multipicar,  
    "dividir": stub.Dividir
}

if operacion in funciones:
    resultado = funciones[operacion](calculadora_pb2.Operacion(a=a, b=b))
    print("Resultado:", resultado.r)
else:
    print("Operación no válida")