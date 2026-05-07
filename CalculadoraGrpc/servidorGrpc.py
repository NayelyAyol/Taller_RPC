import CalculadoraGrpc.calculadora_pb2 as calculadora_pb2
import CalculadoraGrpc.calculadora_pb2_grpc as calculadora_pb2_grpc
import grpc
from concurrent import futures

#Crear la clase servidor, hereda de CalculadoraServicer, que es la base generada automaticamnete desde el archivo .proto
class CalculadoraServidor(
    calculadora_pb2_grpc.CalculadoraServicer
):
    def Sumar(self,request, context):
        resultado = request.a + request.b
        return calculadora_pb2.Resultado(
            r=resultado
        )
    

    def Restar(self,request, context):
        resultado = request.a - request.b
        return calculadora_pb2.Resultado(
            r=resultado
        )
    
    def Multipicar(self,request, context):
        resultado = request.a * request.b
        return calculadora_pb2.Resultado(
            r=resultado
        )
    
    def Dividir(self,request, context):
        resultado = request.a // request.b
        return calculadora_pb2.Resultado(
            r=resultado
        )
    
#Crear el servidor e indicar el numero maximo de hilos
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#Registra la clase dentro del servidor
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadoraServidor(),
    servidor
)

servidor.add_insecure_port('[::]:5000')
servidor.start()
print("Servidor gRPC ejecutándose...")
servidor.wait_for_termination()
