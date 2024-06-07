import os

if __name__== "__main__":

  caminho = input("Digite o caminho de um diretório: ")

  subdiretórios = os.listdir(caminho)

  print(f"Conteúdo do diretório '{caminho}':")

  for item in subdiretórios:
            item_path = os.path.join(caminho, item)
            if os.path.isdir(item_path):
                print(f"Diretório: {item}")
            else:
                print(f"Arquivo: {item}")