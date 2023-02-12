'''Usando decorator para contar tempo'''

import time

def decor_tempo(func):
  def empacotar():
    t1 = time.time()
    func()
    t2 = time.time() - t1
    print(f'{func.__name__} rodou em'\
        f' {t2} segundos.')
  return empacotar

@decor_tempo
def tempo_um():
  '''Simulando um código radando'''
  time.sleep(0.8)


@decor_tempo
def tempo_dois():
  '''Simulando um código radando'''
  time.sleep(.2)


tempo_um()
tempo_dois()

print('FIM!')
