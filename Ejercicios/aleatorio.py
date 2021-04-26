import random; 
from timeit import default_timer; 
def decorador(n): 
    def funcion(): 
            print('-----'); 
            inicio=default_timer(); 
            n()
            fin=default_timer(); 
            tiempo=fin-inicio; 
            print("Segundos %.8f"%tiempo); 
    return funcion; 




@decorador
def aleatorio(): 

    aleatorio=random.randint(1,100); 
    bandera=True; 
    while bandera: 

        valor=int(input("Ingrese un valor positivo ")) ; 
        if valor==aleatorio: 
            bandera=False; 
        else: 
            if valor>aleatorio: 
                print("El numero ingresado es mayor"); 
            else: 
                print("el numero es menor"); 
@decorador         
def aleatorio2(): 
    aleatorio=random.randint(1,100); 
    Lista=[]; 
    for i in range(1,100): 
        Lista.append(i);  
        
    Lista.append(i+1); 
    inicio=0; 
    final=len(Lista)-1; 
    while inicio <=final: 
        PM=(inicio+final)//2; 
        if Lista[PM]==aleatorio: 
            print("encontrado el valor ", aleatorio, 'en la posicion', PM); 
            return PM; 
        elif Lista[PM]>aleatorio: 
             final=PM-1; 
        else: 
            inicio=PM+1; 


#aleatorio(); 
aleatorio2()