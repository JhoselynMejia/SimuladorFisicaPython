import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def animar_mruv(vi, a, t):
    try:
        img_obj = mpimg.imread("carro.png")
        img_fondo = mpimg.imread("carretera.jpg")
    except FileNotFoundError:
        print("Error: Asegúrate de que 'carro.png' y 'carretera.jpg' estén en el mismo directorio que el script.")
        return

    tiempo = np.linspace(0, t, 100)
    x = vi*tiempo + 0.5*a*tiempo**2

    fig, ax = plt.subplots()

    ax.imshow(
        img_fondo,
        extent=[0, max(x)+5, -1, 1],
        aspect='auto'
    )

    ax.set_xlim(0, max(x)+5)
    ax.set_ylim(-1, 1)

    imagebox = OffsetImage(img_obj, zoom=0.1)
    ab = AnnotationBbox(imagebox, (x[0], 0), frameon=False)
    ax.add_artist(ab)

    def actualizar(frame):
        ab.xybox = (x[frame], 0)
        return ab,

    ani = FuncAnimation(fig, actualizar, frames=len(x), interval=50)
    plt.title("Movimiento Rectilíneo Uniformemente Variado")
    plt.show()


def mruv():
    while True:

        print("\n MRUV ")
        print("1. x = vi*t + 0.5*a*t^2")
        print("2. x = ((vi + vf)/2)*t")
        print("3. x = (vf^2-vi^2)/(2*a)")
        print("4. Volver")

        op = input("Opción: ")

        if op == "1":

            vi = float(input("Velocidad inicial: "))
            t = float(input("Tiempo: "))
            a = float(input("Aceleración: "))

            x = vi*t + 0.5*a*t**2
            print("Distancia =", x)

            animar_mruv(vi, a, t)

        elif op == "2":

            vf = float(input("Velocidad final: "))
            vi = float(input("Velocidad inicial: "))
            t = float(input("Tiempo: "))

            x = ((vi + vf)/2)*t
            print("Distancia =", x)

            animar_mruv(vi, (vf-vi)/t, t)

        elif op == "3":

            vf = float(input("Velocidad final: "))
            vi = float(input("Velocidad inicial: "))
            a = float(input("Aceleración: "))

            if a == 0:
                print("La aceleración no puede ser 0")
            else:
                x = (vf**2 - vi**2)/(2*a)
                print("Distancia =", x)

        elif op == "4":
            break


######## CAIDA LIBRE ########

def animar_caida(h, t, g):

    tiempo = np.linspace(0, t, 100)
    y = h - 0.5*g*tiempo**2

    try:
        img_obj = mpimg.imread("pelota.JPG.jpg")
        img_fondo = mpimg.imread("cielo.jpg")
    except FileNotFoundError:
        print("Error: Asegúrate de que 'pelota.JPG.jpg' y 'cielo.jpg' estén en el mismo directorio que el script.")
        return

    fig, ax = plt.subplots()

    ax.imshow(
        img_fondo,
        extent=[-1, 1, 0, max(y)+5],
        aspect='auto'
    )

    ax.set_xlim(-1, 1)
    ax.set_ylim(0, max(y)+5)

    imagebox = OffsetImage(img_obj, zoom=0.1)
    ab = AnnotationBbox(imagebox, (0, y[0]), frameon=False)
    ax.add_artist(ab)

    def actualizar(frame):
        ab.xybox = (0, y[frame])
        return ab,

    ani = FuncAnimation(fig, actualizar, frames=len(y), interval=50)

    plt.title("Caída Libre / Tiro Vertical")
    plt.show()


def caida_libre():
    while True:

        print("\n Caída Libre ")
        print("1. h = (1/2)*g*t^2")
        print("2. h = vo*t+(1/2)*g*t^2")
        print("3. Volver")

        op = input("Opción: ")

        if op == "1":

            direccion = input("¿La pelota cae o sube? (cae/sube): ")

            if direccion == "sube":
                g = -9.8
            else:
                g = 9.8

            t = float(input("Tiempo: "))

            h = (1/2)*g*t**2
            print("Altura =", h)

            animar_caida(h, t, g)

        elif op == "2":

            vo = float(input("Velocidad inicial: "))

            direccion = input("¿La pelota cae o sube? (cae/sube): ")

            if direccion == "sube":
                g = -9.8
            else:
                g = 9.8

            t = float(input("Tiempo: "))

            h = vo*t + (1/2)*g*t**2
            print("Altura =", h)

            animar_caida(h, t, g)

        elif op == "3":
            break


######## TIRO PARABOLICO ########

def animar_tiro(v0, angulo):

    g = 9.8
    ang = np.radians(angulo)

    t_vuelo = (2*v0*np.sin(ang))/g
    tiempo = np.linspace(0, t_vuelo, 100)

    x = v0*np.cos(ang)*tiempo
    y = v0*np.sin(ang)*tiempo - 0.5*g*tiempo**2

    try:
        img_obj = mpimg.imread("proyectil.png")
        img_fondo = mpimg.imread("tiro.jpg")
    except FileNotFoundError:
        print("Error: Asegúrate de que 'proyectil.png' y 'tiro.jpg' estén en el mismo directorio que el script.")
        return

    fig, ax = plt.subplots()

    ax.imshow(
        img_fondo,
        extent=[0, max(x)+2, 0, max(y)+2],
        aspect='auto'
    )

    ax.set_xlim(0, max(x)+2)
    ax.set_ylim(0, max(y)+2)

    ax.plot(x, y, 'k--')

    imagebox = OffsetImage(img_obj, zoom=0.09)
    ab = AnnotationBbox(imagebox, (x[0], y[0]), frameon=False)
    ax.add_artist(ab)

    def actualizar(frame):
        ab.xybox = (x[frame], y[frame])
        return ab,

    ani = FuncAnimation(fig, actualizar, frames=len(x), interval=50)
    plt.title("Tiro Parabólico")
    plt.show()


def tiro_parabolico():
    while True:

        print("\n Tiro Parabólico ")
        print("1. Simular tiro")
        print("2. Volver")

        op = input("Opción: ")

        if op == "1":

            v0 = float(input("Velocidad inicial: "))
            angulo = float(input("Ángulo (grados): "))

            animar_tiro(v0, angulo)

        elif op == "2":
            break


######## MENU PRINCIPAL ########

while True:

    print("\n=== Calculadora de Movimientos ===")
    print("1. MRUV")
    print("2. Caída libre")
    print("3. Tiro parabólico")
    print("4. Salir")

    opcion = input("Selecciona: ")

    if opcion == "1":
        mruv()

    elif opcion == "2":
        caida_libre()

    elif opcion == "3":
        tiro_parabolico()

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")