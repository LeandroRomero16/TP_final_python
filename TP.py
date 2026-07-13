
import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio INTEGER NOT NULL
)
""")

conexion.commit()


    
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
        
        while True:
            nombre = input("Ingrese el nombre del producto o Exit para salir al menú: ").strip().title()
        
            if nombre == "Exit":
                print("Saliendo del menú de agregado de productos...")
                break
            
            if nombre == "":
                print("No se ha agregado ningun producto. Por favor ingrese uno")
                continue
           
        
        
            categoria = input ("Categoria del producto: ").strip().title()
        
            if categoria == "":
                print ("___Debe agregar una categoria del producto___")
                continue
        
            precio =input("Ingrese su precio (sin centavos): ").strip()
        
            if not precio.isdigit():
                print("El precio no debe contener centavos")
                continue
            
            precio = int(precio)
        
            cursor.execute(
                "INSERT INTO productos (nombre, categoria, precio) VALUES (?,?,?)",
                (nombre, categoria, precio)
            )
            conexion.commit()
        
            print ("Producto agregado correctamente")
            
            continuar = input("\nPresiona enter para seguir agregando productos o Exit para salir al menú: ").strip().capitalize()
            
            if continuar == "Exit":
                print("Saliendo al menú...")
                break
    
    #==================
    # MOSTRAR PRODUCTOS
    #==================    
    elif opcion == "2":
        
        cursor.execute("SELECT id, nombre, categoria, precio FROM productos")
        
        productos = cursor.fetchall()
               
        if len(productos) == 0:
            print("no se han encontrado productos")
            
        else:
            
            print("\n===== LISTA DE PRODUCTOS =====")
            
            for numero, producto in enumerate(productos, start=1):

                print(f"{numero}. Nombre: {producto[1]}")
                print(f"   ID real: {producto[0]}")
                print(f"   Categoría: {producto[2]}")
                print(f"   Precio: ${producto[3]}")
                print("--------------------------")            
    
    
    #==================
    # BUSCAR PRODUCTOS
    #==================
    elif opcion == "3":
        
        while True:
            cursor.execute("SELECT COUNT(*) FROM productos")
            cantidad_productos = cursor.fetchone()[0]

            if cantidad_productos == 0:
                print("No hay productos agregados")
                break
        
            buscar = input(
                "Ingresá el nombre del producto o escriba Exit para salir al menú: ").strip().title()
        
            if buscar == "Exit":
                print ("Saliendo del buscador...")
                break
            
            
            if buscar == "":
                print ("Debe ingresar un producto")
                continue
        
            cursor.execute(
                """
                SELECT id, nombre, categoria, precio
                FROM productos
                WHERE nombre like ?
                """,
                (f"%{buscar}%",)
            
            )
        
            productos_encontrados = cursor.fetchall()
        
            if len (productos_encontrados) == 0:
                print("no se encontró ningún producto")
                continue
        
            
            for producto in productos_encontrados:
                
                print("\n--- Producto encontrado ---")

                print(f"ID: {producto[0]}")
                    
                print(f"Nombre: {producto[1]}")
                    
                print(f"Categoría: {producto[2]}")
                    
                print(f"Precio: ${producto[3]}")    
            
            continuar = input("\nPresiona enter para seguir buscando productos o escriba Exit para salir: ").strip().title()
            
            if continuar == "Exit":
                print("Saliendo al menú...")
                break    
                
    
    #====================
    # ELIMINAR PRODUCTOS
    #====================        
            
    elif opcion == "4":
        while True:
            cursor.execute("SELECT id, nombre FROM productos")
            
            productos = cursor.fetchall()
            
            if len(productos) == 0:
                print("No hay productos para eliminar")
                continue
            
            print("\n==== PRODUCTOS ====")
            
            for producto in productos:
                print(f"ID: {producto[0]} - Nombre: {producto[1]}")
                
            eliminar = input("Ingrese el ID del producto que desea eliminar: ").strip()
            
            if not eliminar.isdigit():
                print("Debe ingresar un ID válido")
                continue
            eliminar=int(eliminar)
            
            cursor.execute(
                "DELETE FROM productos WHERE id = ?",
                (eliminar,)
            )
            
            conexion.commit()
            
            if cursor.rowcount > 0:
                print("Producto eliminado correctamente")
                
            else:
                print("No se encontró un producto con ese ID")
            break
    #===================
    # SALIR DEL PROGRAMA   
    #===================
    elif opcion == "5":
        conexion.close()
        print("Programa finalizado")
        break
    
    
              