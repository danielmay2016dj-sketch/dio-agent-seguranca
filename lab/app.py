"""Laboratório: login VULNERÁVEL a SQL Injection.

Código de estudo, criado pelo próprio autor para testar o agente.
NÃO use em produção. Roda só localmente, com banco SQLite em memória.
"""
import sqlite3


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    conn.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha-de-laboratorio')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # FALHA: o SQL é montado juntando o que a pessoa digitou.
    consulta = f"SELECT id FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
    return conn.execute(consulta).fetchone() is not None


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print("Login OK" if login(conn, usuario, senha) else "Login negado")
