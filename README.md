# **Manim (Mathematical Animation Engine)**
### Libreta de código para programar animaciones en [Manim](https://www.manim.community/), para python.

## ¿Qué es Manim?

**Manim** es una biblioteca de animación matemática de código abierto, concebida por Grant Sanderson, el creador de la plataforma educativa [3Blue1Brown](https://www.3blue1brown.com/). El nombre "Manim" proviene de "Mathematical Animation Engine". Lo que hace que Manim sea excepcional es su capacidad para permitir a los usuarios crear animaciones interactivas y visualizaciones matemáticas de alta calidad.

La librería se destaca por su versatilidad y su capacidad para simplificar la explicación de conceptos matemáticos complejos. Las animaciones generadas por Manim no solo son estéticamente atractivas, sino que también ofrecen una comprensión más clara y profunda de los temas, pues facilita la enseñanza y el aprendizaje de conceptos matemáticos de manera intuitiva. La flexibilidad de Manim permite a los creadores personalizar y ajustar las animaciones según sus necesidades, convirtiéndolo en una herramienta valiosa para la educación y la divulgación matemática.

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(72).png)

# Manim Objects

En Manim (Mathematical Animation Engine), los "Manim Objects" (`Mobjects`) son las entidades fundamentales que representan diferentes elementos que pueden aparecer y animarse en la pantalla durante una animación matemática. Estos objetos abarcan desde formas geométricas simples hasta objetos más complejos como ecuaciones, gráficos, texto, cámaras, luces, etc.

## Text and Tex mobjects

En Manim podemos renderizar el texto principalmente de dos formas:
1. Usando **Pango**, que es una biblioteca utilizada para el diseño y dibujo de texto internacional `Text_mobject`.
2. Usando **LaTeX**, que es un sistema de composición de textos especializado para escribrir lenguaje matemático `Tex_mobject`.
### Distintos tipo de \`Text\` 
| Clases       | Definición                                    |
|--------------|-----------------------------------------------|
| MarkupText   | Muestra texto renderizado (no-LaTeX) utilizando Pango. |
| Paragraph    | Muestra un párrafo de texto.                   |
| Text         | Muestra texto renderizado (no-LaTeX) utilizando Pango. |



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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(71).png)

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(73).png)

### ¿Cómo ponemos color al texto?

Podemos poner color a un texto utilizando `color`. También podemos utilizar `t2c`para especificar los caracteres que queremos pintar. Concretamente `t2c`acepta dos formas de escritura, aunque la siguiente es la recomendable:
- Las _keys_ pueden contener índices como `[2:-1]` o `[4:8]`, que funcionan como el ["_string slicing_"](https://realpython.com/python-strings/#string-manipulation) en python. Los valores deben de estar determinados por el caracter específico y el color se indicará `color=COLOR`.
```python
from manim import *
class Texto(Scene):
  def construct(self):
    Textocolor = Text("Google", t2c={'[0:1]': BLUE,'[1:2]': RED, '[2:3]': YELLOW, '[3:4]': BLUE, '[4:5]': GREEN, '[5:6]': RED}, font_size=144) #establecer texto
    self.play(Write(Textocolor)) # animar el texto
    self.wait(3) # esperar durante tres segundos
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(70).png)

Por otro lado, _Pango_ también nos permite configurar el ancho del texto a través de `weight="TIPO DE WEIGHT"`. A modo de ejemplo, insertemos un texto escrito en la fuente Roboto, concretamente en BOLD.
```python
from manim import *
import manimpango

class WeightHEAVY(Scene):
  def construct(self):

    # establecemos el texto y sus configuraciones

    Texto = Text("¡Hola Manim!",
                 font="Roboto",
                 font_size=50,
                 weight="BOLD"
                 )
    
    # animamos el texto

    self.add(Texto)
```
>[!NOTE]
>Los distintos tipos de `weight` lucen de la siguiente forma, asegúrate de utilizar el que mejor te convenga.

>![](https://github.com/BrosReys/ManimCE/blob/Images/DifferentWeights.png)

### ¿Cómo animamos el texto?
La librería de Manim ofrece numerosas formas de introducir/quitar el texto que podemos utilizar mediante los siguientes métodos de animación:
```python
from manim import *
class AnimTexto(Scene):
  def construct(self):

    Ejemplot = Text("¡Hola Manim!")

    # para añadir/quitar el texto instantáneamente

    self.add(Ejemplot)
    self.remove(Ejemplot)

    # para escribir/anular escribir el texto

    self.play(Write(Ejemplot))
    self.play(Unwrite(Ejemplot))

    # para añadir/quitar letra por letra el texto

    self.play(AddTextLetterByLetter(Ejemplot))
    self.play(RemoveTextLetterByLetter(Ejemplot))

    # para añadir primero los bordes y después rellenar

    self.play(DrawBorderThenFill(Ejemplot))
    self.remove(Ejemplot)

    # para aparecer/desaparecer el texto

    self.play(FadeIn(Ejemplot))
    self.play(FadeOut(Ejemplot))
```

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(74).png)

## Texto utilizando LaTeX
### Distintos tipos de \`tex_mobject\`
| Clase                | Descripción                                                  |
|----------------------|--------------------------------------------------------------|
| BulletedList         | Una lista con viñetas.                                       |
| MathTex              | Una cadena compilada con LaTeX en modo matemático.           |
| SingleStringMathTex  | Bloque de construcción fundamental para renderizar texto con LaTeX. |
| Tex                  | Una cadena compilada con LaTeX en modo normal.               |
| Title                | Un objeto representando un título subrayado.                |


 
Consecuentemente, podemos insertar ecuaciones matemáticas utilizando LaTeX[^1] mediante el mobject `MathTex`. 

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(75).png)

### Lista con viñetas
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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(76).png)

### Títulos
Podemos poner títulos utilizando `Title`, es decir:
```python
from manim import *
class Título(Scene):
  def construct(self):
    título = Title("Soy un título") # establecemos un título
    self.add(título) # añadimos el título
```
## Variables y \`ValueTracker\`
En Manim, las variables y ValueTracker son herramientas poderosas que permiten realizar animaciones dinámicas y seguir el cambio de valores a lo largo del tiempo.

1. **Variables**
    - Utilizamos las variables en Manim para almacenar valores que pueden cambiar durante una animación.
    - Pueden ser variables simples como números o incluso objetos más complejos como vectores.
    - Manim ofrece la clase `ValueTracker` que es comúnmente utilizada para seguir y animar el cambio de valores a lo largo del tiempo.
2. **ValueTracker**
    - `ValueTracker` es una clase en Manim que realiza un seguimiento de un valor numérico a lo largo de una animación.
    - Permite vincular ese valor a propiedades de objetos gráficos, de modo que, cuando el valor cambia, los objetos gráficos se actualizan automáticamente.
    - Facilita la creación de animaciones que responden a cambios en variables específicas.
    - Se utiliza junto con la clase `DecimalNumber` para mostrar el valor actualizado en la pantalla.

A modo de ejemplo, analicemos las siguientes líneas de código:
```python
from manim import *
class Variables(Scene):
  def construct(self):
   
    var = 1.5

    # creamos una variable llamada `var` con un valor inicial de 1.5

    variable = Variable(var, MathTex(r" \alpha "), num_decimal_places=3).move_to([0,0,0])
   
    # la clase `Variable` se utiliz para mostrar el valor inicial

    variable.label.set_color(BLUE) # determinamos el color de la etiqueta
    tracker = variable.tracker # establecemos un `ValueTracker`
    var = 10 # `var` muestra el valor final

    # establecemos las animaciones

    self.play(Write(variable))
    self.wait()
    self.play(tracker.animate.set_value(var), run_time=3)
    self.wait(2)
```
1. **Crear una variable**
```python
    var = 1.5
    variable = Variable(var, MathTex(r" \alpha "), num_decimal_places=3)
```
- Se crea una variable llamada `var` con un valor inicial de 1.5.
- La clase `Variable` se utiliza para mostrar el valor de la variable en la pantalla. MathTex(r" \alpha ") es un objeto LaTeX que representa el símbolo alfa.
- `num_decimal_places=3` indica que se mostrarán tres lugares decimales en la pantalla.

2. **Obtener el tracker para la variable**
  ```python
  tracker = variable.tracker
```
El tracker es un `ValueTracker` asociado a la variable. Podemos utilizarlo para animar el cambio del valor de la variable.
3. **Cambiar el valor de la variable
```python
    var = 10
```
Aquí se cambiamos el valor de la variable original `var`. Sin embargo, esto no afecta directamente a lo que se muestra en la pantalla.

**Métodos**
| Método                | Descripción                                            |
|-----------------------|--------------------------------------------------------|
| animate               | Utilizado para animar la aplicación de cualquier método propio. |
| animation_overrides   | Anulaciones para parámetros de animación.                    |
| color                 | La propiedad de color.                                    |
| depth                 | La profundidad del objeto.                              |
| fill_color            | Si hay múltiples colores (para gradientes), esto devuelve el primero. |
| height                | La altura del objeto.                             |
| n_points_per_curve    | Número de puntos por curva.                            |
| sheen_factor          | Propiedad de factor de brillo.                                 |
| stroke_color          | La propiedad de color del trazo.                             |
| width                 | El ancho del objeto.                              |

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
Antes de utilizar las clases mencionadas anteriormente, es importante entender como funciona el posicionamiento[^2] en Manim. Concretamente, se realiza mediante la especificación de puntos en un sistema de coordenadas tridimensional. Podemos utilizar las coordenadas `x, y, z` para definir la posición de los elementos en la escena. Estas son algunas de las pautas para entender cómo funciona el posicionamiento en Manim:
- Coordenadas básicas
    - _X_: Posición horizontal (derecha/izquierda).
    - _Y_: Posición vertical (arriba/abajo).
    - _Z_: Posición hacia/desde la pantalla.
- Sistema de coordenadas
    - _Plano XY_: Si solo se especifica _X_ e _Y_ y dejas _Z_ en cero, trabajas en el plano _XY_.
    - _Mano de derecha_: Manim sigue una convención de mano derecha para las coordenadas tridimensionales.

Para visualizar mejor el posicionamiento de los `Mobjects` podemos utilizar un plano de coordenadas[^3]. Es decir:
```python
>>>Plano = NumberPlane()
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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20Plano.png)

## Figuras geométricas 
Los puntos son la forma mas fácil de entender las posiciones en Manim, sin embargo, también podemos utilizar las posiciones para otros tipos de `Mobjects` , tal es el caso de las figuras geométricas e incluso el texto.
### Polígonos regulares de _n_ lados
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

>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(77).png)

A modo de ejemplo:
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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(78).png)

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20posici%C3%B3n.png)

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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Imagen%20posici%C3%B3n%202.png)

### ¿Cómo utilizamos el método "animate"?
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
En este caso hemos utilizado el método `animate` para cambiar la posición de los distintos Mobjects. No obstante, podemos usar el método `animate` para determinar, entre otros parámetros, la escala y la rotación.
- La escala (`scale`): Para determinar la escala utilizamos números enteros sencillos. Generalmente entre 0.5 y 3.
- La rotación (`rotate`): Para rotar los mobjects indicamos utilizando PI/RADIANES.

```python
from manim import *
class Animate(Scene):
  def construct(self):

    Plano = NumberPlane()
    self.add(Plano)

    # Mobjects

    Punto = Dot(radius=0.3).set_color_by_gradient(BLUE, RED)
    Estrella = Star(color=GREEN).next_to(Punto, DOWN + RIGHT)
    Estrella.set_fill(opacity=0.5, color=YELLOW_B)
    Cuadrado = Square(color=BLUE, side_length=3).set_fill(opacity=0.5, color=GREEN)

    self.add(Punto, Estrella)

    # `animate` cambiando la posición

    self.play(Punto.animate.move_to([-2,3,0]),
              Estrella.animate.shift(2*UP)
              )
    self.wait()
    
    # `animate` cambiando la rotación
    
    self.play(Estrella.animate.rotate(PI/5))
    self.wait()
    self.play(Estrella.animate.move_to([0,0,0]),
              Punto.animate.move_to([0,0,0]),
              Transform(Punto, Cuadrado)
              )


    # `animate` cambiando la escala

    self.play(Estrella.animate.scale(2), Punto.animate.scale(0.5))
    self.play(Estrella.animate.rotate(PI/5))

    self.play(Estrella.animate.move_to([0,0,0]), run_time=3)
    self.play(Punto.animate.move_to([0,-0.25,0]), run_time=3)
    self.wait()
    self.play(FadeOut(Punto))
```
## Líneas, Flechas y Vectores
En Manim, las líneas, flechas y vectores son elementos gráficos fundamentales pues, entre otras cosas, nos ayudan a representar de forma clara y concisa las direcciones.
### Líneas
Las líneas son instancias de la clase `Line`. Podemos crear líneas especificando los puntos de inicio y fin con las coordenadas (x, y, z). Además, podemos establecer propiedades como el color, el grosor de línea y el estilo.

A modo de ejemplo:
```python
from manim import *
import numpy as np
class Líneas(Scene):
  def construct(self):

    # determinamos las líneas

    línea1 = Line(start=np.array([0,0,0]),end=np.array([2,3,0]),
                  color=GOLD                 
                  )
    línea2 = Line(start=ORIGIN, end=2*RIGHT, 
                  color=GREEN)

    self.add(línea1, línea2) # añadimos las líneas
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/l%C3%ADneas.png)
### Flechas
Las flechas son representaciones gráficas que incluyen una punta de flecha en un extremo, y se pueden crear y personalizar utilizando la clase `Arrow`.
```python
from manim import *
class Flechas(Scene):
  def construct(self):

    Plano = NumberPlane()
    self.add(Plano)

    # determinamos las flechas

    flecha1 = Arrow(start=ORIGIN, end=[-3,2,0],
                    color=TEAL_C, stroke_width=3, tip_length=0.6
                    )
    flecha2  = Arrow(start=[-3,2,0], end=[-3,0,0],
                     )
    flecha2.set_color_by_gradient(TEAL, RED)

    flecha3 = Arrow(start=[-3,0,0], end=[5,-2,0],
                    stroke_width=10)
    flecha3.set_color_by_gradient(RED, ORANGE)
    
    
    self.add(flecha1, flecha2, flecha3)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Flechas.png)

**Métodos**

| Método                      | Descripción                                                  |
|-----------------------------|--------------------------------------------------------------|
| `get_default_tip_length`    | Devuelve la longitud predeterminada de la punta de la flecha.|
| `get_normal_vector`         | Devuelve el vector normal de un vector.                       |
| `reset_normal_vector`       | Restablece el vector normal de un vector.                      |
| `scale`                     | Escala una flecha, pero mantiene el grosor de línea y el tamaño de la punta de la flecha fijos. |

**Atributos**

| Atributo                  | Descripción                                            |
|---------------------------|--------------------------------------------------------|
| `animate`                 | Se utiliza para animar la aplicación de cualquier método de `self`. |
| `animation_overrides`     |                                                        |
| `color`                   |                                                        |
| `depth`                   | La profundidad del objeto.                               |
| `fill_color`              | Si hay múltiples colores (para degradado), devuelve el primero.|
| `height`                  | La altura del objeto.                                    |
| `n_points_per_curve`      |                                                        |
| `sheen_factor`            |                                                        |
| `stroke_color`            |                                                        |
| `width`                   | El ancho del objeto.                                    |

### Vectores 
Vectores, cuando nos referimos a un objeto gráfico, hablamos de un `Mobject` específico utilizado para representar flechas en la pantalla. Estos vectores gráficos son instancias de la clase `Arrow` y se utilizan comúnmente para visualizar direcciones y orientaciones en animaciones matemáticas y físicas.

A modo de ejemplo, en las siguientes líneas insertaremos tres vectores distintos mediante la clase `Vector`:
```python
from manim import *
class Vectores(Scene):
  def construct(self):

    Plano = NumberPlane()
    self.add(Plano)

    # determinamos los vectores

    vector1 = Vector([2,-3], color=RED) 
    vector2 = Vector([3,2], color=GREEN)
    vector3 = Vector([-2,1], color=YELLOW)

    # fijamos las etiquetas

    etiqueta1 = vector1.coordinate_label(color=GREEN)
    etiqueta2 = vector2.coordinate_label(color=YELLOW)
    etiqueta3 = vector3.coordinate_label(color=RED)

    # añadimos los vectores y etiquetas

    self.add(vector1, vector2, vector3, etiqueta1, etiqueta2, etiqueta3)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Vectores.png)

**Métodos**
| Método                 | Descripción                                               |
|------------------------|-----------------------------------------------------------|
| `coordinate_label`     | Crea una etiqueta basada en las coordenadas del vector.    |

**Atributos**
| Atributo               | Descripción                                            |
|------------------------|--------------------------------------------------------|
| `animate`              | Se utiliza para animar la aplicación de cualquier método de `self`. |
| `animation_overrides`  |                                                        |
| `color`                |                                                        |
| `depth`                | La profundidad del objeto.                               |
| `fill_color`           | Si hay múltiples colores (para degradado), devuelve el primero.|
| `height`               | La altura del objeto.                                    |
| `n_points_per_curve`   |                                                        |
| `sheen_factor`         |                                                        |
| `stroke_color`         |                                                        |
| `width`                | El ancho del objeto.                                    |

# Gráficos y Funciones
La librería de **Manim** nos ofrece distintas formas de implementar gráficos y funciones en nuestras animaciones. Hasta ahora hemos trabajado con la clase `Scene`, no obstante, existen diversas clases tales como `GraphScene`, `ThreeDScene`, entre otras que pueden facilitarnos la tarea de graficar. Concretamente, para representar gráficos utilizamos fundamentalmente `Scene`, `ThreeDScene` y `GraphScene`.
## \`Scene\` y \`Axes\`
Cuando utilizamos la clase `Scene` para realizar gráficos, trabajamos en un nivel más general y flexible, pues tenemos el control total sobre la creación y animación de elementos en la escena, pero también necesitamos definir manualmente los ejes y configurar los gráficos.
Por otro lado, es posible que necesitemos importar bibliotecas específicas para funciones matemáticas y gráficos, como NumPy, y definir funciones que describan nuestros gráficos.
>[!IMPORTANT]
> En general, este enfoque ofrece más flexibilidad, pero también requiere más código y configuración manual para crear gráficos matemáticos.

### ¿Cómo creamos los ejes utilizando \`Scene\`?
```python
from manim import *
class EjesXY(Scene):
  def construct(self):

    # definimos los ejesXY

    Ejes = Axes(x_range=([-5,5]),
                y_range=([-5,5]),
                x_length=5,
                y_length=5,
    )
    self.add(Ejes)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Ejes.png)

También podemos importar el plano polar mediante `PolarPlane`, es decir:
```python
from manim import *
class Planopolar(Scene):
  def construct(self):

    plano = PolarPlane(azimuth_units="PI radians",
                       size=6,
                       azimuth_label_font_size=33).add_coordinates()
    self.add(plano)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Plano%20Polar.png)

Además, podemos utilizar el `NumberPlane` para representar un gráfico sencillo llamado `LineGraph`:
```python
from manim import *
class GráficoLineal(Scene):
  def construct(self):

    # establecemos el plano

    Gráfico = NumberPlane(x_range=([0,5]),
                          y_range=([0,5]),
                          x_length=5,
                          axis_config = {"include_numbers":True, "color":YELLOW}                            
    )

    Gráfico.center()

    # determinamos el gráfico lineal

    GráficoLineal = Gráfico.plot_line_graph(
        x_values = [1,2,3,4,5],
        y_values = [1,3,1,4,2],
        line_color=RED,
    )

    # añadimos el plano y el gráfico lineal

    self.add(Gráfico, GráficoLineal)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Gr%C3%A1ficoLineal.png)

Esta es la forma más sencilla de importar unos ejes usando la clase `Scene`. Sin embargo, la clase `Axes` presenta una configuración muy variada que podemos determinar según nuestras preferencias. Específicamente, distinguimos los siguientes parámetros:
- x_range (Sequence[float] | None) – Los (x_min, x_max, x_step) valores de `x-axis`.
- y_range (Sequence[float] | None) – Los (y_min, y_max, y_step) valores de  `y-axis`.
- x_length (float | None) – La longitud de `x-axis`.
- y_length (float | None) – La longitud de `y-axis`.
- axis_config (dict | None) – Los argumuentos `NumberLine` que determinan ambos ejes.
- x_axis_config (dict | None) – Los argumentos `NumberLine` que determinan el `x-axis`.
- y_axis_config (dict | None) – Los argumentos `NumberLine` que determinan el `y-axis`.
- tips (bool) – Si incluir o no las puntas de los ejes.
- kwargs (Any) – Argumentos adicionales que se pasarán a `CoordinateSystem` y `VGroup`.

**Métodos**
| Método            | Descripción                                                  |
|-------------------|--------------------------------------------------------------|
| `coords_to_point`  | Acepta coordenadas de los ejes y devuelve un punto con respecto a la escena. |
| `get_axes`        | Obtiene los ejes.                                             |
| `get_axis_labels`  | Define etiquetas para el eje x y el eje y del gráfico.         |
| `plot_line_graph`  | Dibuja un gráfico de líneas.                                  |
| `point_to_coords`  | Acepta un punto de la escena y devuelve sus coordenadas con respecto a los ejes. |

**Atributos**
| Atributo                | Descripción                                            |
|-------------------------|--------------------------------------------------------|
| `animate`               | Se utiliza para animar la aplicación de cualquier método de `self`. |
| `animation_overrides`   |                                                        |
| `color`                 |                                                        |
| `depth`                 | La profundidad del objeto.                               |
| `fill_color`            | Si hay múltiples colores (para degradado), devuelve el primero. |
| `height`                | La altura del objeto.                                   |
| `n_points_per_curve`    |                                                        |
| `sheen_factor`          |                                                        |
| `stroke_color`          |                                                        |
| `width`                 | El ancho del objeto.                                     |



Dicho esto, es importante entender, en primer lugar, qué son los `NumberLine` y los `VGroup` para, posteriormente, modificar los parámetros según nuestras necesidades específicas.
### \`NumberLine\`
Un `NumberLine`, en el contexto de librería de Manim, como su nombre indica, es un objeto gráfico que representa una línea numérica, generalmente utilizada para ilustrar un rango de valores numéricos en una animación. Este objeto es útil para representar escalas numéricas, marcar puntos específicos en la línea y realizar animaciones relacionadas con la posición de los números.

Por ejemplo, insertemos una lista númerica que vaya desde el número -10 hasta el número 10, pero que solo incluya los números -5, 0 y 5. 
```python
from manim import *
class LíneaNum(Scene):
  def construct(self):

    # establecer la línea numérica

    Línea = NumberLine(x_range=([-10,10]),
                       length=10,
                       color=RED,
                       include_numbers=True,
                       include_tip=True,
                       numbers_to_include=([-5,0,5])
    )

    # añadimos la línea numérica

    self.add(Línea)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/L%C3%ADneaNum.png)

Específicamente, el Mobject `NumberLine` admite los siguientes parámetros:
- x_range (Sequence[float] | None) – Los \[x_min, x_max, x_step\] valores para crear la línea.
- length (float | None) – La longitud de la línea numérica.
- unit_size (float) – La distancia entre cada marca de la línea. Sobrescrito por longitud, si se especifica.
- include_ticks (bool) – Si se deben incluir marcas en la recta numérica.
- tick_size (float) – La longitud de cada marca de graduación.
- numbers_with_elongated_ticks (Iterable[float] | None) – Un iterable de valores específicos con ticks alargados.
- longer_tick_multiple (int) – Influye en cuántas veces más grandes son las marcas alargadas que las marcas normales (2 = 2x).
- rotation (float) – El ángulo (en radianes) en el que se gira la línea
- stroke_width (float) – El grosor de la línea.
- include_tip (bool) – Si se debe agregar una punta al final de la línea.
- tip_width (float) – El ancho de la punta.
- tip_height (float) – La altura de la punta.
- tip_shape (type[ArrowTip] | None) – La clase de Mobject utilizado para construir la punta, o ninguno (the default) para la punta de línea por defecto. Las clases tiene que heredar de ArrowTip.
- include_numbers (bool) – Si se deben agregar números a las marcas. El número de decimales está determinado por el tamaño del step, este valor se determina mediante decimal_number_config.
- scaling (_ScaleBase) – La forma en que se escala el valor de `x_range`, es decir, LogBase para una línea numérica logarítmica. Por defecto, es LinearBase.
- font_size (float) – El tamaño de las etiquetas de los objetos gráficos de texto (labels). Por defecto, es 36.
- label_direction (Sequence[float]) –  La posición específica a la cual se añaden los objetos gráficos de texto (labels) en la línea.
- label_constructor (VMobject) – Determina la clase de objeto gráfico que se utilizará para construir las etiquetas de la línea numérica.
- line_to_number_buff (float) – La distancia entre la línea y los objetos gráficos de texto (labels).
- decimal_number_config (dict | None) – Argumentos que se pueden pasar a `DecimalNumber` para influir en los objetos gráficos de números.
- numbers_to_exclude (Iterable[float] | None) – Un conjunto explícito de números que no se añadirán a la línea numérica.
- numbers_to_include (Iterable[float] | None) – Un conjunto explícito de números que se añadirán a la línea numérica.
- kwargs – Argumentos adicionales que se pasarán a `Line` (la clase que representa la línea en sí).
- exclude_origin_tick (bool) – Si se deben excluir las marcas en la posición cero de la línea numérica.

### \`VGroups\`
En Manim,` VGroup` es una clase que representa un "grupo vectorial" o "grupo de vectores". Es una estructura fundamental utilizada para organizar y manipular conjuntos de objetos gráficos bidimensionales o tridimensionales. Algunas de las características fundamentales de los `VGroup` son:
- **Organización de Objetos**: VGroup organiza los objetos gráficos que contiene. Puedes agregar varios objetos al grupo, y estos se consideran miembros del conjunto.
- **Manipulación Conjunta**: Permite aplicar transformaciones (traslación, rotación, escala, etc.) a todos los objetos dentro del grupo simultáneamente. Esto facilita la manipulación de conjuntos de objetos en una animación.
- **Sintaxis Simple**: La sintaxis para trabajar con VGroup es simple y directa. Puedes crear un grupo y agregar objetos con facilidad.
- **Versatilidad Dimensional**: Aunque el nombre sugiere "vectorial," en Manim VGroup puede contener objetos tanto en dos como en tres dimensiones. Es una estructura versátil que se adapta a las necesidades de la escena.
- **Facilita Animaciones Complejas**: Al agrupar objetos en un VGroup, puedes aplicar animaciones complejas a conjuntos de objetos de manera coherente, simplificando el código y mejorando la claridad.

A modo de ejemplo:
```python
from manim import *
class Vgroups(Scene):
  def construct(self):

    # determinamos los mobjects

    Círculo = Circle(radius=0.5, color=BLUE).set_fill(opacity=0.5, color=GREEN)
    Triángulo = Triangle(color=YELLOW_E).set_fill(opacity=0.5, color=YELLOW)
    Triángulo.next_to(Círculo, LEFT)

    # establecemos el VGroup

    Grupo = VGroup(Círculo, Triángulo)
    self.add(Grupo)
    self.wait()

    # movemos el Grupo

    self.play(Grupo.animate.move_to([3,2,0]), run_time=3)
```
### Gráficos
Para graficar en Manim utilizando `Scene`, en primer lugar, determinamos los `Axes` para, posteriormente, animar la gráfica mediante `Axes.plot`. En este caso, hemos configurado la función x^2:
```python
from manim import *
class Graficando(Scene):
  def construct(self):

    # establecemos los ejes y los configuramos

    Ecuación = MathTex(r"f(x)=x^2").move_to([-4,3,0])

    Ejes = Axes(x_range=([-5,5]), y_range=([-5,5]),
                x_length=10, y_length=5,
                axis_config= {"include_numbers":True, "color":RED
                    
                }
                )
    Etiquetas = Ejes.get_axis_labels(x_label="x", y_label="f(x)")
    Gráfica = Ejes.plot(lambda x: x**2)

    # determinamos las animaciones 
    
    self.play(Write(Ecuación))
    self.play(DrawBorderThenFill(Ejes), time_run=3)
    self.wait()
    self.play(Write(Etiquetas))
    self.play(Create(Gráfica), run_time=3)
    self.wait()
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(83).png)

Utilizamos `lambda` para definir funciones anónimas o funciones sin nombre, que son funciones pequeñas y que contienen una sola expresión. Lambda es muy útil cuando tenemos una función temporal y no queremos definir una función completa utilizando `def`. 

La función `Ejes.plot` toma una función como argumento. Aquí, `lambda x: x**2` se utiliza para crear una función cuadrática de x. Podemos entender la función lambda `x: x**2` como una forma más concisa de escribir:
```python
def cuadratica(x):
    return x**2
```
La función lambda toma una variable x y devuelve x**2. En el contexto de `Ejes.plot`, la función se evalúa para cada valor de x en el rango especificado y crea los puntos que forman la gráfica.
Este es un ejemplo simple de cómo podríamos utilizar `lambda` en Manim para definir y graficar una función lineal:
```python
from manim import *
class FunciónLineal(Scene):
  def construct(self):

    # determinamos los ejesXY

    Ecuación = MathTex(r"e=2^t+3")
    Ejes = Axes(x_range=([-10,10]), y_range=([-10,10]),
                x_length=10, y_length=7,
                axis_config= {"include_numbers":True, "color":GREEN_B, "numbers_to_exclude":[-10,0,-9,8,9]},
                y_axis_config={"include_numbers":False}
                )
    Etiquetas = Ejes.get_axis_labels(x_label="t", y_label="e")
    
    # fijamos la gráfica 2*x+3

    Gráfica = Ejes.plot(lambda x: 2*x+3, color=YELLOW_C )
   
    # establecemos las animaciones
    
    self.play(Write(Ecuación), run_time=3)
    self.play(Ecuación.animate.move_to([-4,3,0]))
    self.wait()

    self.play(Write(Ejes), run_time=2)
    self.play(Write(Etiquetas))
    self.play(DrawBorderThenFill(Gráfica), run_time=3)
    self.wait()
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(82).png)

### Funciones Paramétricas utilizando \`Scene\`
Una función paramétrica es una expresión matemática que describe las coordenadas de un punto en función de uno o más parámetros. En lugar de expresar directamente las coordenadas en términos de una variable independiente, como en las funciones cartesianas tradicionales, las funciones paramétricas utilizan parámetros para definir las posiciones de los puntos en un espacio. Un ejemplo simple podría ser una curva paramétrica en el plano xy, donde las coordenadas x e y se expresan como funciones de un parámetro t.

En Manim, las funciones paramétricas representan visualmente cómo los objetos geométricos evolucionan con respecto a un parámetro dado. Podemos utilizar funciones paramétricas para, por ejemplo:
- **Curvas y Trayectorias**: Las funciones paramétricas son ideales para describir curvas y trayectorias en el espacio. Podemos animar la evolución de estas curvas, mostrando cómo cambian con el tiempo o con algún otro parámetro relevante. Esto es útil para visualizar conceptos matemáticos como el movimiento de un punto a lo largo de una curva.
- **Superficies Paramétricas**: Además de curvas, Manim permite la representación y animación de superficies paramétricas en el espacio tridimensional. Esto es útil para visualizar formas complejas y entender cómo cambian en respuesta a cambios en los parámetros.

A modo de ejemplo, animemos la función seno mediante una función paramétrica que represente la evolución de la curva a través de un parámetro t, es decir:
```python
from manim import *
import numpy
class FunciónParat(Scene):
  def construct(self):


    # función sin(x)

    Ecuación = MathTex(r"f(x)=\sin(x)")
    Ecuación.set_color_by_gradient(TEAL_C, PURPLE_A)


    # determinamos los ejes de coordenadas

    Ejes = Axes(x_range=([-5,5]),
                y_range=([-5,5]),
                x_length=10,
                y_length=7,
                axis_config={"color": TEAL_A, "include_numbers":True 
                    
                },
                y_axis_config={"include_numbers":False}
                
                
                )
    Etiquetas = Ejes.get_axis_labels(x_label="x", y_label="f(x)").set_color_by_gradient(TEAL_C, PURPLE_A)

    # definimos la función sin utilizando lambda

    Gráfica = Ejes.plot_parametric_curve(lambda t:[t, np.sin(t),0], t_range=[-5,5], color=PURPLE)

    #animamos

    self.play(Write(Ecuación), run_time=3)
    self.play(Ecuación.animate.shift(4*LEFT, 2*UP))
    self.wait()

    self.play(Create(Ejes), run_time=2)
    self.play(Write(Etiquetas), run_time=2)
   
    self.play(Create(Gráfica), run_time=6)
    self.wait()
  ```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(84).png)

Para utilizar las funciones y objetos de NumPy es importante importar la librería mediante `import numpy`.
```python
from manim import *
import numpy
```
La funciones paramétricas nos permiten representar curvas complejas, tal es el caso de la siguiente función:
```python
from manim import *
import numpy as np
class Corazón(Scene):
  def construct(self):

    # configuración de ejesXY

    Ejes = Axes(x_range=([-24, 24]),
                y_range=([-20, 15]),
                x_length=10,
                y_length=5,
                axis_config= {"include_numbers":False,
                              "color":BLACK,
                              "include_ticks":False
                              }

                )
    
    # determinar función

    Gráfica = Ejes.plot_parametric_curve(lambda t: [16 * np.sin(t)**3, 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t), 0], t_range=[-np.pi, np.pi], color=RED).set_fill(color=RED, opacity=0.5)
    self.play(Create(Gráfica, run_time=5))
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(85).png)

### Trabajar con dos funciones
En Manim, gracias a las ventajas de la librería, podemos trabajar con múltiples funciones en la pantalla al agregar varias instancias de gráficos o animaciones en la misma escena. A modo de ejemplo:
```python
from manim import *
import numpy as np
class DosFunciones(Scene):
  def construct(self):

    # configuración de las ecuaciones

    Ecuación1 = MathTex(r"y=\sin(x)", color=TEAL).move_to([-3.5,0,0])
    Ecuación2 = MathTex(r"f(x)=x^{2}", color=YELLOW).move_to([4,0,0])
  
    # configuración de los EjesXY

    Ejes1 = Axes(x_range=([0,5]), y_range=([0,5]),
                 x_length=4, y_length=4,
                 axis_config = {"color": YELLOW, "include_numbers":True}
                     )
    Etiquetas1 = Ejes1.get_axis_labels(x_label="x", y_label="f(x)")

    Ejes2 = Axes(x_range=([0,5]), y_range=([0,5]),
                 x_length=4, y_length=4,
                 axis_config = {"color": TEAL_C},
                 x_axis_config = {"numbers_to_include":[np.pi]}

                 )
    Etiquetas2 = Ejes2.get_axis_labels(x_label="X", y_label="Y")

    # determinamos las funciones para cada eje

    Gráfica1 = Ejes1.plot(lambda x: x**2, x_range=[0,10], color=GREEN)
    Gráfica2 = Ejes2.plot_parametric_curve(lambda t: [t, np.cos(t), 0], t_range=[0,4], color=PURPLE_C)

    # creamos los VGroups correspondientes

    VGroup1 = VGroup(Ejes1, Etiquetas1, Gráfica1).shift(3.5*RIGHT)
   
    VGroup2 = VGroup(Ejes2, Etiquetas2, Gráfica2).shift(3*LEFT)

    self.add(VGroup1, VGroup2, Ecuación1, Ecuación2)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/DosFunciones.png)

De igual fornma, podemos trabajar hasta con cuatro funciones en un misma escena. A modo de ejemplo:
```python
from manim import *
import numpy as np
class LOVE(Scene):
  def construct(self):

    # configuración de los textos `Text` y `Tex`

    Texto = Text("All you need is...", t2c={'[8:12]': RED}).shift(3*UP)
    Texto1 = Text("L-O-V-E", t2c={'[1:2]':WHITE, '[3:4]':WHITE, '[5:6]':WHITE}, color=RED, font_size=55).shift(3*DOWN)

    Ecuación1 = MathTex(r"y=\frac{1}{2}")
    Ecuación2 = MathTex(r"x^{2}+y^{2}-9=0")
    Ecuación3 = MathTex(r"y=\mid -2x \mid")
    Ecuación4 = MathTex(r"y=-3\mid siny \mid")

    # fijamos los ejes y sus respectivas funciones

    Ejes1 = Axes(x_range=([-5,3]), y_range=(-3,3),
                 x_length=3, y_length=3,
                 axis_config= {"tip_width":0.2, "tip_height":0.2}
              
                 ).move_to([-5.2,0,0])

    Gráfica1 = Ejes1.plot(lambda x: np.clip(1/x, -3, 3), x_range=[0.1, 3], color=RED)  # Limita los valores de y a un rango de -5 a 5
  
    Ejes2 = Axes(x_range=([-5,5]), y_range=(-5,5),
                 x_length=3, y_length=3,
                 axis_config= {"tip_width":0.2, "tip_height":0.2}
              
                 ).move_to([-1.85,0,0])
    Gráfica2 = Ejes2.plot_implicit_curve(lambda x,y: x**2 + y**2 - 9, color=RED)

    Ejes3 = Axes(x_range=([-5,5]), y_range=(-5,5),
                 x_length=3, y_length=3,
                 axis_config= {"tip_width":0.2, "tip_height":0.2}
              
                 ).move_to([1.65,0,0])
    Gráfico3 = Ejes3.plot(lambda x: np.abs(-2*x), x_range=[-2.5,2.5], color=RED)

    Ejes4 = Axes(x_range=([-5,5]), y_range=(-5,5),
                 x_length=3, y_length=3,
                 axis_config= {"tip_width":0.2, "tip_height":0.2}
              
                 ).move_to([5,0,0])
    Gráfico4 = Ejes4.plot_parametric_curve(lambda t: [t, -3*np.abs(np.sin(t)), 0], t_range=[-6,0], color=RED).rotate(-5/PI)         


    # determinamos las posiciones para los Mobjects
 
    Ecuación1.next_to(Ejes1, UP)
    Ecuación2.next_to(Ejes2, UP)
    Ecuación3.next_to(Ejes3, UP)
    Ecuación4.next_to(Ejes4, UP)

    # creamos los VGroups necesarios 

    VGrupo1 = VGroup(Ecuación1, Ejes1, Gráfica1)
    VGrupo2 = VGroup(Ecuación2, Ejes2, Gráfica2)
    VGrupo3 = VGroup(Ecuación3, Ejes3, Gráfico3)
    VGrupo4 = VGroup(Ecuación4, Ejes4, Gráfico4)
 
    # establecemos las animaciones

    self.play(DrawBorderThenFill(VGrupo1), run_time=4)
    self.wait()
    self.play(DrawBorderThenFill(VGrupo2), run_time=4)
    self.wait()
    self.play(DrawBorderThenFill(VGrupo3), run_time=4)
    self.wait()
    self.play(DrawBorderThenFill(VGrupo4), run_time=4)
    self.wait()
    self.play(Write(Texto), run_time=3)
    self.play(FadeIn(Texto1), run_time=3)
```
### Funciones Implícitas
Una función implícita es aquella en la que la variable dependiente no aparece despejada en la expresión de la ecuación. En Manim, para representar este tipo de funciones utilizamos `ImplicitFunction`, a modo de ejemplo:
```python
from manim import *
import numpy as np
class FunciónImpl(Scene):
  def construct(self):

    Plano = NumberPlane(x_range=([-20,20]))
    self.add(Plano)

    Gráfica = ImplicitFunction(lambda x,y: x * y ** 2 - x ** 2 * y - 2, x_range=([-15,15]), color=YELLOW).set_fill(opacity=0.5, color=ORANGE)


    self.add(Gráfica)

    # gracias por la ayuda Erick! :)
```
>![](https://github.com/BrosReys/ManimCE/blob/Images/Funci%C3%B3n%20impl%C3%ADcita.png)





## \`GraphScene\`
Por otro parte, para graficar funciones también utilizamos la clase `GraphScene`, que es una subclase de `Scene` que proporciona funcionalidades específicas para trabajar con gráficos y funciones matemáticas. Está diseñada para simplificar la creación y animación de gráficos en las escenas.

Concretamente, `GraphScene` incluye métodos y atributos útiles para configurar fácilmente el eje de coordenadas, agregar etiquetas, manejar animaciones específicas de gráficos, entre otros. Podemos heredar de `GraphScene` y personalizar sus métodos para crear nuestras propias escenas con gráficos de funciones. Para importar la clase `GraphScene`:
```python
>>>from manim import GraphScene
>>>class GráficoEx(GraphScene):
```
Una vez hayamos importado de la librería de Manim `GraphScene`, 





[^1]: Como usar LaTeX: https://manualdelatex.com/
[^2]: Vídeo tutorial de posicionamiento: https://www.youtube.com/watch?v=1Fv0Nu-Tb7Q&t=676s
[^3]: Gráfico lineal con `NumberPlane`en la sección '¿Cómo creamos los ejes utilizando \`Scene\`?' 

