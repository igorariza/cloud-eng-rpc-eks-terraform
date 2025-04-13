from datetime import datetime
import uuid
import grpc
import os
from dotenv import load_dotenv
from app.proto import account_pb2, account_pb2_grpc, transaction_pb2_grpc, transaction_pb2
load_dotenv()

TRANSACTION_SERVICE_URI = os.getenv("TRANSACTION_SERVICE_URI", "localhost:50051")
class AccountAPIService(account_pb2_grpc.AccountAPIServiceServicer):
    
    def ValidateIfExistAccountName(self, request, context):
        exists = request.name == "existing_account"
        return account_pb2.ValidateIfExistAccountNameResponse(exists=exists)

    def CreateAccount(self, request, context):
        
        create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account_id = str(uuid.uuid4())
        account = account_pb2.Account(
            id=account_id,
            name=request.name,
            balance=request.balance,
            create_at=create_at,
            update_at=create_at,
        )
        print("Creating account... \n" + "id: " + str(account.id) + "\n" + "name: " + str(account.name))
        return account_pb2.CreateAccountResponse(id=account_id)

    def GetAccountBalance(self, request, context):
        print("Getting account balance for ID:", request.id)
        balance = 100.0 if request.id == "123" else 0.0

        return account_pb2.GetAccountBalanceResponse(id=request.id, balance=10.0)
    
    def GetTransactionHistory(self, request, context):
        with grpc.insecure_channel(TRANSACTION_SERVICE_URI) as channel:
            stub = transaction_pb2_grpc.TransactionAPIServiceStub(channel)
            try:
                response = stub.GetTransactionHistory(
                    transaction_pb2.GetTransactionHistoryRequest(
                        id=request.id,
                    )
                )
                print(f"Transaction history for account {request.id}: {response.transactions}")
                return transaction_pb2.GetTransactionHistoryResponse(
                    id=request.id,
                    transactions=response.transactions,
                )
            except grpc.RpcError as e:
                context.set_details(f"gRPC error: {e.details()}")
                context.set_code(e.code())
                return transaction_pb2.GetTransactionHistoryResponse(
                    id=request.id,
                    transactions=[],
                )