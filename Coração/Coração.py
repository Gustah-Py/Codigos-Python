import turtle

def draw_heart():
    turtle.speed(2)  # Define a velocidade de desenho
    turtle.bgcolor("white")  # Cor de fundo da tela
    turtle.pensize(3)  # Define a espessura da caneta
    turtle.color("red")  # Define a cor da caneta

    turtle.begin_fill()  # Inicia o preenchimento da forma
    turtle.left(140)  # Rotaciona a tartaruga
    turtle.forward(180)  # Desenha a linha do lado esquerdo
    turtle.circle(-90, 200)  # Desenha o primeiro arco
    turtle.left(120)  # Rotaciona para desenhar o segundo arco
    turtle.circle(-90, 200)  # Desenha o segundo arco
    turtle.forward(180)  # Desenha a linha do lado direito
    turtle.end_fill()  # Encerra o preenchimento da forma

    turtle.hideturtle()  # Esconde a tartaruga após o desenho

if __name__ == "__main__":
    draw_heart()
    turtle.done()  # Mantém a janela aberta
