"""Teste de laboratório: compara o login vulnerável (app.py) com o corrigido (app_seguro.py).

Roda só localmente, com banco SQLite em memória e dados de laboratório.
Uso: python lab/teste_sqli.py
"""
import app
import app_seguro

CASOS = [
    ("credenciais corretas", "admin", "senha-de-laboratorio", True),
    ("senha errada", "admin", "errada", False),
    ("entrada com aspa no usuário", "admin' --", "qualquer", False),
]


def rodar(nome, modulo):
    print(f"== {nome} ==")
    conn = modulo.criar_banco()
    falhas = 0
    for descricao, usuario, senha, esperado in CASOS:
        obtido = modulo.login(conn, usuario, senha)
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print(f"  [{'OK' if ok else 'FALHA'}] {descricao}: login={obtido} (esperado={esperado})")
    return falhas


if __name__ == "__main__":
    f1 = rodar("app.py (vulnerável)", app)
    f2 = rodar("app_seguro.py (corrigido)", app_seguro)
    print()
    print(f"Vulnerável: {f1} caso(s) com comportamento inesperado")
    print(f"Corrigido:  {f2} caso(s) com comportamento inesperado")
