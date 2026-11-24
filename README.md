# Calculadora de Parcelas

Script em Python que gera o cronograma de uma cobrança parcelada: informa a data
de vencimento e o valor de cada parcela.

## Contexto
Desenvolvi esta ferramenta para uso real no meu trabalho, para resolver um problema
recorrente: clientes atrasavam boletos alegando não saber quanto e quando pagar.
O resultado do script era copiado para o boleto, deixando o cronograma explícito
para o cliente desde o início.

## Como funciona
O usuário informa:
- data inicial;
- intervalo (em dias) até a primeira parcela;
- quantidade de parcelas;
- intervalo (em dias) entre as parcelas;
- valor total.

O programa divide o valor em parcelas iguais e calcula cada vencimento
com `datetime` e `timedelta`.

## Tecnologias
Python 3 (biblioteca padrão: `datetime`).

## Limitações conhecidas
- Não valida entradas (ex.: quantidade de parcelas igual a zero gera erro).
- O arredondamento pode causar diferença de centavos entre a soma das parcelas e o total.
- Usa `float` para valores monetários; em produção o ideal seria `Decimal`.

## Como rodar
1. Instale o Python (3.10+ recomendado).
2. Execute o programa:
   ```bash
   python calculadora_boletos.py
