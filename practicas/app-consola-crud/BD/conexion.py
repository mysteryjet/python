import mysql.connector
from mysql.connector import Error

class DAO: # Data Access Object
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Comadreja234!',
                db='ejercicio1'
            )
        except Error as ex:
            print("Error al intentar conectarse: {}".format(ex))

    # LISTAR CURSO
    def listar_cursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar conectarse: {}".format(ex))

    # REGISTRAR CURSO
    def registrar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{}', '{}', {})"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("Curso registrado.\n")
            except Error as ex:
                print("Error al intentar conectarse: {}".format(ex))

    # ACTUALIZAR CURSO
    def actualizar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{}', creditos = {} WHERE codigo = '{}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("Curso actualizado.\n")
            except Error as ex:
                print("Error al intentar conectarse: {}".format(ex))

    # ELIMINAR CURSO
    def eliminar_curso(self, codigo_curso_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{}'"
                cursor.execute(sql.format(codigo_curso_eliminar))
                self.conexion.commit()
                print("Curso eliminado.\n")
            except Error as ex:
                print("Error al intentar conectarse: {}".format(ex))

