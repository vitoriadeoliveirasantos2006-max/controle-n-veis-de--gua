# Controle de Níveis de Água

## Sobre o projeto

Este projeto consiste em um sistema simples de monitoramento dos níveis de água de um reservatório, desenvolvido em Python. O programa calcula a porcentagem de água armazenada e identifica automaticamente o nível do reservatório, exibindo uma mensagem de alerta com uma cor correspondente.

## Funcionalidades

- Solicita a capacidade total do reservatório em litros.
- Solicita a quantidade atual de água armazenada.
- Calcula a porcentagem de preenchimento do reservatório.
- Identifica o nível da água entre cinco situações.
- Exibe o alerta com uma cor correspondente ao nível.
- Verifica se os valores informados são válidos.

## Níveis do reservatório

| Nível | Porcentagem | Situação | Cor |
|---|---|---|---|
| 1 | Até 20% | Muito baixo (crítico) | Vermelho |
| 2 | Acima de 20% até 40% | Baixo | Amarelo |
| 3 | Acima de 40% até 60% | Médio | Verde |
| 4 | Acima de 60% até 80% | Alto | Ciano |
| 5 | Acima de 80% até 100% | Muito alto (alerta) | Azul |

## Tecnologias utilizadas

- Python
- Biblioteca Colorama

## Instalação

Instale a biblioteca Colorama pelo terminal:

```bash
pip install colorama
```

## Como executar

Execute o arquivo `app.py` pelo terminal:

```bash
python app.py
```

Em seguida, informe a capacidade total do reservatório e a quantidade atual de água em litros. O programa calculará a porcentagem preenchida e exibirá a situação correspondente.

## Conceitos utilizados

Durante o desenvolvimento, foram utilizados conceitos de listas, funções, estruturas condicionais, entrada de dados, cálculos matemáticos e bibliotecas externas em Python.

## Objetivo

Praticar os conteúdos estudados na Agenda 11 de Desenvolvimento de Sistemas I, utilizando uma biblioteca externa para melhorar a visualização das mensagens exibidas no terminal.
