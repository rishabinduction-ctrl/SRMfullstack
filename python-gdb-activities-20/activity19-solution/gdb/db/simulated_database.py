# gdb/db/simulated_database.py
from typing import List, Dict
from gdb.domain.transaction import Transaction

class SimulatedDatabase:
    """Mock in-memory transactional database storage."""

    def __init__(self) -> None:
        self._records: List[Transaction] = []

    def insert(self, transaction: Transaction) -> None:
        self._records.append(transaction)

    def query_all(self) -> List[Transaction]:
        return list(self._records)

    def queryAll(self) -> List[Transaction]:
        return self.query_all()

    def query_by_account(self, account_number: int) -> List[Transaction]:
        acc_no = int(account_number)
        return [t for t in self._records if t.account_number == acc_no or t.from_account == acc_no or t.to_account == acc_no]

    def queryByAccount(self, account_number: int) -> List[Transaction]:
        return self.query_by_account(account_number)

    def clear(self) -> None:
        self._records.clear()
