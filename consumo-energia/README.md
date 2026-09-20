# Calculadora de Consumo de Energia

Este é um aplicativo simples para estimar quanto um aparelho elétrico pode consumir e custar por mês.

Para fazer a estimativa, o app solicita:

- o nome do aparelho;
- a potência do aparelho em watts (W);
- a média de horas de uso por dia.

Com essas informações, o programa calcula o consumo mensal estimado em quilowatt-hora (kWh), considerando 30 dias de uso. Em seguida, calcula o custo mensal estimado em reais, usando a tarifa de `R$ 0,74` por kWh.

## Como executar

Tenha o Python instalado e execute no terminal:

```bash
python app.py
```

Depois, informe os dados solicitados. Ao final, o app mostra o nome do aparelho, o consumo mensal estimado e o custo aproximado da energia.

## Exemplo

Para um aparelho de `100 W` usado durante `5 horas por dia`:

- consumo mensal estimado: `15,00 kWh`;
- custo mensal estimado: `R$ 11,10`.

Os valores são aproximados e podem variar de acordo com a tarifa de energia da sua região e com o tempo real de uso do aparelho.
