"""Tienda de productos  
Una Tienda vende productos, Cada producto tiene un nombre, 
un precio, una cantidad en stock y un tipo, los tipos pueden ser: 
aseo, comida, medicamento. Se requiere desarrollar un 
programa en Python que permita ingresar productos a la tienda, 
y cada que ingrese un producto debe preguntar si se quieren 
ingresar más productos o si no.  Debe verificar que el tipo de 
producto sea uno de los válidos, que la cantidad en stock y 
precio no sean negativos ni cero, y que el nombre del producto sea de mínimo 3 
caracteres.  El programa debe funcionar de manera correcta si los tipos son escritos 
en mayúsculas o minúsculas o combinación de ellas. 
Cuando se termine el ingreso de productos el programa debe mostrar: 
a) La información de todos los productos ingresado 
b) La cantidad de productos de cada tipo que hay en la tienda. 
c) El porcentaje de productos de aseo que hay en la tienda 
d) Un listado de los productos de aseo que hay en la tienda"""

def tienda():
    cantidad_comida = 0
    cantidad_med = 0
    aseo_procentaje = 0
    
    lista_aseo = ""
    lista = ""
    opcion = input("¿desea agregar un poducto?, si o no: ")
    mayus_opcion = opcion.upper()
    
            
    while mayus_opcion != "NO" and mayus_opcion == "SI":
        tipos = int(input("¿en cual categoria pertenece el producto a ingresar? \nmedicamento: 1 \naseo: 2 \ncomida: 3\n: "))

        while tipos >= 4 or tipos <= 0:
            tipos = int(input("ingrese una categoria valida: \nmedicamento: 1 \naseo: 2 \ncomida: 3\n: "))

        nombre = input("ingrese el nombre del producto: ")
        while len(nombre) < 3:   
            nombre = input("ingrese un nombre con minimo 3 caracteres: ")


        prod = int(input("igrese la cantidad del producto: "))
        while prod < 0:
            prod = int(input("igrese la cantidad del producto valida: "))

        if tipos == 1 and prod > 0:
            cantidad_comida += prod
        if tipos == 3 and prod > 0:
            cantidad_med += prod
        if tipos == 2 and prod > 0:
            aseo_procentaje += prod
            lista_aseo = lista_aseo + "\n" "nombres de los productos de aseo: " +  nombre + "\n"
            

        precio = float(input("ingrese el precio del producto: "))
        while precio < 0:
            float(input("ingrese el precio del producto correctamente: "))

        opcion = input("¿desea agregar otro poducto?, si o no: ")
        mayus_opcion = opcion.upper()


        lista = lista + "\n" "nombre:" + nombre +  "\n" "cantidad:" +  str(prod) + "\n" "precio:" + str(precio) + "\n"
    total_productos = cantidad_comida + aseo_procentaje + cantidad_med 
    porcen_as = (aseo_procentaje * 100) / total_productos


    print(lista)
    print("la cantidad de productos que son medicamentos son: ", cantidad_med)
    print("la cantidad de productos que son comida es: ", cantidad_comida)
    print("la cantidad de productos que son productos de aseo es: ", aseo_procentaje)
    print("el total de productos digitados son: ", total_productos, "y el porentaje de los productos de aseo es: ",porcen_as,"%")
    print(lista_aseo)

tienda()
