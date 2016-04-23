#Resolution d'une equation du second degré
from math import sqrt #importation de la fonction racine (sqrt) depuis le module math
print('entrez a, b et c \n')
a=float(input())
b=float(input())
c=float(input())
if a==0 :
    if b==0 :
        if c==0 :
            print('tout reel est solution')
        else:
            print('pas de solutions')
    else:
        print(-c/b)
else:
    d=b*b-4*a*c #calcul du discriminant
    if d==0:
        print(-b/2*a)
    elif d>0:
        print('les solutions sont :\n')
        print((-b-sqrt(d))/2/a,(-b+sqrt(d))/2/a,sep=' et ') #l'interpreteur seclanchera une erreur si on n'importe pas sqrt
    else:
        print('pas de solution dans R')
input() #pour que le programme ne se ferme pas apres l'execution
