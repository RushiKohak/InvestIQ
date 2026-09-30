import sqlite3
import sys
import pandas as pd


DATABASE = "data/investment_analytics.db"


if len(sys.argv) < 2:
    print("Usage: python run_sql.py <sql_file>")
    sys.exit(1)


sql_file = sys.argv[1]


with open(sql_file, "r", encoding="utf-8") as file:
    sql_script = file.read()


# Split SQL file into individual statements
statements = [
    statement.strip()
    for statement in sql_script.split(";")
    if statement.strip()
]


connection = sqlite3.connect(DATABASE)


try:

    for i, statement in enumerate(statements, start=1):

        # Skip comments-only sections
        cleaned = "\n".join(
            line
            for line in statement.splitlines()
            if not line.strip().startswith("--")
        ).strip()

        if not cleaned:
            continue

        print("\n" + "=" * 70)
        print(f"RESULT {i}")
        print("=" * 70)

        result = pd.read_sql_query(
            cleaned,
            connection
        )

        print(result.to_string(index=False))

finally:

    connection.close()