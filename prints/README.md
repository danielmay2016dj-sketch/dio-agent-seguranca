# Evidências

## Teste do laboratório (saída real)

`teste-laboratorio.png` e `teste-laboratorio.txt` são a saída real de `python lab/teste_sqli.py`: o login vulnerável (`app.py`) aceita a entrada com aspa, e o corrigido (`app_seguro.py`) a recusa. Este teste valida o **código**, não o agente.

## Diagramas do projeto

Diagramas gerados para explicar o processo (não são prints de tela):

- `diagrama-skill.png`: as 5 etapas da skill, o formato fixo de saída e as regras defensivas.
- `diagrama-arquivos.png`: arquivos criados e alterados, e o resultado do teste do laboratório.

## Prints do agente no Hermes (a adicionar)

Coloque aqui os prints da sua execução no Hermes, abertos na pasta do projeto:

1. a análise do `lab/app.py` feita pelo agente;
2. as perguntas de contexto que ele faz antes de sugerir comandos (cenário do servidor Ubuntu de laboratório);
3. se quiser, a mesma pergunta em um chat genérico, para comparar.
