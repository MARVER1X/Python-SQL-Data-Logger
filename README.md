# Python & SQL Data Logger 

## 📌 Overview
A functional backend architecture project designed to demonstrate the integration between Python-based mathematical logic and a MySQL relational database. It includes user authentication, error handling, session data persistence, and automated analytics reporting.

> **Visual Proof: Terminal Execution & Real-Time SQL Logging**
> ![Python SQL Demo](python_sql_demo.gif)
> *(Note: The terminal executes the Python logic, while HeidiSQL confirms the dynamic transaction logging in real-time).*

## 🚀 Core Features
* **Authentication System:** Secure login validation before granting access to the calculator engine.
* **Relational Database Logging:** All transactions are recorded in MySQL, including timestamps, specific operational logic, and user IDs.
* **Dynamic CLI UX:** Cross-platform terminal screen clearing (`os.system`) and persistent `while` loops to trap invalid inputs without crashing the application.
* **Exception Handling:** Built-in safeguards against mathematical exceptions (e.g., division by zero) and file-not-found errors during reporting.
* **Data Export:** Functionality to query user-specific logs and export them to dynamically named CSV formats for external analysis.
* **Automated Reporting Module:** Includes a standalone Python script (`analytics_dashboard.py`) that parses exported CSV logs to generate instant, terminal-based Delivery Engineering metrics (tracking active users, total transactions, and latest system activity).

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** MySQL
* **Libraries:** `mysql.connector`, `math`, `csv`, `datetime`, `os`

## 🧠 Engineering Focus
The primary goal of this project was mastering the **Fundamentals** of data persistence, secure database connections, cross-platform CLI user experience, and backend logic flow.

## 🗺️ Future Roadmap (V2.0)
To scale this application for a secure production environment, the following features are planned for the next sprint:
* **Security Hardening (ACE Prevention):** Replacing the built-in `eval()` function with a secure mathematical parser (e.g., `ast.literal_eval` or SymPy) to prevent Arbitrary Code Execution vulnerabilities.
* **Cryptographic Password Hashing:** Upgrading the current local testing credentials to a secure hashing algorithm (like `bcrypt` or `SHA-256`) prior to database insertion.
* **Role-Based Access Control (RBAC):** Implementing `Admin` vs `Standard User` permissions, restricting standard users to querying only their own session logs.
* **Full CRUD Functionality:** Allowing Admins to permanently delete or archive legacy logs to optimize database query speeds.
