from django.db import models
from django.utils import timezone

# Create your models here.

from datetime import datetime #Importamos el módulo para obtener fecha y hora actual

class Categoria(models.Model):
    nombre = models.CharField(max_length = 30, null = False)

class Articulo(models.Model):  #creamos la clase Articulo con sus atributos
    #id_usuario = id_usuario
    titulo = models.CharField(max_length = 30, null = False) #Cambiado titulo.CharField por models.CharFields
    resumen = models.TextField(null = False)
    contenido = models.TextField(null = False)
    fecha_publicacion = models.DateTimeField(auto_now_add = True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media/articulo', default='media/articulo/default_articulo.png')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta: #indentacion cambiada
        ordering = ('-publicado',)
    
    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
    
# class Comentario(): #creamos la clase Comentario con sus atributos
#     def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
#         self.id = id
#         self.id_articulo = id_articulo
#         self.id_usuario = id_usuario
#         self.contenido = contenido
#         self.fecha_hora = fecha_hora
#         self.estado = estado

# class Usuario(): #creamos la clase Usuario con sus atributos y atributos
#     def __init__ (self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online):
#         self.id = id 
#         self.nombre = nombre 
#         self.apellido = apellido 
#         self.telefono = telefono 
#         self.username = username 
#         self.email = email 
#         self.contrasenia = contrasenia 
#         self.fecha_de_registro = fecha_de_registro
#         self.estado = estado
#         self.avatar = avatar 
#         self.online = online 

#     def login(self): #creamos el método para loguear usuario
#         self.online = True #activa el atributo online
#         print('\nEL USUARIO HA INGRESADO CORRECTAMENTE\n')

#     def registrar(self, lista_de_usuarios):  #creamos el método para registrar usuario
#         self.lista_de_usuarios = lista_de_usuarios 
#         self.lista_de_usuarios.append(self) #guarda el usuario registrado en una lista de usuarios
#         print('\nEL USUARIO HA SIDO REGISTRADO CORRECTAMENTE\nDebe loguearse para poder publicar o comentar\n')
    
#     def comentar(self, comentario: Comentario, lista_de_comentarios): #creamos el método para realizar un comentario
#         self.comentario = comentario
#         self.lista_de_comentarios = lista_de_comentarios
#         self.lista_de_comentarios.append(comentario) #guarda el comentario realizado en una lista de comentarios

# class Publico(Usuario):  #creamos la subclase Publico(Usuario) con sus métodos y atributos (tanto propios como heredados)
#     def __init__ (self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_publico):
#         super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
#         self.es_publico = es_publico

# class Colaborador(Usuario):   #Subclase Colaborador(Usuario) con sus métodos y atributos (tanto propios como heredados)
#     def __init__ (self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_colaborador):
#         super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
#         self.es_colaborador = es_colaborador
       
#     def publicar (self, articulo: Articulo, lista_de_articulos): #creamos el método para publicar un artículo
#         self.articulo = articulo
#         self.lista_de_articulos = lista_de_articulos
#         self.lista_de_articulos.append(articulo) #guarda el artículo publicado en una lista de artículos

# #AQUÍ COMIENZA LA EJECUCIÓN DEL PROGRAMA
# usuarios = [] #creamos una lista donde vamos a almacenar los Usuarios
# articulos = [] #creamos una lista donde vamos a almacenar los Artículos
# comentarios = [] #creamos una lista donde vamos a almacenar los Comentarios
# existe_usuario = True #bandera para ingresar al submenú
# existe_contrasenia = False #bandera para ingresar al submenú
# opcion = 1 #inicializamos la variable opción

# #Usuarios de prueba
# maxi = Colaborador(1, 'Maxi', 'Roman', '3624111111', 'maxiroman', 'maxiroman@gmail.com', '1234', '2023-06-06 18:00:00', '1', True, True, True)
# cesar = Colaborador(2, 'Cesar', 'Carrillo', '3624222222', 'cesarcarrillo', '@gmail.com', '1234', '2023-06-06 18:00:00', '1', True, True, True)
# marcelino = Publico(3, 'Marcelino', 'Monzon', '36246333333', 'marcelinom', '@gmail.com', '1234', '2023-06-06 18:00:00', '1', True, True, True)
# pablo = Publico(4, 'Pablo', 'Alegre', '3624444444', 'pabloalegre', '@gmail.com', '1234', '2023-06-06 18:00:00', '1', True, True, True)
# usuarios = [maxi, cesar, marcelino, pablo]

# #Articulos de prueba
# art1 = Articulo(1, 2, 'titulo del articulo 1', 'Resumen del art1', 'Contenido del art1', '2023-06-06 18:00:00', '1', 'publicado')
# art2 = Articulo(2, 1, 'titulo del articulo 2', 'Resumen del art2', 'Contenido del art2', '2023-06-06 18:00:00', '12', 'publicado')
# art3 = Articulo(3, 2, 'titulo del articulo 3', 'Resumen del art3', 'Contenido del art3', '2023-06-06 18:00:00', '21', 'publicado')
# articulos = [art1, art2, art3]

# #Comentarios de prueba
# comentario1 = Comentario(1, 3, 1, 'contenido del comentario 1', '2023-06-06 18:00:00', 'publicado')
# comentario2 = Comentario(2, 2, 1, 'contenido del comentario 2', '2023-06-06 18:00:00', 'publicado')
# comentarios = [comentario1, comentario2]

# #Función para validar usuarios
# def validar_usuario():
#     existe_usuario = True
#     while existe_usuario: 
#             username = input('Ingrese el nombre de usuario: ')
#             existe_usuario = False
#             for i in usuarios:
#                 while i.username == username: #mientras el nombre de usuario coincida con uno existente, solicita ingresar otro
#                     print('\tADVERTENCIA: Ya existe ese nombre de usuario. Debe elegir otro.')
#                     existe_usuario = True
#                     break
#     return username

# #Función para mostrar los artículos publicados
# def mostrar_articulos(lista_de_articulos): 
#     print('ARTÍCULOS PUBLICADOS:')
#     for i in lista_de_articulos:
#         print(f'{i.id}. Título: {i.titulo}\n Resumen: {i.resumen}\n Contenido: {i.contenido}\n Fecha de publicación: {i.fecha_publicacion}')

# #Función para mostrar los comentarios publicados
# def mostrar_comentarios(lista_de_comentarios, lista_de_usuarios, lista_de_articulos):
#     for comentario in lista_de_comentarios:
#         print(f"Comentario N° {comentario.id}: {comentario.contenido}")
#         print(f"\tFecha y hora de publicación: {comentario.fecha_hora}")
#         for articulo in lista_de_articulos: #accedo al título del artículo comentado
#             if articulo.id == comentario.id_articulo:
#                 print(f'\tArtículo comentado: "{articulo.titulo}"')
#         for usuario in lista_de_usuarios: #accedo al nombre y apellido del autor del artículo comentado
#             if usuario.id == comentario.id_usuario:
#                 print(f"\tAutor del artículo: {usuario.nombre} {usuario.apellido}")
   
# #Código para elegir entre registrar usuarios o hacer login (si ya está registrado)
# while opcion != '3':
#     print('--------------------------------------------')
#     print('BIENVENID@ AL SISTEMA DE GESTIÓN DE USUARIOS') #Mensaje de bienvenida
#     print('--------------------------------------------')
#     print('MENÚ PRINCIPAL:')
#     print('1. Registro')
#     print('2. Login')
#     print('3. Salir')
#     opcion = input('\nElija una opción del menú: ')

#     if opcion == '1': # Registro de usuarios
#         username = validar_usuario() #invoca al a función para chequear que no no exista el nombre de usuario ingresado
#         contrasenia = input('Ingrese la contraseña: ') #pide ingreso de los demás atributos
#         nombre = input('Ingrese el nombre: ')
#         apellido = input('Ingrese el apellido: ')
#         telefono = input('Ingrese el teléfono: ')
#         email = input('Ingrese el email: ')
#         avatar = input('Ingrese el avatar: ')
#         id = len(usuarios) + 1
#         fecha_de_registro = datetime.now()
#         estado = True
#         online = False
#         tipo_de_usuario = input('Ingrese un tipo de usuario:\n1. Público\n2. Colaborador\nElija una opción: ')
#         if tipo_de_usuario == '1': #registra al usuario como público
#             es_publico = True
#             usuario = Publico(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_publico)
#             usuario.registrar(usuarios)
#             existe_usuario = True
#         elif tipo_de_usuario == '2': #registra al usuario como colaborador
#             es_colaborador = True
#             usuario = Colaborador(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_colaborador)
#             usuario.registrar(usuarios)
#             existe_usuario = True
#         else:
#             print('ADVERTENCIA: No ha ingresado una opción válida. No pudo realizarse el registro\n') #previsión de error

#     elif opcion == '2': # Login de usuarios
#         username = input('Ingrese el nombre de usuario: ')
#         for usuario in usuarios: #Código para verificar que el ingreso de usuario y contraseña sea correcto
#             if usuario.username == username:
#                 existe_usuario = True
#                 contrasenia = input('Ingrese la contraseña: ')
#                 if usuario.contrasenia == contrasenia:
#                     existe_contrasenia = True
#                     usuario.login()
#                     opcion = '3'
#                     break
#                 else:
#                     existe_contrasenia = False
#                     print('\nCONTRASEÑA INCORRECTA\n')
#                     break
#             else:
#                 existe_usuario = False
#         if not existe_usuario:
#             print('\nNOMBRE DE USUARIO INCORRECTO. Debe registrarse correctamente para poder ingresar\n')
#     elif opcion < '1' or opcion > '3':
#         print('\nLA OPCIÓN INGRESADA ES INCORRECTA. Elija una opción válida\n') #previsión de error en el ingreso al menú

# #Una vez registrado y logueado, código que permita comentar al Publico y además publicar al Colaborador
# if existe_usuario and existe_contrasenia:
#     tarea = 1
#     while tarea != '3':
#         print('-----------------')
#         print('MENÚ DE USUARIOS:') #Sub Menú para publicar o comentar
#         print('-----------------')
#         print('1. Publicar un artículo')
#         print('2. Comentar un artículo')
#         print('3. Salir')
#         tarea = input('\nElija una opción del menú: ')
#         if tarea == '1': #Código para publicar un artículo
#             if isinstance(usuario, (Colaborador)): #chequea que el usuario sea colaborador para permitir publicar
#                 id = len(articulos) + 1 #asigna el ID 
#                 id_usuario = usuario.id
#                 titulo = input('Ingrese un título: ')
#                 resumen = input('Ingrese un resumen: ')
#                 contenido = input('Ingrese un contenido: ')
#                 fecha_publicacion = datetime.now() #registra la fecha y hora actual
#                 imagen = input('Ingrese código de la imagen: ')
#                 estado = 'publicado'
#                 mi_articulo = Articulo(id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado) #crea el objeto Articulo
#                 usuario.publicar(mi_articulo, articulos) #guarda el artículo en la lista de artículos
#                 print('\nSE HA PUBLICADO CORRECTAMENTE SU ARTÍCULO:')
#                 print(f'{mi_articulo.id}. Título: {mi_articulo.titulo}\n Resumen: {mi_articulo.resumen}\n Contenido: {mi_articulo.contenido}\n Fecha de publicación: {mi_articulo.fecha_publicacion}')
#             else:
#                 print('\nUsted no puede publicar porque no se ha registrado como colaborador\n') #da error si un usuario público intenta publicar
#         elif tarea == '2': #Código para comentar un artículo
#             if isinstance(usuario, (Colaborador, Publico)): #chequea que el usuario sea colaborador o público para permitir comentar
#                 if articulos != []: #chequea que la lista de artículos no esté vacía
#                     mostrar_articulos(articulos) #Invoca a la función que muestra los artículos disponibles para comentar
#                     existe_articulo = False
#                     while not existe_articulo: #Verifica la existencia del artículo a comentar
#                         id_articulo = int(input('Ingrese ID del artículo a comentar: '))
#                         for articulo in articulos:
#                             if articulo.id == id_articulo:
#                                 existe_articulo = True
#                                 break
#                         if not existe_articulo:
#                              print('No existe un artículo con ese ID.')    
#                     contenido = input('Ingrese su comentario: ')
#                     id = len(comentarios) + 1 #asigna el ID
#                     id_usuario = usuario.id
#                     fecha_hora = datetime.now() #registra la fecha y hora actual
#                     estado = 'publicado'
#                     mi_comentario = Comentario(id, id_articulo, id_usuario, contenido, fecha_hora, estado) #crea el objeto Comentario
#                     usuario.comentar(mi_comentario, comentarios) #guarda el comentario en la lista de comentarios
#                     print('\nSE HA REALIZADO CORRECTAMENTE SU COMENTARIO.')
#                     print("-------------------------")
#                     print("Los comentarios realizados hasta el momento son los siguientes:")
#                     mostrar_comentarios(comentarios, usuarios, articulos) #invoca a la función para mostrar los comentarios existentes
#                 else:
#                     print('ADVERTENCIA: No puedes comentar porque aún no hay artículos!') #previsión de lista de artículos vacía
#         elif tarea < '1' or tarea > '3':
#             print('\nLA OPCIÓN INGRESADA ES INCORRECTA. Elija una opción válida\n') #previsión de error en el ingreso al submenú
# print('\n------------------------------------------------------------------------------')
# print('Gracias por usar el sistema de gestión de usuarios del Grupo 25. Hasta pronto!') #Mensaje de despedida
# print('------------------------------------------------------------------------------')