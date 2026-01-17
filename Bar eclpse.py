RESET = "\033[0m"

ROSA = "\033[95m"           
MORADO= "\033[35m"   
CELESTE = "\033[96m"      
VERDE = "\033[92m"   



print(ROSA + "===================================" + RESET)
print(MORADO + "           ECLIPSE BAR" + RESET)
print(MORADO + "   Un ambiente que opaca los demas" + RESET)
print(MORADO + "            ABIERTO 24H     "+ RESET)
print(ROSA  + "==================================="+ RESET)
print(" ****** COMBO LUNA NEGRA ****** ")
print(" Entrada Incluye:")
print(" - Entrada a zona VIP")
print(" - Barra libre por 1H")
print(" - Plato de comida exclusiva")
print("*** Precio promoción: $6.50 ***")
print("===================================")
nombre = input("Para acceder, ingrese su nombre: ")
print( VERDE + "Bienvenido,", nombre + RESET)

edad = int(input("Ingrese su edad: "))

subtotalCombo = 6.50
bebidasTotal = 0
total = 0
contBebidas = 0
comida = ""
if edad > 17 and subtotalCombo == 6.50:
    print(MORADO + " ====================================")
    print(MORADO + "   BIENVENIDO AL MEJOR BAR DE LA ZONA")
    print(MORADO + " Aqui no existe limite de bebidas, solo DISFRUTA!! ")
    print(MORADO + " ====================================" + RESET)

    print("1. Mini burguer eclipse")
    print("2. Brochetas Cósmicas")
    dig = input("Elija su comida digitando el numeral:")

    while dig != "1" and dig != "2":
        dig = input ("Elija una opción 1 o 2 ")

 
    if dig == "1":
        comida = "Mini burguer eclipse"
    elif dig == "2":
        comida = "Brochetas Cósmicas"

    print( VERDE + "Su orden estará lista.")
    print("Para completar su pedido puede elegir entre:")
    print("1. Piña colada.......................$3.00")
    print("2. Mojito............................$2.50")
    print("3. 5 Shots de tequila................$5.00")

    cantidad_bebidas = int(input("¿Cuántas bebidas desea elegir?: "))

    for i in range(cantidad_bebidas):
        num = input("Digite el numeral de la bebida (1/2/3): ")

        if num == "1":
            bebidasTotal += 3.00
            
            contBebidas += 1
        elif num == "2":
            bebidasTotal += 2.50
        
            contBebidas += 1
        elif num == "3":
            bebidasTotal += 5.00
         
            contBebidas += 1
        else:
            print("Opción inválida. No se agregó bebida.")
else:
    print(MORADO + " Eres menor de edad")
    print(" Pero contamos con zonas para ti")
    print(" Todos son importantes para nosotros ")
    print("====================================")
    print("********* BIENVENIDO A ECLIPSE FAMILY ZONE *********")
    print("Entrada incluye:" + RESET)
    print("- Acceso a zonas: Pista de baile, videojuegos, inflables")
    print("- Pizza, hamburguesa o salchipapa a elección")
    print("- Fotos con personajes temáticos")
    print("********* Precio promoción: $6.50 *********")


total = subtotalCombo + bebidasTotal


print("===================================")
print(MORADO + "              FACTURA")
print("Cliente:", nombre)

if edad > 17:
    print("Combo: Luna Negra...................$6.50")
    print("Plato:", comida)
else:
    print("Combo: Eclipse Family Zone..........$6.50")
    print("Incluye:", comida)

print("-----------------------------------")
print("Bebidas:")


print("-----------------------------------")
print("Subtotal combo......................$" , subtotalCombo)
print("Subtotal bebidas....................$ " ,bebidasTotal)
print("TOTAL A PAGAR.......................$", total)
print(VERDE + "===================================")
print(VERDE + "¡Gracias por su compra!")
