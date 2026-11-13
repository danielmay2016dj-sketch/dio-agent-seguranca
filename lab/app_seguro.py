"""Laboratório: mesmo login, CORRIGIDO com consulta parametrizada.

Código de estudo. A entrada da pessoa é passada como dado (parâmetro),
nunca como parte do comando SQL.
"""
import sqlite3


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    conn.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha-de-laboratorio')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # CORREÇÃO: placeholders (?) separam o comando dos dados.
    consulta = "SELECT id FROM usuarios WHERE usuario = ? AND senha = ?"
    return conn.execute(consulta, (usuario, senha)).fetchone() is not None


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print("Login OK" if login(conn, usuario, senha) else "Login negado")
