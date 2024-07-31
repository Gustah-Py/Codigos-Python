import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear una tortuga (cursor gráfico)
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(10)

# Función para dibujar un pétalo
def draw_petal():
    pen.circle(100, 60)  # Dibuja un arco de 60 grados con radio 100
    pen.left(120)
    pen.circle(100, 60)  # Dibuja otro arco
    pen.left(120)

# Dibuja una flor con 6 pétalos
for _ in range(6):
    draw_petal()
    pen.right(60)

# Dibuja el tallo
pen.color("green")
pen.right(90)
pen.penup()
pen.forward(200)
pen.pendown()
pen.forward(100)

# Finalizar
pen.hideturtle()
screen.mainloop()
