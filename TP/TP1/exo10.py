#les nombres q'on peut ecrire a partir de 3 chiffres
n=int(input('entrer un entier de 3 chiffrs non nuls : '))
if n>=100 and n<=999:
    #extraction des unités,dizaines et centaines
    c=n//100
    d=(n%100)//10
    u=n%10
    if c!=0 and d!=0 and u!=0:
        i=c*100+u*10+d
        j=u*100+c*10+d
        k=u*100+d*10+c
        l=d*100+c*10+u
        m=d*100+u*10+c
        print(n,i,j,k,l,m)
    else:
        print('les chiffres doivent etre non nuls : ')
else:
    print('le nb doit comporter 3 chiffres')
input() #pour que le programme ne se ferme pas apres l'execution
