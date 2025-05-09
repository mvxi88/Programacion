lista_mascota = []

archivo = open('C:\\Users\\Maximiliano\\Documents\\Introduccion a la Programacion Segura\\Programacion\\veterinaria\\mascotas.txt', 'r+')
lista_mascota = archivo.readlines()

raza = input("Ingrese raza de su mascota: ")
edad = input("Ingrese edad de su mascota: ")
nombre = input("Ingrese nombre de su mascota: ")
dueño = input("Ingrese dueño de su mascota: ")
#tipo = input("Ingrese tipo de su mascota: ")

mascota = [raza,edad,nombre,dueño]
lista_mascota.append(mascota)

archivo.write(str(mascota) + '\n')
archivo.close()