
ingrediente_vegano = "Pimiento", "tofu"


ingrediente_no_vegano = "Peperoni",  "Jamon",  "Salomon"


#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva

respuesta = input("¿Desea una pizza vegetariana? (si/no): ")        
if respuesta.lower() == "si":
    print("Ingredientes disponibles para pizza vegetariana:")
    print(f"1. {ingrediente_vegano}")

    eleccion = input("Seleccione un ingrediente (1 o 2): ")
    
    if eleccion == "1":
        ingrediente_elegido = ingrediente_vegano
    elif eleccion == "2":
        ingrediente_elegido = ingrediente_vegano
    else:
        print("Opción no válida.")
        exit()
    
    print(f"Has elegido una pizza vegetariana con los siguientes ingredientes: Mozzarella, Tomate y {ingrediente_elegido}.")