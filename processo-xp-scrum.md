# Processo XP e Scrum

## 1. Objetivo

A AgileTech Solutions decidiu combinar práticas de **Extreme Programming (XP)** com o framework **Scrum** para organizar o desenvolvimento do sistema web de gestão de projetos ágeis.

A proposta é utilizar o Scrum principalmente para organizar o trabalho, definir ciclos de desenvolvimento e estabelecer momentos de planejamento, acompanhamento e inspeção. As práticas de XP serão utilizadas para orientar a forma como o software será desenvolvido, buscando qualidade técnica, simplicidade, feedback frequente e colaboração entre os desenvolvedores.

---

## 2. Práticas de XP adotadas

A equipe adotará as seguintes práticas de Extreme Programming:

### 2.1 Programação em pares

Duas pessoas trabalham juntas na implementação de uma funcionalidade. Enquanto uma desenvolve, a outra acompanha, revisa e contribui com sugestões. Os papéis podem ser alternados.

Essa prática favorece a revisão contínua do código, o compartilhamento de conhecimento e a identificação antecipada de problemas.

### 2.2 Desenvolvimento orientado a testes

A equipe deve utilizar testes para verificar se as funcionalidades implementadas atendem aos comportamentos esperados. Os testes ajudam a detectar regressões e dão maior segurança para realizar alterações no código.

### 2.3 Refatoração

A equipe deve melhorar continuamente a estrutura interna do código sem alterar o comportamento esperado das funcionalidades. A refatoração ajuda a evitar que pequenas alterações acumulem complexidade desnecessária.

### 2.4 Integração contínua

As alterações devem ser integradas ao repositório com frequência. Dessa maneira, possíveis conflitos e problemas de integração podem ser identificados mais cedo, evitando que grandes quantidades de código permaneçam isoladas durante muito tempo.

### 2.5 Design simples

A equipe deve implementar apenas o que é necessário para atender aos requisitos atuais, evitando funcionalidades especulativas e complexidade antecipada. Essa prática está diretamente relacionada ao princípio YAGNI, utilizado também na Questão 3.

### 2.6 Propriedade coletiva do código

O código pertence à equipe como um todo. Dessa forma, os desenvolvedores podem contribuir em diferentes partes do sistema e o conhecimento não fica concentrado em uma única pessoa.

---

## 3. Integração entre XP e Scrum

Scrum e XP podem ser utilizados de maneira complementar porque possuem focos diferentes.

O **Scrum** fornece uma estrutura para organizar o trabalho, utilizando elementos como Product Backlog, Sprint, planejamento, Daily Scrum, Sprint Review e Sprint Retrospective.

O **XP**, por sua vez, contribui principalmente com práticas técnicas e de desenvolvimento, como programação em pares, testes, refatoração, integração contínua e design simples.

Na AgileTech Solutions, o Scrum será utilizado para organizar o que deve ser feito e acompanhar a evolução da Sprint. As práticas de XP serão utilizadas para definir como o trabalho de desenvolvimento será realizado.

Essa combinação permite que a equipe tenha um processo organizado sem abrir mão de práticas técnicas voltadas à qualidade do software.

---

## 4. Quadro Kanban no GitHub Projects

O GitHub Projects será utilizado para visualizar o fluxo de trabalho da equipe. O quadro está organizado nas seguintes colunas:

| Coluna | Objetivo |
|---|---|
| Backlog | Reúne as user stories e tarefas que ainda não foram iniciadas. |
| Ready | Contém os itens preparados para serem selecionados para desenvolvimento. |
| In progress | Itens que estão sendo implementados pela equipe. |
| In review | Itens que aguardam revisão, validação ou integração. |
| Done | Itens que atenderam aos critérios definidos e foram finalizados. |

### Cards do quadro

O quadro contém os seguintes cinco cards:

1. **Cadastro de Usuário** — Como usuário, quero realizar meu cadastro para poder acessar o sistema.
2. **Login de Usuário** — Como usuário, quero fazer login com meu e-mail e senha para acessar minha conta.
3. **Listagem de Usuário** — Como administrador, quero visualizar os usuários cadastrados para acompanhar os registros do sistema.
4. **Criar Projeto** — Como usuário, quero criar um projeto para organizar meu trabalho.
5. **Visualizar Projeto** — Como usuário, quero visualizar as informações de um projeto para acompanhar seu andamento.

Os cards estão distribuídos no quadro de acordo com o estágio atual do fluxo de trabalho.

### Link para o GitHub Projects

[PA1.EngSoftware.RaissaRangel — GitHub Projects](https://github.com/users/RaissaAbreu/projects/3/views/1)

---

## 5. Fluxo de trabalho semanal

Embora a Sprint tenha duração de duas semanas, a equipe terá uma rotina semanal de acompanhamento.

### Segunda-feira — Planejamento e organização

No início do ciclo, a equipe revisa os itens prioritários e define quais atividades serão realizadas. As tarefas são detalhadas e distribuídas entre os desenvolvedores de acordo com a capacidade da equipe.

### Terça a quinta-feira — Desenvolvimento

Durante os dias de desenvolvimento, a equipe trabalha nas tarefas selecionadas. As práticas de XP são aplicadas continuamente, especialmente programação em pares, testes, integração contínua, refatoração e design simples.

Todos os dias ocorre uma **Daily Scrum** curta para verificar o progresso, identificar impedimentos e alinhar as próximas atividades.

### Sexta-feira — Acompanhamento e melhoria

Ao final da semana, a equipe verifica o andamento dos itens da Sprint e identifica possíveis ajustes necessários.

Quando houver uma entrega ou incremento relevante, ele poderá ser demonstrado ao Product Owner e aos envolvidos. A equipe também registra pontos que deverão ser considerados para melhorar o próximo ciclo.

---

## 6. Sprint de duas semanas

A Sprint terá duração de **duas semanas**. O objetivo é produzir um incremento funcional do sistema ao final do período.

### Cronograma

| Período | Atividade | Duração sugerida | Participantes |
|---|---|---:|---|
| Dia 1 | Sprint Planning | 2 horas | Product Owner e equipe de desenvolvimento |
| Dias 1–10 | Desenvolvimento | 10 dias úteis | Equipe de desenvolvimento |
| Dias 1–10 | Daily Scrum | 15 min/dia | Equipe de desenvolvimento e, quando necessário, Product Owner |
| Dias 1–10 | Programação em pares | Conforme necessidade | Desenvolvedores |
| Dias 1–10 | Testes | Durante o desenvolvimento | Desenvolvedores |
| Dias 1–10 | Integração contínua | Contínua | Desenvolvedores |
| Dias 1–10 | Refatoração | Conforme necessidade | Desenvolvedores |
| Dia 10 | Sprint Review | 1 hora | Product Owner, equipe e interessados |
| Dia 10 | Sprint Retrospective | 1 hora | Equipe de desenvolvimento e Scrum Master |

Os horários são sugestões de organização e podem ser ajustados de acordo com a disponibilidade da equipe.

---

## 7. Aplicação das práticas de XP durante a Sprint

As práticas de XP não ficarão restritas a um dia específico da Sprint. Elas serão utilizadas durante todo o desenvolvimento.

No início de cada tarefa, a equipe define claramente o comportamento esperado. Quando uma funcionalidade for mais complexa ou envolver conhecimento compartilhado, poderá ser utilizada programação em pares.

Durante a implementação, os desenvolvedores deverão utilizar testes para verificar o comportamento esperado. As alterações serão integradas frequentemente ao repositório, reduzindo o risco de conflitos e permitindo identificar problemas mais cedo.

A refatoração será realizada sempre que houver oportunidade de melhorar a estrutura do código sem alterar seu comportamento. O design simples será mantido como orientação para evitar a implementação de funcionalidades que não fazem parte das necessidades atuais.

---

## 8. Cerimônias do Scrum

### Sprint Planning

A Sprint Planning ocorre no início da Sprint. Nessa reunião, o Product Owner apresenta e esclarece os itens prioritários do Product Backlog. A equipe avalia sua capacidade e seleciona os itens que serão trabalhados durante a Sprint.

### Daily Scrum

A Daily Scrum é uma reunião curta realizada diariamente. O objetivo é acompanhar o progresso e identificar impedimentos. A reunião não deve ser utilizada para resolver detalhadamente todos os problemas técnicos, mas para identificar quais questões precisam de atenção.

### Sprint Review

Ao final da Sprint, a equipe apresenta o incremento desenvolvido. O Product Owner e os demais interessados podem avaliar o resultado e fornecer feedback.

### Sprint Retrospective

Depois da Review, a equipe realiza a retrospectiva para analisar o processo de trabalho. São discutidos pontos positivos, dificuldades encontradas e ações que podem melhorar a próxima Sprint.

---

## 9. Entregas esperadas ao final da Sprint

Ao final da Sprint, espera-se que a equipe tenha produzido um incremento funcional e potencialmente utilizável do sistema.

As entregas devem:

- atender aos requisitos das user stories selecionadas;
- estar integradas ao código principal;
- possuir as validações e testes necessários;
- apresentar código organizado e simples;
- estar disponível para demonstração ao Product Owner;
- gerar feedback para orientar as próximas prioridades.

O conteúdo exato do incremento dependerá dos itens selecionados durante a Sprint Planning.

---

## 10. Scrum x Kanban

| Característica | Scrum | Kanban |
|---|---|---|
| Estrutura | Framework com papéis, eventos e artefatos definidos | Método de gestão visual do fluxo de trabalho |
| Organização | Trabalho dividido em Sprints | Fluxo contínuo de tarefas |
| Planejamento | Realizado principalmente no início da Sprint | Pode ocorrer continuamente |
| Mudanças | Normalmente são controladas durante a Sprint | Podem ser incorporadas ao fluxo conforme a capacidade |
| Medição | Pode utilizar velocidade e cumprimento do objetivo da Sprint | Pode utilizar métricas como tempo de ciclo e vazão |
| Quando usar | Quando a equipe se beneficia de ciclos e objetivos definidos | Quando é necessário acompanhar um fluxo contínuo de trabalho |
| Principal característica | Iterações com duração definida | Visualização e otimização do fluxo |
| Combinação | Pode utilizar um quadro para visualizar o trabalho | Pode ser usado dentro de uma equipe Scrum para melhorar a visualização |

### Como combinar Scrum e Kanban

Na AgileTech Solutions, o Scrum será utilizado para estruturar as Sprints, definir objetivos e realizar as cerimônias. O Kanban será utilizado como recurso visual para acompanhar o fluxo das tarefas dentro da Sprint.

Assim, a equipe pode manter a estrutura de Scrum e, ao mesmo tempo, visualizar claramente quais itens estão no Backlog, quais estão prontos, quais estão em desenvolvimento, quais aguardam revisão e quais foram concluídos.

---

## 11. Organização do fluxo

O fluxo utilizado no quadro pode ser representado da seguinte maneira:

```text
Backlog
   ↓
Ready
   ↓
In progress
   ↓
In review
   ↓
Done
```

Os itens devem avançar pelo fluxo conforme o trabalho é realizado. A equipe deve evitar iniciar muitas tarefas simultaneamente, priorizando a conclusão dos itens já iniciados.

---

## 12. Conclusão

A combinação de Scrum e XP oferece à AgileTech Solutions uma forma de organizar o processo sem separar gestão e desenvolvimento técnico. O Scrum fornece uma estrutura para planejamento, acompanhamento, revisão e melhoria, enquanto as práticas de XP ajudam a manter a qualidade do código e a capacidade de adaptação durante a implementação.

O uso de uma Sprint de duas semanas permite trabalhar com ciclos curtos, obter feedback e revisar prioridades regularmente. Ao mesmo tempo, práticas como programação em pares, testes, refatoração, integração contínua, propriedade coletiva e design simples contribuem para reduzir problemas técnicos e evitar complexidade desnecessária.

O GitHub Projects complementa esse processo ao fornecer uma visão visual do fluxo de trabalho. Dessa forma, a equipe consegue acompanhar as tarefas e manter maior transparência sobre o andamento da Sprint.
