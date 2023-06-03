def peoples():
   def write(z):
      size = len(z) + 6
      si = len(z) + 3
      print('=' * size)
      print(f'{z:>{si}}')
      print('=' * size)
   def lin(a):
      print('-'*a)
   list2 = []
   list3 = []
   while True:
      write('    REGISTRED PEOPLES    ')
      lin(31)
      print('< \033[4mOPTIONS\033[m >')
      print('1 ---- SEE ALL THE PEOPLES\n2 ---- REGRISTRE NEW PEOPLE\n3 ---- DELETE PEOPLE REGISTRED\n4 ---- LEAVE')
      lin(31)
      op = str(input('\tOPTION: '))
      lin(31)
      try:
         if op == '2':
            with open('p', 'r+') as arq:
               arq.write(str(input('NAME: ') + '\n'))
               arq.write(str(input('YEAR OLD: ') + '\n'))
               for l in arq:
                  list2.append(l)
      except FileNotFoundError:
         with open('p', 'w') as arq:
            print()

      if op == '3':
         c = 0
         with open('p', 'r') as arq:
            a = list2 = arq.readlines()
            for p, l in enumerate(a):

               f = l.replace('\n', '')
               if p % 2 == 0:
                  print(f'{p}º {f:<15}', end='')
               else:
                  print(f)
         lin(31)
         print('\t\tSTOP --> [999]')
         lin(31)
         n = int(input('POSICION DELETE: '))
         if n != 999:
            list2.pop(n)
            list2.pop(n)
         with open('p', 'w') as arq:
            for l in list2:
               arq.write(l)
      if op == '1':
         with open('p', 'r') as arq:
            a = arq.readlines()
            print('\033[4m|NAME              |YEAR OLD\033[m')
            for p, l in enumerate(a):
               if p % 2 == 0:
                  f = l.replace('\n', '')
                  print(f'|{f:<18}|', end=' ')
               else:
                  print(f'{l}', end='')
            print('\n\n')

      if op == '4':
         break



peoples()