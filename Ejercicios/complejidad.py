from timeit import default_timer
def decorador(name): 
    
    def funcion_c(funcion): 
        def wrapper(*args, **kwargs): 
            inicio=default_timer(); 
            res=funcion(*args, **kwargs); 
            final=default_timer(); 
            final=final-inicio; 
            print(name+"--> Tardo: %.15f Seconds."% final);  
            return res; 
        return wrapper; 
    return funcion_c; 

@decorador('Busqueda Lineal')
def Busqueda_Lineal(): 
    Lista=[1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23,24,25];
    #x=1;# caso mejor
    x=12 #caso medio
    #x=26 # caso peor 
    i=0; 
    n=len(Lista)-1; 
    while (i<n): 
        if Lista[i]==x: 
            return i; 
        i=i+1; 
    return None; 

@decorador('Busqueda Binaria')
def Busqueda_Binaria(): 
    Lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];
    #x=12 # caso mejor
    #x=13 #caso medio
    x=26 # caso peor 
    inicio=0; 
    fin=len(Lista)-1; 
    while inicio<=fin: 
        medio=(inicio+fin) // 2; 
        if Lista[medio]==x: 
            return medio; 
        elif x>Lista[medio]: 
               inicio=medio+1; 
        else: 
                fin=medio-1; 
    return None; 

@decorador('Transponer')
def Transponer(): 
    bandera=True; 
    Lista=[]; 
    while bandera: 
        valor=input("Ingrese un dato o presione 1 para salir: "); 
        if valor=='1': 
            bandera=False; 
        else: 
            Lista.append(valor);
    m=0; 
    n=len(Lista); 
    i=0; 
    k=int(input("Ingrese un numero Positivo: ")); 
    n=n-k;  
    resguardo=k; 

    while k>0: 
        aux=Lista[i]; 
        Lista[i]=Lista[n]; 
        Lista[n]=aux; 
        i=i+1; 
        k=k-1; 
        n=n+1; 

    i=0; 
    k=resguardo; 
    for i in range(0,len(Lista)-1): 
        if i<=k: 
            aux=Lista[i]; 
            Lista[i]=Lista[i+k]; 
            Lista[i+k]=aux; 
        elif k>=1: 
            aux=Lista[i]; 
            k=k-1; 
            Lista[i]=Lista[i+k]; 
            Lista[i+k]=aux; 
    print(Lista); 

@decorador('Burbuja')
def Ordenamiento_Burbuja(): 
    Lista=[1,90,3,4,5,11,7,8,9,10,34,12,13,22,15,16,30,18,19,20,21,22,23,24,25];
    for i in range(0, len(Lista)): 
        for j in range(0,len(Lista)-1): 
            if Lista[j]>Lista[j+1]: 
                aux=Lista[j]; 
                Lista[j]=Lista[j+1]; 
                Lista[j+1]=aux; 
    print (Lista);  

@decorador('Seleccion')
def Seleccion(): 
    Lista=[1,90,3,4,5,11,7,8,9,10,34,12,13,22,15,16,30,18,19,20,21,22,23,24,25];
    for i in range(len(Lista)): 
        minimo=i; 
        for j in range(i, len(Lista)): 
            if Lista[j]<Lista[minimo]: 
                minimo=j; 
        if minimo !=i: 
            aux=Lista[i]; 
            Lista[i]=Lista[minimo]; 
            Lista[minimo]=aux; 
    print (Lista); 
star=default_timer(); 

def particionado(Lista): 
    pivote=Lista[0]; 
    menores=[]; 
    mayores=[]; 
    for i in range(1, len(Lista)): 
        if Lista[i] < pivote:
            menores.append(Lista[i]); 
        else: 
            mayores.append(Lista[i]); 
    return menores, pivote, mayores 

def quick_sort(Lista): 
    if len(Lista)<2: 
        return Lista; 
    else: 
        menores,pivote, mayores=particionado(Lista);
    return quick_sort(menores)+[pivote]+quick_sort(mayores)

finish=default_timer(); 

def particion(Lista, menor, mayor): 
    pivote=Lista[menor]; 
    izq=menor+1; 
    der=mayor; 
    while True: 
        while izq<=der and Lista[izq]<=pivote: 
            izq=izq+1; 
        
        while izq<=der and Lista[der]>=pivote: 
            der=der-1; 
        
        if der<izq: 
            break; 
        else: 
            Lista[izq], Lista[der] = Lista[der], Lista[izq]; 

    Lista[menor], Lista[der] = Lista[der], Lista[menor] 
    
    return der 

def hoare(Lista, menor, mayor): 
    if (menor<mayor): 
        pivote=particion(Lista,menor, mayor); 
        hoare(Lista, menor, pivote-1); 
        hoare(Lista, pivote+1, mayor); 

@decorador('euclides')
def euclides(a,b): 
    resto=a%b; 
    while resto>0: 
        if resto !=0: 
            a=b; 
            b=resto; 
        resto=a%b; 
    return b; 

        
Busqueda_Lineal(); 
#Busqueda_Binaria(); 
#Transponer();
#Ordenamiento_Burbuja();
#Seleccion();
#Lista=[8,12,3,11,5,9,10,4,15,7, 20,21,89,45,123,100,1000]; 
#finish=finish-star; 
#hoare(Lista, 0, len(Lista)-1); 
#print( Lista, " Tiempo de ejecucion: %.8f"% finish); 
#print(euclides(60,48)); 
