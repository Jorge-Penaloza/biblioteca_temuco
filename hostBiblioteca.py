import csv
def traerHost():
    file = open('conexion.dat', "r")  
    reader = csv.reader(file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    sw = False
    for row in reader:
        if reader.line_num == 1:
            return tuple(row)
        elif reader.line_num > 1:
            return False
