def contrauser(): 
	min=0
	max=3
	c="123"
	u="123"
	contra=input("ingrese contraseña: ")
	user=input("ingrese usuario ")
	while contra != c or user == u:
		for i in range (3):
			print("incorrecto")
			print("le quedan ",i, "intentos")

           

def menuprincipal():
	print("[1] Gestion local") 
	print("[2] Crear cuentas de dueños de locales")
	print("[3] Aprobar/Denegar solicitud de descuento")
	print("[4] Gestión de Novedades")
	print("[5] Reporte de utilización de descuentos")
	print("[0] SALIR")
	print("elija opcion de algun numero del 0 a 5")

def GL():
    print("a")
    print("b")
    print("c")
    print("d")



contrauser(min, max)
if min<max: 
	menuprincipal(min, max)
	opcion= input(" elija una opcion: ")
	while opcion != "0":
		if opcion== "1":
			GL()
		elif opcion =="2":
			print("en construccion")
		elif opcion == "3":
			print("en construccion")
		elif opcion == "4":
			menuprincipal()
			print("elija opcion de algun numero del 0 a 5")
		elif opcion == "5":
			print("en construccion")
		else: 
			break


