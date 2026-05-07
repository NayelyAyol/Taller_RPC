import GradosGrpc.grados_pb2 as grados_pb2
import GradosGrpc.grados_pb2_grpc as grados_pb2_grpc
import grpc
from concurrent import futures

#Crear la clase servidor, hereda de CalculadoraServicer, que es la base generada automaticamnete desde el archivo .proto
class CalculadoraServidor(
    grados_pb2_grpc.CalculadoraServicer
):
    def CF(self,request, context):
        resultado = (request.a *9/5)+32
        return grados_pb2.Resultado(
            r=resultado
        )
    

    def FC(self,request, context):
        resultado = (request.a-32)*5/9
        return grados_pb2.Resultado(
            r=resultado
        )
    
    
#Crear el servidor e indicar el numero maximo de hilos
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#Registra la clase dentro del servidor
grados_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadoraServidor(),
    servidor
)

servidor.add_insecure_port('[::]:5000')
servidor.start()
print("Servidor gRPC ejecutándose...")
servidor.wait_for_termination()
