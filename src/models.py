from typing import TypedDict


class Transaction(TypedDict):
    id: str
    amount: float
    currency: str
