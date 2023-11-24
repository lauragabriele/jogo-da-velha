class Verificador:
    def verificar_vitoria(self, tabuleiro, jogador_atual):
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ' \
                    or tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
                return f"Jogador {jogador_atual.simbolo} venceu!"

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ' \
                or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
            return f"Jogador {jogador_atual.simbolo} venceu!"

        return None
