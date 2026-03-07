import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def animar_mruv(vi, a, t):
    # con esto se carga la imagen del objeto y del fondo
    try:#Intenta ejecutar  este codigo pero si ocurre un error no funcionara
        img_obj = mpimg.imread("carro.png")       # Imagen del objeto en movimiento
        #imread   convierte la imagen en datos que PY pueda usar
        img_fondo = mpimg.imread("carretera.jpg")   # Fondo de la animación
    except FileNotFoundError:#Si no se escuentra el archivo se ejecutara el print
        print("Error: Asegúrate de que 'carro.png' y 'carretera.png' estén en el mismo directorio que el script.")
        return
# generamos 100 momentos de tiempo entre 0 y el tiempo total
    tiempo = np.linspace(0, t, 100)
    # fórmula de posición del MRUV
    x = vi*tiempo + 0.5*a*tiempo**2
# creamos la ventana donde se va a mostrar la animación
    fig, ax = plt.subplots()

    # Mostrar el fondo cubriendo toda la vista
    # Usa extent para definir tamaño y posición del fondo
    ax.imshow(
        img_fondo,
        extent=[0, max(x)+5, -1, 1],  # ajusta estos valores para que cubra toda la vista
        aspect='auto'
    )

    # límites del gráfico para que el carro no se salga
    ax.set_xlim(0, max(x)+5)
    ax.set_ylim(-1, 1)

    # Crear la imagen del objeto como un OffsetImage
    '''OffsetImage es una función en la biblioteca Matplotlib 
    de Python (específicamente en offsetbox) que permite 
    colocar imágenes como marcadores o anotaciones en gráficos,
    escalando su tamaño y ajustando su posición. Se usa 
    comúnmente para reemplazar puntos de datos estándar 
    con imágenes pequeñas o emojis, generalmente junto con
      AnnotationBbox.'''
    imagebox = OffsetImage(img_obj, zoom=0.1)  # Ajusta zoom según tamaño
    # Crear una AnnotationBbox para el objeto
    ab = AnnotationBbox(imagebox, (x[0], 0), frameon=False)
    ax.add_artist(ab)
    # esta función se ejecuta en cada frame de la animación
    def actualizar(frame):
        # Actualizar la posición de la imagen
        ab.xybox = (x[frame], 0)
        return ab,
    # FuncAnimation hace que la animación corra automáticamente
    ani = FuncAnimation(fig, actualizar, frames=len(x), interval=50)
        # título del gráfico
    plt.title("Movimiento Rectilíneo Uniformemente Variado")
        # mostramos la animación
    plt.show()

    # menú de MRUV donde el usuario elige qué fórmula usar
def mruv():
    while True:

        # menú de opciones
        print("\n MRUV ")
        print("1. x = vi*t + 0.5*a*t^2")
        print("2. x = ((vi + vf)/2)*t")
        print("3. x = (vf^2-vi^2)/(2*a)")
        print("4. Volver")

        op = input("Opción: ")

        # primera fórmula de MRUV
        if op == "1":

            # pedimos datos al usuario
            vi = float(input("Velocidad inicial: "))
            t = float(input("Tiempo: "))
            a = float(input("Aceleración: "))

            # aplicamos la fórmula
            x = vi*t + 0.5*a*t**2

            print("Distancia =", x)

            # mostramos la animación
            animar_mruv(vi, a, t)

        # segunda fórmula
        elif op == "2":

            vf = float(input("Velocidad final: "))
            vi = float(input("Velocidad inicial: "))
            t = float(input("Tiempo: "))

            # cálculo de distancia
            x = ((vi + vf)/2)*t

            print("Distancia =", x)

            # calculamos aceleración para poder animar
            animar_mruv(vi, (vf-vi)/t, t)

        # tercera fórmula
        elif op == "3":

            vf = float(input("Velocidad final: "))
            vi = float(input("Velocidad inicial: "))
            a = float(input("Aceleración: "))

            # evitamos dividir entre 0
            if a == 0:
                print("La aceleración no puede ser 0")
            else:
                x = (vf**2 - vi**2)/(2*a)

                print("Distancia =", x)

        # regresar al menú principal
        elif op == "4":
            break


#######CAIDA LIBER######
def animar_caida(h, t):
    g = 9.8
    tiempo = np.linspace(0, t, 100)
    y = h - 0.5*g*tiempo**2

    try:
        img_obj = mpimg.imread("pelota.JPG.jpg")
        img_fondo = mpimg.imread("cielo.jpg")
    except FileNotFoundError:
        print("Error: Asegúrate de que 'pelota.JPG.jpg' y 'cielo.jpg' estén en el mismo directorio que el script.")
        return

    fig, ax = plt.subplots()

    # Mostrar el fondo cubriendo toda la vista
    ax.imshow(
        img_fondo,
        extent=[-1, 1, 0, h+5],  # ajusta según tamaño del fondo
        aspect='auto'
    )

    # Configurar límites del gráfico
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, h+5)

    # Imagen del objeto
    imagebox = OffsetImage(img_obj, zoom=0.1)
    ab = AnnotationBbox(imagebox, (0, y[0]),  frameon=False)
    ax.add_artist(ab)

    def actualizar(frame):
        ab.xybox= (0, y[frame])
        return ab,

    ani = FuncAnimation(fig, actualizar, frames=len(y), interval=50)
    plt.title("Caída Libre")
    plt.show()


# menú de caída libre
def caida_libre():
    while True:

        print("\n Caída Libre ")
        print("1. h = (1/2)*g*t^2")
        print("2. h = vo*t+(1/2)*g*t^2")
        print("3. Volver")

        op = input("Opción: ")

        if op == "1":

            g = 9.8
            t = float(input("Tiempo: "))

            # fórmula de caída libre
            h = (1/2)*g*t**2

            print("Altura =", h)

            # animamos
            animar_caida(h, t)

        elif op == "2":

            vo = float(input("Velocidad inicial: "))
            g = 9.8
            t = float(input("Tiempo: "))

            h = vo*t + (1/2)*g*t**2

            print("Altura =", h)

            animar_caida(h, t)

        elif op == "3":
            break


        #      Tiro parabolico 
        # esta función simula el movimiento de un proyectil

def animar_tiro(v0, angulo):
    # gravedad
    g = 9.8
    #convertimos el angulo de gados a radianes
    ang = np.radians(angulo)
    # tiempo total de vuelo
    t_vuelo = (2*v0*np.sin(ang))/g
    
    tiempo = np.linspace(0, t_vuelo, 100)
# ecuaciones del tiro parabólico
    x = v0*np.cos(ang)*tiempo
    y = v0*np.sin(ang)*tiempo - 0.5*g*tiempo**2
# con esto se carga la imagen del objeto y del fondo
    try:
        img_obj = mpimg.imread("proyectil.png")
        img_fondo = mpimg.imread("tiro.jpg")
    except FileNotFoundError:
        print("Error: Asegúrate de que 'proyectil.png' y 'tiro.jpg' estén en el mismo directorio que el script.")
        return

    fig, ax = plt.subplots()

    # Mostrar el fondo cubriendo toda la vista
    ax.imshow(
        img_fondo,
        extent=[0, max(x)+2, 0, max(y)+2],  # ajusta tamaño
        aspect='auto'
    )

    # Configurar límites del gráfico
    ax.set_xlim(0, max(x)+2)
    ax.set_ylim(0, max(y)+2)

# Trayectoria de kirby
    ax.plot(x, y, 'k--')

    # Flecha de dirección
    ax.arrow(x[0], y[0], x[-1] - x[0], y[-1] - y[0], head_width=0.2, head_length=0.5, fc='blue', ec='blue', length_includes_head=True)

    # Imagen del proyectil
    imagebox = OffsetImage(img_obj, zoom=0.09)
    ab = AnnotationBbox(imagebox, (x[0], y[0]), frameon=False)
    ax.add_artist(ab)

    def actualizar(frame):
        ab.xybox = (x[frame], y[frame])
        return ab,

    ani = FuncAnimation(fig, actualizar, frames=len(x), interval=50)
    plt.title("Tiro Parabólico")
    plt.show()

    # menú del tiro parabólico
def tiro_parabolico():
    while True:

        print("\n Tiro Parabólico ")
        print("1. Simular tiro")
        print("2. Volver")

        op = input("Opción: ")

        if op == "1":

            # pedimos velocidad y ángulo
            v0 = float(input("Velocidad inicial: "))
            angulo = float(input("Ángulo (grados): "))

            # ejecutamos la animación
            animar_tiro(v0, angulo)

        elif op == "2":
            break


# ---------------- MENU PRINCIPAL ----------------
# aquí empieza realmente el programa
while True:

    print("\n=== Calculadora de Movimientos ===")
    print("1. MRUV")
    print("2. Caída libre")
    print("3. Tiro parabólico")
    print("4. Salir")

    opcion = input("Selecciona: ")

    # dependiendo de lo que el usuario elija
    # llamamos a la función correspondiente

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