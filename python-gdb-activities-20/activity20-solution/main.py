# main.py
import sys
from gdb.db.simulated_database import SimulatedDatabase
from gdb.logging.database_log_destination import DatabaseLogDestination
from gdb.logging.transaction_logger import TransactionLogger
from gdb.service.account_service import AccountService
from gdb.ui.account_ui import AccountUI

def main() -> None:
    print("=" * 60)
    print("       GLOBAL DIGITAL BANK (GDB) APPLICATION")
    print("=" * 60)

    # Setup Logging Subsystem via Bridge Pattern
    db = SimulatedDatabase()
    dest = DatabaseLogDestination(db)
    logger = TransactionLogger(dest)

    # Initialize Service Layer & UI
    service = AccountService(logger)
    ui = AccountUI(service)

    # Launch Interactive Console
    ui.start()

if __name__ == "__main__":
    main()
