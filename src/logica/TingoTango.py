class TingoTango:
    def textoTingoTango(self,numero):
        s = ""
        if (numero % 3 == 0):
            s += "Tingo"
        if (numero % 5 == 0):
            s += "Tango"
        if type(numero)==str:
            print("Error: Ingresa un entero")

        if (len(s)):
            return s
        else:
            return str(numero)