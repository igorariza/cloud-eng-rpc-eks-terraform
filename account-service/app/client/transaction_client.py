import sys
import os
from concurrent import futures
import grpc
from dotenv import load_dotenv

from app.proto import account_pb2, account_pb2_grpc 
from app.proto import transaction_pb2, transaction_pb2_grpc
import uuid
load_dotenv()


GRPC_PORT = os.getenv("GRPC_PORT", "50051")
TRANSACTION_SERVICE_URI = os.getenv("TRANSACTION_SERVICE_URI", "localhost:50051")

class TransactionAPIService(transaction_pb2_grpc.TransactionAPIServiceServicer):
    def ProcessTransaction(self, request, context):
        print(f"Processing transaction from {request.from_account} to {request.to_account} for {request.amount}")
        return transaction_pb2.TransactionResponse(
            status="SUCCESS",
            message=f"Transaction from {request.from_account} to {request.to_account} processed successfully."
        )

    def CreateAccount(self, request, context):
        with grpc.insecure_channel(TRANSACTION_SERVICE_URI) as channel:
            stub = account_pb2_grpc.AccountAPIServiceStub(channel)
            try:
                response = stub.CreateAccount(
                    account_pb2.CreateAccountRequest(
                        name=request.name,
                        balance=request.balance,
                    )
                )
                print(f"Account created in account-service: {response.id}")
                return transaction_pb2.CreateAccountResponse(id=response.id)
            except grpc.RpcError as e:
                context.set_details(f"gRPC error: {e.details()}")
                context.set_code(e.code())
                return transaction_pb2.CreateAccountResponse()

    def GetAccountBalance(self, request, context):
        with grpc.insecure_channel(TRANSACTION_SERVICE_URI) as channel:
            stub = account_pb2_grpc.AccountAPIServiceStub(channel)
            try:
                response = stub.GetAccountBalance(
                    account_pb2.GetAccountBalanceRequest(
                        id=request.id,
                    )
                )
                print(f"Balance for account {request.id} retrieved from account-service: {response.balance}")
                return transaction_pb2.GetAccountBalanceResponse(id=response.id, balance=response.balance)
            except grpc.RpcError as e:
                context.set_details(f"gRPC error: {e.details()}")
                context.set_code(e.code())
                return transaction_pb2.GetAccountBalanceResponse()

def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_pb2_grpc.add_TransactionAPIServiceServicer_to_server(TransactionAPIService(), server)
    server.add_insecure_port(GRPC_PORT)
    print(f"Transaction gRPC Server running on {GRPC_PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve_grpc()