from concurrent import futures
import grpc
import os
from dotenv import load_dotenv
from app.services.account_service import AccountAPIService
import app.proto.account_pb2_grpc as account_pb2_grpc

# Load environment variables
load_dotenv()

GRPC_PORT = os.getenv("GRPC_PORT", "50051")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountAPIServiceServicer_to_server(AccountAPIService(), server)
    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    print(f"Account Server running on port {GRPC_PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()