# print("\033c")
# #Ejemplo 1 Crear una lista de numeros e imprimir el contenido
# numeros=[23,45,23,33,25,100,-100]
# print(numeros)

# lista="["
# for i in numeros:

#     lista+=f"{i}, "
# print(f"{lista}]")

# lista="["
# for i in range(0,len(numeros)):
#     lista+=f"{numeros[i]}, "
# print(f"{lista}]")

# lista="["
# i=0
# while i<len(numeros):
#     lista+=f"{numeros[i]}, "
#     i+=1
# print(f"{lista}]")



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabra=input("palabra a buscar: ")

# if palabra in palabra:
#     print(f"Esta palabra: {palabra}, si se encuentra en la lista")
# else:
#     print(f"Esta palabra: {palabra}, no se encuentra en la lista")


#2DA FORMA
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabra=input("palabra a buscar: ")

# encontre=False
# for i in palabras:
#     if i==palabra:
#         encontre=True
# if encontre:
#     print(f"Esta palabra: {palabra}, si se encuentra en la lista")
# else:
#     print(f"Esta palabra: {palabra}, no se encuentra en la lista")
        
 

#3er FORMA
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabra=input("palabra a buscar: ")

# encontre=False
# while encontre==False:
#     for i in palabras:
#         if i==palabra:
#             encontre=True
#         else:
#             encontre=False
# if encontre:
#     print(f"Esta palabra: {palabra}, si se encuentra en la lista")
# else:
#     print(f"Esta palabra: {palabra}, no se encuentra en la lista")


# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabra=input("palabra a buscar: ")

# encontre=False
# for i in range(0,len)
# if encontre:
#     print(f"Esta palabra: {palabra}, si se encuentra en la lista")
# else:
#     print(f"Esta palabra: {palabra}, no se encuentra en la lista")

#Ejemplo 3 Añadir elementos a la lista
# lista=[]
# true="S"
# while true=="S":
#     valor=input("dame una palabra para la lista").upper().strip()
#     lista.append(valor)
#     true=input("deseas añadir otra palabra a la lista (S/N)? ").upper().strip()
  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["carlos","6181234567"],
        ["juan","6182345678"],
        ["Tony","182342323"]
        ]


for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}"
    lista+="\n"
print("["+lista+"]")
# print(agenda)
# for i in agenda:
#     print(i)

