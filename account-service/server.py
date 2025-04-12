import grpc
import sys
import os
from concurrent import futures
from datetime import datetime
import uuid
import account_pb2
import account_pb2_grpc
import transaction_pb2
import transaction_pb2_grpc

class AccountAPIService(account_pb2_grpc.AccountAPIServiceServicer):
    def ValidateIfExistAccountName(self, request, context):
        exists = request.name == "existing_account"
        return account_pb2.ValidateIfExistAccountNameResponse(exists=exists)
    
    def CreateAccount(self, request, context):
        create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account_id = str(uuid.uuid4())
        print("sererver")
        account = account_pb2.Account(id=account_id, name=request.name, balance=request.balance, create_at=create_at, update_at=create_at)
        return account_pb2.CreateAccountResponse(id=account_id)
    
    def GetAccountBalance(self, request, context):
        balance = 100.0 if request.id == "123" else 0.0
        return account_pb2.GetAccountBalanceResponse(id=request.id, balance=balance)

    def notify_transaction(self, from_account, to_account, amount):
        with grpc.insecure_channel('127.0.0.1:50057') as channel:
            stub = transaction_pb2_grpc.TransactionAPIServiceStub(channel)
            try:
                response = stub.ProcessTransaction(
                    transaction_pb2.TransactionRequest(
                        from_account=from_account,
                        to_account=to_account,
                        amount=amount,
                    )
                )
                print(f"Transaction notification response: {response.status} - {response.message}")
            except grpc.RpcError as e:
                print(f"gRPC error: {e.code()} - {e.details()}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountAPIServiceServicer_to_server(AccountAPIService(), server)
    server.add_insecure_port('[::]:50056')
    print("Account Server running on port 50056")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()