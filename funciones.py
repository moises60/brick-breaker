import pygame

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Dimensiones
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
ANCHO_PALETA = 100
ALTO_PALETA = 10
RADIO_PELOTA = 10

# Inicialización de Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Rompe Ladrillos')
reloj = pygame.time.Clock()

def inicializar_ladrillos(filas, columnas):
    """
    Argumentos:
        filas (int): Número de filas de ladrillos .
        columnas (int): Número de columnas de ladrillos.

    Descripción:
        Esta función genera una lista de rectángulos que representan los ladrillos
        y los posiciona en la pantalla según las filas y columnas especificadas.
    """
    ancho_ladrillo = ANCHO_PANTALLA // columnas
    alto_ladrillo = 20
    ladrillos = []

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_ladrillo
            y = fila * alto_ladrillo
            ladrillos.append(pygame.Rect(x, y, ancho_ladrillo, alto_ladrillo))

    return ladrillos
def dibujar_ladrillos(pantalla, ladrillos):
    """
    Argumentos:
        pantalla (pygame.Surface): La superficie donde se dibujarán los ladrillos.
        ladrillos (list): Lista de rectángulos que representan los ladrillos.

    Descripción:
        Dibuja todos los ladrillos en la pantalla.
    """
    for ladrillo in ladrillos:
        pygame.draw.rect(pantalla, ROJO, ladrillo)


def mover_paleta(posicion_x, velocidad):
    """
    Argumentos:
        posicion_x (int): La posición actual en el eje X de la paleta.
        velocidad (int): La velocidad a la que se mueve la paleta.

    Descripción:
        Mueve la paleta a la izquierda o derecha según la velocidad,
        asegurándose de que no se salga de los límites de la pantalla.
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posicion_x -= velocidad
    if keys[pygame.K_RIGHT]:
        posicion_x += velocidad

    if posicion_x < 0:
        posicion_x = 0
    elif posicion_x > ANCHO_PANTALLA - ANCHO_PALETA:
        posicion_x = ANCHO_PANTALLA - ANCHO_PALETA

    return posicion_x
def mover_pelota(posicion_x, posicion_y, velocidad_x, velocidad_y):
    """
    Argumentos:
        posicion_x (int): La posición actual en el eje X de la pelota.
        posicion_y (int): La posición actual en el eje Y de la pelota.
        velocidad_x (int): La velocidad en el eje X de la pelota.
        velocidad_y (int): La velocidad en el eje Y de la pelota.

    Descripción:
        Mueve la pelota según su velocidad actual y cambia la dirección
        si colisiona con los bordes de la pantalla.
    """
    posicion_x += velocidad_x
    posicion_y += velocidad_y

    if posicion_x <= 0 or posicion_x >= ANCHO_PANTALLA - RADIO_PELOTA:
        velocidad_x = -velocidad_x
    if posicion_y <= 0:
        velocidad_y = -velocidad_y

    return posicion_x, posicion_y, velocidad_x, velocidad_y
  



def comprobar_colision_paleta(pelota_x, pelota_y, paleta_x, paleta_y, velocidad_y):
    """
     Argumentos:
        pelota_x (int): Posición en X de la pelota.
        pelota_y (int): Posición en Y de la pelota.
        paleta_x (int): Posición en X de la paleta.
        paleta_y (int): Posición en Y de la paleta.
        velocidad_y (int): Velocidad en Y de la pelota.

    Descripción:
        Verifica si la pelota colisiona con la paleta y cambia su dirección en Y.
    """
    if pelota_y >= paleta_y - RADIO_PELOTA and paleta_x <= pelota_x <= paleta_x + ANCHO_PALETA:
        velocidad_y = -velocidad_y

    return velocidad_y


def comprobar_colision_ladrillos(pelota_x, pelota_y, ladrillos, velocidad_y, puntuacion):
    """
    Argumentos:
        pelota_x (int): Posición en X de la pelota.
        pelota_y (int): Posición en Y de la pelota.
        ladrillos (list): Lista de rectángulos que representan los ladrillos.
        velocidad_y (int): Velocidad en Y de la pelota.
        puntuacion (int): Puntuación actual del jugador .

    Descripción:
        Verifica si la pelota colisiona con algún ladrillo, en caso afirmativo
        elimina el ladrillo, incrementa la puntuación y cambia la dirección
        de la pelota en Y.
    """
    for ladrillo in ladrillos[:]:
        if ladrillo.collidepoint(pelota_x, pelota_y):
            ladrillos.remove(ladrillo)
            velocidad_y = -velocidad_y
            puntuacion += 10
            break

    return velocidad_y, puntuacion



def mostrar_texto(pantalla, texto, fuente, color, x, y):
    """
    Argumentos:
        pantalla (pygame.Surface): Superficie donde se mostrará el texto.
        texto (str): El texto a mostrar.
        fuente (pygame.font.Font): La fuente utilizada para renderizar el texto.
        color (tuple): El color del texto.
        x (int): La posición en X para dibujar el texto.
        y (int): La posición en Y para dibujar el texto.

    Descripción:
        Renderiza y muestra un texto en la pantalla en la posición especificada.
    """
    superficie_texto = fuente.render(texto, True, color)
    pantalla.blit(superficie_texto, (x, y))


def guardar_resultado(nombre, puntuacion, archivo="resultados.txt"):
    """
    Argumentos:
        nombre (str): El nombre del jugador.
        puntuacion (int): La puntuación obtenida por el jugador.
        archivo (str): El archivo donde se guardarán los resultados.

    Descripción:
        Guarda el nombre del jugador y su puntuación en un archivo de texto.
    """
    with open(archivo, "a") as file:
        file.write(f"{nombre}: {puntuacion}\n")
