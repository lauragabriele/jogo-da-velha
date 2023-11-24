class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def reiniciar(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def verificar_empate(self):
        return all(cell != ' ' for row in self.tabuleiro for cell in row)
