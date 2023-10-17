from datetime import datetime

def calcular_imposto(valor_bruto, aliquota):
    return valor_bruto * (aliquota / 100)

valor_bruto = float(input("Digite o valor bruto: "))

while True:
    aliquota = input("Digite o valor da aliquota do estado desejado (dois digitos): ")
    
    if len(aliquota) == 2 and aliquota.isdigit():
        aliquota = int(aliquota)
        print(f"Aliquota: {aliquota}")
        break
    else:
        print("Entrada invalida. Certifique-se de digitar exatamente dois digitos.")

if aliquota is not None:
    imposto = calcular_imposto(valor_bruto, aliquota)
    
    print(f"Aliquota Brasileira: {aliquota}%")
    print(f"Valor do Imposto: R${imposto:.2f}")
    
    print("\nAgora vou fazer o calculo do ICMS para minha linda Ju")
    
    data_nota = input("Digite a data da nota fiscal (no formato DD/MM/AAAA): ")

    if len(data_nota) == 10 and data_nota[2] == "/" and data_nota[5] == "/":
        dia, mes, ano = map(int, data_nota.split('/'))
        
        data_de_hoje = datetime.now().date()
        data_nota_date = datetime(ano, mes, dia).date()
        print("Data de hoje:", data_de_hoje)
        
        if data_nota_date >= data_de_hoje:
            deduz = imposto - (imposto * 0.2)
            print(f"O valor deduzido e: R${deduz:.2f}")
        else:
            print(f"O valor continua o mesmo: R${imposto:.2f}")
    else:
        print("Formato de data invalido. Certifique-se de usar o formato DD/MM/AAAA.")
