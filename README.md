# **ManimCE**
### Libreta de código para programar animaciones en [ManimCE](https://www.manim.community/), para python.

## ¿Qué es Manim?

**Manim** es una biblioteca de animación matemática de código abierto desarrollada en Python. El nombre "Manim" proviene de "Mathematical Animation Engine". Fue creado por Grant Sanderson, el creador de la plataforma educativa en línea "3Blue1Brown". 

Manim permite a los usuarios crear animaciones interactivas y visualizaciones matemáticas de alta calidad. Es particularmente útil para explicar conceptos matemáticos de manera intuitiva, ya que las animaciones pueden proporcionar una comprensión más clara y profunda de los temas.

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

## Manim Objects

En Manim (Mathematical Animation Engine), los "Manim Objects" (`Mobjects`) son las entidades fundamentales que representan diferentes elementos que pueden aparecer y animarse en la pantalla durante una animación matemática. Estos objetos abarcan desde formas geométricas simples hasta objetos más complejos como ecuaciones, gráficos, texto, cámaras, luces, etc.

### `Text` and `Tex` mobjects

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

Para implementar los colores gradientes en el texto, utilizamos `gradient=COLOR1, COLOR2`. De esta forma establecemos un gradiente conformado por los colores que hemos nombrado.
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
 
Por otro lado, también podemos insertar ecuaciones matemáticas utilizado LaTeX[^2] mediante el mobject `MathTex`. 

En el contexto de la librería de animación matemática Manim, `MathTex` es una clase que se utiliza para renderizar expresiones matemáticas escritas en el formato LaTeX. LaTeX es un sistema de composición de documentos que se utiliza ampliamente para la creación de documentos científicos y matemáticos debido a su capacidad para producir fórmulas matemáticas de alta calidad.

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
## Posicionamiento en Manim
Antes de utilizar las clases mencionadas anteriormente, es importante entender como funciona el posicionamiento[^3] en Manim. Concretamente, se realiza mediante la especificación de puntos en un sistema de coordenadas tridimensional. Podemos utilizar las coordenadas `x, y, y z` para definir la posición de los elementos en la escena. Estas son algunas de las pautas para entender cómo funciona el posicionamiento en Manim:
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














[^2]: Como usar LaTeX: https://manualdelatex.com/
[^3]: Vídeo tutorial de posicionamiento: https://www.youtube.com/watch?v=1Fv0Nu-Tb7Q&t=676s
