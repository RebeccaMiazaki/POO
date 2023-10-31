class Datas(object):
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def setdia(self, dia):
        if dia in (1, 2, 3):
            self.dia = dia
        else:
            self.dia = 1

    def getDia(self):
        return self.dia

    def setMes(self, mes):
        self.Mes = mes

    def getMes(self):
        return self.mes

    def setAno(self, ano):
        self.Ano = ano

    def getAno(self):
        return self.ano

    def __str__(self):
        return "\n\nDia: " + str(self.dia) + "\n Mes: " + str(self.mes) + "\nAno: " + str(self.ano)