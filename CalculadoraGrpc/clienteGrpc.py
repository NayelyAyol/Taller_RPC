import grpc
import CalculadoraGrpc.calculadora_pb2 as calculadora_pb2
import CalculadoraGrpc.calculadora_pb2_grpc as calculadora_pb2_grpc

#stub cliente automatico que llamara a las funciones remotas 

cliente = grpc.insecure_channel(
    'localhost:5000'
)

stub = calculadora_pb2_grpc.CalculadoraStub(
    cliente
)

r1 = stub.Sumar(
    calculadora_pb2.Operacion(a=10, b=5)
)

print("La suma es: ", r1)