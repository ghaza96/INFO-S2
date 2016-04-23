#la mention selon la moyenne
m=float(input('entrer la moyenne : '))
if m<0 or m>20 :
    print('la moyenne doit etre comprise entre 0 et 20')
elif m>=16:
    print('tres bien')
elif m>=14:
    print('bien')
elif m>=12:
    print('assez bien')
elif m>=10:
    print('passable')
else:
    print('ajjourné')
#En Python elif est equivalente à sinon si
input() #pour que le programme ne se ferme pas apres l'execution
