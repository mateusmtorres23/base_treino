from contextlib import closing

from database.connection import get_connection
from entities.entity import Produto


class DAOEntity:

    def create(self, produto: Produto) -> Produto:
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                """
                INSERT INTO produtos (nome, preco, quantidade)
                VALUES (?, ?, ?)
                """,
                (produto.nome, produto.preco, produto.quantidade),
            )
            conn.commit()

            produto.id = cursor.lastrowid
            return produto

    def find_all(self) -> list[Produto]:
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                "SELECT id, nome, preco, quantidade FROM produtos"
            )
            rows = cursor.fetchall()

            return [
                Produto(
                    id=row[0],
                    nome=row[1],
                    preco=row[2],
                    quantidade=row[3],
                )
                for row in rows
            ]

    def find_by_id(self, produto_id: int) -> Produto | None:
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                """
                SELECT id, nome, preco, quantidade
                FROM produtos
                WHERE id = ?
                """,
                (produto_id,),
            )
            row = cursor.fetchone()

            if row is None:
                return None

            return Produto(
                id=row[0],
                nome=row[1],
                preco=row[2],
                quantidade=row[3],
            )

    def update(self, produto: Produto) -> bool:
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                """
                UPDATE produtos
                SET nome = ?, preco = ?, quantidade = ?
                WHERE id = ?
                """,
                (
                    produto.nome,
                    produto.preco,
                    produto.quantidade,
                    produto.id,
                ),
            )
            conn.commit()

            return cursor.rowcount == 1

    def delete(self, produto_id: int) -> bool:
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                "DELETE FROM produtos WHERE id = ?",
                (produto_id,),
            )
            conn.commit()

            return cursor.rowcount == 1