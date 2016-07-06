def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def rad_decay( start , stop ):
    exposed = 0
    for i in range(start, stop+1):
        exposed = exposed + f(i)
        print("exposed:")
        print(i)
        print(exposed)

    print("Exposed to radioactive : ")
    print(exposed)


rad_decay(5,11)    
    
    
