from datetime import datetime
import uuid
import grpc
from app.proto import account_pb2, account_pb2_grpc
from app.client.transaction_client import TransactionAPIService

class AccountAPIService(account_pb2_grpc.AccountAPIServiceServicer):
    def __init__(self):
        self.transaction_client = TransactionAPIService()

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
        print("Getting transaction history for account ID:", request.id)
        transactions = [
            account_pb2.Transaction(id="1", from_account=request.id, to_account="456", amount=100.0, timestamp="2023-10-01T10:00:00Z"),
            account_pb2.Transaction(id="2", from_account=request.id, to_account="789", amount=50.0, timestamp="2023-10-02T12:00:00Z"),
        ]
        print("Transaction history:", "transactions")
        #self.transaction_client.GetTransactionHistory(request, context)
        return account_pb2.GetTransactionHistoryResponse(transactions=transactions)