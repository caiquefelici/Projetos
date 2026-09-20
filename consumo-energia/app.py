aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
uso_diario = float(input("Digite a média de horas de uso diário: "))
consumo_mensal = (potencia * uso_diario * 30) / 1000  # Consumo em kWh
custo_estimado = 0.74 * consumo_mensal  # Custo mensal estimado em reais

print(f"Aparelho: {aparelho}")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh.")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f}.")
