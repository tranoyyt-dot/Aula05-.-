#Menu de opções para analise simples
def analise_velocidade():
    nome = input("Informe o nome do motorista: ")
    velocidade = float(input("Informe a velocidade registrada (km/h): "))

    if velocidade <= 80:
        classificacao = "Dentro do limite"
    elif 81 <= velocidade <= 100:
        classificacao = "Acima do limite (leve)"
    else:
        classificacao = "Acima do limite (grave)"

    print(f"\nNome: {nome}")
    print(f"Velocidade registrada: {velocidade:.1f} km/h")
    print(f"Classificação: {classificacao}")

def saude_imc():
    nome = input('\nNOME: ')
    h = float(input('ALTURA (m): '))
    kg = float(input('PESO (kg): '))
    
    imc = kg / (h ** 2)

    if 25 <= imc <= 29.9:
        situacao = 'Sobrepeso'
    elif 18.5 <= imc <= 24.9:
        situacao = 'Peso normal'
    elif 0 <= imc < 18.5:
        situacao = 'Abaixo do peso'
    else:
        situacao = 'Obesidade'
    
    print(f'\nNome: {nome}')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {situacao}')


def consumo_combustivel():
    nome = input('\nInforme o nome do motorista: ')
    km = float(input('Informe quantos quilômetros percorridos: '))
    l = float(input('Informe a quantidade de combustível gasto (litros): '))
    
    kmpl = km / l

    if kmpl >= 15:
        situacao = 'Econômico'
    elif 10 <= kmpl < 15:
        situacao = 'Regular'
    elif 0 <= kmpl < 10:
        situacao = 'Alto consumo'
    else:
        situacao = 'Erro'
    
    print(f'\nNome: {nome}')
    print(f'Km/l: {kmpl:.2f}')
    print(f'Consumo: {situacao}')


# --- Menu inicial ---
print("Escolha a opção desejada:")
print("1 - Análise de saúde do peso (IMC)")
print("2 - Análise de consumo de combustível")
print("3 - Análise de controle de velocidade"

opcao = input("\nDigite: ")

if opcao == "1":
    saude_imc()
elif opcao == "2":
    consumo_combustivel()
elif opcao == "3":
    analise_velocidade
else:
    print("Opção inválida.")