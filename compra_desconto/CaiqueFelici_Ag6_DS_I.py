# Primeiro, vamos solicitar ao usuário que informe o valor da compra
valor_compra = float(input("Digite o valor da sua compra R$ ").replace(",", "."))

# Possíveis Descontos: 5%, 10% e 15%
desconto1 = 0.05
desconto2 = 0.10
desconto3 = 0.15

# Política de Descontos
# Descontos de acordo com o valor da compra:
# Compras menores que R$ 200 recebem 5% de desconto;
# Compras entre R$ 200 e R$ 299,99 recebem 10% de desconto;
# Compras maiores ou iguais a R$ 300 recebem 15% de desconto.
if valor_compra < 200:
    desconto = desconto1
elif valor_compra < 300:
    desconto = desconto2
else:
    desconto = desconto3

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

# Mensagens de saída para o usuário com todas as informações
# Conversão do valor do desconto para porcentagem
# Formatação dos valores monetários em R$
print(f"Parabéns! Você recebeu um desconto de {desconto*100:.0f}% na sua compra!")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
