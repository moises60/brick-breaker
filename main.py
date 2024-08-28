import random
import pygame
import sys
from funciones import (
    pantalla, reloj, NEGRO, BLANCO, AZUL,
    ANCHO_PANTALLA, ALTO_PANTALLA, ANCHO_PALETA, ALTO_PALETA, RADIO_PELOTA,
    inicializar_ladrillos, dibujar_ladrillos, mover_paleta,
    mover_pelota, comprobar_colision_paleta, comprobar_colision_ladrillos,
    mostrar_texto, guardar_resultado
)

def main():
    """
    Descripción:
        Función principal que maneja el bucle del juego .
        Inicializa posiciones, puntuación y vidas, y maneja las actualizaciones de la pantalla.
    """
    pygame.font.init()
    fuente = pygame.font.Font(None, 36)
    nombre_jugador = input("Introduce tu nombre: ")
    paleta_x = (ANCHO_PANTALLA - ANCHO_PALETA) / 2
    paleta_y = ALTO_PANTALLA - 40
    velocidad_paleta = 7
    pelota_x = ANCHO_PANTALLA / 2
    pelota_y = ALTO_PANTALLA / 2
    velocidad_pelota_x = 4 * random.choice((-1, 1))
    velocidad_pelota_y = -4
    
    ladrillos = inicializar_ladrillos(5, 7)
    vidas = 3
    puntuacion = 0
    corriendo = True
    while corriendo:
          # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
 

        # Movimiento de la paleta
        paleta_x = mover_paleta(paleta_x, velocidad_paleta)

         # Movimiento de la pelotaa
        pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y = mover_pelota(
            pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y
        )

        # Comprobación de  colisiones
        velocidad_pelota_y = comprobar_colision_paleta(
            pelota_x, pelota_y, paleta_x, paleta_y, velocidad_pelota_y
        )
        velocidad_pelota_y, puntuacion = comprobar_colision_ladrillos(
            pelota_x, pelota_y, ladrillos, velocidad_pelota_y, puntuacion
        )



        # Verificar si la pelota cae
        if pelota_y > ALTO_PANTALLA:
            vidas -= 1
            pelota_x = ANCHO_PANTALLA / 2
            pelota_y = ALTO_PANTALLA / 2
            velocidad_pelota_x = 4 * random.choice((-1, 1))
            velocidad_pelota_y = -4

            if vidas == 0:
                corriendo = False
        #  Dibujar en la pantalla
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, (paleta_x, paleta_y, ANCHO_PALETA, ALTO_PALETA))
        pygame.draw.circle(pantalla, AZUL, (int(pelota_x), int(pelota_y)), RADIO_PELOTA)
        dibujar_ladrillos(pantalla, ladrillos)

 
        # puntua ción y vidas
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente, BLANCO, 20, 20)
        mostrar_texto(pantalla, f"Vidas: {vidas}", fuente, BLANCO, ANCHO_PANTALLA - 120, 20)

        # Actualizar la pantalla
        pygame.display.flip()
        # Controlar la velocidad del juego
        reloj.tick(60)

    

    pantalla.fill(NEGRO)
    mostrar_texto(pantalla, f"Juego Terminado", fuente, BLANCO, ANCHO_PANTALLA // 2 - 100, ALTO_PANTALLA // 2 - 50)
    mostrar_texto(pantalla, f"Puntuación Final: {puntuacion}", fuente, BLANCO, ANCHO_PANTALLA // 2 - 100, ALTO_PANTALLA // 2)
    pygame.display.flip()
    
    # Guardar los resultados
    guardar_resultado(nombre_jugador, puntuacion)
    # Esperar 4 segundos 
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

