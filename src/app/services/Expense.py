from typing import Optional
from langchain_mistralai import ChatMistralAI
from langchain_core.pydantic_v1 import BaseModel, Field

class Expense(BaseModel):
        amount: Optional[str] = Field(title="expense", description="Amount of expense made on the transaction")
        merchant: Optional[str] = Field(title="merchant", description="Marchant name whom the transaction has been made")
        currency: Optional[str] = Field(title="currency", description="currency of the transaction (Rs means INR)")
        type: Optional[str] = Field(title="type", description="type of transaction debit or credit")