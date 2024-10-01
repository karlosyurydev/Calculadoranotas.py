import pandas as pd

# Função para coletar notas dos alunos
def coletar_notas():
    notas = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        try:
            nota = float(input(f"Digite a nota do aluno {nome}: "))
            notas[nome] = nota
        except ValueError:
            print("Por favor, insira um valor numérico válido para a nota.")
    return notas

# Função para salvar as notas em um arquivo CSV
def salvar_notas(notas):
    df = pd.DataFrame(list(notas.items()), columns=['Nome', 'Nota'])
    df.to_csv('notas_alunos.csv', index=False)
    print("Notas salvas em 'notas_alunos.csv'.")

# Função principal
def main():
    print("Sistema de Controle de Notas")
    notas = coletar_notas()
    if notas:
        salvar_notas(notas)
    else:
        print("Nenhuma nota foi registrada.")

if __name__ == "__main__":
    main()

