# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app/proto/transaction.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'app/proto/transaction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pp/proto/transaction.proto\x12\x14transaction.v1alpha1\"f\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_account\x18\x02 \x01(\t\x12\x12\n\nto_account\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x02\x12\x11\n\ttimestamp\x18\x05 \x01(\t\"P\n\x14TransferMoneyRequest\x12\x14\n\x0c\x66rom_account\x18\x01 \x01(\t\x12\x12\n\nto_account\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\"p\n\x15TransferMoneyResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_account\x18\x02 \x01(\t\x12\x12\n\nto_account\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x02\x12\x11\n\ttimestamp\x18\x05 \x01(\t\"2\n\x1cGetTransactionHistoryRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"X\n\x1dGetTransactionHistoryResponse\x12\x37\n\x0ctransactions\x18\x01 \x03(\x0b\x32!.transaction.v1alpha1.Transaction\"5\n\x14\x43reateAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x02\"#\n\x15\x43reateAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\"N\n\x12TransactionRequest\x12\x14\n\x0c\x66rom_account\x18\x01 \x01(\t\x12\x12\n\nto_account\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"6\n\x13TransactionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd9\x03\n\x15TransactionAPIService\x12h\n\rTransferMoney\x12*.transaction.v1alpha1.TransferMoneyRequest\x1a+.transaction.v1alpha1.TransferMoneyResponse\x12\x80\x01\n\x15GetTransactionHistory\x12\x32.transaction.v1alpha1.GetTransactionHistoryRequest\x1a\x33.transaction.v1alpha1.GetTransactionHistoryResponse\x12h\n\rCreateAccount\x12*.transaction.v1alpha1.CreateAccountRequest\x1a+.transaction.v1alpha1.CreateAccountResponse\x12i\n\x12ProcessTransaction\x12(.transaction.v1alpha1.TransactionRequest\x1a).transaction.v1alpha1.TransactionResponseB\x16Z\x14transaction/v1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.proto.transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024transaction/v1alpha1'
  _globals['_TRANSACTION']._serialized_start=53
  _globals['_TRANSACTION']._serialized_end=155
  _globals['_TRANSFERMONEYREQUEST']._serialized_start=157
  _globals['_TRANSFERMONEYREQUEST']._serialized_end=237
  _globals['_TRANSFERMONEYRESPONSE']._serialized_start=239
  _globals['_TRANSFERMONEYRESPONSE']._serialized_end=351
  _globals['_GETTRANSACTIONHISTORYREQUEST']._serialized_start=353
  _globals['_GETTRANSACTIONHISTORYREQUEST']._serialized_end=403
  _globals['_GETTRANSACTIONHISTORYRESPONSE']._serialized_start=405
  _globals['_GETTRANSACTIONHISTORYRESPONSE']._serialized_end=493
  _globals['_CREATEACCOUNTREQUEST']._serialized_start=495
  _globals['_CREATEACCOUNTREQUEST']._serialized_end=548
  _globals['_CREATEACCOUNTRESPONSE']._serialized_start=550
  _globals['_CREATEACCOUNTRESPONSE']._serialized_end=585
  _globals['_TRANSACTIONREQUEST']._serialized_start=587
  _globals['_TRANSACTIONREQUEST']._serialized_end=665
  _globals['_TRANSACTIONRESPONSE']._serialized_start=667
  _globals['_TRANSACTIONRESPONSE']._serialized_end=721
  _globals['_TRANSACTIONAPISERVICE']._serialized_start=724
  _globals['_TRANSACTIONAPISERVICE']._serialized_end=1197
# @@protoc_insertion_point(module_scope)
