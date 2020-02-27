
listaNo=[0,3,2] #Declaracion de una lista las frecuencias de Si
listaSi=[4,2,3] #Declaracion de una lista con las frecuencias de No
#nublado=(listaNo[0]+listaSi[0]) #Sumatorias de frecuencias de nublado
#lluvia=(listaNo[1]+listaSi[1]) #Sumatorias de frecuencias de lluvia
#soleado=(listaNo[2]+listaSi[2]) #Sumatorias de frecuencias de soleado
sumano=0  #Suma de frecuencuas en no
sumasi=0  #Suma de frecuencias en si
frecuenciasTotales=0 #Total de frecuencias de las dos listas.

for i in listaNo: #Recorremos y sumamos los elementos de la listaNo
    sumano+=i
for i in listaSi: #Recorremos y sumamos los elementos de la listaSi
    sumasi+=i

frecuenciasTotales=sumasi+sumano #Suma los totales de las frecuencias en si y en no.

#Metodo para calcular la probabilidad de Si.
def bayesSi(listaSi,sumasi,frecuenciasTotales,listaNo):

    bayes=(((listaSi/sumasi)*(sumasi/frecuenciasTotales))/((listaNo+listaSi)/frecuenciasTotales))
    return bayes

#Metodo para calcular la probabilidad de No.
def bayesNo(listaNo,sumano,frecuenciasTotales,listaSi): 
    bayes=(((listaNo/sumano)*(sumano/frecuenciasTotales))/((listaNo+listaSi)/frecuenciasTotales))
    return bayes

#Declaracion y asiganacion de metodos.
nubladoSi=bayesSi(listaSi[0],sumasi,frecuenciasTotales,listaNo[0])
nubladoNo=bayesNo(listaNo[0],sumano,frecuenciasTotales,listaSi[0])
lluviaSi=bayesSi(listaSi[1],sumasi,frecuenciasTotales,listaNo[1])
lluviaNo=bayesNo(listaNo[1],sumano,frecuenciasTotales,listaSi[1])
soleadoSi=bayesSi(listaSi[2],sumasi,frecuenciasTotales,listaNo[2])
soleadoNo=bayesNo(listaNo[2],sumano,frecuenciasTotales,listaSi[2])


#Impresion de variables que contienen los resultados de los metodos.
print("-------------------------\nSumas")
print("Elementos en no: ",sumano)
print("Elementos en si: ",sumasi)   
print("Total de elementos",frecuenciasTotales)
print("\n-------Bayes Naive-------")
print("NubladoSi: ",nubladoSi)
print("NubladoNo: ",nubladoNo)
print("LluviaSi: ",lluviaSi)
print("LluviaNo: ",lluviaNo)
print("SoleadoSi: ",soleadoSi)
print("SoleadoNo: ",soleadoNo)
