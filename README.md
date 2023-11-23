![image](https://github.com/juanseverich/README.md/assets/151221322/c6443b90-c6c1-4fab-a7a3-998f719b9334)

# UNIVERSIDAD PRIVADA DOMINGO SAVIO
# FACULTAD DE INGENIERIA

# PROGRAMACIÓN 1
# INTEGRANTES
JUAN DE DIOS SEVERICH AGUIRRE

JOSE DANIEL SALAZAR JUSTINIANO
# DOCENTE
ING.JAIME ZAMBRANA CHACÓN

# Nave Recolector de Asteroides

Este código implementa un juego simple en Pygame donde controlas una nave espacial que recolecta asteroides mientras evita colisionar con ellos. La dinámica principal consiste en mover la nave con las teclas direccionales y recolectar los asteroides que aparecen aleatoriamente en la pantalla.

This code implements a simple game in Pygame where you control a spaceship that collects asteroids while avoiding colliding with them. The main dynamic consists of moving the ship with the directional keys and collecting the asteroids that appear randomly on the screen.

## Instrucciones de Uso

1. **Instalación de Dependencias**
   - Asegúrate de tener Pygame instalado en tu entorno de Python para ejecutar este código.

2. **Ejecución del Juego**
   - Ejecuta el archivo principal del código para iniciar el juego.

# DESARROLLO
 Que es python?
 
 Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza 
 para desarrollar aplicaciones de todo tipo, por ejemplo: Instagram, Netflix, Spotify, Panda3D, entre otros

 Que es pygame?
 Pygame es un conjunto de módulos del lenguaje Python que permiten la creación de videojuegos en dos dimensiones de una manera sencilla.
 Está orientado al manejo de sprites. Gracias al lenguaje, se puede prototipar y desarrollar rápidamente.

 Que es os en Python?
 El módulo os en Python proporciona y expone los detalles y la funcionalidad del sistema operativo. Proporciona funcionalidad              independiente del sistema operativo.

 Que es Ramdon en Python?
 El módulo random de la librería estándar de Python incluye un conjunto de funciones que permiten obtener de distintos modos números
 aleatorios o, para ser rigurosos, pseudoaleatorios.
 


## Funcionalidades Principales

- **Control de la Nave:**
  - Utiliza las teclas direccionales (arriba, abajo, izquierda, derecha) para mover la nave por la pantalla.
  
- **Objetivo:**
  - Recolecta los asteroides que aparecen en la pantalla alrededor de la nave.
  - Evita chocar la nave con los asteroides para mantener tu puntaje y vidas.
  
- **Puntaje y Vidas:**
  - Tu puntaje aumenta cada vez que recolectas un asteroide.
  - Pierdes una vida cada vez que colisionas con un asteroide.
  - El juego finaliza cuando tu contador de vidas llega a cero.
  - Si alcanzas 50 puntos, ¡ganarás el juego!

## Estructura del Código

- **Inicialización de Pygame:**
  - Configuración de la pantalla y carga de imágenes y sonidos necesarios para el juego.

- **Bucle Principal:**
  - El juego se ejecuta en un bucle principal donde se manejan los eventos de teclado, se actualizan las posiciones de los elementos (nave, asteroides) y se verifica la lógica del juego (colisiones, puntajes, vidas).

- **Elementos del Juego:**
  - Nave: Representa la nave espacial controlada por el jugador.
  - Asteroides: Elementos que aparecen aleatoriamente en la pantalla para ser recolectados.
  
- **Finalización del Juego:**
  - El juego termina cuando se agotan las vidas (contador de vidas llega a cero) o cuando se alcanza el puntaje objetivo de 50.
 
# IMAGENES
![image](https://github.com/juanseverich/README.md/assets/151221322/b17230c4-2196-48c6-aa19-5072e1b453de)



![image](![image](https://github.com/juanseverich/README.md/assets/151221322/d3c0fb4b-9ecb-4076-a892-39fe6037d04a)


![image](![image](https://github.com/juanseverich/README.md/assets/151221322/7dbf322a-774e-4fe2-b580-d084718a09f8)

## CODIGO DEL JUEGO
   https://github.com/juanseverich/README.md/blob/main/juego.py
## CONCLUSION
El proyecto ilustra la versatilidad de Python como lenguaje de programación para la creación de juegos. Con el uso de Pygame, 'os' y 'random', se ha desarrollado un juego interactivo donde se controla una nave espacial para recolectar asteroides. Este ejemplo resalta la capacidad de Python para construir aplicaciones de entretenimiento complejas de manera accesible. Muestra cómo el lenguaje, combinado con sus extensiones, facilita la implementación ágil de dinámicas de juego. En síntesis, este proyecto ejemplifica cómo Python ofrece un entorno propicio para crear juegos y aplicaciones interactivas de forma rápida y eficiente en múltiples ámbitos.
## BIBLIOGRAFIA

https://www.photopea.com/

https://www.youtube.com/watch?v=xjAvXGT5z3E&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM

https://www.cosmiclearn.com/lang-es/python-os.php#:~:text=El%20m%C3%B3dulo%20os%20en%20Python,funcionalidad%20independiente%20del%20sistema%20operativo.

https://es.wikipedia.org/wiki/Python

https://es.wikipedia.org/wiki/Pygame

https://python-para-impacientes.blogspot.com/2015/09/el-modulo-random.html#:~:text=El%20m%C3%B3dulo%20random%20de%20la,%2C%20para%20ser%20rigurosos%2C%20pseudoaleatorios.
