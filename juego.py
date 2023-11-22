
#NOMBRE DEL JUEGO NAVE RECOLECTOR DE ASTEROIDES

import pygame
import os
import random

# Inicializa pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))


# Obtiene la ruta de la imagen del fondo
imagen = os.path.join(os.getcwd(), 'img', 'fondo.jpeg')

# Carga la imagen del fondo
fondo = pygame.image.load(imagen)

# Cargar imagen de nave
navejuan = os.path.join(os.getcwd(),'img', 'nave.png')
nave1 = pygame.image.load(navejuan)

# Cargar imagen de asteroide
asteroidejuan = os.path.join(os.getcwd(),'img', 'asteroide.png')
asteroide1 = pygame.image.load(asteroidejuan)

#-----------------------------------------------------------------------------
# Cargar imagen de asteroide en formato PNG
asteroide_png = os.path.join(os.getcwd(), 'img', 'asteroide2.png')
asteroide3 = pygame.image.load(asteroide_png)
#Caragar Corazon de Vidas
corazon_png = os.path.join(os.getcwd(), 'img', 'corazon.png')
corazon = pygame.image.load(corazon_png)

# Crear lista de asteroides con la nueva imagen 
asteroides = []
num_asteroides = 50  # Puedes ajustar la cantidad de asteroides

for _ in range(num_asteroides):
    asteroide = {
        'surface': asteroide3,  # Utilizar la imagen cargada
        'x': random.randint(0, 780 - asteroide3.get_width()),
        'y': random.randint(-600, -50),  # Empiezan arriba de la pantalla
        'speed': random.randint(2, 2)  # Velocidad variable
    }
    asteroides.append(asteroide)
#----------------------------------------------------------------------------

# Cargar sonido de fondo de la nave
sonido_nave = os.path.join(os.getcwd(),'sonidos', 'musica1.mp3')
pygame.mixer.music.load(sonido_nave)
#Para que se repita el sonido
pygame.mixer.music.play(-1)

sonido_colision3 = os.path.join(os.getcwd(),'sonidos', 'movimientodelanave.wav')


sonido_colision = os.path.join(os.getcwd(),'sonidos', 'sonidochocar.wav')
sonido_colision2 = os.path.join(os.getcwd(),'sonidos', 'chocar.wav')
# Crear nave
nave_x = 340
nave_y = 500

# Crear asteroide
asteroide_x = random.randint(0, 780 - asteroide1.get_width())
asteroide_y = random.randint(0, 500 - asteroide1.get_height())

# Configura el bucle principal del juego
ventana = True
score = 0
vida = 5
fuente = pygame.font.Font(None, 60)

while ventana:
    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventana = False




    # Leer teclas de flecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        nave_y -= 1
        pygame.mixer.Sound(sonido_colision3).play()
        
    if keys[pygame.K_DOWN]:
        nave_y += 1
        pygame.mixer.Sound(sonido_colision3).play()        
    if keys[pygame.K_LEFT]:
        nave_x -= 1
        pygame.mixer.Sound(sonido_colision3).play()        
    if keys[pygame.K_RIGHT]:
        nave_x += 1
        pygame.mixer.Sound(sonido_colision3).play()         
#----------------------------------------------------------------------------------
    # Restringir los valores de nave_x y nave_y
    nave_x = max(nave_x, 0) # No permitir que nave_x sea menor a 0
    nave_x = min(nave_x, 800 - nave1.get_width()) # No permitir que nave_x sea mayor a 800 - ancho de la nave
    nave_y = max(nave_y, 0) # No permitir que nave_y sea menor a 0
    nave_y = min(nave_y, 600 - nave1.get_height()) # No permitir que nave_y sea mayor a 600 - alto de la nave
#----------------------------------------------------------------------------------
    
    # Comprobar colisión entre la nave y el asteroide
    if (nave_x < asteroide_x + asteroide1.get_width() and
        nave_x + nave1.get_width() > asteroide_x and
        nave_y < asteroide_y + asteroide1.get_height() and
        nave_y + nave1.get_height() > asteroide_y):



        asteroide_x = random.randint(0, 750 - asteroide1.get_width())
        asteroide_y = random.randint(0, 400 - asteroide1.get_height())

        #Si colisiona suma un punto
        score += 1
        pygame.mixer.Sound(sonido_colision).play()

        # Mueve los asteroides y los hace aparecer en la pantalla nuevamente
    for asteroide in asteroides:
            asteroide['y'] += asteroide['speed']

        # Si los asteroides se salen de la pantalla, los reposiciona arriba
    if asteroide['y'] > 600:
            asteroide['x'] = random.randint(0, 780 - asteroide3.get_width())
            asteroide['y'] = random.randint(-600, -50)

        # Comprobar colisión entre la nave y el asteroide
    if (nave_x < asteroide['x'] + asteroide3.get_width() and
                    nave_x + nave1.get_width() > asteroide['x'] and
                    nave_y < asteroide['y'] + asteroide3.get_height() and
                    nave_y + nave1.get_height() > asteroide['y']):


                    asteroide['x'] = random.randint(0, 750 - asteroide3.get_width())
                    asteroide['y'] = random.randint(-600, -50)
                    vida -=1
                    pygame.mixer.Sound(sonido_colision2).play()
#--------------------------------------------------------------------------------------

    # Dibuja el fondo en la pantalla
    screen.blit(fondo, (0, 0))
    #DIBUJAR TEXTO
    text = fuente.render('PROYECTO FINAL', True, (0, 255, 255))
    screen.blit(text, (220, 560))
    text = fuente.render('Puntos: %s' % score, True, (255, 255, 255))
    screen.blit(text, (1, 1))
    text = fuente.render(': %s' % vida, True, (255, 255, 255))
    screen.blit(text, (700, 15))


 
    screen.blit(nave1, (nave_x, nave_y))
    screen.blit(asteroide1, (asteroide_x, asteroide_y))
    screen.blit(asteroide3, (asteroide['x'], asteroide['y']))
    screen.blit(corazon, (630, 1))
    #SI LA VIDA ES IGUAL A 0 SE CIERRA LA VENTANA
    if vida == 0:
        text = fuente.render('GAME OVER', True, (255, 0, 0))
        screen.blit(text, (270, 280))
              
        ventana= False
    if score == 50:
        text = fuente.render('GANADOR', True, (228, 255, 0))
        screen.blit(text, (270, 280))
        print("HAZ GANADO")
        
        ventana = False

    
    # Actualiza la pantalla
    pygame.display.flip()

# Finaliza el juego
pygame.quit()


