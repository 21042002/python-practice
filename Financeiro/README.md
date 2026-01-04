# Folha de Pagamento

Este é um projeto simples em Python para calcular a folha de pagamento, incluindo deduções de INSS (Instituto Nacional do Seguro Social) e IR (Imposto de Renda), com base nas regras brasileiras atuais.

## Descrição

O script `folhadePagamento.py` solicita o salário bruto do usuário e calcula:
- Dedução do INSS
- Base de cálculo para IR
- Dedução do IR
- Salário líquido final

As alíquotas e faixas seguem as tabelas oficiais do governo brasileiro (valores atualizados para 2023/2024).

## Requisitos

- Python 3.x instalado no sistema

## Como executar

1. Certifique-se de que o Python está instalado.
2. Execute o script no terminal:

   ```bash
   python folhadePagamento.py
   ```

3. Digite o salário bruto quando solicitado.
4. O programa exibirá o detalhamento da folha de pagamento.

## Exemplo de uso

```
*** FOLHA DE PAGAMENTO ***
Informe o seu salário: R$3000

Salário bruto:         R$3000.00
Salário base:          R$2760.00
INSS:                  R$240.00
IR: (7.5%)             R$138.00
Valor IR:              R$138.00
Salário Liquido:       R$2622.00
```

## Observações

- Os valores de alíquotas podem mudar conforme legislação. Verifique as tabelas oficiais para atualizações.
- Este é um cálculo simplificado e não substitui consultoria profissional ou sistemas oficiais.

## Licença

Este projeto é de uso pessoal e educacional.