print('w x y z F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((x==y)and(z and not(w))) == (not(((y<=w)and(z==y))or y)):
                    F=1
                else:
                    F=0
                print(w,x,y,z,F)
