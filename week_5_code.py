import math
import os
import csv
import mysql.connector

from datetime import datetime
from datetime import date

# ---------------- DATABASE CONNECTION ----------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="calculator_db"
)

# Adding buffered=True fixes the "Unread result" error
cursor = connection.cursor(buffered=True)

# ---------------- FUNCTIONS ----------------

def clear_screen():
    # 'nt' means Windows. If it's not Windows, it assumes Mac/Linux and uses 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def checkUserExists(username, password):
    query = "SELECT user_id FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result[0] if result else None

def add_log(user_id, calculation, result, timestamp):
    insert_sql = """
        INSERT INTO logs (user_id, calculation, result, timestamp)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_sql, (user_id, calculation, str(result), timestamp))
    connection.commit()

def search_logs_by_username(username):
    query = """
        SELECT users.username, logs.calculation, logs.result, logs.timestamp
        FROM logs
        JOIN users ON logs.user_id = users.user_id
        WHERE users.username = %s
    """
    cursor.execute(query, (username,))
    return cursor.fetchall()

def export_logs_to_csv(logs, filename="exported_logs.csv"):
    if not logs:
        print("No logs found. CSV will NOT be created.")
        return
    
    keys = ["username", "calculation", "result", "timestamp"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        
        for row in logs:
            row_dict = dict(zip(keys, row))
            writer.writerow(row_dict)

    print(f"CSV exported successfully: {filename}")

# ---------------- LOGIN ----------------
while True:
    print("\n********** Login System **********")
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_id = checkUserExists(username, password)

    if user_id:
        print("Successfully logged in")
        break
    else:
        print("Wrong username or password")

# ---------------- MAIN CALCULATOR LOOP ----------------
while True:
    # ---------------- MENU ----------------
    print("\nSelect an operation")
    print("1. + for addition")
    print("2. - for subtraction")
    print("3. * for multiplication")
    print("4. / for division")
    print("5. sin for sine")
    print("6. cos for cosine")
    print("7. tan for tangent")
    print("8. log for logarithm")
    print("9. sqrt for square root")
    print("10. square")
    print("11. exp for exponent")
    print("12. sei (string equation)")
    print("13. search logs")
    print("0. exit")

    operation = input("Select an option: ")

    # REAL EXIT
    if operation == "0":
        print("Calculator Closed")
        break  # Drops out of the loop to run the export logic

    # INPUT VALIDATION
    if not operation.isdigit() or int(operation) > 13:
        print("Invalid option")
        continue  # Restarts the menu instead of crashing

    num1 = None
    num2 = None
    answer = None

    # ---------------- CALCULATOR ----------------

    if operation == "1":
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        answer = num1 + num2

    elif operation == "2":
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        answer = num1 - num2

    elif operation == "3":
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        answer = num1 * num2

    elif operation == "4":
        num1 = float(input("Numerator: "))
        num2 = float(input("Denominator: "))
        if num2 == 0:
            print("Division by zero error")
            continue  # Restarts the menu instead of crashing
        answer = num1 / num2

    elif operation == "5":
        num1 = float(input("Number: "))
        answer = math.sin(math.radians(num1))

    elif operation == "6":
        num1 = float(input("Number: "))
        answer = math.cos(math.radians(num1))

    elif operation == "7":
        num1 = float(input("Number: "))
        answer = math.tan(math.radians(num1))

    elif operation == "8":
        num1 = float(input("Number: "))
        num2 = float(input("Base: "))
        answer = math.log(num1, num2)

    elif operation == "9":
        num1 = float(input("Number: "))
        answer = math.sqrt(num1)

    elif operation == "10":
        num1 = float(input("Number: "))
        answer = num1 ** 2

    elif operation == "11":
        num1 = float(input("Base: "))
        num2 = float(input("Power: "))
        answer = num1 ** num2

    elif operation == "12":
        expr = input("Insert equation: ")
        # =========================================================
        # SECURITY NOTE: eval() is used here strictly for local demo 
        # purposes. In production, this must be replaced with a secure 
        # parser to prevent Arbitrary Code Execution (ACE).
        # =========================================================
        answer = eval(expr)

    elif operation == "13":
        search_username = input("Username to search: ")
        logs = search_logs_by_username(search_username)
        if logs:
            for log in logs:
                print(f"{log[0]} | {log[1]} = {log[2]} @ {log[3]}")
        else:
            print("No logs found")

        # ----------- Pause after output and logging -----------
        input("\nPress Enter to continue...")
        clear_screen()
        continue  # Restarts the menu instead of crashing

    print("Answer:", answer)

    # ---------------- LOGGING ----------------
    operation_map = (
        "+", "-", "*", "/", "sin", "cos", "tan",
        "log", "sqrt", "square", "exp", "sei"
    )

    # Fix: If it's a string equation (12), use the actual equation text
    if operation == "12":
        calc_string = f"Expression: {expr}"
    else:
        calc_string = str(num1) + " " + operation_map[int(operation)-1]
        if num2 is not None:
            calc_string += " " + str(num2)

    add_log(user_id, calc_string, answer, datetime.now())

# ----------- Pause after output and logging -----------
    input("\nPress Enter to continue...")
    clear_screen()

# ---------------- EXPORT ----------------
# This section now safely runs only after you press '0' to exit the loop
logs = search_logs_by_username(username)

export_choice = input("\nExport logs to CSV? (yes/no): ").lower()
if export_choice == "yes":
    filename = "logs_" + date.today().strftime('%d_%m_%Y') + ".csv"
    export_logs_to_csv(logs, filename)

print("Program finished successfully.")

# Clean up database connections
cursor.close()
connection.close()
