
productos = []


    
while True:
    
    
    print("\n======Menú======")
    print("1. Agregar productos")
    print("2. Mostrar Productos")
    print("3. Buscar productos") 
    print("4. Eliminar productos")
    print("5. Salir")
    
    opcion = input("Elegí una opción: ").strip()
    
    #================
    #Agregar producto
    #================
    
    if opcion == "1":
        
        nombre = input("Nombre del producto: ").strip().capitalize()
        
        if nombre == "":
            print("no se ha agregado ningún producto")
            continue
        
        categoria = input ("Categoria del producto: ").strip().capitalize()
        
        if categoria == "":
            print ("___Debe agregar una categoria del producto___")
            continue
        
        precio =input("Ingrese su precio (sin centavos): ").strip()
        
        if not precio.isdigit():
            print("El precio no debe contener centavos")
            continue
            
        precio = int(precio)
        
        producto = [nombre,categoria,precio]
        
        productos.append(producto)
        
        print ("Producto agregado correctamente")
    
    #==================
    # MOSTRAR PRODUCTOS
    #==================    
    elif opcion == "2":
        
        if len(productos) == 0:
            print("no se han encontrado productos")
            
        else:
            
            print("\n===== LISTA DE PRODUCTOS =====")
            
            for i, producto in enumerate(productos):
                
                print(f"{i+1}. Nombre: {producto[0]} ")
                
                print(f"   Categoria: {producto[1]}")
                
                print(f"   Precio: ${producto[2]}")
                
                print("--------------------------")            
    
    
    #==================
    # BUSCAR PRODUCTOS
    #==================
    elif opcion == "3":
        
        if len(productos) == 0:
            print("no hay productos para mostrar")
            continue
        
        buscar = input("Ingresá el nombre del producto: ").strip().capitalize()
        
        if buscar == "":
            print ("Debe ingresar un producto")
            continue
        
        encontrado = False
        
        for producto in productos:
            
            if buscar in producto[0]:
                
                print("\n--- Producto encontrado ---")

                print(f"Nombre: {producto[0]}")
                
                print(f"Categoría: {producto[1]}")
                
                print(f"Precio: ${producto[2]}")    
                
                encontrado = True
        
        if encontrado == False:
            print("No se ha encontrado el producto")
    
    #====================
    # ELIMINAR PRODUCTOS
    #====================        
            
    elif opcion == "4":
        
        if len(productos) == 0:
            print ("No hay productos para eliminar")
            continue
        
        for i, producto in enumerate(productos):
            
            print(f"{i+1}. Nombre: {producto[0]}")
            
        eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
        
        encontrado = False
        
        for producto in productos:
            
            if eliminar == producto [0]:
                
                productos.remove(producto)
                
                print(f"Producto '{eliminar}' eliminado correctamente")
                
                encontrado = True
                
                break
            
        if not encontrado:
            print("Producto no encontrado")
            
    #===================
    # SALIR DEL PROGRAMA   
    #===================
    elif opcion == "5":
        print("Programa finalizado")
        break
    
    
              