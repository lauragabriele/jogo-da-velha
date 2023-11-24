class Jogador:
    def __init__(self):
        self.simbolo = 'X'

    def definir_simbolo(self, simbolo):
        self.simbolo = simbolo

    def alternar_jogador(self):
        self.simbolo = 'O' if self.simbolo == 'X' else 'X'
