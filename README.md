# **Manim (Mathematical Animation Engine)**
### Libreta de código para programar animaciones en [Manim](https://www.manim.community/), para python.

## ¿Qué es Manim?

**Manim** es una biblioteca de animación matemática de código abierto, concebida por Grant Sanderson, el creador de la plataforma educativa [3Blue1Brown](https://www.3blue1brown.com/). El nombre "Manim" proviene de "Mathematical Animation Engine". Lo que hace que Manim sea excepcional es su capacidad para permitir a los usuarios crear animaciones interactivas y visualizaciones matemáticas de alta calidad.

La librería destaca por su versatilidad y su capacidad para simplificar la explicación de conceptos matemáticos complejos. Las animaciones generadas por Manim no solo son estéticamente atractivas, sino que también ofrecen una comprensión más clara y profunda de los temas, pues facilita la enseñanza y el aprendizaje de conceptos matemáticos de manera intuitiva. La flexibilidad de Manim permite a los creadores personalizar y ajustar las animaciones según sus necesidades, convirtiéndolo en una herramienta valiosa para la educación y la divulgación matemática.

### Python y Manim
Manim utiliza [Python](https://www.python.org/) como lenguaje de programación principal. Python es un lenguaje de programación de alto nivel, fácil de aprender y de sintaxis clara, lo que lo hace adecuado para la creación rápida de prototipos y el desarrollo eficiente. Manim se beneficia de las características poderosas de Python y su amplio ecosistema de bibliotecas.

El flujo de trabajo típico en Manim implica la creación de escenas y objetos gráficos mediante la definición de clases y métodos en Python. La biblioteca utiliza la sintaxis de Python para describir las animaciones y la disposición de los elementos en la escena.

Por ejemplo:

```python
from manim import *
class Circulo(Scene):
    def construct(self):
        circulo = Circle(radius=3)  # crear el círculo
        circulo.set_fill(PINK, opacity=0.5)  # establecer el color y la opacidad
        self.play(Create(circulo))  # animar el círculo
        self.wait(2) # esperar dos segundos
```
En este caso, hemos creado un círculo utilizando la clase `Circulo`, concretamente hemos establecido el Mobject `Circle`, de radio=3, PINK, opacity=0,5. De esta forma, Manim analiza el script y lo "traduce" a una animación que renderizará en un vídeo.

La primera línea del script importa todo el contenido necesario de la biblioteca para llevar a cabo la animación.
```python
from manim import *
```
Ahora analicemos las segundas dos líneas:
```python
class Circulo(Scene):
    def construct(self):
    # resto del código
```
En Manim, la creación de animaciones se realiza en gran medida dentro del método `construct()` de una clase `Scene()`.
1. **Clase `Scene()`**: En primer lugar, creamos una clase que hereda de `Scene()` que actuará como contenedor de las animaciones.
2. **Método construct `construct()`**: Dentro de la clase que hemos creado, en este caso llamada `Circulo`, definimos un método llamado `construct`. Este método es donde colocas el código que crea y anima los objetos de la escena, dicho código es `self`.

Las próximas dos líneas crean un círculo y establecen, en este caso, su opacidad.

```python
circulo = Circle(radius=3)  # crear el círculo
circulo.set_fill(PINK, opacity=0.5)  # establecer el color y la opacidad
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(72).png)

# Manim Objects

En Manim (Mathematical Animation Engine), los "Manim Objects" (`Mobjects`) son las entidades fundamentales que representan diferentes elementos que pueden aparecer y animarse en la pantalla durante una animación matemática. Estos objetos abarcan desde formas geométricas simples hasta objetos más complejos como ecuaciones, gráficos, texto, cámaras, luces, etc.

## Text and Tex mobjects

En Manim podemos renderizar el texto principalmente de dos formas:
1. Usando **Pango**, que es una biblioteca utilizada para el diseño y dibujo de texto internacional `Text_mobject`.
2. Usando **LaTeX**, que es un sistema de composición de textos especializado para escribrir lenguaje matemático `Tex_mobject`.

## Texto utilizando **_Pango_**

Por ejemplo, la forma más simple de animar un texto no LaTeX es a través del mobject `Text` :
```python
from manim import *
class Ejemplo(Scene):
  def construct(self):
    Texto = Text("Soy un texto en ITALIC.", slant=ITALIC) # crear el texto y establecer colo y estilo
    self.play(Write(Texto)) # animar el texto
    self.wait(1) # esperar un segundo
    self.play(FadeOut(Texto)) # desaparecer el texto
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(71).png)

Usamos `stant` para especificar el estilo de texto, que puede ser el por defecto `NORMAL`, o bien `ITALIC` y `OBLIQUE`. Por lo general, el estilo `ITALIC` y el `OBLIQUE` lucen igual, sin embargo, el `ITALIC` usa el _**Roman Style**_, mientras que el `OBLIQUE` utiliza el _**Italic Style**_.

### ¿Cómo usamos las fuentes de texto?

Podemos utilizar los distintos tipos de fuentes a través de `font`.
> Nota: La fuente que utilicemos debe de estar instalada en el sistema, y _Pango_ tiene que saberlo. Podemos insertar una lista fuentes utilizando `manimpango.list_fonts()`.
> ```python
>>>>import manimpango
>>>>manimpango.list_fonts()
> ```
A modo de ejemplo, insertemos un texto escrito en la fuente _Noto Sans_.
```python
from manim import *
import manimpango # importar de manimpango
manimpango.list_fonts()
class Texto(Scene): # establecer escena
  def construct(self):
    Textoejemplo = Text("Soy un texto escrito en Noto Sans.", font="Noto Sans", font_size=50) # Establecemos el texto, su fuente y su tamaño
    self.play(Write(Textoejemplo)) # añadimos el texto
    self.wait(3) #esperar tres segundos
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(73).png)

### ¿Cómo ponemos color al texto?

Podemos poner color a un texto utilizando `color`. También podemos utilizar `t2c`para especificar los caracteres que queremos pintar. Concretamente `t2c`[^1] acepta dos formas de escritura, aunque la siguiente es la recomendable:
- Las _keys_ pueden contener índices como `[2:-1]` o `[4:8]`, que funcionan como el ["_string slicing_"](https://realpython.com/python-strings/#string-manipulation) en python. Los valores deben de estar determinados por el caracter específico y el color se indicará `color=COLOR`.
```python
from manim import *
class Texto(Scene):
  def construct(self):
    Textocolor = Text("Google", t2c={'[0:1]': BLUE,'[1:2]': RED, '[2:3]': YELLOW, '[3:4]': BLUE, '[4:5]': GREEN, '[5:6]': RED}, font_size=144) #establecer texto
    self.play(Write(Textocolor)) # animar el texto
    self.wait(3) # esperar durante tres segundos
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(70).png)

## Utilizando gradient
En Manim, el término "gradient" se refiere generalmente a la transición suave de un color a otro a lo largo de un objeto. Por ejemplo, podemos utilizar gradientes para darle un aspecto más atractivo a las animaciones, especialmente en situaciones donde deseamos resaltar la estructura o forma de un objeto mediante una variación gradual de colores.

Para implementar los colores gradientes en el texto, utilizamos:
- `gradient=COLOR1, COLOR2`
- `Mobject.set_color_by_gradient(COLOR1, COLOR2)`
  
De esta forma establecemos un gradiente conformado por los colores que hemos nombrado.
```python
from manim import *
class TextoGradiente(Scene):
  def construct(self):
    gradiente = Text("Soy un texto gradiente.", gradient=(BLUE, PINK), font_size=50) # establecer texto gradiente
    self.play(Write(gradiente)) # escribir el texto
    self.wait(3) # esperar tres segundos
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(74).png)

## Texto utilizando LaTeX
 
Por otro lado, también podemos insertar ecuaciones matemáticas utilizando LaTeX[^2] mediante el mobject `MathTex`. 

En el contexto de la librería de animación matemática Manim, `MathTex` es una clase que se utiliza para renderizar expresiones matemáticas escritas en el formato LaTeX: un sistema de composición de documentos que se utiliza ampliamente para la creación de documentos científicos y matemáticos debido a su capacidad para producir fórmulas matemáticas de alta calidad.

A modo de ejemplo, escribamos la fórmula general de la derivada de una función:
```python
from manim import *
class Latex(Scene):
  def construct(self):
    Ecuación = MathTex(r"\frac{d}{dx}f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}").set_color_by_gradient(BLUE, ORANGE) # crear la ecuación utilizando LaTeX
    self.play(Write(Ecuación)) # escribir la ecuación
    self.wait(4) # esperar cuatro segundos
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(75).png)

## Lista con viñetas
En Manim podemos crear una lista de viñetas utilizando `BulletedList`:
```python
from manim import *
class ListadeViñetas(Scene):
  def construct(self):
    lista = BulletedList("Zanahorias", "Manzanas", "Fresas") # establecer los ítems de la lista
    lista.set_color_by_tex("Zanahorias", color=ORANGE) # color
    lista.set_color_by_tex("Manzanas", color=GREEN) # color
    lista.set_color_by_tex("Fresas", color=PINK) # color
    self.play(Create(lista), run_time=3) # animar la lista
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(76).png)

## Títulos
Podemos poner títulos utilizando `Title`, es decir:
```python
from manim import *
class Título(Scene):
  def construct(self):
    título = Title("Soy un título") # establecemos un título
    self.add(título) # añadimos el título
```
# VMobject (Vectorized Movable Object)
En Manim, la clase `VMobject` sirve como base para la creación de diversas figuras y objetos visuales en animaciones matemáticas. Estos son algunos de los aspectos claves de _VMobject_:
1. "_Vectorized_": Se refiere a que las formas `VMobject` están definidas en términos de vectores, lo que permite una representación eficiente ya que los vectores pueden describir direcciones, magnitudes y formas en el espacio.
2. "_Movable_": Los `VMobject` son móviles, es decir, se pueden trasladar por toda la pantalla y, de esta forma, crear animaciones dinámicas.
3. "_Manipulación de propiedades_": Se pueden manipular diversas propiedades como la posición, la escala, el color, la opacidad, entre otras.

A modo de ejemplo:
```python
from manim import *
class VMobjects(Scene):
  def construct(self):
    círculo = Circle(radius=2, color=ORANGE, fill_opacity=0.5) # establecemos el círculo
    cuadrado = Square(color=BLUE, fill_opacity=0.5) # creamos el cuadrado
    self.play(Create(círculo), run_time=2) # animamos el círculo
    self.play(Transform(círculo, cuadrado), run_time=3) # hacemos la transformación
    self.wait(3)
```
En este caso, hemos creado un círculo utilizando `Circle` y un cuadrado `Square` para, posteriormente, animar ambos VMobjects. Concretamente, hemos transformado el círculo al cuadrado mediante `Transform`.
```python
self.play(Transform(círculo, cuadrado), run_time=3) # hacemos la transformación
```
## Posicionamiento en Manim
Antes de utilizar las clases mencionadas anteriormente, es importante entender como funciona el posicionamiento[^3] en Manim. Concretamente, se realiza mediante la especificación de puntos en un sistema de coordenadas tridimensional. Podemos utilizar las coordenadas `x, y, z` para definir la posición de los elementos en la escena. Estas son algunas de las pautas para entender cómo funciona el posicionamiento en Manim:
- Coordenadas básicas
    - _X_: Posición horizontal (derecha/izquierda).
    - _Y_: Posición vertical (arriba/abajo).
    - _Z_: Posición hacia/desde la pantalla.
- Sistema de coordenadas
    - _Plano XY_: Si solo se especifica _X_ e _Y_ y dejas _Z_ en cero, trabajas en el plano _XY_.
    - _Mano de derecha_: Manim sigue una convención de mano derecha para las coordenadas tridimensionales.

Para visualizar mejor el posicionamiento de los `Mobjects` podemos utilizar un plano de coordenadas. Es decir:
```python
>>>Plano = Plane()
>>>self.add(Plano)
```
### Puntos
Los puntos los representamos utilizando `Dot`, que representa un punto en el espacio y se puede colocar en una escena en una ubicación específica. Para indicar la ubicación del punto en el espacio utilizamos el sistema de coordenadas `x, y e z` mediante `point=[x,y,z]`.
```python
from manim import *
class Puntos(Scene):
  def construct(self):
    Plano = NumberPlane() # establecemos el plano 
    self.add(Plano)

    # configuramos los puntos

    Punto1 = Dot(color=BLUE)
    Punto2 = Dot(color=PINK, point=[2,2,0])
    Punto3 = Dot(color=RED, point=[4,3,2])

    # añadimos los puntos

    self.add(Punto1, Punto2, Punto3)
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20Plano.png)

### Figuras geométricas 
Los puntos son la forma mas fácil de entender las posiciones en Manim, sin embargo, también podemos utilizar las posiciones para otros tipos de `Mobjects` , tal es el caso de las figuras geométricas e incluso el texto. A modo de ejemplo:
```python
from manim import *
class Puntos(Scene):
  def construct(self):

    # establecemos los Mobjects principales

    cuadrado = Square(color=GREY, fill_opacity=0.5)
    rectángulo = Rectangle(width=3, height=1.5, fill_opacity=0.5).set_color_by_gradient(BLUE, RED)

    # configuramos la posición 

    cuadrado.move_to([3,2,1])
    rectángulo.move_to([-3,-2,2])

    # animamos las figuras

    self.play(Create(cuadrado), run_time=3)
    self.play(Create(rectángulo))
    self.wait()
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(78).png)

Entonces, para establecer una posición concreta para un Mobject utilizamos `.move_to([x,y,z])`. No obstante, podemos utilizar otros tipos de métodos tales como:
- Método `next_to(Mobject, POSITION)`, con el próposito de colocar los `Mobjects` cerca de otros, para ello usamos `UP` , `DOWN` , `RIGHT` , `LEFT` .
- Método `shift([x,y,z)]` or `shift(Time*POSITION)`.

De esta forma:
```python
from manim import *
class Movimiento(Scene):
  def construct(self):
   
   # fijamos un plano para visualizar las posiciones

   Plano = NumberPlane()
   self.add(Plano)

   # creamos los Mobjects

   texto1 = Text("Soy un triángulo", font_size=20)
   texto2 = Text("Soy una estrella", font_size=20)
   triángulo = Triangle(color=YELLOW_E)
   triángulo.set_fill(opacity=0.5, color=RED_C)
   estrella = Star(color=GREEN_D).scale(2)
   estrella.set_fill(opacity=0.5, color=GREEN)

   # determinamos las posiciones

   triángulo.move_to([-4,0,0])
   texto1.next_to(triángulo, UP)
   estrella.move_to([4,0,0])
   texto2.next_to(estrella, UP)

   # añadimos las figuras

   self.add(texto1, texto2, triángulo, estrella)
 ```
![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20posici%C3%B3n.png)

Por otro lado, si utilizamos el método `shift`, haremos lo siguiente:
```python
from manim import *
class Shift(Scene):
  def construct(self):

    # determinamos las figuras

    figura1 = RegularPolygon(n=5, color=PURPLE)
    figura1.set_fill(opacity=0.5, color=GREEN)
    figura2 = RegularPolygon(n=6, color=RED_C)
    figura2.set_fill(opacity=0.5, color=BLUE_C)

    # fijamos las posiciones 
    
    figura1.shift([-3,0,0])
    figura2.shift(2*RIGHT + 1*UP)

    # añadimos ambas figuras

    self.add(figura1)
    self.add(figura2)
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20posici%C3%B3n%202.png)

### Animar los movimientos
Hasta el momento hemos determinado las posiciones mediante los métodos `shift` , `move_to` y `next_to`, que logran el posicionamiento inicial de los Mobjects, pero no su desplazamiento. Por ello, con el objetivo de lograr el movimiento de las distintas figuras, utilizaremos el método `animate`, que luce de la siguiente forma:
```python
self.play(figura1.animate.move_to([-2,-1,1]))
```
Por ejemplo, imaginemos la siguiente animación:
```python
from manim import *
class AnimarMov(Scene):
  def construct(self):

    # establecemos los Mobjects principales

    Mobject0 = Dot(color=GREEN,
                   radius=0.2,
                   fill_opacity=1,
                   point=([0,0,0])
                   )
    Mobject1 = Circle(radius=1, color=GREEN)
    Mobject1.set_fill(color=RED, opacity=0.5)

    # fijamos los Mobjects y realizamos las animaciones

    self.add(Mobject0)
    self.add(Mobject1)
    self.play(Mobject1.animate.move_to([-3,0,0]))
    self.wait()
    self.play(Mobject0.animate.move_to([3,0,0]))
    self.wait()
```


## Polígonos regulares de _n_ lados
La librería de Manim contiene figuras geométricas muy variadas tales como los polígonos regulares, estrellas y círculos que podemos modificar según nuestras necesidades.

Los polígonos regulares son aquellos que creamos mediante `RegularPolygon` e indicamos sus lados utilizando `n=Xlados`. Por ejemplo:
```python
from manim import *
class Polígonos(Scene):
  def construct(self):
    polígono = RegularPolygon(n=9, color=RED, fill_opacity=0.5) # establecemos el polígono
    self.play(Create(polígono), run_time=3) # creamos el polígono
    self.wait()
```
En este caso hemos creado un polígono de nueve lados, de color rojo y opacidad 0.5.

![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(77).png)





## Ejes y funciones









[^2]: Como usar LaTeX: https://manualdelatex.com/
[^3]: Vídeo tutorial de posicionamiento: https://www.youtube.com/watch?v=1Fv0Nu-Tb7Q&t=676s
