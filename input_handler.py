def input_interactive():
    print("Iniciando Validação de Perfil Profissional...")
    return {
        "nome": input("Digite seu nome completo: "),
        "idade": input("Digite sua idade: "),
        "endereco": input("Digite seu endereço: "),
        "altura": input("Digite sua altura (ex: 1.78): "),
        "peso": input("Digite seu peso em kg (ex: 80.5): "),
        "sexo": input("Digite o sexo (M/F/O): "),
    }
