# ManimCE
### Libreta de código para programar animaciones en ManimCE, para python.

_¿Qué es Manim?_

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




## Manim Objects
### Text and Tex mobjects
En Manim podemos renderizar el texto principalmente de dos formas:
1. Usando **Pango**, que es una biblioteca utilizada para el diseño y dibujo de texto internacional `Text_mobject`.
2. Usando **LaTeX**, que es un sistema de composición de textos especializado para escribrir lenguaje matemático `Tex_mobject`.
### Texto utilizando **_Pango_**

Por ejemplo, la forma más simple de animar un texto no LaTeX es a través del mobject `Text` :
```python
from manim import *
class Ejemplo(Scene):
  def construct(self):
    Texto = Text("Aquí va el texto") # crear el texto
    self.play(Write(Texto)) # animar el texto
    self.wait(1) # esperar un segundo
    self.play(FadeOut(Texto)) # desaparecer el texto
```
![](https://github.com/BrosReys/ManimCE/blob/main/Captura%20de%20pantalla%20(68).png)

Usamos `stant` para especificar el estilo de texto, que puede ser el por defecto `NORMAL`, o bien `ITALIC` y `OBLIQUE`. Por lo general, el estilo `ITALIC` y el `OBLIQUE` lucen igual, sin embargo, el `ITALIC` usa el _**Roman Style**_, mientras que el `OBLIQUE` utiliza el _**Italic Style**_.

**_¿Cómo ponemos color al texto?_**

Podemos poner color a un texto utilizando `color`. También podemos utilizar `t2c`para especificar los caracteres que queremos pintar. Concretamente `t2c` acepta dos formas de escritura:
- Las _keys_ pueden contener índices como `[2:-1]` o `[4:8]`. Los valores deben ser el color del Text de `color`.
- Las _keys_ contienen palabras que deben de ser coloreados por separado y los valores deben de ser el color de `color`.
```python
from manim import *
class Texto(Scene):
  def construct(self):
    Textocolor = Text("Google", t2c={'[0:1]': BLUE,'[1:2]': RED, '[2:3]': YELLOW, '[3:4]': BLUE, '[4:5]': GREEN, '[5:6]': RED}, font_size=144) #establecer texto
    self.play(Write(Textocolor)) # animar el texto
    self.wait(3) # esperar durante tres segundos
```
! 



 

Por otro lado, también podemos insertar ecuaciones matemáticas utilizado el mobject `MathTex`:
```python
from manim import *
class Latex(Scene):
  def construct(self):
    Ecuación = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}") # crear ecuación
    self.play(Create(Ecuación)) # animar ecuación
    self.wait(4) # esperar cuatro segundos
```
![](https://github.com/BrosReys/ManimCE/blob/main/Captura%20de%20pantalla%20(69).png)


