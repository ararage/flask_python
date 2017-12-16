grades = [77,80,90,95,100]
tupla = (77,80,90,95,100) #immutable
setGrades = {77,80,90,95,100} #unique & unordered

#print sum(grades) / len(grades)

grades.append(109)

tupla = tupla + (200,)

#print setGrades
#print tupla

loteria = {1,2,3,4,5}
ganador = {1,3,5,7,9,11}

#Interseccion, elementos en comun 
print (loteria.intersection(ganador))
#Union de elementos
print(loteria.union(ganador)) 
#Diferencia de dos sets, en este caso 3 y 4
print({1,2,3,4}.difference({1,2}))
