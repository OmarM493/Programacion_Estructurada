print("\033c")
trabajadores=0
sueldos_netos=0
respuesta="S"
while respuesta=="S":
    nombre=input("introdusca su nombre: ")
    horas_trabajo=int(input("ingrasar horas trabajadas: "))
    sueldo_hora=float(input("ingresar sueldo por hora: "))
    sueldo=sueldo_hora*horas_trabajo
    if horas_trabajo == 10:
        aumento=sueldo*.2
    elif horas_trabajo==15:
        aumento=sueldo*.3
    elif horas_trabajo==20:
        aumento=sueldo*.15
    elif horas_trabajo>=25:
        aumento=sueldo*.08
    print(f"el aumento es de: ${aumento}")
    sueldo=sueldo_hora*horas_trabajo
    sueldo_neto=sueldo+aumento
    sueldos_netos=sueldos_netos+sueldo_neto
    trabajadores+=1
    respuesta=input("¿Desea imngresar otro trabajador? (S/N)")
print(f"los trabajadores ingresados fueron: {trabajadores}")
print(f"los sueldos netos fueron: ${sueldos_netos}")