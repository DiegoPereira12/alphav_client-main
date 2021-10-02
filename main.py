from os import system
import sys

def main():  

     while True:

          print('Consumir dados API')
          print('Selecione uma opção no menu: ')
          print('1 - Intraday series')
          print('2 - Daily series')

          opcao = int(input('Digite um opção => '))

          if opcao == 1:
               print('=' * 60)
               print('Seus dados Intraday Series estão sendo gerados ....')
               import intraday_series
               print('=' * 60)
               break
               
               
          elif opcao == 2:
             
               print('daily_series')
               print('=' * 60) 
          
          else:
               print('Entrada invalida')
     
          #main()

if __name__ == '__main__':
     main()