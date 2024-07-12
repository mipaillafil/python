import random
import csv

trabajadores = [['Juan Pérez'], ['María Garcia'], ['Carlos López'], ['Ana Martínez'], ['Pedro Rodríguez'], ['Laura Hernández'], ['Miguel Sánchez'], ['Isabel Goméz'], ['Francisco Díaz'], ['Elena Fernandez']]
def asignar_sueldo(trabajadores):
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        trabajador.append(sueldo)
    print("\nLos sueldos se han asignado exitosamente.\n")
    return trabajadores

def clasificar_sueldos(trabajadores):
    print()
    print("="*20)
    print("CLASIFICAR SUELDOS")
    print("="*20)
    try:
        print("==SUELDOS MENORES A $800000==")
        print("Nombre empleado\t| Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] < 800000:
                print(trabajador)
        
        print("\n==SUELDOS ENTRE $800000 Y $2000000==")
        print("Nombre empleado\t| Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] >= 800000 and trabajador[1] <= 2000000:
                print(trabajador)
        
        print("\n==SUELDOS SUPERIORES A $2000000==")
        print("Nombre empleado\t| Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] > 2000000:
                print(trabajador)
                                        
    except IndexError:
       print("\nNo hay sueldos registrados.\n")
    
def estadisticas(trabajadores):
    try:
        sueldos =[]
        for trabajadoresregistrados in trabajadores:
            sueldos.append(trabajadoresregistrados[1])
    except:
        print("\nNo hay sueldos registrados.\n")
    else:
        print("="*20)
        print("VER ESTADISTICAS")
        print("="*20)
    
        sueldo_alto = max(sueldos)
        sueldo_menor = min(sueldos)
        promedio_sueldo = round(sum(sueldos)/10)
        
        
        print(f"Sueldo más alto: {sueldo_alto}")
        print(f"Sueldo más bajo: {sueldo_menor}")
        print(f"Promedio de sueldos: {promedio_sueldo}")
     
        
def reporte_sueldos(trabajadores):
    try:
        with open('Reporte_Sueldos.csv', 'w', newline='') as archivo:
            archivo.write("Nombre empleado| Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Liquido")
            for trabajador in trabajadores:
                nombre = trabajador[0]
                sueldoBase = trabajador[1]
                DescSalud = round(sueldoBase * 0.07)
                DescAFP = round(sueldoBase * 0.12)
                sueldoLiquido = sueldoBase - DescSalud - DescAFP
                archivo.write(f"\n{nombre},{sueldoBase},{DescSalud},{DescAFP},{sueldoLiquido}")
        print("\nSe ha generado un archivo de reporte de sueldos.\n")
    except IndexError:
        print("\nNo hay sueldos registrados.\n")
        
while True:
    print("="*20)
    print("\tMENÚ")
    print("="*20)
    print("1.- Asignar sueldos aleatorios.")
    print("2.- Clasificar sueldos.")
    print("3.- Ver estadísticas.")
    print("4.- Reporte de sueldos.")
    print("5.- Salir del programa.")
    opc = int(input("> "))
    
    if opc == 1:
        asignar_sueldo(trabajadores)
    elif opc == 2:
        clasificar_sueldos(trabajadores)
    elif opc == 3:
        estadisticas(trabajadores)
    elif opc == 4:
        reporte_sueldos(trabajadores)
    elif opc == 5:
        print("Finalizando programa...")
        print("Desarrollado por Millaray Paillafil González.")
        print("RUT 21.291.888-1")
        break
    else:
        print("\nLa opción seleccionada no es valida. Intentelo de nuevo.\n")