tipo_imovel = input("Digite o tipo de imóvel (1. Comercial, 2. Casa, 3. Apartamento): ")
if not tipo_imovel in ["1", "2", "3"]:
    print("Tipo de imóvel inválido")
#Validação caso o usuário digite um valor diferente de 1, 2 ou 3.
consumo_agua = float(input("Digite o consumo de água em metros cúbicos (m³): ").replace(",", "."))
#Caso o usuário use vírgula para separar os decimais, o programa irá substituir por ponto.
if tipo_imovel == "1":
    print ("Tarifa comercial aplicada, consulte o plano corporativo.")
elif tipo_imovel == "3" and consumo_agua < 10:
    print("Consumo econômico – excelente controle de água!")
elif tipo_imovel == "3" or tipo_imovel == "2" and consumo_agua <= 25:
    print("Consumo moderado – dentro do padrão residencial.")   
else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

