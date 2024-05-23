while True:
    # Define a entrada
    valor = int(input("Digite um número: "))

    # Cria os contadores
    fatorial = 1
    numero = 1

    # Cálculo do fatorial
    while numero <= valor:
        fatorial *= numero
        numero += 1

    # Retorna o fatorial
    print(fatorial)
