def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Exemplo de uso
if __name__ == "__main__":
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"Seu IMC é {imc:.2f} - {classificacao}")
    print("Boa noite cinderela!!!")


    