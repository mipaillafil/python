import csv

trabajadores = []
cargos = ["CEO", "Analista de Datos", "Desarrollador"]
ceoS = []
analistas = []
desarrollador = []


def worker(sueldoLiquido):
    name = nombre
    position = cargo
    salarioBruto = sueldobruto
    calcularsueldo = sueldoLiquido()
    return name, position, salarioBruto, calcularsueldo


def sueldoLiquido():
    porcentaje = 0.12
    descAFP = round(sueldobruto * porcentaje)

    porcentaje2 = 0.07
    descSalud = round(sueldobruto * porcentaje2)
    
    sueldoliquido = round(sueldobruto - descAFP - descSalud)
    
    print("Nombre |","Cargo |","Sueldo Bruto |","Desc.AFP |","Desc.Salud |","Sueldo Liquido |")
    print(f"{nombre}\t  {cargo}\t  {sueldobruto}\t  {descAFP}    {descSalud}\t{sueldoliquido}")

def listatrabajadores():
    print("="*20)
    print("LISTA DE TRABAJADORES")
    print("="*20)
    for i  in trabajadores:
        print(i)
        
def planillas():
    print("="*20)
    print("\tMENÚ")
    print("="*20)
    print("1.- Imprimir planilla de CEO's.")
    print("2.- Imprimir planilla de Desarrolladores.")
    print("3.- Imprimir planilla de Analistas de datos.")
    print("4.- Imprimir planilla de todos los trabajadores.")
    planilla = input("> ")

    if planilla == "1":
        print(ceoS)
        with open('planillasceoS.txt', 'w', newline='') as archivo:
            archivo.read('"Nombre","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Sueldo Liquido"')
            for trabajador in ceoS:
                archivo.write(str(trabajador))
                print("Se ha generado un archivo de texto.")
                
    elif planilla == "2":
        print(desarrollador)
        with open('planillasdesarrolladores.txt', 'w', newline='') as archivo:
            archivo.write('"Nombre","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Sueldo Liquido"')
            for trabajador in desarrollador:
                archivo.write(str(trabajador))
                print("Se ha generado un archivo de texto.")
                
    elif planilla == "3":
        print(analistas)
        with open('planillasanalistas.txt', 'w', newline='') as archivo:
            archivo.write(("Nombre","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Sueldo Liquido"))
            for trabajador in analistas:
                archivo.write(str(trabajador))
                print("Se ha generado un archivo de texto.")
                
    elif planilla == "4":
        print(trabajadores)
        with open('planillastrabajadores.txt', 'w', newline='') as archivo:
            archivo.write('"Nombre","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Sueldo Liquido"')
            for trabajador in trabajadores:
                archivo.write(str(trabajador))
                print("Se ha generado un archivo de texto.")
     
    else:
        print("La opción ingresada no es valida")
    
while True:
    print("="*20)
    print("\tMENÚ")
    print("="*20)
    print("1.- Registrar trabajador.")
    print("2.- Listar todos los trabajadores.")
    print("3.- Imprimir planilla de sueldos.")
    print("4.- Salir del programa.")
    opc = input("> ")
    
    match opc:
        case "1":
            while True:
                try:
                    nombre = input("Ingrese el nombre del trabajador: ")
                    cargo = input("Ingrese el cargo del trabajador: ")
                    sueldobruto = int(input("Ingrese el sueldo bruto del trabajador: "))
                except:
                    print("Verfique que todos los valores hayan sido ingresados correctamente.")
                else:
                    break
                
            trabajador = worker
            
            if cargo not in cargos:
                print("El cargo ingresado no existe dentro de la empresa.")
            else:
                trabajadores.append(trabajador)
                worker(sueldoLiquido)
                print("\nEl trabajador ha sido registrado.")
            
            if cargo == cargos[0]:
                ceoS.append(trabajador)
            elif cargo == cargos[1]:
                analistas.append(trabajador)
            elif cargo == cargos[2]:
                desarrollador.append(trabajador)
                
        case "2":
            listatrabajadores()
            
        case "3":
            planillas()
            
        case "4":
            print("Cerrando sesión")
            break