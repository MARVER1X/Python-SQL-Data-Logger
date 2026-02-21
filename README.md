# Python & SQL Data Logger 

## Overview
This is a functional backend architecture project designed to demonstrate the integration between Python-based mathematical logic and a MySQL relational database. It includes user authentication, error handling, and session data persistence.

## Core Features
* **Authentication System:** Secure login validation before access to the calculator engine.
* **Relational Database Logging:** All transactions are recorded in MySQL, including timestamps and specific operational logic.
* **Exception Handling:** Built-in safeguards against mathematical exceptions (e.g., division by zero).
* **Data Export:** Functionality to query user-specific logs and export them to CSV formats for external analysis.
* **Automated Reporting Module:** Includes a standalone Python script (analytics_dashboard.py) that parses exported CSV logs to generate instant, terminal-based metric summaries (tracking active users, total transactions, and latest system activity).

## Tech Stack
* **Language:** Python
* **Database:** MySQL
* **Libraries:** `mysql.connector`, `math`, `csv`, `datetime`

## Engineering Focus
The primary goal of this project was mastering the **Fundamentals** of data persistence, secure database connections, and backend logic flow.
