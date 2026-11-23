import os
import sqlite3


def get_connection():
    database_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "produtos.db"
    )

    return sqlite3.connect(database_path)