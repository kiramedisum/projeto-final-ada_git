# Coleta da idade do pet, garantindo que seja um número inteiro
def validar_idade(mensagem: str) -> int:
    while True:
        try:
            idade = int(input(mensagem))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                return idade
        except ValueError:
            print("Erro: por favor, insira um número válido para a idade.")


# Coleta do peso do pet, garantindo que seja um número flutuante
def validar_peso(mensagem: str) -> float:
    while True:
        try:
            peso = float(input(mensagem))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                return peso
        except ValueError:
            print("Erro: por favor, insira um número válido para o peso.")

# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    while True:
        print("\nPor favor, insira as informações sobre seu pet.")

        nome = input("Nome do pet: ")
        idade = validar_idade("Idade do pet (em anos): ")
        peso = validar_peso("Peso do pet (em kg): ")

        # Exibindo as informações coletadas
        print("\nInformações do pet:")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Peso: {peso} kg")

        # Perguntar se o usuário deseja adicionar outro pet
        continuar = input("\nVocê deseja adicionar outro pet? (s/n): ").strip().lower()
        if continuar != 's':
            break

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
