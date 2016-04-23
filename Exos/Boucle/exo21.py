#Affichage des nombres verifiants (10*c+d)*(10*a+b) entre 10 et 100
for i in range(10,100):
    a=i%10
    b=i//10
    for j in range(10,100):
        c=j%10
        d=j//10
        if i*j==(10*c+d)*(10*a+b)and (a!=b or c!=d) and (a!=d or b!=c) and i<j:
            #from cond2 to cond5 are to avoid redendency
            print (b,a,'*',d,c,'=',a,b,'*',c,d)
input()
