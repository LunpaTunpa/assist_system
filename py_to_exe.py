from cx_Freeze import setup, Executable

setup(
    name=input("Digite o nome desejado: "),
    version=input("Digite a versão do arquvio: "),
    # description="Descrição do seu script",
    executables=[Executable(input("Digite o nome do arquivo a ser compilado: "))],
)
