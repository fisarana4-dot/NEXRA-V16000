import sqlite3
from pathlib import Path
DB = Path(__file__).resolve().parents[2] / "data"
DB /= "review_intelligence.db"

def initialize() -> None:
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    try:
        with con:
            con.execute("PRAGMA foreign_keys = ON")
            con.execute(
                "CREATE TABLE IF NOT EXISTS clients ("
                "id INTEGER PRIMARY KEY, name TEXT NOT NULL)"
            )
            con.execute(
                "CREATE TABLE IF NOT EXISTS reviews ("
                "id INTEGER PRIMARY KEY,"
                "client_id INTEGER NOT NULL REFERENCES clients(id)," 
                "rating REAL NOT NULL CHECK (rating BETWEEN 0 AND 5)," 
                "feedback TEXT)"
            )
    finally:
        con.close()

if __name__ == "__main__":
    initialize()
    print(f"Initialized {DB}")
