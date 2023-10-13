#import os
import hostBiblioteca as hb
import mysql.connector


class Libros:
    def __init__(self):
        conexion = hb.traerHost()
        self.servidor = conexion[0]
        self.usuario = conexion[1]
        self.clave = conexion[2].strip()
        self.db = conexion[3]

    def buscar(self, codigo):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad` FROM `libros`"
        query += " WHERE codigo = '"+codigo+"';"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        filas = mycursor.rowcount
        
        if( filas == 1):
            return (True, datos)
        else:
            return (False, datos)

    def eliminar(self, codigo):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "DELETE FROM `libros` WHERE `codigo` = \'"+codigo+"\'"
        mycursor.execute(query)
        mydb.commit()

    def insertar(self, codigo, nombre, autor, descripcion, anio,cantidad):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "INSERT INTO `libros` (`codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad`) "
        query += " VALUES ('"+codigo+"',"
        query += " '"+nombre+"', "
        query += "'"+autor+"', "
        query += "'"+descripcion+"', "
        query += "'"+anio+"', "
        query += "'"+cantidad+"')"
        
        #INSERT INTO `libros` (`codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad`) VALUES ('2', '2', '2', '2', '2', '2');
        mycursor.execute(query)
        mydb.commit()
        
    def actualizar(self, codigo, nombre, autor, descripcion, anio,cantidad):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "UPDATE `libros` SET `nombre` = '"+nombre
        query += "', `autor` = '"+autor
        query += "', `descripcion` = '"+descripcion
        query += "', `anio` = '"+anio
        query += "', `cantidad` = '"+cantidad
        query += "' WHERE `codigo` = '"+codigo+"';"
        #UPDATE `libros` SET `nombre` = 'J', `autor` = 'Richard Bach1', `descripcion` = 'Juan', `anio` = '1971', `cantidad` = '10' WHERE `libros`.`codigo` = 'A10';
        #print(query)
        mycursor.execute(query)
        mydb.commit()
    
    def cambiarCantidad(self,codigo, cantidad):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "UPDATE `libros` SET `cantidad` = '"+str(cantidad)
        query += "' WHERE `codigo` = '"+codigo+"';"
        #UPDATE `libros` SET `nombre` = 'J', `autor` = 'Richard Bach1', `descripcion` = 'Juan', `anio` = '1971', `cantidad` = '10' WHERE `libros`.`codigo` = 'A10';
        #print(query)
        mycursor.execute(query)
        mydb.commit()
        
    def listado(self):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad` FROM `libros` WHERE 1;"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        return datos
