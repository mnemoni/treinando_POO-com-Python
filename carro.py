# criar classe carro
# 3 ou mais propriedades
# 3 ou mais métodos

# Class
# Syntax

#Marca, Modelo, Cor
class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    pass


    def ignicao(self):
        print('dando partida')

    def acelerar(self):
        print('vrum!vrum!vrum!')

    def frear(self):
        print('brecando!!!!!')

    def ficha(self):
        print(self.marca, self.modelo, self.cor)

# Ignição, Acelerar, Frear

carro1 = Carro('Tesla', 'Model-S', 'Prata')
carro1.ficha()
carro1.ignicao()
carro1.acelerar()
carro1.frear()
carro2 = Carro('Honda', 'Civic', 'Branco')
carro3 = Carro('Lamborghini', 'Aventador', 'Verde')
