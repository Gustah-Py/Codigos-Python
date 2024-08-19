import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.tentativas_maximas = 10

        self.label = tk.Label(root, text="Digite seu palpite (1 a 100):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Enviar", command=self.verificar_palpite)
        self.button.pack()

        self.resultado = tk.Label(root, text="")
        self.resultado.pack()

    def verificar_palpite(self):
        try:
            palpite = int(self.entry.get())
            self.tentativas += 1

            if palpite < self.numero_secreto:
                self.resultado.config(text="Muito baixo!")
            elif palpite > self.numero_secreto:
                self.resultado.config(text="Muito alto!")
            else:
                self.resultado.config(text=f"Parabéns! Você acertou em {self.tentativas} tentativas.")
                messagebox.showinfo("Parabéns!", f"Você acertou o número {self.numero_secreto}!")
                self.root.quit()

            if self.tentativas >= self.tentativas_maximas and palpite != self.numero_secreto:
                self.resultado.config(text=f"Você não conseguiu adivinhar o número. Era {self.numero_secreto}.")
                messagebox.showinfo("Fim do Jogo", f"O número era {self.numero_secreto}.")
                self.root.quit()

        except ValueError:
            self.resultado.config(text="Por favor, insira um número válido.")

root = tk.Tk()
app = JogoAdivinhacao(root)
root.mainloop()
