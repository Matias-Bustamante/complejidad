
def Merge_Sort(lista): 
    if len(lista)>1: 
        media=len(lista)//2; 
        primera_mitad=lista[:media]; 
        segunda_mitad=lista[media:]; 
        Merge_Sort(primera_mitad); 
        Merge_Sort(segunda_mitad); 
        i=0; 
        j=0; 
        k=0; 
        while i<len(primera_mitad) and j<len(segunda_mitad): 
            if primera_mitad[i]<segunda_mitad[j]: 
                lista[k]=primera_mitad[i]; 
                i=i+1; 
            else: 
                lista[k]=segunda_mitad[j]; 
                j=j+1; 
            k=k+1; 
        
        while i<len(primera_mitad): 
            lista[k]=primera_mitad[i]; 
            i=i+1; 
            k=k+1; 
        
        while j<len(segunda_mitad): 
            lista[k]=segunda_mitad[j]; 
            j=j+1; 
            k=k+1; 
    
lista=[15,10,8,90,100]; 
print("Lista desordenada: ", lista); 
Merge_Sort(lista); 
print("Lista ordenada: ", lista); 