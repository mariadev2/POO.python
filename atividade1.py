class bicicletaria:
    def caracteristicas(self, cor, modelo, ano, valor,em_movimneto=False):
        self.cor= cor
        self.modelo= modelo
        self.ano= ano
        self.valor=valor
        self.em_movimento=em_movimneto

    def buzinar(self):
        print("BIBIBIBIBIBIBIBBIBIBIB!")
    
    def correr(self):
        self.em_movimento=True
        print("vruuuuuu...")

    def parar(self):
        self.em_movimento=False
        print("parado")

bicicleta1 = bicicletaria("azul","antiga","2022","540",True)
bicicleta1.correr()