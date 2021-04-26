from timeit import default_timer; 
inicio=default_timer(); 
def euclides(M,N): 
    if N==0: 
        return M; 
    else: 
        res=euclides(N,M%N); 
        return res; 

final=default_timer(); 
final=final-inicio; 
print(euclides(2353,1651), "Tiempo de ejecucion: %.8f"%final); 