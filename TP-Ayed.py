contador=0
per=0
ind=0
com=0
#ListaUser = ["admin","locala","localb","cliente"]*4
#ListaContra = ["123","a","b","33"] "estas 2 pueden ser 1 array bidimensianal. Los otros 2 supongo que es uni"

def principal():
	maxim=3
	global contador
	c=str("admin")
	u=str("admin")
	while contador < 3:
		import getpass
		user=input("Ingrese su usuario: ")
		password = getpass.getpass("Ingrese su contraseña: ")  
		if password==c and user == u:
			contador = 5
			menuop1()
		else: 
			print("Datos incorrectos")
			contador=contador+1
			maxim=maxim-1
			print("Le quedan ", maxim, "intentos. Si supera los 3 intentos se cerrara el programa")
		if contador==3:
			print("Ha superado el límite de intentos. Se cierra el programa.")

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
	global opcion1
	print("Bienvenido!")
	menuprincipal()
	opcion1= str(input("Su opción es: "))
	while opcion1<"0" or opcion1>"5":
		print("Ingreso de número incorrecto. Vuelva a intentarlo.")
		opcion1= str(input("Su opción es: "))
	while opcion1 != "0":
		if opcion1=="1":
			locales()
		elif opcion1=="4":
			novedades()
		else:
			construccion()
		opcion1= str(input("Su opción es: "))
		while opcion1<"0" or opcion1>"5":
			print("Ingreso de número incorrecto. Vuelva a intentarlo.")
			opcion1= str(input("Su opción es: "))		

def GestionNovedades():
	print("[1] Crear Novedades")
	print("[2] Modificar Novedad")
	print("[3] Eliminar Novedad")
	print("[4] Ver Reporte de Novedades")
	print("[5] Volver") 

def novedades():
	GestionNovedades()
	opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar:"))
	while opcionalt<"1" or opcionalt>"5":
		print("Opción invalida. Vuelva a intentarlo.")
		opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar: "))
	while opcionalt != "5":
		construccion()
		opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar:"))
		while opcionalt<"1" or opcionalt>"5":
			print("Opción invalida. Vuelva a intentarlo.")
			opcionalt=str(input("Ingrese el número de la sección a la que quiera ingresar: "))
	menuprincipal()

def Gestionlocalopciones():
	print("[1] Crear Local")
	print("[2] Modificar Local")
	print("[3] Eliminar Local")
	print("[4] Volver") 

def locales():
	Gestionlocalopciones()
	opcion2=input("Ingrese el número de la seccion a la que quiere entrar:")
	while opcion1<"0" or opcion1>"4":
		print("Ingreso de número incorrecto. Vuelva a intentarlo.")
		opcion2=input("Ingrese el número de la seccion a la que quiere entrar:")
	while opcion2 !="4":
		if opcion2=="1":
			crearlocal()
		else:
			construccion()
		Gestionlocalopciones()
		opcion2=input("Ingrese el número de la seccion a la que quiere entrar:")
		while opcion1<"0" or opcion1>"4":
			print("Ingreso de número incorrecto. Vuelva a intentarlo.")
			opcion2=input("Ingrese el número de la seccion a la que quiere entrar:")
	menuprincipal()

def rubros():
	print("Indique a que tipo de rubro pertenece el local.")
	print("[a] Indumentaria")
	print("[b] Perfumería")
	print("[c] Comida")

def crearlocal():
	print("IMPORTANTE: Si pone un * en el nombre del local, terminara la carga de locales.")
	localA()
	localB()
	
def localA():
	global com, per, ind
	nombrelocal=input("Ingrese el Nombre del local: ")
	while nombrelocal!="*":
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
			ind=ind+1
		nombrelocal=input("Ingrese el Nombre del local: ")

def localB():
	global com, per, ind
	if (com>per) and (com>ind):
		print("El rubro que más locales tiene es el de Comida con ",com,"locales.")
		if (per>ind):
			print("El rubro que menos locales tiene es el de Indumentaria con", ind, "locales.")
		else:
			print("El rubro que menos locales tiene es el de Perfumería con ", per, "locales.")
	elif (per>com) and (per>ind):
		print("El rubro que más locales tiene es el de Perfumería con ",per,"locales.")
		if (com>ind):
			print("El rubro que menos locales tiene es el de Indumentaria con ", ind, "locales.")
		else:
			print("El rubro que menos locales tiene es el de Comida con ", com, "locales.")
	else:
		print("El rubro que más locales tiene es el de Indumentaria con ",ind,"locales.")
		if (per>com):
			print("El rubro que menos locales tiene es el de Comida con ", com, "locales.")
		else:
			print("El rubro que menos locales tiene es el de Perfumería con ", per, "locales.")


principal()
