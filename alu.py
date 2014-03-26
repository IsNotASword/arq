# -*- coding: utf-8 -*-

# Autor: Brando Pérez Pacheco.
# Programa: parser de instrucciones.

def decorador_operaciones(op):
    """ Función decoradora de métodos operacionales. """
    def inner(*args):
        print "Se ha ejecutado la operación: " + op.__name__.upper()  + \
              " con estos parámetros: %s." % ', '.join(args[1])
        op(*args)
    return inner

class Alu(object):
    """ 
        Clase que contiene un atributo de almacenamiento y métodos  que simulan
        una ALU.
    """
    __ac = 0
    __count = 0
    __instrucciones = []
    __mem = ()

    def leer_instrucciones(self, ins):
        """ Método que lee instrucciones a partir de un archivo de texto """
        ins = ins.split(" ")
        for i in range(len(ins)):
            ins[i] = ins[i].replace(",", "") # filtrando por comas
            ins[i] = ins[i].replace("\n", "") # obteniendo la operación
            com = ins[0].upper()
        self.__instrucciones.append([com, ins[1:]])

    def get_ac(self): return self.__ac

    def get_ac(self): return self.__count

    def get_instrucciones(self):
        """ Método de impresiónde instrucciones. """
        for ins, args in self.__instrucciones:
            print ins, ', '.join(args)

    def __set_registro(self, reg, ac):
        """ Método que ingresa un nuevo registro o actualiza uno existente. """
        self.__mem[reg] = ac

    def __get_registro(self, reg):
        """ Método que obtiene algún registro ya existente. """
        try:
            registros = [i[0] for i in self.__mem.iteritems()]
            if reg in registros: 
                return self.__mem[reg]
            raise Exception(reg)
        except Exception, e:
            print "El registros" + e.args + "no existe."


    def __operaciones(self, ins, *args):
        """ Método que realiza las operaciones de las instrucciones. """

        @decorador_operaciones
        def move(self, *args):
            pass

        @decorador_operaciones
        def stor(self, *args):
            pass

        @decorador_operaciones
        def load(self, *args):
            pass

        @decorador_operaciones
        def sub(self, *args):
            args, len_args = args[0], len(args[0])

        @decorador_operaciones
        def add(self, *args):
            pass

        @decorador_operaciones
        def mpy(self, *args):
            pass

        @decorador_operaciones
        def div(self, *args):
            pass

        try:
            if len(args[0]) > 0 and  len(args[0]) < 4:
                try:
                    if ins == "MOVE":
                        self.__count += 1
                        return move(self, *args)
                    elif ins == "STOR":
                        self.__count += 1
                        return stor(self, *args)
                    elif ins == "LOAD":
                        self.__count += 1
                        return load(self, *args)
                    elif ins == "SUB":
                        self.__count += 1
                        return sub(self, *args)
                    elif ins == "ADD":
                        self.__count += 1
                        return add(self, *args)
                    elif ins == "MPY":
                        self.__count += 1
                        return mpy(self, *args)
                    elif ins == "DIV":
                        self.__count += 1
                        return div(self, *args)
                    raise Exception(ins)
                except Exception, e:
                    print "La instrucción ", e.args, "no existe."
            raise Exception(len(args[0]))
        except Exception, e:
            print "Número de variables inválidas: " + e.args

    def ejecutar(self):
        for ins, args in self.__instrucciones:
            self.__operaciones(ins, args)

if __name__ == '__main__':
    alu = Alu()
    while True:
        try:
            path = raw_input('Ingresa la dirección del archivo: ')
            f = open(path)
            line = f.readline()
            break
        except IOError:
            print 'El archivo no existe. Vuelve a intentarlo.'

    while line != '':
        alu.leer_instrucciones(line)
        line = f.readline()
    f.close()

    alu.get_instrucciones()
    alu.ejecutar()

# TODO: terminar las métodos.