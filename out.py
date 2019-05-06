import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=UserWarning) 

nome = ''
try:
    nome = sys.argv[1]
except:
    print('Argumento nome não definido. Exemplo de chamada: python out.py "Maria"')
    quit()

from modeloRandomForest import getSexoRandomForest, getSexoSVC


#nome = "marcel" # name in Portuguese
c = getSexoRandomForest(nome)
print('NAME: "{0}"'.format(nome))
print('RandomForest results:\n\tSex: {0}\n\t{1}'.format(c[0], c[1]))

c = getSexoSVC(nome)
print('\nSVC results:\n\tSex: {0}'.format(c))