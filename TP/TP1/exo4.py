#Convertion d'un nombre de secondes au format HH:MM:SS
s=int(input('entrez un nombre de second : ')) #lecture de s et convertion en entier
h=s//3600 #h est le nombre d'heures
m=(s%3600)//60 #m est le nombre de minutes
s=(s%3600)%60 #s est le nombre de secondes
print(h,':',m,':',s)
#une variante de la ligne precedente
#print(h,m,s,sep=':')
input() #pour que le programme ne se ferme pas apres l'execution
