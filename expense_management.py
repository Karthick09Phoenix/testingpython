import pyodbc
from datetime import datetime

# Database connection details
server = 'KARTHICK\SQLEXPRESS'  
database = 'ExpenseDB'
username = 'sa'
password = 'uno'

# Establishing the connection
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

def add_expense(amount, category, date, description):
    cursor.execute("INSERT INTO Expenses (Amount, Category, Date, Description) VALUES (?, ?, ?, ?)",
                   (amount, category, date, description))
    conn.commit()
    print("Expense added successfully.")

def view_expenses():
    cursor.execute("SELECT * FROM Expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(f"ID: {expense.Id}, Amount: {expense.Amount}, Category: {expense.Category}, Date: {expense.Date}, Description: {expense.Description}")

def update_expense(expense_id, amount, category, date, description):
    cursor.execute("UPDATE Expenses SET Amount = ?, Category = ?, Date = ?, Description = ? WHERE Id = ?",
                   (amount, category, date, description, expense_id))
    conn.commit()
    print("Expense updated successfully.")

def delete_expense(expense_id):
    cursor.execute("DELETE FROM Expenses WHERE Id = ?", (expense_id,))
    conn.commit()
    print("Expense deleted successfully.")

# Main menu
def main_menu():
    while True:
        print("\nExpense Management System")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), '%Y-%m-%d')
            description = input("Enter description: ")
            add_expense(amount, category, date, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter expense ID to update: "))
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            date = datetime.strptime(input("Enter new date (YYYY-MM-DD): "), '%Y-%m-%d')
            description = input("Enter new description: ")
            update_expense(expense_id, amount, category, date, description)

        elif choice == '4':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

# Closing the connection
cursor.close()
conn.close()

#finished by karthick