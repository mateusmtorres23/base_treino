from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        table_exists = connection.execute(
            "SELECT 1 FROM sqlite_master "
            "WHERE type = 'table' AND name = 'produtos'"
        ).fetchone()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK (preco >= 0),
                quantidade INTEGER NOT NULL CHECK (quantidade >= 0)
            )
        """)

        if table_exists is None:
            connection.executemany(
                """
                INSERT INTO produtos (nome, preco, quantidade)
                VALUES (?, ?, ?)
                """,
                [
                    ("Caderno", 15.90, 20),
                    ("Caneta", 2.50, 50),
                ],
            )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")