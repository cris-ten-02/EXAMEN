productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
                       }
#productos ={modelo:[marca,pantalla,Ram.disco,Gb de DD, PROCESADOR,VIDEO},...}]}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 }

def stock_marca():
    marca = input('Ingrese marca de producto: ').capitalize()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower() and modelo in stock:
            print(f'Modelo: {modelo}, Stock: {stock[modelo][1]}, Precio: ${stock[modelo][0]}')
            encontrados = True
    if not encontrados:
        print(f'No se encontraron productos para la marca "{marca}".')
          
def busqueda_ram_precio():
    try:
        ram_min = int(input('Ingrese RAM mínima (GB): '))
        ram_max = int(input('Ingrese RAM máxima (GB): '))
        precio_max = int(input('Ingrese precio máximo: '))
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")
        return

    for modelo, datos in productos.items():
        if modelo in stock:
            ram_str = datos[2].replace('GB', '')
            try:
                ram = int(ram_str)
            except:
                continue
            precio = stock[modelo][0]
            if ram_min <= ram <= ram_max and precio <= precio_max:
                print(f'{modelo} - RAM: {ram}GB - Precio: ${precio}')
                

def eliminar_producto(modelo):
  while True:
    if modelo != None:
        del productos[modelo]
        del stock[marcas]
        print('producto eliminado exitosamente')
        otro=('desea eliminar otro producto?')
        if otro=='si':
             eliminar_producto(modelo)
        else:
             menu()
    else:
        print('prducot no encontrado')

def menu():
 while True:
    print('MENÚ PRINCIPAL BIENVENIDO')
    print('=================================')
    print('1- Stock Marca ')
    print('2- busqueda por Ram y precio.')
    print('3- eliminar producto ')
    print('3- salir')
            
    opc = input("Seleccione una opción (1-5): ")
        
    if opc == "1":
          stock_marca(marcas)
    elif opc == "2":
            print('holi')
    elif opc == "3":
            eliminar_producto(modelo)
    elif opc == "4":
            print("Gracias por usar Pibooks.")
            break
    else:
            print("Opción no válida. Intente nuevamente.")

#
menu()