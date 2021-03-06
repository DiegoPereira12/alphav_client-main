from time import sleep

def main():  
     
     print('--   Consumir dados API   --')
     print('Selecione uma opção no menu: ')
     print('1 - Intraday series')
     print('2 - Daily series')
     print('3 - Daily adjusted series')
     print('4 - Weekly series')
     print('5 - Weekly adjusted series')
     print('6 - Monthly series')
     print('7 - Monthly adjusted series')

     opcao = input('Digite uma opção => ')

     if opcao == '1':
          print('=' * 60)
          print('Seus dados Intraday Series estão sendo gerados ....')
          sleep(5)
          
          import intraday_series
          print('=' * 60)    
               
     elif opcao == '2':
          print('=' * 60)
          print('Seus dados Daily Series estão sendo gerados ....')
          sleep(5)
          import daily_series
          print('=' * 60)

     elif opcao == '3':
          print('=' * 60)
          print('Seus dados Daily Adjusted Series estão sendo gerados ....')
          sleep(5)
          import daily_adjusted_series
          print('=' * 60)

     elif opcao == '4':
          print('=' * 60)
          print('Seus dados Weekly Series estão sendo gerados ....')
          sleep(5)
          import weekly_series
          print('=' * 60)
     
     elif opcao == '5':
          print('=' * 60)
          print('Seus dados Weekly Adjusted Series estão sendo gerados ....')
          sleep(5)
          import weekly_adjusted_series
          print('=' * 60)
     
     elif opcao == '6':
          print('=' * 60)
          print('Seus dados Monthly Series estão sendo gerados ....')
          sleep(5)
          import monthly_series
          print('=' * 60)
     
     elif opcao == '7':
          print('=' * 60)
          print('Seus dados Monthly Adjusted Series estão sendo gerados ....')
          sleep(5)
          import monthly_adjusted_series
          print('=' * 60)

     else:
          print('Digite uma opção valida')              

if __name__ == '__main__':
     main()

     