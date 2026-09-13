print("## Meu Consumo de Energia Elétrica: Consultar Bandeira ##")

consumo = float(input("Informe o valor do seu consumo de energia elétrica em kWh: "))

if consumo <= 100:
    print("Bandeira Branca: Seu consumo está baixo.")
elif consumo <= 200:
    print("Bandeira Amarela: Seu consumo está moderado.")
else: 
    print("Bandeira Vermelha: Seu consumo está alto.")    



          
