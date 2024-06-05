class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando o motor...")
        print("Motor Ligado!")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        return f"{'Sim' if self.carregado else 'Não'} estou carregado"

moto = Motocicleta("Preta", "ABC-1234", 2)
carro = Carro("Azul", "CBA-2314", 4)
caminhao = Caminhao("Verde", "LFK-3948", 8, False)

print(caminhao)
print(carro)
print(moto)
print(caminhao.esta_carregado())
