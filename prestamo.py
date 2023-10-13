#import os
import hostBiblioteca as hb
import mysql.connector


class Prestamo:
    def __init__(self):
        conexion = hb.traerHost()
        self.servidor = conexion[0]
        self.usuario = conexion[1]
        self.clave = conexion[2].strip()
        self.db = conexion[3]

    def ultimoPrestamo(self):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT MAX(prestamo)+1 AS registro   FROM `prestamo`;"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        filas = mycursor.rowcount
        if( filas == 1):
            return (True, datos)
        else:
            return (False, datos)

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

    def insertar(self, prestamo, fecha, horario, usuario, codigolibro,codigocolaboracion,estado):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        #INSERT INTO `prestamo` (`id`, `prestamo`, `fecha`, `horario`, `usuario`, `codigolibro`, `codigocolaboracion`, `estado`) VALUES (NULL, '1', '2021-10-13', '20:30:53', 'jorge', 'A10', '1', 'En préstamo');
        query = "INSERT INTO `prestamo` (`id`, `prestamo`, `fecha`, `horario`, `usuario`, `codigolibro`, `codigocolaboracion`, `estado`) "
        query += " VALUES ( NULL, "
        query += "'"+str(prestamo)+"',"
        query += " '"+fecha+"', "
        query += "'"+horario+"', "
        query += "'"+usuario+"', "
        query += "'"+codigolibro+"', "
        query += "'"+codigocolaboracion+"', "
        query += "'"+estado+"')"
        
        #INSERT INTO `libros` (`codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad`) VALUES ('2', '2', '2', '2', '2', '2');
        mycursor.execute(query)
        mydb.commit()
        
    def devolver(self, usuario, codigolibro ):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "UPDATE `prestamo` SET `estado` = 'Devuelto' "
        query += "WHERE `usuario` = '"+usuario+"' AND `codigolibro` = '"+codigolibro+"';"
        mycursor.execute(query)
        mydb.commit()
        
        
    def usuariosConPrestamo(self):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `usuario` FROM `prestamo` WHERE estado = 'En préstamo' GROUP BY usuario;"
        mycursor.execute(query)
        #print(query)
        datos = mycursor.fetchall()
        return datos

    def librosConPrestamo(self, usuario):
        mydb = mysql.connector.connect( host=self.servidor, user=self.usuario, password=self.clave,database=self.db )
        mycursor = mydb.cursor()
        mycursor.execute("USE "+self.db+";")
        query = "SELECT `codigolibro` FROM `prestamo` WHERE "
        query += "estado = 'En préstamo' AND usuario ='"+usuario+"' "
        query += "GROUP BY codigolibro;"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        return datos