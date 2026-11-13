# Demonstração da skill `vulnerability-analysis`

> **Aviso importante:** esta conversa foi feita com o **Claude**, seguindo o `SKILL.md`. **Não foi executada no Hermes.** Serve para mostrar o comportamento esperado da skill (perguntar o contexto antes de agir, uma pergunta por vez, formato fixo de saída). As falas do estudante são reais e estão como foram digitadas. O teste citado na etapa 5 é a saída real de `python lab/teste_sqli.py`.

Código analisado: [`lab/app.py`](../lab/app.py).

---

## Etapa 1: contexto (uma pergunta por vez)

**Agente:** Li o `lab/app.py`. Antes de dizer qualquer coisa sobre ele, preciso entender o contexto, porque a mesma falha pode ter riscos bem diferentes conforme o cenário. Primeira pergunta: esse código é seu e roda só em laboratório, sem dados reais?

**Estudante:** sim

**Agente:** Ótimo, código seu e de laboratório está dentro do escopo. Segunda pergunta: onde esse login roda e quem consegue acessá-lo? Por exemplo: só na sua máquina, numa rede interna ou exposto na internet?

**Estudante:** nao e apenas educacional

**Agente:** Só para não errar o escopo, porque ele muda tudo: sua frase pode ter dois sentidos. "Não, é apenas educacional" (só estudo, na sua máquina, sem dados reais) ou "Não é apenas educacional" (ele tem outro uso além do estudo). Qual das duas é?

**Estudante:** so estudo na minha maquina

---

## Etapas 2 e 3: identificar a falha e avaliar o risco

**Agente:** Entendido: só estudo, na sua máquina. Pelo código, os dados são de teste e não vejo nenhuma defesa por perto. Vou assumir isso e avisar onde o contexto muda a conclusão.

## Análise de vulnerabilidade

- **Ativo:** `lab/app.py`, função de login (Python + SQLite em memória)
- **Contexto:** local, sem exposição, dados de teste, sem defesas adicionais
- **Vulnerabilidade:** SQL Injection. CWE-89, OWASP Top 10 A03:2021 (Injection). Pela técnica do MITRE ATT&CK, T1190 (Exploit Public-Facing Application) só se aplicaria se o login estivesse exposto; aqui vale como referência de estudo.
- **Onde:** na função `login`, a linha que monta `consulta` com f-string, juntando o usuário e a senha digitados direto no texto do SQL
- **Por que é falha:** o banco não consegue separar o que é comando do que é dado. Uma entrada com uma aspa, por exemplo, pode fechar o texto da consulta e mudar o sentido dela.
- **Impacto:** baixo aqui (dados de teste), mas alto em produção (confidencialidade e integridade)
- **Probabilidade:** baixa aqui (só o estudante acessa); seria alta se estivesse na internet
- **Severidade:** baixa neste contexto. A classe da falha continua séria, por isso se corrige mesmo no laboratório.

**Pergunta guia (antes da correção):** o que muda se o texto digitado for passado ao banco como dado, separado do comando? Dica: ver como o `execute` do `sqlite3` aceita valores à parte, usando `?` na consulta.

**Estudante:** segue 4 e 5

---

## Etapa 4: orientar a correção

**Causa raiz:** a entrada é misturada ao comando. O conserto é separar os dois, com consulta parametrizada (não vale bloquear aspas ou palavras suspeitas, que é paliativo).

```python
def login(conn, usuario, senha):
    consulta = "SELECT id FROM usuarios WHERE usuario = ? AND senha = ?"
    return conn.execute(consulta, (usuario, senha)).fetchone() is not None
```

Ações por prioridade:

- **Agora:** usar a consulta parametrizada (versão em [`lab/app_seguro.py`](../lab/app_seguro.py)).
- **Em seguida:** guardar a senha com hash forte e salt (bcrypt, scrypt ou Argon2), não em texto puro (CWE-256).
- **Depois:** limitar tentativas de login (CWE-307), usar conta de banco com o menor privilégio possível e registrar logs das falhas, se o login sair do laboratório.

## Etapa 5: validar

Saída real de `python lab/teste_sqli.py` (ver [`teste-laboratorio.txt`](teste-laboratorio.txt)):

| Caso | `app.py` (vulnerável) | `app_seguro.py` (corrigido) |
|------|-----------------------|------------------------------|
| credenciais corretas | aceito (esperado) | aceito (esperado) |
| senha errada | recusado (esperado) | recusado (esperado) |
| entrada com aspa no usuário | **aceita (falha)** | **recusada (esperado)** |

**Resultado:** a SQL Injection foi mitigada.

**Risco residual:** a senha ainda é guardada em texto puro e não há limite de tentativas. Não é SQL Injection, mas é o próximo ponto a corrigir.

**Teste de regressão sugerido:** manter o `teste_sqli.py` e rodá-lo a cada mudança no login.
