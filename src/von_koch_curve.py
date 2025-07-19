# src/von_koch_curve.py
import turtle

def von_koch_curve(n, length):
    """Generate a von Koch curve for fractal coil design."""
    if n == 0:
        turtle.forward(length)
    else:
        von_koch_curve(n - 1, length / 3)
        turtle.left(60)
        von_koch_curve(n - 1, length / 3)
        turtle.right(120)
        von_koch_curve(n - 1, length / 3)
        turtle.left(60)
        von_koch_curve(n - 1, length / 3)

turtle.speed(0)
for _ in range(3):
    von_koch_curve(2, 100)
    turtle.right(120)
turtle.done()

