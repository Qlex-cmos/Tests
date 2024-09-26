
try:
    numero = int(input('Donner un numéro: '))
    toto = 1/numero

except ZeroDivisionError:
    print('Erreur : division par zéro')
except ValueError :
    print('Erreur : Valeur non valable')
else:
    print('toto = ', toto)

