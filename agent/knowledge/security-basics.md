# Fundamentos de segurança

Arquivo de conhecimento usado pela skill `vulnerability-analysis`. Consulte-o para manter os conceitos e os critérios consistentes entre análises.

## Conceitos-chave

| Termo | Significado | Exemplo |
|-------|-------------|---------|
| **Vulnerabilidade** | Fraqueza em um sistema, código ou configuração que pode ser explorada | Login que monta o SQL juntando o texto digitado |
| **Ameaça** | Qualquer coisa ou alguém que pode explorar uma vulnerabilidade | Pessoa mal-intencionada, malware, erro humano |
| **Exploração (exploit)** | O ato ou a técnica de aproveitar uma vulnerabilidade | Entrada que altera o sentido da consulta |
| **Risco** | Chance de uma ameaça explorar uma vulnerabilidade somada ao dano que isso causa | Vazamento de dados de clientes |
| **Controle** | Medida que reduz o risco | Consulta parametrizada, firewall, MFA, backup |

Relação resumida: **risco = ameaça × vulnerabilidade × impacto**. Sem vulnerabilidade ou sem ameaça plausível, o risco cai.

## Tríade CIA

| Pilar | Pergunta | Exemplo de quebra |
|-------|----------|-------------------|
| **Confidencialidade** | Só quem deve vê a informação? | Vazamento de senhas ou dados pessoais |
| **Integridade** | A informação continua correta e sem alteração indevida? | Registro modificado por quem não tinha permissão |
| **Disponibilidade** | O sistema está acessível quando preciso? | Serviço derrubado, dados apagados ou criptografados |

Ao avaliar o impacto, diga **quais pilares** são afetados.

## Critérios de classificação

**Impacto:** baixo (incômodo, sem dado sensível), médio (dado limitado ou serviço degradado), alto (dado sensível ou parada relevante), crítico (comprometimento total, dados em massa ou risco à operação).

**Probabilidade:** baixa (exige acesso privilegiado ou condições raras), média (exige alguma condição, como estar na rede), alta (exposta na internet, fácil de explorar, sem defesa).

### Matriz de severidade

| Probabilidade \ Impacto | Baixo | Médio | Alto | Crítico |
|-------------------------|-------|-------|------|---------|
| **Baixa** | Baixa | Baixa | Média | Alta |
| **Média** | Baixa | Média | Alta | Alta |
| **Alta** | Média | Alta | Alta | Crítica |

Esta matriz é um guia, não uma regra absoluta. Sempre justifique a classificação com o contexto.

## Referências para citar

- **CWE:** catálogo de tipos de fraqueza. Exemplos: CWE-89 (SQL Injection), CWE-798 (credencial fixa no código), CWE-306 (falta de autenticação em função crítica).
- **OWASP Top 10:** categorias de risco em aplicações web. SQL Injection está em A03:2021 (Injection).
- **MITRE ATT&CK:** táticas e técnicas de ataque. Exemplo: T1190 (Exploit Public-Facing Application) para exploração de aplicação exposta.
- Se não tiver certeza de um identificador, **diga isso** em vez de inventar.

## Boas práticas

1. **Menor privilégio:** cada usuário, serviço e conta de banco com apenas o acesso necessário.
2. **Defesa em profundidade:** várias camadas, para que a falha de uma não derrube tudo.
3. **Nunca confiar na entrada:** validar e tratar como dado, nunca como comando (consultas parametrizadas, escape correto por contexto).
4. **Segredos fora do código:** senhas e chaves em variáveis de ambiente ou cofre.
5. **Senhas com hash forte e salt:** bcrypt, scrypt ou Argon2, nunca texto puro nem hash rápido.
6. **Atualizações em dia** e remoção de serviços e portas desnecessários.
7. **Logs e monitoramento** para detectar e investigar incidentes.
8. **Backups testados** e separados do ambiente principal.
9. **Mensagens de erro genéricas** para o usuário, detalhes só nos logs.
10. **Revisão de segurança antes da produção** (DevSecOps).

## Ética e escopo

Analise apenas o que é seu ou está autorizado. Testes só em ambiente de laboratório próprio.
