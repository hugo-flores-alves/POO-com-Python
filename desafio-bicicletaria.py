class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim...")
        
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
        
    def correr(self):
        print("Vruummmmmm...")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
        
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar
b1.correr
b1.parar


b2 = Bicicleta("Verde", "Monark", 2000, 189)

print(b1)
print(b2)


