#Signe d'un produit sans le calculer
print('saisir deux reels : ')
a=int(input())
print()
b=int(input())
if a==0 or b==0:
    print('nul')
else:
    if (a>0 and b>0) or (a<0 and b<0):
        print ('positif')
    else:
        print ('negatif')
    #si imbriquée
input() #pour que le programme ne se ferme pas apres l'execution
