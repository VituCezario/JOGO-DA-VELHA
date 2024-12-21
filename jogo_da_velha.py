a1 = '_'
a2 = '_'
a3 = '_'
b1 = '_'
b2 = '_'
b3 = '_'
c1 = '_'
c2 = '_'
c3 = '_'

def win_X():
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  if a1 == 'X' and a2 == 'X' and a3 == 'X':
    a1 = '\033[1;34mX\033[m'
    a2 = '\033[1;34mX\033[m'
    a3 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif b1 == 'X' and b2 == 'X' and b3 == 'X':
    b1 = '\033[1;34mX\033[m'
    b2 = '\033[1;34mX\033[m'
    b3 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif c1 == 'X' and c2 == 'X' and c3 == 'X':
    c1 = '\033[1;34mX\033[m'
    c2 = '\033[1;34mX\033[m'
    c3 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a1 == 'X' and b1 == 'X' and c1 == 'X': 
    a1 = '\033[1;34mX\033[m'
    b1 = '\033[1;34mX\033[m'
    c1 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a2 == 'X' and b2 == 'X' and c2 == 'X':
    a2 = '\033[1;34mX\033[m'
    b2 = '\033[1;34mX\033[m'
    c2 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a3 == 'X' and b3 == 'X' and c3 == 'X': 
    a3 = '\033[1;34mX\033[m'
    b3 = '\033[1;34mX\033[m'
    c3 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a1 == 'X' and b2 == 'X' and c3 == 'X':
    a1 = '\033[1;34mX\033[m'
    b2 = '\033[1;34mX\033[m'
    c3 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a3 == 'X' and b2 == 'X' and c1 == 'X':
    a3 = '\033[1;34mX\033[m'
    b2 = '\033[1;34mX\033[m'
    c1 = '\033[1;34mX\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")

def win_O():
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  
  if a1 == 'O' and a2 == 'O' and a3 == 'O':
    a1 = '\033[1;34mO\033[m'
    a2 = '\033[1;34mO\033[m'
    a3 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif b1 == 'O' and b2 == 'O' and b3 == 'O':
    b1 = '\033[1;34mO\033[m'
    b2 = '\033[1;34mO\033[m'
    b3 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if c1 == 'O' and c2 == 'O' and c3 == 'O':
    c1 = '\033[1;34mO\033[m'
    c2 = '\033[1;34mO\033[m'
    c3 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a1 == 'O' and b1 == 'O' and c1 == 'O': 
    a1 = '\033[1;34mO\033[m'
    b1 = '\033[1;34mO\033[m'
    c1 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if a2 == 'O' and b2 == 'O' and c2 == 'O': 
    a2 = '\033[1;34mO\033[m'
    b2 = '\033[1;34mO\033[m'
    c2 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a3 == 'O' and b3 == 'O' and c3 == 'O': 
    a3 = '\033[1;34mO\033[m'
    b3 = '\033[1;34mO\033[m'
    c3 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if a1 == 'O' and b2 == 'O' and c3 == 'O':
    a1 = '\033[1;34mO\033[m'
    b2 = '\033[1;34mO\033[m'
    c3 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a3 == 'O' and b2 == 'O' and c1 == 'O':
    a3 = '\033[1;34mO\033[m'
    b2 = '\033[1;34mO\033[m'
    c1 = '\033[1;34mO\033[m'
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
    
def tabela():
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  print('\033[1;31m  1   2   3\033[m')
  print('\033[1;31ma\033[m {} | {} | {}'.format(a1,a2,a3))
  print('----+---+---')
  print('\033[1;31mb\033[m {} | {} | {}'.format(b1,b2,b3))
  print('----+---+---')
  print('\033[1;31mc\033[m {} | {} | {}'.format(c1,c2,c3))
    
def maquina_começa():
  import random 
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3
  a1 = 'O'
  print(' ')
  tabela()
  casas = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
  casas.remove('a1')
  while True:
    print(' ')
    jo1 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if jo1 == 'A1' or jo1 == 'A2'  or jo1 == 'A3' or jo1 == 'B1' or jo1 == 'B2' or jo1 == 'B3' or jo1 == 'C1'  or jo1 == 'C2' or jo1 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if jo1 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo1.lower() == 'a2':
      break
    elif jo1.lower() == 'a3':
      break
    if jo1.lower() == 'b1':
      break
    elif jo1.lower() == 'b2':
      break
    elif jo1.lower() == 'b3':
      break
    if jo1.lower() == 'c1':
      break
    elif jo1.lower() == 'c2':
      break
    elif jo1.lower() == 'c3':
      break
    if jo1 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
      

  if jo1 == 'a1':
    a1 = 'X'
  elif jo1 == 'a2':
    a2 = 'X'
  if jo1 == 'a3':
    a3 = 'X'
  elif jo1 == 'b1':
    b1 = 'X'
  if jo1 == 'b2':
    b2 = 'X'
  elif jo1 == 'b3':
    b3 = 'X'
  if jo1 == 'c1':
    c1 = 'X'
  elif jo1 == 'c2':
    c2 = 'X'
  if jo1 == 'c3':
    c3 = 'X'
  
  while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == jo1:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break
      
  print(' ')
  tabela()
  print(' ')
  casas.remove(jo1)
  while True:
    print(' ')
    jo2 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if jo2 == 'A1' or jo2 == 'A2'  or jo2 == 'A3' or jo2 == 'B1' or jo2 == 'B2' or jo2 == 'B3' or jo2 == 'C1'  or jo2 == 'C2' or jo2 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if jo2 == jo1:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo2 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo2 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo2 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo2 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo2.lower() == 'a1':
      break
    if jo2.lower() == 'a2':
      break
    elif jo2.lower() == 'a3':
      break
    if jo2.lower() == 'b1':
      break
    elif jo2.lower() == 'b2':
      break
    elif jo2.lower() == 'b3':
      break
    if jo2.lower() == 'c1':
      break
    elif jo2.lower() == 'c2':
      break
    elif jo2.lower() == 'c3':
      break
    if jo2 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  
  if jo2 == 'a1':
    a1 = 'X'
  elif jo2 == 'a2':
    a2 = 'X'
  if jo2 == 'a3':
    a3 = 'X'
  elif jo2 == 'b1':
    b1 = 'X'
  if jo2 == 'b2':
    b2 = 'X'
  elif jo2 == 'b3':
    b3 = 'X'
  if jo2 == 'c1':
    c1 = 'X'
  elif jo2 == 'c2':
    c2 = 'X'
  if jo2 == 'c3':
    c3 = 'X'
  win_X()

  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'O' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c3 == 'O' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'O' and c3 == 'O' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and c1 == 'O' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'O' and a1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'O' and c2 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'O' and a3 == 'O' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b3 == 'O' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'O' and b2 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'O' and a3 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  if a1 == 'X' and a2 == 'X' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c3 == 'X' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'X' and c3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and c1 == 'X' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'X' and a1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'X' and c2 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'X' and a3 == 'X' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b3 == 'X' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'X' and b2 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'X' and a3 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == jo2:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break

    
  
  win_O()
  print(' ')
  tabela()
  print(' ')
  casas.remove(jo2)
  while True:
    print(' ')
    jo3 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if jo3 == 'A1' or jo3 == 'A2'  or jo3 == 'A3' or jo3 == 'B1' or jo3 == 'B2' or jo3 == 'B3' or jo3 == 'C1'  or jo3 == 'C2' or jo3 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if jo3 == jo1 or jo3 == jo2:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
      continue
    if jo3 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo3 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo3 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo3 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo3 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo3 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo3 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo3 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo3 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo3.lower() == 'a1':
      break
    if jo3.lower() == 'a2':
      break
    elif jo3.lower() == 'a3':
      break
    if jo3.lower() == 'b1':
      break
    elif jo3.lower() == 'b2':
      break
    elif jo3.lower() == 'b3':
      break
    if jo3.lower() == 'c1':
      break
    elif jo3.lower() == 'c2':
      break
    elif jo3.lower() == 'c3':
      break
    if jo3 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if jo3 == 'a1':
    a1 = 'X'
  elif jo3 == 'a2':
    a2 = 'X'
  if jo3 == 'a3':
    a3 = 'X'
  elif jo3 == 'b1':
    b1 = 'X'
  if jo3 == 'b2':
    b2 = 'X'
  elif jo3 == 'b3':
    b3 = 'X'
  if jo3 == 'c1':
    c1 = 'X'
  elif jo3 == 'c2':
    c2 = 'X'
  if jo3 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'O' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c3 == 'O' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'O' and c3 == 'O' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and c1 == 'O' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'O' and a1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'O' and c2 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'O' and a3 == 'O' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b3 == 'O' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'O' and b2 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'O' and a3 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  if a1 == 'X' and a2 == 'X' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c3 == 'X' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'X' and c3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and c1 == 'X' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'X' and a1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'X' and c2 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'X' and a3 == 'X' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b3 == 'X' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'X' and b2 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'X' and a3 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == jo3:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break
      
  win_O()
  print(' ')
  tabela()
  print(' ')
  casas.remove(jo3)
  while True:
    print(' ')
    jo4 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if jo4 == 'A1' or jo4 == 'A2'  or jo4 == 'A3' or jo4 == 'B1' or jo4 == 'B2' or jo4 == 'B3' or jo4 == 'C1'  or jo4 == 'C2' or jo4 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if jo4 == jo1 or jo4 == jo2 and jo4 == jo3:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo4 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
    elif jo4 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo4 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo4 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo4 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo4 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo4 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif jo4 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo4 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if jo4.lower() == 'a1':
      break
    if jo4.lower() == 'a2':
      break
    elif jo4.lower() == 'a3':
      break
    if jo4.lower() == 'b1':
      break
    elif jo4.lower() == 'b2':
      break
    elif jo4.lower() == 'b3':
      break
    if jo4.lower() == 'c1':
      break
    elif jo4.lower() == 'c2':
      break
    elif jo4.lower() == 'c3':
      break
    if jo4 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if jo4 == 'a1':
    a1 = 'X'
  elif jo4 == 'a2':
    a2 = 'X'
  if jo4 == 'a3':
    a3 = 'X'
  elif jo4 == 'b1':
    b1 = 'X'
  if jo4 == 'b2':
    b2 = 'X'
  elif jo4 == 'b3':
    b3 = 'X'
  if jo4 == 'c1':
    c1 = 'X'
  elif jo4 == 'c2':
    c2 = 'X'
  if jo4 == 'c3':
    c3 = 'X'

  if a1 == '_':
    a1 = 'O'
  elif a2 == '_':
    a2 = 'O'
  elif b2 == '_':
    b2 = 'O'
  elif c2 == '_':
    c2 = 'O'
  elif b1 == '_':
    b1 = 'O'
  elif c1 == '_':
    c1 = 'O'
  elif a3 == '_':
    a3 = 'O'
  elif b3 == '_':
    b3 = 'O'
  elif b3 == '_':
    b3 = 'O'

  win_O()
  win_X()
  print(' ')
  tabela()
  print(' ')
  exit('DEU VELHA!')

def jogador_começa():
  tabela()
  print()
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  
  casas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
  while True:
    print(' ')
    j1 = input('\033[1;32mQual a sua primeira jogada?:\033[m ')
    if j1 == 'A1' or j1 == 'A2'  or j1 == 'A3' or j1 == 'B1' or j1 == 'B2' or j1 == 'B3' or j1 == 'C1'  or j1 == 'C2' or j1 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if j1.lower() == 'a1':
      break
    if j1.lower() == 'a2':
      break
    elif j1.lower() == 'a3':
      break
    if j1.lower() == 'b1':
      break
    elif j1.lower() == 'b2':
      break
    elif j1.lower() == 'b3':
      break
    if j1.lower() == 'c1':
      break
    elif j1.lower() == 'c2':
      break
    elif j1.lower() == 'c3':
      break
    if j1 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if j1 == 'a1':
    a1 = 'X'
  elif j1 == 'a2':
    a2 = 'X'
  if j1 == 'a3':
    a3 = 'X'
  elif j1 == 'b1':
    b1 = 'X'
  if j1 == 'b2':
    b2 = 'X'
  elif j1 == 'b3':
    b3 = 'X'
  if j1 == 'c1':
    c1 = 'X'
  elif j1 == 'c2':
    c2 = 'X'
  if j1 == 'c3':
    c3 = 'X'
  
  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'OO' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif a1 == 'O' and c3 == 'O' and c1 == '_': 
    c1  = 'O'
    casas.remove('c1')
  elif b1 == 'O' and c1 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif b2 == 'O' and c3 == 'O' and b1 == '_':
    b1 = 'O'
    casas.remove('b1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a3 == 'O' and c1 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif b1 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif b2 == 'O' and b3 == 'O' and b1 == '_':
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a1 == 'X' and a2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')  
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif a1 == 'X' and c3 == 'X' and c1 == '_': 
    c1  = 'O'
    casas.remove('c1')
  elif b1 == 'X' and c1 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif b2 == 'X' and c3 == 'X' and b1 == '_':
    b1 = 'O'
    casas.remove('b1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a3 == 'X' and c1 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif b1 == 'X' and b3 == 'X' and c3 == '_': 
    c3 = 'O'
    casas.remove('c3')
  elif b2 == 'X' and b3 == 'X' and b1 == '_':
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == j1:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break
  
  print(' ')
  tabela()
  print(' ')
  casas.remove(j1)
  while True:
    print(' ')
    j2 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if j2 == 'A1' or j2 == 'A2'  or j2 == 'A3' or j2 == 'B1' or j2 == 'B2' or j2 == 'B3' or j2 == 'C1'  or j2 == 'C2' or j2 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if j2 == j1:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j2 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j2 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j2 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j2 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j2.lower() == 'a1':
      break
    if j2.lower() == 'a2':
      break
    elif j2.lower() == 'a3':
      break
    if j2.lower() == 'b1':
      break
    elif j2.lower() == 'b2':
      break
    elif j2.lower() == 'b3':
      break
    if j2.lower() == 'c1':
      break
    elif j2.lower() == 'c2':
      break
    elif j2.lower() == 'c3':
      break
    if j2 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if j2 == 'a1':
    a1 = 'X'
  elif j2 == 'a2':
    a2 = 'X'
  if j2 == 'a3':
    a3 = 'X'
  elif j2 == 'b1':
    b1 = 'X'
  if j2 == 'b2':
    b2 = 'X'
  elif j2 == 'b3':
    b3 = 'X'
  if j2 == 'c1':
    c1 = 'X'
  elif j2 == 'c2':
    c2 = 'X'
  if j2 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'O' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c3 == 'O' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'O' and c3 == 'O' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and c1 == 'O' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'O' and a1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'O' and c2 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'O' and a3 == 'O' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b3 == 'O' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'O' and b2 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'O' and a3 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  if a1 == 'X' and a2 == 'X' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c3 == 'X' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'X' and c3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and c1 == 'X' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'X' and a1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'X' and c2 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'X' and a3 == 'X' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b3 == 'X' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'X' and b2 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'X' and a3 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == j2:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break

    
  print(' ')
  tabela()
  win_O()
  print(' ')
  casas.remove(j2)
  while True:
    print(' ')
    j3 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if j3 == 'A1' or j3 == 'A2' or j3 == 'A3' or j3 == 'B1' or j3 == 'B2' or j3 == 'B3' or j3 == 'C1' or j3 == 'C2' or j3 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if j3 == j2 or j3 == j1:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j3 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j3 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j3 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j3 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j3.lower() == 'a1':
      break
    if j3.lower() == 'a2':
      break
    elif j3.lower() == 'a3':
      break
    if j3.lower() == 'b1':
      break
    elif j3.lower() == 'b2':
      break
    elif j3.lower() == 'b3':
      break
    if j3.lower() == 'c1':
      break
    elif j3.lower() == 'c2':
      break
    elif j3.lower() == 'c3':
      break
    if j3 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  print(' ')
  if j3 == 'a1':
    a1 = 'X'
  elif j3 == 'a2':
    a2 = 'X'
  if j3 == 'a3':
    a3 = 'X'
  elif j3 == 'b1':
    b1 = 'X'
  if j3 == 'b2':
    b2 = 'X'
  elif j3 == 'b3':
    b3 = 'X'
  if j3 == 'c1':
    c1 = 'X'
  elif j3 == 'c2':
    c2 = 'X'
  if j3 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'O' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c3 == 'O' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'O' and c3 == 'O' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and c1 == 'O' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'O' and a1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'O' and c2 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'O' and a3 == 'O' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b3 == 'O' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'O' and b2 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'O' and a3 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  if a1 == 'X' and a2 == 'X' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c3 == 'X' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'X' and c3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and c1 == 'X' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'X' and a1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'X' and c2 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'X' and a3 == 'X' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b3 == 'X' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'X' and b2 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'X' and a3 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == j3:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break
  
  print(' ')
  tabela()
  win_O()
  print(' ')

  casas.remove(j3)
  while True:
    print(' ')
    j4 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if j4 == 'A1' or j4 == 'A2'  or j4 == 'A3' or j4 == 'B1' or j4 == 'B2' or j4 == 'B3' or j4 == 'C1'  or j4 == 'C2' or j4 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if j4 == j1 or j4 == j2 or j4 == j3:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j4 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j4 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j4 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j4 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j4.lower() == 'a1':
      break
    if j4.lower() == 'a2':
      break
    elif j4.lower() == 'a3':
      break
    if j4.lower() == 'b1':
      break
    elif j4.lower() == 'b2':
      break
    elif j4.lower() == 'b3':
      break
    if j4.lower() == 'c1':
      break
    elif j4.lower() == 'c2':
      break
    elif j4.lower() == 'c3':
      break
    if j4 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if j4 == 'a1':
    a1 = 'X'
  elif j4 == 'a2':
    a2 = 'X'
  if j4 == 'a3':
    a3 = 'X'
  elif j4 == 'b1':
    b1 = 'X'
  if j4 == 'b2':
    b2 = 'X'
  elif j4 == 'b3':
    b3 = 'X'
  if j4 == 'c1':
    c1 = 'X'
  elif j4 == 'c2':
    c2 = 'X'
  if j4 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'O' and a2 == 'O' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'O' and a3 == 'O' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'O' and a3 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'O' and b1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'O' and b2 == 'O' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'O' and c3 == 'O' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'O' and c3 == 'O' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'O' and c1 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'O' and c1 == 'O' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'O' and a1 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'O' and b2 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'O' and c2 == 'O' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'O' and c2 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'O' and c3 == 'O' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'O' and c3 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'O' and b3 == 'O' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'O' and a3 == 'O' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b2 == 'O' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'O' and b3 == 'O' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'O' and b2 == 'O' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'O' and c2 == 'O' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'O' and c3 == 'O' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'O' and c3 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'O' and b2 == 'O' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'O' and b2 == 'O' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'O' and a3 == 'O' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  if a1 == 'X' and a2 == 'X' and a3 == '_':
      a3 = 'O'
      casas.remove('a3')
  elif a2 == 'X' and a3 == 'X' and a1 == '_':
      a1 = 'O'
      casas.remove('a1')
  elif a1 == 'X' and a3 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a1 == 'X' and b1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a1 == 'X' and b2 == 'X' and c3 == '_': ###
    c3 = 'O'
    casas.remove('c3')
  elif a1 == 'X' and c3 == 'X' and b2 == '_': 
    b2  = 'O'
    casas.remove('b2')
  elif b2 == 'X' and c3 == 'X' and a1 == '_':
    a1 = 'O'
    casas.remove('a1')
  elif a1 == 'X' and c1 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif b1 == 'X' and c1 == 'X' and a1 == '_':
    c1 = 'O'
    casas.remove('a1')
  elif b1 == 'X' and a1 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a2 == 'X' and b2 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif b2 == 'X' and c2 == 'X' and a2 == '_':
    a2 = 'O'
    casas.remove('a2')
  elif a2 == 'X' and c2 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':
    c3 == 'O'
    casas.remove('c3')
  elif a3 == 'X' and c3 == 'X' and b3 == '_':
    b3 = 'O'
    casas.remove('b3')
  elif b3 == 'X' and c3 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif a3 == 'X' and b3 == 'X' and c3 == '_':  
    c3 = 'O'
    casas.remove('c3')
  elif c3 == 'X' and a3 == 'X' and b3 == '_':  
    c3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b2 == 'X' and b3 == '_': 
    b3 = 'O'
    casas.remove('b3')
  elif b1 == 'X' and b3 == 'X' and b2 == '_': 
    b2 = 'O'
    casas.remove('b2')
  elif b3 == 'X' and b2 == 'X' and b1 == '_': 
    b1 = 'O'
    casas.remove('b1')
  elif c1 == 'X' and c2 == 'X' and c3 == '_':
    c3 = 'O'
    casas.remove('c3')
  elif c1 == 'X' and c3 == 'X' and c2 == '_':
    c2 = 'O'
    casas.remove('c2')
  elif c2 == 'X' and c3 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif a3 == 'X' and b2 == 'X' and c1 == '_':
    c1 = 'O'
    casas.remove('c1')
  elif c1 == 'X' and b2 == 'X' and a3 == '_':
    a3 = 'O'
    casas.remove('a3')
  elif c1 == 'X' and a3 == 'X' and b2 == '_':
    b2 = 'O'
    casas.remove('b2')
  else:
    while True:
      casa_aleatoria = random.choice(casas)
      if casa_aleatoria == j4:
        continue
      if casa_aleatoria.lower() == 'a2' and a2 == '_':
        a2 = 'O'
        casas.remove('a2')
        break
      elif casa_aleatoria.lower() == 'a3' and a3 == '_':
        a3 = 'O'
        casas.remove('a3')
        break
      if casa_aleatoria.lower() == 'b1' and b1 == '_':
        b1 = 'O'
        casas.remove('b1')
        break
      elif casa_aleatoria.lower() == 'b2' and b2 == '_':
        b2 = 'O'
        casas.remove('b2')
        break
      if casa_aleatoria.lower() == 'b3' and b3 == '_':
        b3 = 'O'
        casas.remove('b3')
        break
      elif casa_aleatoria.lower() == 'c1' and c1 == '_':
        c1 = 'O'
        casas.remove('c1')
        break
      if casa_aleatoria.lower() == 'c2' and c2 == '_':
        c2 = 'O'
        casas.remove('c2')
        break
      elif casa_aleatoria.lower() == 'a2' and c3 == '_':
        c3 = 'O'
        casas.remove('c3')
        break
  
  tabela()
  win_O()
  print(' ')
  print(' ')
  casas.remove(j4)
  while True:
    print(' ')
    j5 = input('\033[1;32mQual a sua jogada?:\033[m ')
    if j5 == 'A1' or j5 == 'A2'  or j5 == 'A3' or j5 == 'B1' or j5 == 'B2' or j5 == 'B3' or j5 == 'C1'  or j5 == 'C2' or j5 == 'C3':
      print('\033[1;31mDigite com letra minuscula!\033[m')
      continue
    if j5 == j1 or j5 == j2 and j5 == j3 and j5 == j4:
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5 == 'a1' and a1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j5 == 'a2' and a2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5 == 'a3' and a3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j5 == 'b1' and b1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5 == 'b2' and b2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j5 == 'b3' and b3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5 == 'c1' and c1 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    elif j5 == 'c2' and c2 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5 == 'c3' and c3 == 'O':
      print(' ')
      print('\033[1;31mCasa já selecionada\033[m')
      print(' ')
      print('Essas são as casas disponivéis: {}'.format(casas))
      continue
    if j5.lower() == 'a1':
      print(' ')
      break
    if j5.lower() == 'a2':
      print(' ')
      break
    elif j5.lower() == 'a3':
      print(' ')
      break
    if j5.lower() == 'b1':
      print(' ')
      break
    elif j5.lower() == 'b2':
      print(' ')
      break
    elif j5.lower() == 'b3':
      print(' ')
      break
    if j5.lower() == 'c1':
      print(' ')
      break
    elif j5.lower() == 'c2':
      print(' ')
      break
    elif j5.lower() == 'c3':
      print(' ')
      break
    if j5 != casas:
      print('\033[1;31mDigite uma casa corretamente!\033[m')
      continue
  if j5 == 'a1':
    a1 = 'X'
  elif j5 == 'a2':
    a2 = 'X'
  if j5 == 'a3':
    a3 = 'X'
  elif j5 == 'b1':
    b1 = 'X'
  if j5 == 'b2':
    b2 = 'X'
  elif j5 == 'b3':
    b3 = 'X'
  if j5 == 'c1':
    c1 = 'X'
  elif j5 == 'c2':
    c2 = 'X'
  if j5 == 'c3':
    c3 = 'X'

  win_O()
  win_X()
  tabela()
  print(' ')
  exit('DEU VELHA!')

import random 

print('\033[1;31;107m Ciencia da computação, turma A \033[m')
print(' ')
print('\033[1;31mEquipe:\033[m \033[4;97mAngela Dias Caruso;\033[m')
print('        \033[4;97mRickeelme Lopes De Souza;\033[m')
print('        \033[4;97mSthefany Felix Marques;\033[m')
print('        \033[4;97mVitor de Medeiros Cezairo.\033[m')
print(' ')

print('\033[1;31;107m JOGO DA VELHA \033[m')
print(' ')
print('\033[1;31mOLÁ, VOCÊ ESTÁ INICIANDO O JOGO DA VELHA!\033[m')
print(' ')
jogador = str(input('\033[4;97mPrimeiramente, qual seu nome?\033[m '))
sorteio = [jogador, 'a Máquina']
escolhido = random.choice(sorteio)
print(' ')
print('\033[0;30mMuito prazer {}! Antes de começa... Será realizado um sorteio, para vê quem começará jogando.\033[m'.format(jogador))
print(' ')
print('\033[1;30;107mQuem começará jogando será {}!\033[m'.format(escolhido))
print(' ')
if escolhido == jogador:
  jogador_começa()
elif escolhido == 'a Máquina':
  maquina_começa()
