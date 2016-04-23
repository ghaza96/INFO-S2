#calcul du prix ttc et du prix total ttc
tva=0.2
ht=float(input('entrez le prix ht : ')) #lecture du ht et convertion en entier
print() #saut de ligne
nb=int(input('entrez le nombres d\'articles : '))
print() #saut de ligne
ttc=ht+(ht*tva)
tttc=ttc*nb
print('ttc=',ttc)
print() #saut de ligne
print('total ttc=',tttc)
input() #pour que le programme ne se ferme pas apres l'execution
