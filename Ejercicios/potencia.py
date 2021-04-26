def potencia(base,exponente): 

    if exponente==0: 
        base=1; 
    else: 
        base=base*potencia(base,exponente-1); 
        
    return base; 

print(potencia(2,3)); 
