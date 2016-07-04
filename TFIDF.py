import math
import re

archivo=input('cual es el nombre del archivo?: ')
buscar=input('cual es la palabra a buscar?: ')


separador="____________________________________________________________________"

#crea la lista
def crearlista(doc):
    
    infile=open(doc, 'r')
    lista=[]
    
    for line in infile.readlines():
        lista.append(line.split())
        
    infile.close()
    return (lista)

lista=crearlista(archivo)

def listaTerminos():
    terminos=[]
    for i in lista:
        for x in i:
            if x in terminos:
                z=0
            else:
                terminos.append(x)
              

    return (terminos)



#Cuenta cuantos documentos hay en el archivo
def totalDocs():
    numDocs=0
    for i in lista:
        for x in i:
            if x=='.I':
                numDocs=numDocs+1
    return(numDocs)

#total de veces que se repite la palabra
def totalRepetidas():
    totalVeces=0
    for i in lista:
        for x in i:
            if x==buscar:
                totalVeces=totalVeces+1
    return(totalVeces)

#busca el IDF
def palabrasIDF():
    palabraIDF=0
    for i in lista:
        for x in i:
            if x==buscar:
                palabraIDF=palabraIDF+1
                break
    return(palabraIDF)
idf=math.log(totalDocs()/palabrasIDF())                  


#genera la tabla de frec de terminos     
def frecTerm():
    frecT=[]
    for i in lista:
        term=0
        for x in i:
            if x==buscar:
                term=term+1
        frecT.append(term)
    return(frecT)
listaFT=frecTerm()
#______________________________

def tablaIDF():
    tablaIDF=[]
    for i in listaFT:
        if i > 0:
            x=math.log(totalDocs()/i)
            tablaIDF.append(x)
        else:
            x=0
            tablaIDF.append(x)

            
    return(tablaIDF)
    
    

def tfidf():
    z=idf*totalRepetidas()
    return (z)







print("lista de tablas sin repetirse las palabras: ", listaTerminos())
print(separador)
print("numero de Documentos: ", totalDocs())
print(separador)
print("veces que se encuentra la palabra ",buscar,": ", totalRepetidas())
print(separador)

print("El IDF es: ", idf)
print(separador)
print ("documentos donde se encuentra", listaFT)
print(separador)
print ("IDF donde por documento", tablaIDF())
print(separador)
print("El TFIDF es de ", tfidf())
print(separador)

