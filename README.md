# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidade](skills/vulnerability-analysis/SKILL.md) | Conduz a análise de uma falha de segurança: pergunta o contexto, avalia impacto, probabilidade e severidade e orienta a correção | "Esse login monta o SQL juntando o que digitam. Analisa pra mim?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀

---

## 🛡️ Especialização em cibersegurança (desafio DIO)

Esta versão do DIO Agent ganhou uma especialização em **análise de vulnerabilidades**. Nenhum modelo foi treinado: o agente aprende só pelo que está escrito nos arquivos.

### A especialização e o porquê

Em vez de responder direto ("está vulnerável, use isto"), o agente conduz a análise como um profissional de segurança: **pergunta o contexto primeiro**, avalia **impacto, probabilidade e severidade** e orienta a correção. Em segurança, a mesma falha tem riscos muito diferentes conforme a exposição, os dados e as defesas. Responder sem contexto leva a conselhos genéricos ou errados. A abordagem também mantém o espírito do DIO Agent: ensinar a pensar, não entregar resposta pronta.

### Arquivos criados ou alterados

| Arquivo | O que é |
|---------|---------|
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | Roteiro de 5 etapas que o agente segue (contexto, falha, risco, correção, validação) |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | Explicação da skill para pessoas |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | Vulnerabilidade, ameaça, risco, tríade CIA, matriz de severidade e boas práticas |
| [`agent/persona.md`](agent/persona.md) | Alterado: seção "Modo mentor de cibersegurança" |
| [`AGENTS.md`](AGENTS.md) | Alterado: linha da skill na tabela e arquivo de conhecimento listado |
| `README.md` | Alterado: skill na tabela e esta seção |
| [`lab/app.py`](lab/app.py), [`lab/app_seguro.py`](lab/app_seguro.py) e [`lab/teste_sqli.py`](lab/teste_sqli.py) | Login de laboratório vulnerável a SQL Injection, a versão corrigida (consulta parametrizada) e um teste que compara os dois |
| [`prints/`](prints/README.md) | Evidências da execução no agente |

### Como rodar o agente no harness (Hermes)

1. Instale o Hermes pela [documentação oficial](https://hermes-agent.nousresearch.com/docs).
2. Clone este repositório: `git clone https://github.com/danielmay2016dj-sketch/dio-agent-seguranca.git`.
3. **Abra o terminal na pasta do projeto** e rode `hermes`. Aberto em outro lugar, ele não encontra os arquivos.
4. Teste:
   - "Atue como especialista em AppSec, analise o `lab/app.py`, encontre a falha, explique a exploração, cite a técnica do MITRE ATT&CK e proponha a correção."
   - Aplique a consulta parametrizada (`lab/app_seguro.py`) e peça uma nova varredura para confirmar a mitigação.
   - Descreva um cenário ("servidor Ubuntu de laboratório exposto na internet") e confira que o agente **pergunta o contexto antes de sugerir comandos**.

### Melhoria escolhida

**Saída sempre no mesmo formato** (ativo, contexto, vulnerabilidade, onde, impacto, probabilidade, severidade, correção, validação e risco residual), com a matriz de severidade em `security-basics.md`. Assim os casos podem ser comparados entre si.

### Segurança e ética

Todos os testes usam apenas código e servidores **meus, de laboratório**. A skill recusa analisar sistemas de terceiros sem autorização e não gera payloads prontos nem roteiros de ataque.

### Evidências

- Teste do laboratório (saída real do código): [`prints/teste-laboratorio.png`](prints/teste-laboratorio.png) e [`prints/teste-laboratorio.txt`](prints/teste-laboratorio.txt). O login vulnerável aceita a entrada com aspa e o corrigido a recusa. Gerado com `python lab/teste_sqli.py`.
- Diagramas do processo: [`prints/diagrama-skill.png`](prints/diagrama-skill.png) (as 5 etapas) e [`prints/diagrama-arquivos.png`](prints/diagrama-arquivos.png) (arquivos e resultado do teste). São diagramas, não prints de tela.
