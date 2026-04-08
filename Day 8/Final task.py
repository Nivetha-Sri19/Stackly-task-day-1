import sqlite3
from abc import ABC, abstractmethod
from functools import reduce
from datetime import date

DB_MODE = "sqlite"

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "nivetha@20011998",
    "database": "expense_db"
}

SQLITE_FILE = "expenses.db"


def get_connection():
    if DB_MODE == "mysql":
        import mysql.connector
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        return conn
    else:
        conn = sqlite3.connect(SQLITE_FILE)
        conn.row_factory = sqlite3.Row
        return conn


def execute_query(query, params=(), fetchone=False, fetchall=False, commit=False):
    conn = get_connection()
    cursor = conn.cursor()

    if DB_MODE == "mysql":
        query = query.replace("?", "%s")
        query = query.replace("INTEGER PRIMARY KEY AUTOINCREMENT", "INT PRIMARY KEY AUTO_INCREMENT")
        query = query.replace("REAL", "FLOAT")

    cursor.execute(query, params)

    result = None
    if fetchone:
        row = cursor.fetchone()
        if row and DB_MODE == "mysql":
            columns = [desc[0] for desc in cursor.description]
            result = dict(zip(columns, row))
        else:
            result = row
    elif fetchall:
        rows = cursor.fetchall()
        if rows and DB_MODE == "mysql":
            columns = [desc[0] for desc in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
        else:
            result = rows

    if commit:
        conn.commit()

    cursor.close()
    conn.close()
    return result


def setup_database():
    if DB_MODE == "mysql":
        import mysql.connector
        base_config = {k: v for k, v in MYSQL_CONFIG.items() if k != "database"}
        conn = mysql.connector.connect(**base_config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_CONFIG['database']}")
        conn.commit()
        cursor.close()
        conn.close()

    execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50)
        )
    """, commit=True)

    execute_query("""
        CREATE TABLE IF NOT EXISTS expenses (
            exp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            category VARCHAR(50),
            description VARCHAR(100),
            date DATE,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """, commit=True)

    print(f"Database ready. Mode: {DB_MODE.upper()}")


class BaseEntity(ABC):
    def __init__(self, entity_id):
        self._entity_id = entity_id

    @abstractmethod
    def display(self):
        pass

    def get_id(self):
        return self._entity_id


class User(BaseEntity):
    def __init__(self, user_id, name):
        super().__init__(user_id)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def display(self):
        print(f"User ID : {self.get_id()}")
        print(f"Name    : {self.__name}")

    def create_user(self):
        execute_query(
            "INSERT INTO users (name) VALUES (?)",
            (self.__name,),
            commit=True
        )
        print(f"\nUser '{self.__name}' created successfully.")

    @staticmethod
    def get_all_users():
        return execute_query("SELECT * FROM users", fetchall=True)

    @staticmethod
    def user_exists(user_id):
        result = execute_query(
            "SELECT user_id FROM users WHERE user_id = ?",
            (user_id,),
            fetchone=True
        )
        return result is not None


class Expense(User):
    def __init__(self, user_id, amount, category, description, expense_date, name=""):
        super().__init__(user_id, name)
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = expense_date

    def get_amount(self):
        return self.__amount

    def get_category(self):
        return self.__category

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def display(self):
        print(f"User ID     : {self.get_id()}")
        print(f"Amount      : ₹{self.__amount:.2f}")
        print(f"Category    : {self.__category}")
        print(f"Description : {self.__description}")
        print(f"Date        : {self.__date}")

    def add_expense(self):
        if not User.user_exists(self.get_id()):
            print("User not found. Please create the user first.")
            return

        execute_query(
            "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
            (self.get_id(), self.__amount, self.__category, self.__description, self.__date),
            commit=True
        )
        print(f"\nExpense of ₹{self.__amount:.2f} added under '{self.__category}'.")

    @staticmethod
    def get_expenses_by_user(user_id):
        return execute_query("""
            SELECT e.exp_id, u.name, e.amount, e.category, e.description, e.date
            FROM expenses e
            JOIN users u ON e.user_id = u.user_id
            WHERE e.user_id = ?
            ORDER BY e.date DESC
        """, (user_id,), fetchall=True) or []

    @staticmethod
    def filter_by_category(user_id, category):
        all_expenses = Expense.get_expenses_by_user(user_id)
        return list(filter(lambda e: e["category"].lower() == category.lower(), all_expenses))

    @staticmethod
    def filter_by_date(user_id, filter_date):
        all_expenses = Expense.get_expenses_by_user(user_id)
        return [e for e in all_expenses if str(e["date"]) == filter_date]

    @staticmethod
    def calculate_total(user_id):
        expenses = Expense.get_expenses_by_user(user_id)
        if not expenses:
            return 0.0
        amounts = list(map(lambda e: e["amount"], expenses))
        return reduce(lambda acc, x: acc + x, amounts)

    @staticmethod
    def category_wise_spending(user_id):
        expenses = Expense.get_expenses_by_user(user_id)
        breakdown = {e["category"]: 0 for e in expenses}
        for e in expenses:
            breakdown[e["category"]] += e["amount"]
        return breakdown

    @staticmethod
    def get_highest_expense(user_id):
        expenses = Expense.get_expenses_by_user(user_id)
        if not expenses:
            return None
        return reduce(lambda a, b: a if a["amount"] >= b["amount"] else b, expenses)

    @staticmethod
    def monthly_report(user_id):
        expenses = Expense.get_expenses_by_user(user_id)
        report = {}
        for e in expenses:
            month_key = str(e["date"])[:7]
            report[month_key] = report.get(month_key, 0) + e["amount"]
        return report

    @staticmethod
    def smart_insight(user_id):
        breakdown = Expense.category_wise_spending(user_id)
        total = Expense.calculate_total(user_id)
        if total == 0:
            print("No spending data available to generate insights.")
            return
        print("\n--- Smart Insights ---")
        for category, amount in breakdown.items():
            percentage = (amount / total) * 100
            if percentage > 40:
                print(f"You are spending too much on {category} this month! ({percentage:.1f}% of total)")
            elif percentage > 25:
                print(f"Your {category} spending is moderate ({percentage:.1f}%). Consider reviewing it.")
            else:
                print(f"{category} spending looks healthy ({percentage:.1f}%).")

    @staticmethod
    def update_expense(exp_id, amount=None, category=None, description=None, expense_date=None):
        if amount is not None:
            execute_query("UPDATE expenses SET amount = ? WHERE exp_id = ?", (amount, exp_id), commit=True)
        if category is not None:
            execute_query("UPDATE expenses SET category = ? WHERE exp_id = ?", (category, exp_id), commit=True)
        if description is not None:
            execute_query("UPDATE expenses SET description = ? WHERE exp_id = ?", (description, exp_id), commit=True)
        if expense_date is not None:
            execute_query("UPDATE expenses SET date = ? WHERE exp_id = ?", (expense_date, exp_id), commit=True)
        print(f"\nExpense #{exp_id} updated successfully.")

    @staticmethod
    def delete_expense(exp_id):
        execute_query("DELETE FROM expenses WHERE exp_id = ?", (exp_id,), commit=True)
        print(f"\nExpense #{exp_id} deleted successfully.")


def print_expense_table(rows):
    if not rows:
        print("No expenses found.")
        return
    print(f"\n{'ID':<5} {'Name':<15} {'Amount':>10} {'Category':<15} {'Description':<25} {'Date'}")
    print("-" * 85)
    for row in rows:
        print(f"{row['exp_id']:<5} {row['name']:<15} ₹{row['amount']:>9.2f} {row['category']:<15} {row['description']:<25} {row['date']}")


def create_user_flow():
    print("\n--- Create New User ---")
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    User(None, name).create_user()


def add_expense_flow():
    print("\n--- Add Expense ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    if not User.user_exists(user_id):
        print("User not found.")
        return

    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Invalid amount.")
        return

    print("Categories: Food, Travel, Shopping, Entertainment, Health, Education, Utilities, Other")
    category = input("Category: ").strip().title()
    description = input("Description: ").strip()
    expense_date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()

    if not expense_date:
        expense_date = str(date.today())

    Expense(user_id, amount, category, description, expense_date).add_expense()


def view_expenses_flow():
    print("\n--- View Expenses ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    rows = Expense.get_expenses_by_user(user_id)
    print_expense_table(rows)
    print(f"\nTotal: ₹{Expense.calculate_total(user_id):.2f}")


def filter_expenses_flow():
    print("\n--- Filter Expenses ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    print("Filter by:\n1. Category\n2. Date")
    choice = input("Choice: ").strip()

    if choice == "1":
        category = input("Category name: ").strip()
        print_expense_table(Expense.filter_by_category(user_id, category))
    elif choice == "2":
        filter_date = input("Date (YYYY-MM-DD): ").strip()
        print_expense_table(Expense.filter_by_date(user_id, filter_date))
    else:
        print("Invalid choice.")


def category_spending_flow():
    print("\n--- Category-wise Spending ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    breakdown = Expense.category_wise_spending(user_id)
    if not breakdown:
        print("No expenses found.")
        return

    print()
    for category, amount in sorted(breakdown.items(), key=lambda x: x[1], reverse=True):
        print(f"{category:<20}: ₹{amount:.2f}")


def monthly_report_flow():
    print("\n--- Monthly Report ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    report = Expense.monthly_report(user_id)
    if not report:
        print("No data found.")
        return

    print()
    for month, amount in sorted(report.items(), reverse=True):
        print(f"{month}  :  ₹{amount:.2f}")


def highest_expense_flow():
    print("\n--- Highest Expense ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return

    highest = Expense.get_highest_expense(user_id)
    if not highest:
        print("No expenses found.")
        return

    print(f"\nHighest Expense:")
    print(f"  ID          : {highest['exp_id']}")
    print(f"  Amount      : ₹{highest['amount']:.2f}")
    print(f"  Category    : {highest['category']}")
    print(f"  Description : {highest['description']}")
    print(f"  Date        : {highest['date']}")


def smart_insight_flow():
    print("\n--- Smart Insights ---")
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid user ID.")
        return
    Expense.smart_insight(user_id)


def update_expense_flow():
    print("\n--- Update Expense ---")
    try:
        exp_id = int(input("Expense ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    print("Leave blank to skip a field.")
    raw_amount = input("New amount: ").strip()
    category = input("New category: ").strip() or None
    description = input("New description: ").strip() or None
    expense_date = input("New date (YYYY-MM-DD): ").strip() or None

    amount = None
    if raw_amount:
        try:
            amount = float(raw_amount)
        except ValueError:
            print("Invalid amount.")
            return

    Expense.update_expense(exp_id, amount, category, description, expense_date)


def delete_expense_flow():
    print("\n--- Delete Expense ---")
    try:
        exp_id = int(input("Expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    Expense.delete_expense(exp_id)


def list_users_flow():
    users = User.get_all_users()
    if not users:
        print("No users found.")
        return
    print(f"\n{'ID':<5} {'Name'}")
    print("-" * 25)
    for u in users:
        print(f"{u['user_id']:<5} {u['name']}")


def main():
    setup_database()

    menu = {
        "1":  ("Create user",            create_user_flow),
        "2":  ("Add expense",            add_expense_flow),
        "3":  ("View expenses",          view_expenses_flow),
        "4":  ("Filter expenses",        filter_expenses_flow),
        "5":  ("Category-wise spending", category_spending_flow),
        "6":  ("Monthly report",         monthly_report_flow),
        "7":  ("Highest expense",        highest_expense_flow),
        "8":  ("Smart insights",         smart_insight_flow),
        "9":  ("Update expense",         update_expense_flow),
        "10": ("Delete expense",         delete_expense_flow),
        "11": ("List all users",         list_users_flow),
        "0":  ("Exit",                   None),
    }

    while True:
        print(f"\n===== Expense Manager  [{DB_MODE.upper()}] =====")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("=" * 40)

        choice = input("Select option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in menu:
            _, action = menu[choice]
            action()
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
