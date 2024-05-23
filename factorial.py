while True:
    # Define a entrada
    valor = int(input("Digite um número inteiro: "))

    # Cria os contadores
    fatorial = 1
    numero = 1

    # Cálculo do fatorial
    while numero <= valor:
        fatorial *= numero
        numero += 1

    # Retorna o fatorial
    print(f"\nO fatorial de {valor} é {fatorial}.")
