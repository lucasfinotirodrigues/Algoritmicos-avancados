class Teatro:
    def __init__(self, linhas, colunas, valor_ingresso):
        self.linhas = linhas
        self.colunas = colunas
        self.valor_ingresso = valor_ingresso
        self.poltronas = [[False for _ in range(colunas)] for _ in range(linhas)]

    def iniciar(self):
        print("Iniciando o teatro.")

    def reservar_lugar(self, linha, coluna):
        print(f"Reservando lugar na linha {linha}, coluna {coluna}.")

    def comprar_lugar(self, linha, coluna):
        print(f"Comprando lugar na linha {linha}, coluna {coluna}.")

    def liberar_lugar(self, linha, coluna):
        print(f"Liberando lugar na linha {linha}, coluna {coluna}.")

    def listar_poltronas(self):
        print("Listando poltronas.")

    def encerrar_espetaculo(self):
        print("Encerrando o espetáculo.")

    def reiniciar_espetaculo(self):
        print("Reiniciando o espetáculo.")


def main():
    linhas = int(input("Informe o número de linhas do teatro: "))
    colunas = int(input("Informe o número de colunas do teatro: "))
    valor_ingresso = float(input("Informe o valor do ingresso: "))

    teatro = Teatro(linhas, colunas, valor_ingresso)

    while True:
        opcao = menu()
        if opcao == 1:
            teatro.iniciar()
        elif opcao == 2:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.reservar_lugar(linha, coluna)
        elif opcao == 3:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.comprar_lugar(linha, coluna)
        elif opcao == 4:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.liberar_lugar(linha, coluna)
        elif opcao == 5:
            teatro.listar_poltronas()
        elif opcao == 6:
            teatro.encerrar_espetaculo()
        elif opcao == 7:
            teatro.reiniciar_espetaculo()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu():
    print("--- MENU ---")
    opcoes = {
        1: "[1] - Iniciar o teatro",
        2: "[2] - Reservar lugar",
        3: "[3] - Comprar lugar",
        4: "[4] - Liberar lugar",
        5: "[5] - Listar poltronas",
        6: "[6] - Encerrar o espetáculo",
        7: "[7] - Reiniciar o espetáculo",
        0: "[0] - Sair"
    }
    for opcao, descricao in opcoes.items():
        print(descricao)
    return int(input("Escolha uma opção: "))


if __name__ == "__main__":
    main()
