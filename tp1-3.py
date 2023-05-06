contador=0
per=0
ind=0
com=0

def valido():
	maxim=3
	global contador
	c=str("123")
	u=str("123")
	while contador < 3:
		import getpass
		user=input("Ingrese su usuario: ")
		password = getpass.getpass("Ingrese su contraseña: ")  
		if password==c and user == u:
			print("Bienvenido")
			contador= 5
			inicio()
		else: 
			print("Datos incorrectos")
			contador=contador+1
			maxim=maxim-1
			print("Le quedan ", maxim, "intentos. Si supera los 3 intentos se cerrara el programa")
		if contador==3:
			print("Ha superado el límite de intentos. Se cierra el programa.")

def inicio():
	menuprincipal()
	menuop1()

def construccion():
	print("En construcción...")

def menuprincipal():
	print("[1] Gestión local") 
	print("[2] Crear cuentas de dueños de locales")
	print("[3] Aprobar/Denegar solicitud de descuento")
	print("[4] Gestión de Novedades")
	print("[5] Reporte de utilización de descuentos")
	print("[0] SALIR")
	print("Elija un número de acuerdo a la sección a la que quiera ingresar.")

def menuop1():
	global contador
	opcion1= str(input("Su opción es: "))
	while opcion1<"0" or opcion1>"5":
		print("Ingreso de número incorrecto. Vuelva a intentarlo.")
		menuprincipal()
		opcion1= input("Su opción es: ")
	if opcion1=="1":
		gestionlocal()
	elif opcion1=="4":
		gestionnovedades()
	elif opcion1=="0":
		contador=5
	else:
		construccion()
		volvermenu()

def GestionlocalNovedades():
	print("[1] Crear Novedades")
	print("[2] Modificar Novedad")
	print("[3] Eliminar Novedad")
	print("[4] Ver Reporte de Novedades")
	print("[5] Volver") 

def gestionnovedades():
	GestionlocalNovedades()
	opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar:"))
	while opcionalt<"1" or opcionalt>"5":
		print("Opción invalida. Vuelva a intentarlo.")
		GestionlocalNovedades()
		opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar: "))
	if opcionalt=="5":
		inicio()
	else:
		construccion()
		volvermenu()		

def Gestionlocalopciones():
	print("[1] Crear Local")
	print("[2] Modificar Local")
	print("[3] Eliminar Local")
	print("[4] Volver") 

def gestionlocal():
	Gestionlocalopciones()
	opcion2=str(input("Ingrese el número de la sección a la que quiera ingresar: "))
	while opcion2<"1" or opcion2>"4":
		print("Opción invalida. Vuelva a intentarlo")
		Gestionlocalopciones()
		opcion2=str(input("Ingrese un número de acuerdo a la opción que quiera seleccionar."))
	if opcion2=="1":
		crearlocal()
	elif opcion2=="4":
		inicio()
	elif opcion2=="2":
		construccion()
		volvermenu()
	else:
		construccion()
		volvermenu()

def opcioncrear():
	print("Quiere crear un local?")
	print("[1] Si")
	print("[2] No")

def rubros():
	print("Indique a qué tipo de rubro pertenece el local.")
	print("[a] Indumentaria")
	print("[b] Perfumería")
	print("[c] comida")

def crearlocal():
	opcioncrear()
	global com, per, ind
	opcion3=str(input("Elija una opcion:"))
	while opcion3!="1" and opcion3!="2":
		print("Opción inválida. Vuelva a intentarlo.")
		opcioncrear()
		opcion3=str(input("Elija una opción:"))
	while opcion3=="1":
		nombrelocal=input("Ingrese el Nombre del local: ")
		ubilocal=input("Ingrese la Ubicación de local: ")
		rubros()
		opcion4= str(input("Elija el tipo de rubro e ingrese la letra del rubro a la que pertenece el local: "))
		while opcion4<"a" or opcion4>"c":
			print("Datos incorrectos. Vuelva a intentarlo.")
			rubros()
			opcion4= str(input("Elija el tipo de rubro e ingrese la letra del rubro a la que pertenece el local: "))
		if opcion4=="c":
			com=com+1
		elif opcion4=="b":
			per=per+1
		else:
			opcion4=="a"
			ind=ind+1
		opcioncrear()
		opcion3=str(input("Elija una opción:"))
		while opcion3!="1" and opcion3!="2":
			print("Opcion invalida. Vuelva a intentarlo.")
			opcioncrear()
			opcion3=str(input("Elija una opción:"))
	if opcion3=="2":
		if ((com>per) and (per>ind)):
			print("El rubro que mas locales tiene es el de Comida con ",com,"locales.")
			print("El rubro que menos locales tiene es el de Indumenatria con ", ind, "locales.")
		elif ((com>ind) and (ind>per)):
			print("El rubro que mas locales tiene es el de Comida con ",com,"locales.")
			print("El rubro que menos locales tiene es el de Perfumeria con ", per, "locales.")
		elif ((per>com) and (com>ind)):
			print("El rubro que mas locales tiene es el de Perfumeria con ",per,"locales.")
			print("El rubro que menos locales tiene es el de Indumenatria con ", ind, "locales.")
		elif ((per>ind) and (ind>com)):
			print("El rubro que mas locales tiene es el de Perfumeria con ",per,"locales.")
			print("El rubro que menos locales tiene es el de Comida con ", com, "locales.")
		elif ((ind>com) and (com>per)):
			print("El rubro que mas locales tiene es el de Indumenatria con ",ind,"locales.")
			print("El rubro que menos locales tiene es el de Perfumeria con ", per, "locales.")
		else:
			print("El rubro que mas locales tiene es el de Indumenatria con ",ind,"locales.")
			print("El rubro que menos locales tiene es el de Comida con ", com,"locales.")
		volvermenu()

def volvermenu():
	print("Va a volver al menú principal.")
	inicio()
	
valido()



