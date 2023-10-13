#import os
import hostBiblioteca as hb
import mysql.connector


class Colaborador:
    def __init__(self):
        conexion = hb.traerHost()
        self.servidor = conexion[0]
        self.usuario = conexion[1]
        self.clave = conexion[2].strip()
        self.db = conexion[3]

    def listado(self):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `codigo`, `nombre` FROM `colaboracion` WHERE 1 ORDER BY codigo DESC;"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        return datos
