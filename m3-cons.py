#Funcion que imprime la lista, completa o por categoría
def imprimir_nombres(nombres,imprimir):
    if imprimir == "Todo":
        for i, nombres in nombres.items():
            print(f"{nombres[0]} y su categoría es {nombres[1]}")
    elif imprimir == "Mago":
        for i, nombres in nombres.items():
            if nombres[1]== imprimir:
                print(nombres[0])
    elif imprimir == "Científico":
        for i, nombres in nombres.items():
            if nombres[1]== imprimir:
                print(nombres[0])
    elif imprimir == "Capo":
        for i, nombres in nombres.items():
            if nombres[1]== imprimir:
                print(nombres[0])

#funcion que cambia el nombre de los magos a traves de una variable auxiliar lista
def hacer_grandioso(nombres):
    for i ,nombre in nombres.items():
        if nombre[1]== "Mago":
            nombre_nuevo = "El gran " + nombre[0]
            lista_auxiliar=list(nombres[i])
            lista_auxiliar[0]=nombre_nuevo
            nombres[i]=tuple(lista_auxiliar)

nombres={}
nombres[0]=("Harry Houdini", "Mago")
nombres[1]=("Newton", "Científico")
nombres[2]=("David Blane", "Mago")
nombres[3]=("Hawking", "Científico")
nombres[4]=("Messi", "Capo")
nombres[5]=("Teller", "Mago")
nombres[6]=("Einstein", "Científico")
nombres[7]=("Fernández", "Capo")
nombres[8]=("Valdivia", "Capo")
print("Hola")
print("La lista de nombres es")
imprimir = "Todo" 
imprimir_nombres(nombres,imprimir)
hacer_grandioso(nombres)
print("Los nombres de los magos grandiosos es")
imprimir = "Mago"
imprimir_nombres(nombres,imprimir)
print("Los nombres de los cientificos es")
imprimir = "Científico"
imprimir_nombres(nombres,imprimir)
print("Los nombres de los capos es")
imprimir = "Capo"
imprimir_nombres(nombres,imprimir)
print("Adios")
