def valido():
	contador=0
	max=3
	c="123"
	u="123"
	while contador < 3:
		user=input("ingrese usuario ")
		contra=input("ingrese contraseña: ")
		if contra==c and user == u:
			print("Bienvenido")
			contador= 5
			menuprincipal()
			choice1()
		else: 
			print("Datos incorrectos")
			contador=contador+1
			max=max-1
			print("Le quedan ", max, "intentos. Si supera los 3 intentos se cerrara el programa")
			if contador ==3:
				print ("Intentos superados")

def menuprincipal():
	print("[1] Gestion local") 
	print("[2] Crear cuentas de dueños de locales")
	print("[3] Aprobar/Denegar solicitud de descuento")
	print("[4] Gestión de Novedades")
	print("[5] Reporte de utilización de descuentos")
	print("[0] SALIR")
	print("elija opcion de algun numero del 0 a 5")

def GL():
    print("[A]Crear Local")
    print("B")
    print("C")
    print("D")

def opcionescrear():
	print("Quiere crear un local?")
	print("[1] SI")
	print("[2] NO")



def crearlocal():
	local=0
	perfum=0
	comida=0
	indum=0
	choice= input ("opcion " )
	if choice=="1":
		opcionescrear()
		opcion3= input ("ingrese el numero de acuerdo a su opcion")
		if opcion3=="2":
			menuprincipal()
			choice1()
		while opcion3=="1":
			local=local+1
			nombre= input("ingrese el nombre del local: ")
			ubi= input("ingrese la ubicacion del local: ")
			print("Elija uno de estos rubros")
			print("a Perfumeria")
			print("b indumentaria")
			print("c Comida")
			rubro= input("ingrese la letra: ")
			if rubro=="a":
				perfum=perfum+1
			elif rubro=="b":
				indum=indum+1
			else:
				rubro=="c"
				comida= comida+1
			opcionescrear()
			opcion3= input ("ingrese el numero de acuerdo a su opcion") 
	else:
		print ("en construccion")






def choice1():
    opcion= input(" opcion es ")
    if opcion == "4":
        menuprincipal()
        crearlocal()
    else:
        while opcion != "4" and opcion != "0":
            if opcion == "1":
                GL()
                crearlocal()
            elif opcion == "2":
                print("construccion")
            elif opcion == "3":
                print("construccion")
            else:
                opcion == "0"
                contador =5



valido()


