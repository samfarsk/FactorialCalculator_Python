while True:
    # Define a entrada
    valorInput = int(input("Digite um número inteiro: "))

    # Cria os contadores
    fatorial = 1
    contagem = 1

    # Cálculo do fatorial
    while contagem <= valorInput:
        fatorial *= contagem
        contagem += 1

    # Retorna o fatorial
    print(f"\nO fatorial de {valorInput} é {fatorial}.\n")
