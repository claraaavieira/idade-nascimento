##verificadonascimentoidade
nome = str(input("digite o seu nome completo: "))
while True:
    try:
        nascimento = int(input("Informe sua data de nascimento entre 1922 e 2022: "))
        if not 1922 <= nascimento <= 2022:
            raise ValueError("Ano não permitido")
    except ValueError as e:
        print("ano inválido:", e)
    else:
        idade = input(2022 - (nascimento))
        break
nascimento = int(input("informe sua data de nascimento: "))
idade = (2022 - (nascimento))