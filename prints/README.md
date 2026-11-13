# Evidências

## Teste do laboratório (saída real)

`teste-laboratorio.png` e `teste-laboratorio.txt` são a saída real de `python lab/teste_sqli.py`: o login vulnerável (`app.py`) aceita a entrada com aspa, e o corrigido (`app_seguro.py`) a recusa. Este teste valida o **código**, não o agente.

## Diagramas do projeto

Diagramas gerados para explicar o processo (não são prints de tela):

- `diagrama-skill.png`: as 5 etapas da skill, o formato fixo de saída e as regras defensivas.
- `diagrama-arquivos.png`: arquivos criados e alterados, e o resultado do teste do laboratório.

## Demonstração da skill (feita com o Claude, não com o Hermes)

`demonstracao-skill.md` mostra a skill de ponta a ponta: perguntas de contexto, análise no formato fixo, correção e validação. Foi conduzida com o Claude seguindo o `SKILL.md`, **não com o Hermes**, e o aviso está no topo do arquivo.

