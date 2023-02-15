from FUNCIONALIDADE.cadastrando import nome_cpf

print("=============================")
print ("1 - Para sair do programa.")
print("2 - Para realizar o cadastro.")
print("=============================")
print()

inicio = int(input("Digite a opção desejada: "))

if inicio == 1:
    print("Obrigado por usar nosso sistema!")

elif inicio == 2:
    nome_cpf()


