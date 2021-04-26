def factorial(numero): 
    if numero==2: 
            numero=2; 
            
    else: 
        numero=numero*factorial(numero-1);
    return numero; 

print(factorial(4)); 