
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    print(f"el nombre del alumno es: {nombre} {apellidos}")
#invocar la funcion
funcion1()


 #3.- Funcion que recibe parametros y no regresa valor
def funcion3(nombre,apellidos):
    print("\033c")
    print(f"el nombre del alumno es: {nombre} {apellidos}") 
#invocar la funcion
print("\033c")
nombre=input("Nombre: ").strip().upper()
apellidos=input("apellidos: ").strip().upper()
funcion3(nombre,apellidos)


 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion2()
print(nombre,apellidos)


 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    print("\033c")
    nombre=nom
    apellidos=ape
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion4("Omar","Mancinas")
print(nombre,apellidos)



#Invocar las funciones
"""
funcion1()

nombre=input("Nombre: ").strip().upper()
apellidos=input("apellidos: ").strip().upper()
funcion3(nombre, apellidos)

nombre,apellidos=funcion2()
print(nombre,apellidos)

nombre,apellidos=funcion4(nom,ape)
print(nombre,apellidos)
"""