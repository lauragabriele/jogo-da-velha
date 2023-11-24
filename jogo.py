import pyxel
from tabuleiro import Tabuleiro
from jogador import Jogador
from verificador import Verificador
from excecoes import CelulaOcupadaException, EmpateException

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_atual = Jogador()
        self.verificador = Verificador()
        self.resultado = None

        escolha_simbolo = input("Escolha o símbolo para começar (X ou O): ").upper()
        while escolha_simbolo not in ['X', 'O']:
            print("Escolha inválida. Tente novamente.")
            escolha_simbolo = input("Escolha o símbolo para começar (X ou O): ").upper()
        self.jogador_atual.definir_simbolo(escolha_simbolo)

        pyxel.init(150, 150, fps=30)
        pyxel.caption = "Jogo da Velha"

        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        if pyxel.btnp(pyxel.KEY_R):
            self.reiniciar_partida()

        if self.resultado is None:
            mapeamento_teclado = {
                pyxel.KEY_1: (0, 0), pyxel.KEY_2: (0, 1), pyxel.KEY_3: (0, 2),
                pyxel.KEY_4: (1, 0), pyxel.KEY_5: (1, 1), pyxel.KEY_6: (1, 2),
                pyxel.KEY_7: (2, 0), pyxel.KEY_8: (2, 1), pyxel.KEY_9: (2, 2),
            }

            for tecla, posicao in mapeamento_teclado.items():
                if pyxel.btnp(tecla):
                    try:
                        linha, coluna = posicao

                        if self.tabuleiro.tabuleiro[linha][coluna] == ' ':
                            self.tabuleiro.tabuleiro[linha][coluna] = self.jogador_atual.simbolo
                            self.verificar_vitoria()
                            self.jogador_atual.alternar_jogador()
                            self.verificar_empate()

                    except (IndexError, CelulaOcupadaException, EmpateException) as e:
                        print(f"Erro: {e}")

    def verificar_vitoria(self):
        resultado = self.verificador.verificar_vitoria(self.tabuleiro.tabuleiro, self.jogador_atual)
        if resultado:
            self.resultado = f"{resultado} UHUUUU! \n Pressione 'R' para reiniciar."

    def verificar_empate(self):
        if self.tabuleiro.verificar_empate() and self.resultado is None:
            raise EmpateException("Empateee! XIIIII! \n Pressione 'R' para reiniciar.")

    def reiniciar_partida(self):
        self.tabuleiro.reiniciar()
        self.jogador_atual = Jogador()
        self.resultado = None

    def desenhar(self):
        pyxel.cls(15)

        for i in range(1, 3):
            pyxel.line(50 * i, 0, 50 * i, 150, 0)
            pyxel.line(0, 50 * i, 150, 50 * i, 0)

        for i in range(3):
            for j in range(3):
                if self.tabuleiro.tabuleiro[i][j] == 'X':
                    pyxel.line(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, 8)
                    pyxel.line((j + 1) * 50, i * 50, j * 50, (i + 1) * 50, 8)
                elif self.tabuleiro.tabuleiro[i][j] == 'O':
                    pyxel.circ(j * 50 + 25, i * 50 + 25, 20, 6)

        if self.resultado is not None:
            pyxel.text(25, 70, self.resultado, 0)

if __name__ == "__main__":
    JogoDaVelha()
