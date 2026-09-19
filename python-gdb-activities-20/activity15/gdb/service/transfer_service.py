# gdb/service/transfer_service.py
from gdb.domain.iaccount import IAccount
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException
from gdb.exceptions.invalid_pin_exception import InvalidPinException

class TransferService:
    """Service managing funds transfer operations, validations, and daily tier limits."""

    def __init__(self) -> None:
        pass

    def transfer(self, from_acc: IAccount, to_acc: IAccount, amount: float, pin: int) -> None:
        # ============================================================
        # 📝 STEP 1: Transfer Funds With Daily Limit
        #
        # INSTRUCTIONS:
        #   1. Null check: if from_acc or to_acc is None, raise AccountException("Source and destination accounts are required").
        #   2. Active check: if not from_acc.is_active() or not to_acc.is_active(), raise InactiveAccountException("Both accounts must be active to transfer funds").
        #   3. PIN verify: if not from_acc.verify_pin(pin), raise InvalidPinException("Incorrect PIN").
        #   4. Balance check: if not from_acc.can_withdraw(amount): raise InsufficientBalanceException(f"Insufficient balance for transfer of Rs. {amount}").
        #   5. Daily-limit check: call from_acc.reset_daily_transfer_if_needed()
        #      if not from_acc.can_transfer(amount), raise AccountException(f"Daily transfer limit exceeded. Remaining today: Rs. {from_acc.get_remaining_daily_transfer_limit()}").
        #   6. Debit: from_acc.withdraw(amount, pin).
        #   7. Credit: to_acc.deposit(amount).
        #   8. Update total: from_acc.update_daily_transfer_total(amount).
        # ============================================================
        # TODO: validate, debit the sender, credit the receiver, and record against daily limit
        raise NotImplementedError("TODO: Step 1 - implement transfer method")

