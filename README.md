# 🛡️ Security Log Analyzer

> Uma ferramenta desenvolvida em Python para analisar logs de autenticação, identificar atividades suspeitas e auxiliar na investigação de possíveis incidentes de segurança.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Security](https://img.shields.io/badge/focus-blue%20team-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## O que é este projeto?

O **Security Log Analyzer** é uma ferramenta de análise de logs desenvolvida em Python com o objetivo de identificar padrões potencialmente suspeitos em registros de autenticação.

Em ambientes computacionais, os logs registram eventos importantes para a segurança, como tentativas de login, acessos bem-sucedidos e falhas de autenticação. A análise desses registros pode ajudar a identificar comportamentos anormais e investigar possíveis incidentes.

O projeto busca automatizar parte desse processo, transformando registros brutos em informações mais fáceis de interpretar.

**Exemplos de situações que a ferramenta pretende identificar:**

* Múltiplas tentativas de login malsucedidas.
* Possíveis tentativas de força bruta (*brute force*).
* Endereços IP associados a um número elevado de falhas de autenticação.
* Sequências incomuns de eventos de login.
* Atividades que merecem uma investigação manual.

O objetivo é construir uma ferramenta educacional que demonstre conceitos de Python, análise de dados, monitoramento de segurança e detecção de ameaças.

---

## Objetivos de aprendizagem

Este projeto foi criado para desenvolver conhecimentos práticos nas seguintes áreas:

* **Python:** leitura de arquivos, funções, estruturas de dados e tratamento de erros.
* **Cibersegurança:** autenticação, análise de eventos e detecção de comportamentos suspeitos.
* **Blue Team:** monitoramento, investigação inicial e análise de logs.
* **Análise de dados:** agrupamento de eventos, contagem de ocorrências e identificação de padrões.
* **Engenharia de software:** organização do código, testes, documentação e controle de versão com Git.

---

## Arquitetura

A ferramenta seguirá inicialmente um fluxo simples, priorizando clareza e facilidade de manutenção.

```text
[Arquivo de Logs]
       |
       v
[Leitura e Validação]
       |
       v
[Normalização dos Eventos]
       |
       v
[Motor de Detecção]
       |
       +-------------------+
       |                   |
       v                   v
[Eventos Normais]   [Eventos Suspeitos]
                           |
                           v
                  [Relatório de Análise]
```

O sistema será organizado em quatro etapas principais:

| Componente                | Responsabilidade                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| **Leitor de logs**        | Carregar os arquivos e identificar registros válidos.                                        |
| **Processador**           | Extrair informações relevantes, como data, endereço IP, usuário e resultado da autenticação. |
| **Motor de detecção**     | Aplicar regras para identificar padrões potencialmente suspeitos.                            |
| **Gerador de relatórios** | Apresentar os resultados da análise de forma organizada.                                     |

As regras iniciais serão baseadas em critérios explícitos e configuráveis. A identificação de um evento como suspeito não significa, por si só, que um ataque ocorreu.

---

## Funcionalidades planejadas

* [ ] Estrutura inicial do projeto em Python.
* [ ] Leitura de arquivos de logs de autenticação.
* [ ] Validação e tratamento de registros inválidos.
* [ ] Extração de data, usuário, endereço IP e resultado do login.
* [ ] Contagem de tentativas malsucedidas por endereço IP.
* [ ] Detecção de possíveis tentativas de força bruta.
* [ ] Configuração de limites para geração de alertas.
* [ ] Exibição dos resultados no terminal.
* [ ] Exportação de relatórios em CSV.
* [ ] Registro de erros durante o processamento.
* [ ] Testes automatizados das regras de detecção.
* [ ] Documentação com exemplos de entrada e saída.

As funcionalidades serão marcadas como concluídas conforme forem implementadas e testadas.

---

## Stack Tecnológica

| Componente                  | Tecnologia                                                          |
| --------------------------- | ------------------------------------------------------------------- |
| Linguagem principal         | Python 3.11+                                                        |
| Manipulação de arquivos     | Biblioteca padrão do Python                                         |
| Processamento de dados      | `datetime`, `collections` e expressões regulares, quando apropriado |
| Exportação de relatórios    | `csv`                                                               |
| Testes automatizados        | `pytest`                                                            |
| Controle de versão          | Git e GitHub                                                        |
| Ambiente de desenvolvimento | Linux ou Windows                                                    |

A versão inicial priorizará bibliotecas simples e recursos da biblioteca padrão do Python, evitando dependências desnecessárias.

---

## Estrutura do Repositório

```text
security-log-analyzer/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── data/
│   └── sample_logs.log
│
├── reports/
│   └── .gitkeep
│
├── src/
│   ├── main.py
│   ├── log_reader.py
│   ├── log_parser.py
│   ├── detector.py
│   └── report_generator.py
│
├── tests/
│   ├── test_log_parser.py
│   └── test_detector.py
│
└── docs/
    ├── detection_rules.md
    └── sample_report.md
```

### Responsabilidade dos arquivos

| Arquivo               | Descrição                                              |
| --------------------- | ------------------------------------------------------ |
| `main.py`             | Ponto de entrada da aplicação.                         |
| `log_reader.py`       | Leitura dos arquivos de entrada.                       |
| `log_parser.py`       | Interpretação e normalização dos registros.            |
| `detector.py`         | Implementação das regras de detecção.                  |
| `report_generator.py` | Geração dos relatórios de análise.                     |
| `tests/`              | Testes para verificar o funcionamento dos componentes. |
| `data/`               | Arquivos de exemplo, sem dados sensíveis reais.        |
| `docs/`               | Documentação complementar do projeto.                  |

A estrutura representa a organização planejada e poderá ser ajustada durante o desenvolvimento.

---

## Como Rodar

A documentação de instalação e execução será atualizada conforme a implementação avançar.

### Pré-requisitos

* Python 3.11 ou superior.
* Git.
* Um arquivo de logs compatível com o formato aceito pela ferramenta.

### Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/security-log-analyzer.git
cd security-log-analyzer
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Linux:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

A instalação das dependências e o comando de execução serão documentados após a implementação da primeira versão funcional.

---

## Roadmap

| Fase   | Descrição                                       | Status          |
| ------ | ----------------------------------------------- | --------------- |
| Fase 1 | Definição dos requisitos e estrutura do projeto | 🔄 Em andamento |
| Fase 2 | Leitura e interpretação dos logs                | ⏳ Planejado     |
| Fase 3 | Implementação das regras de detecção            | ⏳ Planejado     |
| Fase 4 | Geração de relatórios e exportação CSV          | ⏳ Planejado     |
| Fase 5 | Testes automatizados e tratamento de erros      | ⏳ Planejado     |
| Fase 6 | Documentação, exemplos e revisão de segurança   | ⏳ Planejado     |

---

## Segurança e Limitações

Este projeto possui finalidade educacional e de defesa cibernética.

* Os testes devem utilizar dados sintéticos, dados públicos apropriados ou registros que o usuário esteja autorizado a analisar.
* Os endereços IP e nomes de usuários presentes nos logs podem conter informações sensíveis. Esses dados devem ser tratados com cuidado.
* As regras de detecção podem produzir falsos positivos e falsos negativos.
* Um alerta representa um indício que merece análise, não uma confirmação automática de ataque.
* A versão inicial não substitui um SIEM, um sistema de monitoramento corporativo ou uma investigação profissional de incidentes.

---

## Motivação

Este projeto nasceu do interesse em aprender cibersegurança de forma prática, utilizando Python para resolver um problema relacionado ao monitoramento e à análise de eventos.

Além de desenvolver habilidades de programação, a proposta é compreender como profissionais de segurança investigam registros, reconhecem comportamentos suspeitos e transformam dados técnicos em informações úteis para a tomada de decisão.

O Security Log Analyzer faz parte da construção de um portfólio voltado para segurança da informação, automação e análise defensiva.

---

## Licença

Este projeto pretende utilizar a licença MIT. O arquivo `LICENSE` deverá ser incluído no repositório com o texto oficial da licença antes da publicação da versão licenciada.
