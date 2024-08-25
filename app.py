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
   opcao_escolhida = int(input("Escolha uma opcão:"))
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
   tipodeMedida = input("Digite o tipo de unidade de medida do produto:")
   quantidade = input("Digite a quantidade:")
   descrição = input("Digite a descrição do produto: Caso não queira apenas aperte Enter")
   #Fazer dicionário do produto com compreensão de lista
   voltar()

def remover_produto():
   subtitulo("Selecione o produto que deseja remover:")
   input("Digite o nome do produto:")
   #código para a remoção do produto.

def pesquisar_produtos():
   input("Digite o nome do produto:")
   #adicionar o código para a pesquisa.

def main():
   os.system('cls')
   opcoes()
   escolher_opcoes()

if __name__== '__main__':
    main()