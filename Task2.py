class Motor:
    def __init__(self,cai_putere):
        self.cai_putere = cai_putere

class Sofer:
    def __init__(self,nume,data_nasterii):
        self.nume = nume
        self.data_nasterii = data_nasterii

class Masina (Sofer,Motor):
    def __init__(self, marca, model, an_fabricatie, cai_putere, nume, data_nasterii):
        Sofer.__init__(self, nume, data_nasterii)
        Motor.__init__(self, cai_putere)
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie

    def cerinta (self):
        if self.cai_putere > 105 :
            print("Dl./Dna.", self.nume, "nascut la data de", self.data_nasterii, "detine un", self.marca,
                  self.model, "din anul", self.an_fabricatie, "cu", self.cai_putere,"cai putere.\n")
            print
        else :
            print(self.nume,"NU respecta conditia.\n")

if __name__ == "__main__":
    x = []
    x.append(Masina("Mercedes", "GLE", 2020, 571, "Popescu Ion", "1990/06/25"))
    x.append(Masina("VW", "Tiguan", 2010, 140, "Ionescu Marcel", "1984/03/15"))
    x.append(Masina("Fiat", "500", 2018, 60, "Verde Andrei", "1990/11/27"))
    x.append(Masina("Porsche", "911 Turbo S", 2020, 650, "Abecedar Vasile", "1990/09/06"))
    for i in  x:
        Masina.cerinta(i)
