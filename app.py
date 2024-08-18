#Lista de Compras
import os

def subtitulo(texto):
   os.system('cls')
   linha = "-" * len(texto)
   print(linha)
   print(texto)
   print(linha)
   print("")

def opcoes():
   subtitulo("Lista de opções")
   print("1. Adicionar produto:")
   print("2. Remover produto:")
   print("3. Pesquisar produtos:")
   print("4. Sair do programa:")

def escolher_opcoes():
   opcao_escolhida = input(int("Escolha uma opcão:"))
   try:
      if opcao_escolhida == 1:
         adicionar_produto()
      elif opcao_escolhida == 2:
         remover_produto()
      elif opcao_escolhida == 3:
         pesquisar_produtos()
      elif opcao_escolhida == 4:
         sair()
      else:
         opcao_invalida()
   except:
      opcao_invalida()

def voltar():
   input("\nAperte Enter para voltar:")
   main()

def sair():
   subtitulo("Programa finalizado.")

def opcao_invalida():
   subtitulo("Opção inválida\n")
   input("Aperte Enter para voltar ao início:")
   main()

def adicionar_produto():
   subtitulo("Digite um nome para o produto") #Deve exibir nome, unidade de medida, quantidade e descrição do produto.
   nomeprod = input("Digite o nome do produto:")

def main():
   os.system('cls')
   opcoes()
   escolher_opcoes()
if __name__== '__main__':
    main()