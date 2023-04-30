contador=0
maxim=3

def valido():
	global contador,maxim
	c="123"
	u="123"
	while contador < 3:
		user=input("Ingrese su usuario: ")
		contra=input("Ingrese su contraseña: ")
		if contra==c and user == u:
			print("Bienvenido")
			contador= 5
			inicio()
		else: 
			print("Datos incorrectos")
			contador=contador+1
			maxim=maxim-1
			print("Le quedan ", maxim, "intentos. Si supera los 3 intentos se cerrara el programa")


def inicio():
	menuprincipal()
	menuop1()
	

def menuprincipal():
	print("[1] Gestion local") 
	print("[2] Crear cuentas de dueños de locales")
	print("[3] Aprobar/Denegar solicitud de descuento")
	print("[4] Gestión de Novedades")
	print("[5] Reporte de utilización de descuentos")
	print("[0] SALIR")
	print("Elija un numero de acuerdo a la seccion a la que quiera ingresar.")

def menuop1():
	opcion1= input("Su opcion es ")
	while opcion1<"0" or opcion1>"5":
		print("Ingreso de numero incorrecto. Vuelva a intentar")
		menuprincipal()
		opcion1= input("Su opcion es ")
	if opcion1=="1":
		gestionlocal()
	elif opcion1=="4":
		gestionnovedades()
	elif opcion1=="0":
		contador=5
	else:
		print("En construccion")


def GestionlocalNovedades():
	print("[1] Crear Novedad")
	print("[2] Modificar Novedades")
	print("[3] Eliminar Novedad")
	print("[4] Ver Reporte de Novedades")
	print("[5] Vover") 

def gestionnovedades():
	GestionlocalNovedades()
	opcionalt=input("Ingrese el numero de la seccion a la que quiera ingresar:")
	while opcionalt<1 or opcionalt>5:
		print("Opcion invalida. Vuelva a intentarlo.")
		GestionlocalNovedades()
		opcionalt=input("Ingrese el numero de la aseccion a la que quiera ingresar: ")
	if opcionalt=="5":
		inicio()
	else:
		print("En construccion...")

def Gestionlocalopciones():
	print("[1] Crear Local")
	print("[2] Modificar Local")
	print("[3] Eliminar Local")
	print("[4] Volver") 

def gestionlocal():
	Gestionlocalopciones()
	opcion2=input("Ingrese el numero de la seccion a la que quiera ingresar: ")
	while opcion2<"1" or opcion2>"4":
		print("Opcion invalida. Vuelva a intentarlo")
		Gestionlocalopciones()
		opcion2=input("Ingrese una letra de acuerdo a la opcion que quiera seleccionar.")
	if opcion2=="1":
		crearlocal()
	if opcion2=="4":
		inicio()
	else:
		print("En construccion...")


def opcioncrear():
	print("Quiere crear un local?")
	print("[1] Si")
	print("[2] No")

def rubros():
	print("Indique a que tipo de rubro pertenece el local.")
	print("Indumentaria1, Comida2 o Perfumeria3.")


def crearlocal():
	opcioncrear()
	p=0
	i=0
	c=0
	opcion3=input("Elija una opcion:")
	while opcion3<"1" or opcion3>"2":
		print("Opcion invalida. Vuelva a intentarlo.")
		opcion3=input("Elija una opcion:")
	while opcion3=="1":
		rubros()
		opcion4= input("Elija el tipo de rubro y escriba exactamente de la misma forma en la que esta escrito arriba: ")
		while opcion4<"1" or opcion4>"3":
			print("Datos incorrectos. Vuelva a intentarlo.")
			rubros()
			opcion4= input("Elija el tipo de rubro y escriba exactamente de la misma forma en la que esta escrito arriba: ")
		if opcion4=="Comida":
			c=c+1
		elif opcion4=="Perfumeria":
			p=p+1
		else:
			opcion4=="Indumentaria"
			i=i+1
		opcioncrear()
		opcion3=input("Elija una opcion:")
	if opcion3=="2":
		inicio()

valido()


