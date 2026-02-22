# Python & SQL Data Logger 

## 📌 Overview
A functional backend architecture project designed to demonstrate the integration between Python-based mathematical logic and a MySQL relational database. It includes user authentication, error handling, session data persistence, and automated analytics reporting.

### 🎥 Visual Demonstrations

**1. The Backend Engine (Terminal & Real-Time SQL Sync)**
> ![Backend Operations](backend_demo.gif)
> *(Note: The terminal executes the Python logic and parses complex string equations, while HeidiSQL confirms the dynamic transaction logging in real-time).*

**2. The Analytics Pipeline (Data Parsing & Reporting)**
> ![Analytics Dashboard](analytics_demo.gif)
> *(Note: A decoupled Python script processing the dynamically generated CSV files to calculate delivery engineering metrics like total transactions and unique active users).*

## 🚀 Core Features
* **Authentication System:** Secure login validation before granting access to the calculator engine.
* **Normalized Database Architecture:** All transactions are securely recorded in MySQL using normalized relational integrity (linking internal `user_id` foreign keys to human-readable tables).
* **Dynamic CLI UX:** Cross-platform terminal screen clearing (`os.system`) and persistent `while` loops to trap invalid inputs and provide a seamless, software-like user experience.
* **Exception Handling:** Built-in safeguards against mathematical exceptions (e.g., division by zero) and file-not-found errors during reporting.
* **Multi-Tenant Data Export:** Queries user-specific logs and exports them to isolated, dynamically named CSV formats (e.g., `logs_admin_22_02_2026.csv`) to prevent cross-user data overwriting.
* **Automated Reporting Module:** A standalone analytics script (`analytics_dashboard.py`) that parses exported CSV logs to generate instant, terminal-based metrics (tracking active users, total transactions, and latest system activity).

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** MySQL
* **Libraries:** `mysql.connector`, `math`, `csv`, `datetime`, `os`

## 🧠 Engineering Focus
The primary goal of this project was mastering the **Fundamentals** of data persistence, secure database connections, 3rd Normal Form (3NF) relational database structures, cross-platform CLI user experience, and backend logic flow.

## 🗺️ Future Roadmap (V2.0)
To scale this application for a secure production environment, the following features are planned for the next sprint:
* **Security Hardening (ACE Prevention):** Replacing the built-in `eval()` function with a secure mathematical parser (e.g., `ast.literal_eval` or SymPy) to prevent Arbitrary Code Execution vulnerabilities.
* **Cryptographic Password Hashing:** Upgrading the current local testing credentials to a secure hashing algorithm (like `bcrypt` or `SHA-256`) prior to database insertion.
* **Role-Based Access Control (RBAC):** Implementing `Admin` vs `Standard User` permissions, restricting standard users to querying only their own session logs.
* **Full CRUD Functionality:** Allowing Admins to permanently delete or archive legacy logs to optimize database query speeds.
