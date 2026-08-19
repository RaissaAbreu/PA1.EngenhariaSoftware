# Prática Avaliada 1 — ES1

## Sobre o projeto

Este repositório contém a implementação da **Prática Avaliada 1 (ES1)** da disciplina de Engenharia de Software.

A atividade aborda três temas principais:

- princípios e valores do **Manifesto Ágil**;
- integração de práticas de **Extreme Programming (XP)** com **Scrum**;
- aplicação do princípio **YAGNI (You Aren't Gonna Need It)** por meio de Design Simples em Python.

A proposta utiliza o cenário da startup **AgileTech Solutions**, que está iniciando o desenvolvimento de um sistema web para gestão de projetos ágeis.

## Objetivos

O trabalho tem como objetivos:

1. Analisar o processo de desenvolvimento da AgileTech Solutions e propor melhorias com base nos princípios ágeis.
2. Estruturar um processo de desenvolvimento combinando práticas de XP e Scrum.
3. Aplicar o princípio YAGNI na simplificação de uma implementação Python.
4. Documentar as decisões tomadas durante a atividade.
5. Organizar o trabalho utilizando o GitHub Projects.

## Estrutura do projeto

```text
PA1.EngenhariaSoftware/
├── .gitignore
├── README.md
├── analise-processo.md
├── processo-xp-scrum.md
├── analise-yagni.md
└── src/
    └── usuario_simples.py
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `README.md` | Documentação geral do projeto. |
| `analise-processo.md` | Análise do Manifesto Ágil, abordagem ágil, práticas ágeis, programação em pares e dificuldades essenciais de Brooks. |
| `processo-xp-scrum.md` | Processo utilizando XP e Scrum, fluxo de trabalho, Sprint e comparação entre Scrum e Kanban. |
| `analise-yagni.md` | Análise das funcionalidades desnecessárias e das violações do princípio YAGNI. |
| `src/usuario_simples.py` | Implementação simplificada do gerenciamento de usuários em Python. |
| `.gitignore` | Arquivos e diretórios que não devem ser versionados. |

## Contexto da atividade

A AgileTech Solutions possui uma equipe pequena, formada por cinco desenvolvedores e um Product Owner. O cliente participa do projeto, mas possui disponibilidade limitada. Os requisitos iniciais são vagos e sujeitos a mudanças frequentes, existe pressão por entregas rápidas e a empresa possui histórico de documentação extensa que rapidamente ficava desatualizada.

Nesse cenário, a atividade propõe uma abordagem ágil, combinando práticas de XP e Scrum e aplicando Design Simples ao desenvolvimento do código.

## Questão 1 — Análise de Processo e Manifesto Ágil

Nesta etapa são analisados os quatro valores do Manifesto Ágil no contexto da AgileTech Solutions, além da escolha de uma abordagem ágil em comparação ao modelo tradicional em cascata.

Também são abordados:

- práticas ágeis que devem ser adotadas;
- programação em pares e seus benefícios;
- desafios da programação em pares em um curso a distância;
- adaptações para equipes remotas;
- dificuldades essenciais de Brooks: complexidade, conformidade, mutabilidade e invisibilidade.

O conteúdo completo está em [`analise-processo.md`](analise-processo.md).

## Questão 2 — Processo XP e Scrum

A segunda etapa estrutura um processo de desenvolvimento combinando XP e Scrum.

São contemplados:

- práticas de XP adotadas pela equipe;
- integração entre XP e Scrum;
- fluxo de trabalho semanal;
- Sprint de duas semanas;
- cerimônias do Scrum;
- aplicação das práticas de XP durante a Sprint;
- comparação entre Scrum e Kanban;
- organização das tarefas no GitHub Projects.

A documentação está em [`processo-xp-scrum.md`](processo-xp-scrum.md).

### GitHub Projects

O quadro Kanban criado para a atividade está disponível em:

[PA1.EngSoftware.RaissaRangel — GitHub Projects](https://github.com/users/RaissaAbreu/projects/3/views/1)

O quadro contém as etapas **Backlog, Ready, In progress, In review e Done**, além das user stories e tarefas utilizadas para representar o fluxo de trabalho.

## Questão 3 — Design Simples e YAGNI

A terceira etapa trabalha o princípio **YAGNI — You Aren't Gonna Need It**.

O objetivo é analisar uma implementação de gerenciamento de usuários que possui funcionalidades além das necessidades atuais e refatorá-la para uma versão mais simples.

A versão final deve manter somente:

- cadastro de usuários com nome, e-mail e senha;
- login validando e-mail e senha;
- listagem de usuários;
- validação de e-mail duplicado;
- validação de senha, podendo utilizar hash.

A análise está em [`analise-yagni.md`](analise-yagni.md) e a implementação está em [`src/usuario_simples.py`](src/usuario_simples.py).

## Tecnologias e ferramentas

- **Python** — implementação do sistema de usuários;
- **Markdown** — documentação;
- **Git/GitHub** — versionamento;
- **GitHub Projects** — organização do fluxo de trabalho.

## Execução

Após clonar o repositório, entre no diretório do projeto e execute:

```bash
python src/usuario_simples.py
```

A implementação deve disponibilizar as funcionalidades básicas solicitadas: cadastro de usuários, login e listagem.

## Organização do trabalho

O desenvolvimento segue a proposta da atividade, buscando aplicar princípios ágeis e manter o código simples, objetivo e alinhado aos requisitos atuais.

O GitHub Projects é utilizado para representar o fluxo de trabalho da equipe e organizar as user stories e tarefas relacionadas ao desenvolvimento.

## Referência

Este README foi elaborado com base no enunciado da **Prática Avaliada 1 — ES1**, que define os requisitos, critérios de avaliação, estrutura de arquivos e funcionalidades esperadas para o trabalho.
