# main.py
import sys
from gdb.db.simulated_database import SimulatedDatabase
from gdb.logging.database_log_destination import DatabaseLogDestination
from gdb.logging.transaction_logger import TransactionLogger
from gdb.service.account_service import AccountService
from gdb.ui.account_ui import AccountUI

def main() -> None:
    # ============================================================
    # 📝 STEP 14: Wire Up Dependencies And Start The UI
    #
    # INSTRUCTIONS:
    #   1. Print a welcome banner, e.g. "GLOBAL DIGITAL BANK (GDB) APPLICATION" between two lines of "=" * 60.
    #   2. db = SimulatedDatabase()
    #   3. dest = DatabaseLogDestination(db)     -- the Bridge implementor (Activity 18)
    #   4. logger = TransactionLogger(dest)      -- the Bridge abstraction
    #   5. service = AccountService(logger)      -- the service layer (Activity 19)
    #   6. ui = AccountUI(service)
    #   7. ui.start()
    # ============================================================
    # TODO: build the logging bridge, the service and the UI, then start the menu loop
    raise NotImplementedError("TODO: Step 14 - wire up dependencies and start the UI")

if __name__ == "__main__":
    main()
