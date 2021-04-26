from timeit import default_timer
inicio=default_timer(); 
def euclides(a,b): 
    resto=a%b; 
    while resto>0: 
        if resto !=0: 
            a=b; 
            b=resto; 
        resto=a%b; 
    return b; 
final=default_timer(); 
final=final-inicio; 
print(euclides(2353,1651), "Tiempo de ejecucion %.8f"%final); 