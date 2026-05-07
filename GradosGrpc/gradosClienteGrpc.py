import grpc
import grados_pb2
import grados_pb2_grpc

# Conectar al servidor gRPC
canal = grpc.insecure_channel('localhost:5000')
stub = grados_pb2_grpc.CalculadoraStub(canal)

print("Ingrese la operación que desea realizar:\n- CF\n- FC")
operacion = input("Operación: ").strip().upper()

a = input("Número: ")

funciones = {
    "CF": stub.CF,
    "FC": stub.FC
}
if operacion in funciones:
    resultado = funciones[operacion](grados_pb2.Operacion(a=a))
    print("Resultado:", resultado.r)
else:
    print("Operación no válida")