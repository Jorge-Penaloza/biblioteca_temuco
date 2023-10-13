#import os
import hostBiblioteca as hb
import mysql.connector
import hashlib

class Usuarios:
    def __init__(self):
        conexion = hb.traerHost()
        self.servidor = conexion[0]
        self.usuario = conexion[1]
        self.clave = conexion[2].strip()
        self.db = conexion[3]

    def buscar(self, usuario, clave):
        claveEnBytes = str.encode(clave)
        claveCodificada = hashlib.new("sha1", claveEnBytes)
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT nombre, perfil  FROM `usuarios` "
        query += "WHERE usuario  = '"+usuario+"' AND "
        query += "clave = '" + claveCodificada.hexdigest() +"'"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        filas = mycursor.rowcount
        
        if( filas == 1):
            return (True, datos)
        else:
            return (False, datos)
    def buscarUsuario(self, usuario):
        #claveEnBytes = str.encode(clave)
        #claveCodificada = hashlib.new("sha1", claveEnBytes)
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT nombre, perfil  FROM `usuarios` "
        query += "WHERE usuario  = '"+usuario+"'"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        filas = mycursor.rowcount
        
        if( filas == 1):
            return (True, datos)
        else:
            return (False, datos)

    def insertar(self, usuario, clave, perfil, nombre):
        claveEnBytes = str.encode(clave)
        claveCodificada = hashlib.new("sha1", claveEnBytes)
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "INSERT INTO `usuarios` (`id`,`usuario`, `clave`, `perfil`, `nombre`)"
        query += " VALUES (NULL,'"+usuario+"', '"+claveCodificada.hexdigest()
        query += "', '"+perfil+"','"+nombre+"');"
        #print(query)
        mycursor.execute(query)
        mydb.commit()
        
    def actualizar(self, usuario, clave, perfil, nombre):
        claveEnBytes = str.encode(clave)
        claveCodificada = hashlib.new("sha1", claveEnBytes)
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "UPDATE `usuarios` SET `clave` = '"+claveCodificada.hexdigest()
        query += "', `perfil` = '"+perfil
        query += "', `nombre` = '"+nombre+"' WHERE `usuarios`.`usuario` = '"+usuario+"';"
        #print(query)
        mycursor.execute(query)
        mydb.commit()
        
        
    def listado(self):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `nombre`,`usuario`, IF(`perfil` = 'A','Administrador',IF(`perfil` = 'U','Usuario','ERROR')) AS perfil FROM `usuarios` WHERE 1;"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        return datos
