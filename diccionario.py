def mostrar_menu():
    """
    Función que muestra el menú de opciones del diccionario informático.
    """
    print("Bienvenido al Diccionario Informático de Fernando")
    print("1. Buscar definición")
    print("2. Salir")

def buscar_definicion(diccionario, termino):
    """
    Función que busca la definición de un término en el diccionario.
    
    Parameters:
    - diccionario (dict): Diccionario con los términos y sus definiciones.
    - termino (str): Término a buscar en el diccionario.
    """
    try:
        definicion = diccionario[termino]
        print(f"Definición de {termino}: {definicion}")
    except KeyError:
        print("¡Término no encontrado en el diccionario!")

def menu_interactivo(diccionario):
    """
    Función que maneja el menú interactivo del diccionario informático.
    
    Parameters:
    - diccionario (dict): Diccionario con los términos y sus definiciones.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            termino = input("Ingrese el término que desee buscar: ")
            buscar_definicion(diccionario, termino)
        elif opcion == '2':
            print("¡Hasta luego bye bye!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Diccionario de definiciones informáticas
diccionario_informatico = {
    "Python": "Lenguaje de programación de alto nivel",
    "HTML": "Lenguaje de marcado para el desarrollo web",
    "CPU": "Unidad Central de Procesamiento",
    "RAM": "Memoria de Acceso Aleatorio",
    "GPU": "Unidad de Procesamiento Gráfico",
    "API": "Interfaz de Programación de Aplicaciones",
    "IDE": "Entorno de Desarrollo Integrado",
    "DNS": "Sistema de Nombres de Dominio",
    "URL": "Localizador de Recursos Uniforme",
    "LAN": "Red de Área Local",
    "WAN": "Red de Área Extensa",
    "VPN": "Red Privada Virtual",
    "SSL": "Capa de Conexión Segura",
    "SQL": "Lenguaje de Consulta Estructurada",
    "XML": "Lenguaje de Marcado Extensible",
    "JSON": "Notación de Objetos de JavaScript",
    "FTP": "Protocolo de Transferencia de Archivos",
    "SSH": "Shell Seguro",
    "IoT": "Internet de las Cosas",
    "Big Data": "Conjuntos de Datos Extremadamente Grandes",
    "Blockchain": "Cadena de Bloques",
    "IDE": "Entorno de Desarrollo Integrado",
    "DNS": "Sistema de Nombres de Dominio",
    "URL": "Localizador de Recursos Uniforme",
    "LAN": "Red de Área Local",
    "WAN": "Red de Área Extensa",
    "VPN": "Red Privada Virtual",
    "SSL": "Capa de Conexión Segura",
    "SQL": "Lenguaje de Consulta Estructurada",
    "XML": "Lenguaje de Marcado Extensible",
    "JSON": "Notación de Objetos de JavaScript",
    "FTP": "Protocolo de Transferencia de Archivos",
    "SSH": "Shell Seguro",
    "IoT": "Internet de las Cosas",
    "Big Data": "Conjuntos de Datos Extremadamente Grandes",
    "Blockchain": "Cadena de Bloques",
    "IPv4": "Protocolo de Internet versión 4",
    "IPv6": "Protocolo de Internet versión 6",
    "HTTP": "Protocolo de Transferencia de Hipertexto",
    "HTTPS": "Protocolo Seguro de Transferencia de Hipertexto",
    "TCP": "Protocolo de Control de Transmisión",
    "UDP": "Protocolo de Datagramas de Usuario",
    "NoSQL": "Base de Datos No Relacional",
    "SaaS": "Software como Servicio",
    "PaaS": "Plataforma como Servicio",
    "IaaS": "Infraestructura como Servicio",
    "Cloud Computing": "Computación en la Nube",
    "Machine Learning": "Aprendizaje Automático",
    "Deep Learning": "Aprendizaje Profundo",
    "Algoritmo": "Conjunto de pasos para realizar una tarea",
    "Ciberseguridad": "Seguridad de la Información en el ámbito digital",
    "Hacker": "Persona experta en el manejo de sistemas informáticos",
    "Cracker": "Persona que realiza acciones maliciosas en sistemas informáticos",
    "Firewall": "Sistema de seguridad que controla el tráfico de red",
    "Back-end": "Parte de un sistema que no es visible para el usuario final",
    "Front-end": "Parte de un sistema que interactúa directamente con el usuario",
    "Framework": "Estructura de soporte para desarrollar aplicaciones",
    "Git": "Sistema de control de versiones",
    "Repository": "Repositorio de código",
    "Branch": "Rama de desarrollo en un repositorio",
    "Merge": "Combinar cambios de diferentes ramas en un repositorio",
    "Pull Request": "Solicitud para fusionar cambios en un repositorio",
    "Bug": "Error en un programa o sistema",
    "Debugging": "Proceso de encontrar y corregir errores en un programa",
    "Agile": "Metodología de desarrollo de software basada en iteraciones cortas",
    "Scrum": "Marco de trabajo ágil para gestionar proyectos",
    "DevOps": "Colaboración entre desarrolladores y operaciones de TI",
    "Container": "Entorno de software ligero y autónomo",
    "Virtual Machine": "Máquina virtual que opera como un sistema informático independiente",
    "Microservices": "Arquitectura de software basada en servicios pequeños e independientes",
    "Artificial Intelligence": "Inteligencia artificial, capacidad de las máquinas para realizar tareas que requieren inteligencia humana",
    "API Gateway": "Servicio que actúa como interfaz de entrada para APIs",
    "Load Balancer": "Equilibra la carga de tráfico entre servidores",
    "Redundancy": "Disponibilidad de componentes de respaldo para evitar fallos",
    "Scalability": "Capacidad de un sistema para crecer y adaptarse a la demanda",
    "UML": "Lenguaje de Modelado Unificado",
    "Docker": "Plataforma de contenedores para facilitar la creación y despliegue de aplicaciones",
    "Kubernetes": "Orquestador de contenedores para gestionar aplicaciones en entornos de producción",
    "Cyberattack": "Ataque cibernético que busca dañar sistemas informáticos",
    "Metadata": "Datos que describen otros datos",
    "Encryption": "Proceso de codificación de información para proteger su confidencialidad",
    "Decryption": "Proceso de descifrado de información codificada",
    "Rootkit": "Tipo de software malicioso diseñado para acceder a un sistema de forma encubierta",
    "Scalability": "Capacidad de un sistema para crecer y adaptarse a la demanda"
    # Agrega más definiciones aquí
}

menu_interactivo(diccionario_informatico)