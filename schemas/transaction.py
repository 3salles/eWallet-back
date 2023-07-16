from pydantic import BaseModel
from typing import Optional, List
from models.transaction import TransactionModel

class TransactionSchema(BaseModel):
    category: str = "entertainment"
    date: Optional[str] = '2023-06-17T00:00:00'
    amount: float = 300.0
    description: str = "Hogwarts Legacy"
    institution: str = "PS Store"

class ListTransactionsSchema(BaseModel):
    transactions:List[TransactionSchema]

    def list_transactions(transactions: List[TransactionModel]):
      result = []
      for transaction in transactions:
        result.append(**transaction)
      return {'transactions': result}

class AddTransactionSchema(BaseModel):
    uid: str = "752d013d-4a7d-48c7-993c-87f8296757c8"
    category: str = "entertainment"
    date: Optional[str] = '2023-06-17T00:00:00'
    amount: float = 300.0
    description: str = "Hogwarts Legacy"
    institution: str = "PS Store"

class DeleteTransactionSchema(BaseModel):
   message: str