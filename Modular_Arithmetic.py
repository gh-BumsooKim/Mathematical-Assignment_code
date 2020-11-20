# modular arithmetic Test using Python Time Module

#import time as t
import timeit as ti

def mod(x, t):
    answer = divmod(x,t)
    
    return answer[1]

# modular arithmetic number = 2011
# private numA = 55
# private numB = 123
    
def modular_arithmetic():
    A0 = 3**55
    k1 = mod(A0,2011)
    print(k1)
    
    B0 = 3**123
    k2 = mod(B0,2011)
    print(k2)
    
    # Start time
    #start_time = t.time()
    
    answer1 = mod(k1**123,2011)
    answer2 = mod(k2**55,2011)
    
    if(answer1 == answer2):
        #end_time = t.time()
        #print("WorkingTime : {0:.12f} sec ". format(end_time-start_time))
        print(answer1)
        
ans = ti.timeit('modular_arithmetic', 
                setup='from __main__ import modular_arithmetic', number=1)
print("WorkingTime : {0:.24f} sec ". format(ans))