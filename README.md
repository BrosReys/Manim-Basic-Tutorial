# **Manim (Mathematical Animation Engine)**
### Libreta de código para programar animaciones en [Manim](https://www.manim.community/), para python.
## ¿Qué es Manim?

**Manim** es una biblioteca de animación matemática de código abierto, concebida por Grant Sanderson, el creador de la plataforma educativa [3Blue1Brown](https://www.3blue1brown.com/). El nombre "Manim" proviene de "Mathematical Animation Engine". Lo que hace que Manim sea excepcional es su capacidad para permitir a los usuarios crear animaciones interactivas y visualizaciones matemáticas de alta calidad.

La librería se destaca por su versatilidad y su capacidad para simplificar la explicación de conceptos matemáticos complejos. Las animaciones generadas por Manim no solo son estéticamente atractivas, sino que también ofrecen una comprensión más clara y profunda de los temas, pues facilita la enseñanza y el aprendizaje de conceptos matemáticos de manera intuitiva. La flexibilidad de Manim permite a los creadores personalizar y ajustar las animaciones según sus necesidades, convirtiéndolo en una herramienta valiosa para la educación y la divulgación matemática.

### Python y Manim
Manim utiliza [Python](https://www.python.org/) como lenguaje de programación principal. Python es un lenguaje de programación de alto nivel, fácil de aprender y de sintaxis clara, lo que lo hace adecuado para la creación rápida de prototipos y el desarrollo eficiente. Manim se beneficia de las características poderosas de Python y su amplio ecosistema de bibliotecas.

|[Documentación oficial de python](https://docs.python.org/3/)|
|-------------------------------|

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

# Manim Objects (Mobjects)
En Manim (Mathematical Animation Engine), los "Manim Objects" (`Mobjects`) son las entidades fundamentales que representan diferentes elementos que pueden aparecer y animarse en la pantalla durante una animación matemática. Estos objetos abarcan desde formas geométricas simples hasta objetos más complejos como ecuaciones, gráficos, texto, cámaras, luces, etc.
### Métodos de Mobject
| Método | Descripción |
| ------ | ----------- |
| `add` | Agrega mobjects como submobjects. |
| `add_animation_override` | Agrega una anulación de animación. |
| `add_background_rectangle` | Agrega un BackgroundRectangle como submobject. |
| `add_background_rectangle_to_family_members_with_points` | Agrega un BackgroundRectangle a los miembros de la familia con puntos. |
| `add_background_rectangle_to_submobjects` | Agrega un BackgroundRectangle a los submobjects. |
| `add_n_more_submobjects` | Agrega n submobjects adicionales. |
| `add_to_back` | Agrega todos los mobjects proporcionados al fondo de los submobjects. |
| `add_updater` | Agrega una función de actualización a este mobject. |
| `align_data` | Alinea los datos de este mobject con otro mobject. |
| `align_on_border` | La dirección solo necesita ser un vector que apunte hacia un lado o una esquina en el plano 2D. |
| `align_points` | ... |
| `align_points_with_larger` | ... |
| `align_submobjects` | ... |
| `align_to` | Alinea el mobject con otro Mobject en una dirección específica. |
| `animation_override_for` | Devuelve la función que define una anulación de animación específica para esta clase. |
| `apply_complex_function` | Aplica una función compleja a un Mobject. |
| `apply_function` | ... |
| `apply_function_to_position` | ... |
| `apply_function_to_submobject_positions` | ... |
| `apply_matrix` | ... |
| `apply_over_attr_arrays` | ... |
| `apply_points_function_about_point` | ... |
| `apply_to_family` | Aplica una función a este Mobject y a cada submobject con puntos de manera recursiva. |
| `arrange` | Ordena los Mobjects uno al lado del otro en la pantalla. |
| `arrange_in_grid` | Organiza los submobjects en una cuadrícula. |
| `arrange_submobjects` | Organiza la posición de los submobjects con un pequeño margen. |
| `become` | Edita puntos, colores y submobjects para ser idénticos a otro Mobject. |
| `center` | Mueve el centro del mobject al centro de la escena. |
| `clear_updaters` | Elimina todos los actualizadores. |
| `copy` | Crea y devuelve una copia idéntica del Mobject, incluyendo todos los submobjects. |
| `fade` | ... |
| `fade_to` | ... |
| `family_members_with_points` | ... |
| `flip` | Voltea / Refleja un mobject sobre su centro. |
| `generate_points` | Inicializa los puntos y, por lo tanto, la forma. |
| `generate_target` | ... |
| `get_all_points` | Devuelve todos los puntos de este mobject y de todos los submobjects. |
| `get_array_attrs` | ... |
| `get_bottom` | ... |
| `get_boundary_point` | ... |
| `get_center` | ... |
| `get_center_of_mass` | ... |
| `get_color` | Devuelve el color del Mobject. |
| `get_coord` | Destinado a generalizar get_x, get_y y get_z. |
| `get_corner` | ... |
| `get_critical_point` | Imagina una caja que limita el Mobject. |
| `get_edge_center` | ... |
| `get_end` | Devuelve el punto donde el trazo que rodea el Mobject termina. |
| `get_extremum_along_dim` | ... |
| `get_family` | ... |
| `get_family_updaters` | ... |
| `get_group_class` | ... |
| `get_image` | ... |
| `get_left` | ... |
| `get_merged_array` | Devuelve todos los valores de un atributo dado de este mobject y de todos los submobjects. |
| `get_midpoint` | ... |
| `get_mobject_type_class` | Devuelve la clase base de este tipo de mobject. |
| `get_nadir` | ... |
| `get_num_points` | ... |
| `get_pieces` | ... |
| `get_point_mobject` | El mobject más simple para ser transformado hacia o desde este mobject. |
| `get_points_defining_boundary` | ... |
| `get_right` | ... |
| `get_start` | Devuelve el punto donde el trazo que rodea el Mobject comienza. |
| `get_start_and_end` | Devuelve el punto de inicio y el punto final de un trazo como una tupla. |
| `get_time_based_updaters` | Devuelve todos los actualizadores que utilizan el parámetro dt. |
| `get_top` | ... |
| `get_updaters` | Devuelve todos los actualizadores. |
| `get_x` | Devuelve la coordenada x del centro del Mobject como un número decimal. |
| `get_y` | Devuelve la coordenada y del centro del Mobject como un número decimal. |
| `get_z` | Devuelve la coordenada z del centro del Mobject como un número decimal. |
| `get_z_index_reference_point` | ... |
| `get_zenith` | ... |
| `has_no_points` | Verifica si el Mobject no contiene puntos. |
| `has_points` | Verifica si el Mobject contiene puntos. |
| `has_time_based_updater` | Prueba si self tiene un actualizador basado en el tiempo. |
| `init_colors` | Inicializa los colores. |
| `insert` | Inserta un mobject en una posición específica dentro de self.submobjects. |
| `interpolate` | Convierte este Mobject en una interpolación entre mobject1 y mobject2. |
| `interpolate_color` | ... |
| `invert` | Invierte la lista de submobjects. |
| `is_off_screen` | ... |
| `length_over_dim` | Mide la longitud de un Mobject en una dirección específica. |
| `match_color` | Combina el color con el color de otro Mobject. |
| `match_coord` | Combina los Point3Ds con los Point3Ds de otro Mobject. |
| `match_depth` | Combina la profundidad con la profundidad de otro Mobject. |
| `match_dim_size` | Combina la dimensión especificada con la dimensión de otro Mobject. |
| `match_height` | Combina la altura con la altura de otro Mobject. |
| `match_points` | Edita puntos, posiciones y submobjects para ser idénticos a otro Mobject, manteniendo el estilo inalterado. |
| `match_updaters` | Combina los actualizadores del mobject dado. |
| `match_width` | Combina el ancho con el ancho de otro Mobject. |
| `match_x` | Combina la coordenada x. |
| `match_y` | Combina la coordenada y. |
| `match_z` | Combina la coordenada z. |
| `move_to` | Mueve el centro del Mobject a un punto específico. |
| `next_to` | Mueve este Mobject junto a otro Mobject o Point3D. |
| `nonempty_submobjects` | ... |
| `null_point_align` | Si un Mobject con puntos se está alineando con otro sin puntos, trátalos a ambos como grupos y coloca el que tiene puntos en su propia lista de submobjects. |
| `point_from_proportion` | ... |
| `pose_at_angle` | ... |
| `proportion_from_point` | ... |
| `push_self_into_submobjects` | ... |
| `put_start_and_end_on` | ... |
| `reduce_across_dimension` | Encuentra el valor mínimo o máximo de una dimensión entre todos los puntos en este y los submobjects. |
| `remove` | Elimina submobjects. |
| `remove_updater` | Elimina un actualizador. |
| `repeat` | Esto puede hacer que las animaciones de transición sean más agradables. |
| `repeat_submobject` | ... |
| `replace` | ... |
| `rescale_to_fit` | ... |
| `reset_points` | Establece los puntos como un array vacío. |
| `restore` | Restaura el estado que se guardó previamente con save_state(). |
| `resume_updating` | Habilita la actualización desde actualizadores y animaciones. |
| `reverse_points` | ... |
| `rotate` | Rota el Mobject alrededor de un punto específico. |
| `rotate_about_origin` | Rota el Mobject alrededor del ORIGEN, que está en [0,0,0]. |
| `save_image` | Guarda una imagen de solo este Mobject en su posición en un archivo png. |
| `save_state` | Guarda el estado actual (posición, color y tamaño). |
| `scale` | Escala el tamaño por un factor. |
| `scale_to_fit_depth` | Escala el Mobject para que se ajuste a una profundidad manteniendo proporciones de ancho/alto. |
| `scale_to_fit_height` | Escala el Mobject para que se ajuste a una altura manteniendo proporciones de ancho/profundidad. |
| `scale_to_fit_width` | Escala el Mobject para que se ajuste a un ancho manteniendo proporciones de altura/profundidad. |
| `set` | Establece atributos. |
| `set_color` | La condición es una función que toma un argumento (x, y, z). |
| `set_color_by_gradient` | PARÁMETROS COLORS: Los colores a utilizar para el degradado. Úsalo como set_color_by_gradient(RED, BLUE, GREEN). |
| `set_colors_by_radial_gradient` | ... |
| `set_coord` | ... |
| `set_default` | Establece los valores predeterminados de los argumentos de palabras clave. |
| `set_submobject_colors_by_gradient` | ... |
| `set_submobject_colors_by_radial_gradient` | ... |
| `set_x` | Establece el valor x del centro del Mobject (entero o decimal). |
| `set_y` | Establece el valor y del centro del Mobject (entero o decimal). |
| `set_z` | Establece el valor z del centro del Mobject (entero o decimal). |
| `set_z_index` | Establece el z_index del Mobject en el valor especificado en z_index_value. |
| `set_z_index_by_z_Point3D` | Establece el z Point3D del Mobject en el valor de z_index. |
| `shift` | Desplaza según los vectores proporcionados. |
| `shift_onto_screen` | ... |
| `show` | ... |
| `shuffle` | Baraja la lista de submobjects. |
| `shuffle_submobjects` | Baraja el orden de los submobjects. |
| `sort` | Ordena la lista de submobjects mediante una función definida por submob_func. |
| `sort_submobjects` | Ordena los submobjects. |
| `space_out_submobjects` | ... |
| `split` | ... |
| `stretch` | ... |
| `stretch_about_point` | ... |
| `stretch_to_fit_depth` | Estira el Mobject para que se ajuste a una profundidad sin mantener proporciones de ancho/alto. |
| `stretch_to_fit_height` | Estira el Mobject para que se ajuste a una altura sin mantener proporciones de ancho/profundidad. |
| `stretch_to_fit_width` | Estira el Mobject para que se ajuste a un ancho sin mantener proporciones de altura/profundidad. |
| `surround` | ... |
| `suspend_updating` | Deshabilita la actualización desde actualizadores y animaciones. |
| `throw_error_if_no_points` | ... |
| `to_corner` | ... |
| `to_edge` | ... |
| `to_original_color` | ... |
| `update` | Aplica todos los actualizadores. |
| `wag` | ... |

### Atributos de Mobject

| Atributo | Descripción |
| -------- | ----------- |
| `animate` | Se utiliza para animar la aplicación de cualquier método de self. |
| `animation_overrides` | ... |
| `depth` | La profundidad del mobject. |
| `height` | La altura del mobject. |
| `width` | El ancho del mobject.|

### ¿Qué son los métodos, los parámetros y los atributos?
**Parámetro**
- **Definición**: Un parámetro es una variable que se utiliza en la declaración de una función o método para recibir valores durante su llamada. Los parámetros son utilizados para permitir la flexibilidad y personalización de una función.
- **Ejemplo**:
```python
def suma(a, b):
    return a + b
```
En este caso, `a y b` son parámetros de la función `suma`.

**Métodos**
- **Definición**: Un método es una función asociada a un objeto o clase. Los métodos definen el comportamiento de un objeto y pueden realizar acciones específicas o devolver información sobre el objeto.
- **Ejemplo**:
```python
class Persona:
    def saludar(self):
        print("Hola, soy una persona.")
```
En este ejemplo, `saludar` es un método de la clase `Persona`.

**Atributos**
- **Definición**: Un atributo es una propiedad o característica de un objeto. Los atributos almacenan información sobre el estado de un objeto y pueden ser accedidos o modificados.
- **Ejemplo**:
```python
class Coche:
    def __init__(self, marca):
        self.marca = marca
```
Aquí, `marca` es un atributo de la clase `Coche`.

**¿Qué relación existe entre ellos?**
1. **Parámetros y Métodos**: Los parámetros se utilizan para pasar información a un método durante su llamada. Los métodos son funciones que pueden usar estos parámetros para realizar tareas específicas.
2. **Atributos y Métodos**: Los métodos pueden acceder y manipular los atributos de un objeto. Los atributos representan las características del objeto y son utilizados por los métodos para realizar acciones.

En resumen, los parámetros permiten la personalización de funciones, los métodos definen el comportamiento de un objeto y los atributos representan propiedades del objeto. Estos conceptos son fundamentales en la programación orientada a objetos y se utilizan para modelar y organizar el código de manera eficiente.

## Text and Tex mobjects
En Manim podemos renderizar el texto principalmente de dos formas:
1. Usando **Pango**, que es una biblioteca utilizada para el diseño y dibujo de texto internacional `Text_mobject`.
2. Usando **LaTeX**, que es un sistema de composición de textos especializado para escribrir lenguaje matemático `Tex_mobject`.
### Distintos tipo de \`text_mobject\` 
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

### \`MathTex\`
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
# Actualizadores, Variables y \`ValueTracker\`
En Manim, las variables, actualizadores y `ValueTracker` son herramientas poderosas que permiten realizar animaciones dinámicas y seguir el cambio de valores a lo largo del tiempo.
## Variables
Usamos la clase `Variable` en Manim, perteneciente al módulo `manim.mobject.text.numbers`, para mostrar un texto que representa una variable con su respectivo valor. La clase está diseñada para mostrar "label = value", donde el valor se actualiza continuamente desde un `ValueTracker`.
### Usos de la clase \`Variable\`
- Utilizamos las variables en Manim para almacenar valores que pueden cambiar durante una animación.
- Pueden ser variables simples como números o incluso objetos más complejos como vectores.
- Manim ofrece la clase `ValueTracker` que es comúnmente utilizada para seguir y animar el cambio de valores a lo largo del tiempo.

A modo de ejemplo, analicemos las siguientes líneas de código:
```python
from manim import *
class Variables(Scene):
  def construct(self):
    # creamos una variable llamada `var` con un valor inicial de 1.5
    var = 1.5

    variable = Variable(var, MathTex(r" \alpha "), num_decimal_places=3).move_to([0,0,0])
    # la clase `Variable` se utiliza para mostrar el valor inicial

    variable.label.set_color(BLUE) # determinamos el color de la etiqueta
    tracker = variable.tracker # establecemos un `ValueTracker`
    var = 10
    # `var` muestra el valor final

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
- El tracker es un `ValueTracker` asociado a la variable. Podemos utilizarlo para animar el cambio del valor de la variable.

3. **Cambiar el valor de la variable**
```python
    var = 10
```
- Aquí se cambiamos el valor de la variable original `var`. Sin embargo, esto no afecta directamente a lo que se muestra en la pantalla.

**Atributos para la clase \`Variable\`**
| Atributo                | Descripción                                            |
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

## Actualizadores
En Manim, los "actualizadores" (updaters en inglés) son funciones que se aplican a un objeto Mobject en cada cuadro (frame) cuando se renderiza una animación. Estas funciones permiten modificar dinámicamente las propiedades de un objeto a lo largo del tiempo, lo que es fundamental para crear animaciones fluidas y complejas.
>[!Important]
> Los actualizadores son funciones especiales que se utilizan para actualizar dinámicamente ciertos objetos en la escena en función de un valor rastreado por un `ValueTracker`.

Por ejemplo, el actualizador `always_redraw` se utiliza para indicar que el objeto debe volver a dibujarse en cada fotograma, incluso si no ha cambiado explícitamente. 

Esto es útil para objetos que dependen de valores rastreados y deben actualizarse constantemente, es decir:
```python
from manim import * 
class Test(Scene):
    def construct(self):

        lado = ValueTracker(4) # determinamos un `ValueTracker` con un valor inicial de 4

        # creamos un cuadrado utilizando `always_redraw`
        #establecemos el `color` y `side_length` del cuadrado

        cuadrado = always_redraw(lambda: Square(color=RED, side_length=lado.get_value()).set_fill(opacity=0.5, color=PINK))

        # añadimos el cuadrado a la escena
        # cambiamos el valor de `lado` a 2

        self.add(cuadrado)
        self.play(lado.animate.set_value(2), run_time=2)
```
Las líneas de código mencionadas previamente establecen un `ValueTracker` denominado "lado" que determina el `side_length` del cuadrado y que se actualizará progresivamente gracias al actualizador `always_redraw`. Esto es:
1. Creamos el `ValueTracker`
```python
lado = ValueTracker(4) # determinamos un `ValueTracker` con un valor inicial de 4
```
2. Determinamos el actualizador `always_redraw`
```python
cuadrado = always_redraw(lambda: Square(color=RED, side_length=lado.get_value()).set_fill(opacity=0.5, color=PINK))
```
3. Cambiamos el valor de `lado` a 2
```python
self.add(cuadrado)
        self.play(lado.animate.set_value(2), run_time=2)
   ```
### \`add_updater\`
Aparte de `alwways_redraw`, existen otros actualizadores importantes como el método `add_updater` que pertenece a la clase `Mobject` y se utiliza para agregar funciones de actualización a un objeto.

La sintaxis para utilizar `add_updater` es la siguiente:
```python
Mobject.add_updater(update_function)
```
- **Mobject**: El objeto al que se le desea agregar la función de actualización.
- **update_function**: La función de actualización que se aplicará al objeto en cada cuadro.

Concretamente, distinguimos dos variantes del método `add_updater`:

**DtUpdater**
```python
from manim import *
class Updaters(Scene):
    def construct(self):
       
       triangulo = Triangle(color=GREEN).set_fill(opacity=0.5, color=YELLOW)
       # creamos un Mobject

       triangulo.add_updater(lambda mobject, dt: mobject.rotate(np.pi / 2))
       # establecemos el actualizador

       self.add(triangulo) # añadimos el triangulo a la escena
       self.wait(2) # esperamos 2 segundos
```
Para entender como funciona `DtUpdater`, analicemos las líneas de código:
1. **Creación del triángulo**
```python
triangulo = Triangle(color=GREEN).set_fill(opacity=0.5, color=YELLOW)
```
- Aquí creamos un triángulo con color verde (GREEN) y relleno amarillo (YELLOW) con una opacidad del 50%.
2. **Añadir actualizador**
```python
triangulo.add_updater(lambda mobject, dt: mobject.rotate(np.pi / 2))
```
- Añadimos un actualizador al triángulo utilizando una función `lambda`. La función de actualización toma el triángulo y el tiempo transcurrido (dt) como parámetros y rota el triángulo en sentido antihorario en un ángulo de π/2 en cada cuadro.
3. **Añadir el triángulo a la escena y esperar**
```python
self.add(triangulo)
self.wait(2)
```
- Añadimos el Mobject a la escena y la animación espera durante 2 segundos.

**NextToUpdater**
```python
from manim import *
class Updater(Scene):
    def construct(self):

        # determinamos el punto (Mobject) y la etiqueta (DecimalNumber)

        Punto = Dot(3*RIGHT, color=GREEN)
        etiqueta = DecimalNumber(color=GREEN)

        # fijamos a la etiqueta la función updater

        etiqueta.add_updater(lambda m: m.set_value(Punto.get_center()[0]).next_to(Punto))

        self.add(etiqueta, Punto) 
        # añadimos el punto y la etiqueta

        # establecemos una rotación completa

        self.play(Rotating(Punto, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))
        self.wait(2)
```
**Análisis del código**
1. Creamos un punto (Punto) usando la clase `Dot`. El punto se coloca en la posición 3 unidades a la derecha del origen `(3*RIGHT)` y se le asigna el color verde `(color=GREEN)`.
2. Creamos una etiqueta (etiqueta) usando la clase `DecimalNumber` y se le asigna el color verde.
3. Añadimos una función updater a la etiqueta utilizando `add_updater`. La función lambda dentro de `add_updater` actualiza la etiqueta para que su valor sea igual a la coordenada x del centro del punto (Punto) y se coloca junto al punto.
4. Añadimos el punto y la etiqueta a la escena usando `self.add(etiqueta, Punto)`.
5. Ejecutamos una animación de rotación completa `(angle=TAU)` alrededor del origen `(about_point=ORIGIN)` para el punto `(Punto)`. La animación se realiza en un tiempo igual a 2π segundos `(run_time=TAU)`, y la función de tasa `(rate_func)` se establece como lineal.
6. Esperamos 2 segundos después de la animación utilizando `self.wait(2)`.

>[!Important]
>`TAU` es una constante matemática que representa la relación entre la circunferencia de un círculo y su radio, de manera similar a la constante π (pi). La constante TAU se define como 
2π, lo que significa que es aproximadamente igual a 6.28318.

En el código mencionado anteriormente `angle=TAU` en la función `Rotating` significa que estamos rotando el objeto (en este caso, el punto `dot`) alrededor del origen en un ángulo igual a 
2π radianes, que es equivalente a una vuelta completa alrededor del círculo.
 
## \`ValueTracker\`
En Manim, ValueTracker es una clase que se utiliza para realizar un seguimiento de parámetros en tiempo real, especialmente para animar cambios en esos parámetros. No está destinado a ser visualizado directamente; en cambio, su posición o valor se utiliza para representar un número que puede ser utilizado por otras animaciones o actualizaciones continuas.

La principal utilidad de ValueTracker es permitir animar su valor con la sintaxis de animación de Manim, y luego utilizar ese valor para controlar otras animaciones o actualizaciones en la escena. Puedes pensar en ValueTracker como un objeto que "rastrea" o "sigue" un valor particular a medida que cambia con el tiempo.

**Puntos importantes**:
- `ValueTracker` es una clase en Manim que realiza un seguimiento de un valor numérico a lo largo de una animación.
- Permite vincular ese valor a propiedades de objetos gráficos, de modo que, cuando el valor cambia, los objetos gráficos se actualizan automáticamente.
- Facilita la creación de animaciones que responden a cambios en variables específicas.
- Se utiliza junto con la clase `DecimalNumber` para mostrar el valor actualizado en la pantalla.

A modo de ejemplo:
```python
from manim import *
class Rastreadores(Scene):
  def construct(self):

    rastreador = ValueTracker(4)
    # establecemos un `ValueTracker`

    cuadrado = always_redraw(lambda: Square(side_length=rastreador.get_value(), color=RED).set_fill(opacity=0.5, color=PINK))
    # creamos un cuadrado utilizando `always_redraw`

    # añadimos el cuadrado
    # cambiando el valor de `rastreador` a 2
    
    self.add(cuadrado)
    self.play(rastreador.animate.set_value(2), run_time=3)
    self.wait()
```
**Análisis del código**
1. Se crea un `ValueTracker` llamado rastreador con un valor inicial de 4.
2. Se utiliza `always_redraw` para crear un cuadrado que tiene su lado vinculado al valor del `ValueTracker`. La función lambda dentro de `always_redraw` garantiza que el cuadrado se vuelva a dibujar en cada cuadro de la animación, actualizando así su tamaño a medida que el valor del `ValueTracker` cambia. El cuadrado también se colorea con RED y se rellena con un 50% de opacidad y color PINK.
3. El cuadrado se añade a la escena usando `self.add(cuadrado)`.
4. Se anima el `ValueTracker` para cambiar su valor a 2 en un lapso de 3 segundos utilizando `self.play(rastreador.animate.set_value(2), run_time=3)`.
5. La función `self.wait()` se utiliza para esperar hasta que la animación termine.
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

## \`Braces\`
En Manim, `Brace` es la clase que se utiliza para referirse a los corchetes curvados ("llaves") que se utilizan para señalar o resaltar partes específicas de una escena o gráfico. Estos corchetes pueden ser utilizados para indicar ecuaciones, intervalos, o cualquier otra información relevante en una animación matemática.

Podemos crear braces utilizando la clase `Brace`. Este es un ejemplo simple de cómo podríamos utilizar los braces:
```python
from manim import *
class Llaves(Scene):
    def construct(self):
        
        # determinamos los mobjects 
        cuadrado = Square(color=BLUE, side_length=3).set_fill(opacity=0.5, color=BLUE)
        llave = Brace(cuadrado, RIGHT)
        texto = llave.get_tex("3cm").set_color(BLUE)
        # texto para la llave
        
        Grupo = VGroup(cuadrado, llave) # creamos un VGroup
        self.add(cuadrado, llave, texto) # añadimos los mobjects a la escena
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Llavesbasic_ManimCE_v0.18.0.png)

Dentro de los distintos tipos de "braces" distinguimos además, algunas variaciones, tal es el caso de `ArcBrace`: una clase que representa una llave formada por un arco, es decir:
```python
from manim import *
import numpy as np
class Llaves(Scene):
    def construct(self):
        

        # determinamos los mobjects 
        círculo = Circle(color=ORANGE, radius=2).set_fill(opacity=0.5, color=ORANGE)
        linea = Line(start=[2,0,0], end=[-2,0,0], color=PURPLE)

        # establecemos un arco
        arco = Arc(radius=np.pi/2, start_angle=0, angle=PI) # creamos el `Arc`
        
        llavearco = ArcBrace(arc=arco, color=PURPLE) # creamos el `ArcBrace`
        texto = llavearco.get_tex("\pi/Rad") # añadimos un texto
        
        Grupo = VGroup(círculo, llavearco, texto, linea) # creamos un VGroup
        self.add(Grupo) # añadimos los mobjects a la escena
```
![](https://github.com/BrosReys/ManimCE/blob/Images/Llaves_ManimCE_v0.18.0.png)

**Métodos**
| Método           | Descripción                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| `get_direction`  | Utiliza `shoelace_direction()` para calcular la dirección.                                   |
| `get_tex`        | Obtiene un objeto `Tex` (objeto de texto LaTeX) asociado al `ArcBrace`.                      |
| `get_text`       | Similar a `get_tex`, obtiene un objeto `Text` asociado al `ArcBrace`.                         |
| `get_tip`        | Obtiene un objeto `ArrowTip` asociado al extremo de la llave (`ArcBrace`).                  |
| `put_at_tip`     | Coloca el objeto pasado como argumento en el extremo de la llave (`ArcBrace`).               |

**Atributos**
| Atributo              | Descripción                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| `animate`             | Se utiliza para animar la aplicación de cualquier método de sí mismo.                          |
| `animation_overrides` | Overrides de animación.                                                                       |
| `color`               | Color de la mobject.                                                                          |
| `depth`               | La profundidad de la mobject.                                                                 |
| `fill_color`          | Si hay varios colores (para degradado), esto devuelve el primero.                               |
| `height`              | La altura de la mobject.                                                                      |
| `n_points_per_curve`  | Número de puntos por curva.                                                                   |
| `sheen_factor`        | Factor de brillo.                                                                             |
| `stroke_color`        | Color del trazo de la mobject.                                                                |
| `width`               | El ancho de la mobject.                                                                      |

# Gráficos y Funciones
La librería de **Manim** nos ofrece distintas formas de implementar gráficos y funciones en nuestras animaciones. Hasta ahora hemos trabajado con la clase `Scene`, no obstante, existen diversas clases tales como `GraphScene`, `ThreeDScene`, entre otras que pueden facilitarnos la tarea de graficar. Concretamente, para representar gráficos utilizamos fundamentalmente `Scene`, `ThreeDScene` y `GraphScene`.
## \`Scene\` y \`Axes\`
Cuando utilizamos la clase `Scene` para realizar gráficos, trabajamos en un nivel más general y flexible, pues tenemos el control total sobre la creación y animación de elementos en la escena, pero también necesitamos definir manualmente los ejes y configurar los gráficos. Por otro lado, es posible que necesitemos importar bibliotecas específicas para funciones matemáticas y gráficos, como NumPy, y definir funciones que describan nuestros gráficos.

De la misma forma, trabajar con `Axes`, que es una subclase de `CoordinateSystem`, proporciona funcionalidades específicas para la creación de ejes cartesianos. Es especialmente útil para crear gráficos de funciones matemáticas, dado que incluye métodos convenientes para agregar etiquetas a los ejes, dibujar gráficos de funciones, trazar puntos y realizar otras operaciones comunes asociadas con sistemas de coordenadas cartesianas.
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

Asímismo, lo siguientes métodos y atributos:

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

Por otro lado, `CoordinateSystem` , es más general y nos permite definir sistemas de coordenadas personalizados, pero a expensas de la simplicidad y las funciones integradas que `Axes` ofrece para tareas comunes. La elección entre ellas dependerá de tus necesidades y de cuánta flexibilidad estés buscando en tu animación. Distinguimos los siguientes métodos:

**Métodos**
| Método                        | Descripción                                                  |
|-------------------------------|--------------------------------------------------------------|
| `add_coordinates`             | Agrega etiquetas a los ejes                                   |
| `angle_of_tangent`            | Devuelve el ángulo con respecto al eje x de la tangente a la curva trazada en un valor particular de x |
| `c2p`                         | Abreviatura de `coords_to_point()`                            |
| `coords_to_point`             | Convierte coordenadas en puntos con respecto a la escena      |
| `get_T_label`                 | Crea un marcador de triángulo etiquetado con una línea vertical desde el eje x hasta una curva en un valor de x dado |
| `get_area`                    | Devuelve un polígono que representa el área bajo el gráfico pasado |
| `get_axes`                    | Obtiene los ejes                                             |
| `get_axis`                    | Obtiene un eje específico                                    |
| `get_axis_labels`             | Define etiquetas para el eje x y el eje y del gráfico         |
| `get_graph_label`             | Crea una etiqueta correctamente posicionada para el gráfico pasado, con un punto opcional |
| `get_horizontal_line`         | Una línea horizontal desde el eje y hasta un punto dado en la escena |
| `get_line_from_axis_to_point` | Devuelve una línea recta desde un eje dado hasta un punto en la escena |
| `get_lines_to_point`          | Genera líneas horizontales y verticales desde el eje hasta un punto |
| `get_origin`                  | Obtiene el origen de los ejes                                |
| `get_riemann_rectangles`      | Genera un VGroup de los rectángulos de Riemann para una curva dada |
| `get_secant_slope_group`      | Crea dos líneas que representan dx y df, las etiquetas para dx y df, y |
| `get_vertical_line`           | Una línea vertical desde el eje x hasta un punto dado en la escena |
| `get_vertical_lines_to_graph` | Obtiene múltiples líneas desde el eje x hasta la curva         |
| `get_x_axis`                  | Obtiene el eje x                                             |
| `get_x_axis_label`            | Genera una etiqueta para el eje x                             |
| `get_x_unit_size`             | Obtiene el tamaño de la unidad en el eje x                    |
| `get_y_axis`                  | Obtiene el eje y                                             |
| `get_y_axis_label`            | Genera una etiqueta para el eje y                             |
| `get_y_unit_size`             | Obtiene el tamaño de la unidad en el eje y                    |
| `get_z_axis`                  | Obtiene el eje z                                             |
| `i2gc`                        | Alias para `input_to_graph_coords()`                          |
| `i2gp`                        | Alias para `input_to_graph_point()`                           |
| `input_to_graph_coords`       | Devuelve una tupla de las coordenadas relativas al eje del punto en el gráfico basado en el valor de x dado |
| `input_to_graph_point`        | Devuelve las coordenadas del punto en un gráfico correspondientes a un valor de x |
| `p2c`                         | Abreviatura de `point_to_coords()`                            |
| `plot`                        | Genera una curva basada en una función                        |
| `plot_antiderivative_graph`   | Trama el gráfico de una antiderivada                         |
| `plot_derivative_graph`       | Devuelve la curva de la derivada del gráfico pasado          |
| `plot_implicit_curve`         | Crea las curvas de una función implícita                      |
| `plot_parametric_curve`       | Una curva paramétrica                                        |
| `plot_polar_graph`            | Un gráfico polar                                            |
| `plot_surface`                | Genera una superficie basada en una función                   |
| `point_to_coords`             | Convierte un punto en coordenadas                             |
| `point_to_polar`              | Obtiene coordenadas polares a partir de un punto              |
| `polar_to_point`              | Obtiene un punto a partir de coordenadas polares              |
| `pr2pt`                       | Abreviatura de `polar_to_point()`                            |
| `pt2pr`                       | Abreviatura de `point_to_polar()`                            |
| `slope_of_tangent`            | Devuelve la pendiente de la tangente a la curva trazada en un valor particular de x |

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
## Gráficos
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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(82).png)

### \`LineGraph\`
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

## Funciones
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
>![](https://github.com/BrosReys/ManimCE/blob/Images/Captura%20de%20pantalla%20(85).png)

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

## Coordenadas y Funciones polares
El plano polar es un sistema de coordenadas en el que los puntos se representan mediante su distancia al origen (radio) y el ángulo entre la línea que los conecta al origen y el eje x (ángulo polar). Manim proporciona la clase `PolarPlane` para trabajar con representaciones visuales de sistemas de coordenadas polares.

**Parámetros para `PolarPlane`**
- **azimuth_step (float | None):** Número de divisiones en el azimut (ángulo polar). Si es `None`, se usará el valor predeterminado especificado por `azimuth_units`. Valores no enteros resultarán en una división parcial al final del círculo.
- **size (float | None):** Diámetro del plano polar.
- **radius_step (float):** Distancia entre las líneas de radio atenuadas.
- **radius_max (float):** Valor máximo del radio.
- **azimuth_units (str | None):** Sistema de etiquetado predeterminado para el azimut. Opciones incluyen "PI radians", "TAU radians", "degrees", "gradians" o `None`.
- **azimuth_compact_fraction (bool):** Si el sistema de etiquetado del azimut tiene etiquetas fraccionarias, elige si combinar la constante en una forma compacta (por ejemplo, 2π) en lugar de mostrarla por separado.
- **azimuth_offset (float):** Desplazamiento angular del azimut, expresado en radianes.
- **azimuth_direction (str):** Dirección del azimut, "CW" (sentido horario) o "CCW" (sentido antihorario).
- **azimuth_label_buff (float):** Espacio adicional para las etiquetas del azimut.
- **azimuth_label_font_size (float):** Tamaño de fuente de las etiquetas del azimut.
- **radius_config (dict[str, Any] | None):** Configuración del eje para el radio.
- **background_line_style (dict[str, Any] | None):** Estilo de línea para las líneas de fondo.
- **faded_line_style (dict[str, Any] | None):** Estilo de línea para las líneas atenuadas.
- **faded_line_ratio (int):** Relación de atenuación de las líneas.
- **make_smooth_after_applying_functions (bool):** Indica si suavizar después de aplicar funciones.
- **kwargs (Any):** Argumentos adicionales.

>[!Important]
>El azimut es un concepto utilizado en geometría y navegación que se refiere a la medida del ángulo en el plano horizontal entre un punto de referencia (generalmente el norte) y una dirección específica, medida en sentido horario. En términos más sencillos, el azimut proporciona la dirección de un objeto en relación con el norte en un plano horizontal.
>En el contexto de Manim y gráficos polares, el azimut puede referirse al ángulo polar en coordenadas polares, donde se mide en relación con el eje horizontal en sentido horario. En este caso, el azimut es una medida angular que se utiliza para especificar la dirección de una línea o vector en el plano polar.

Consecuentemente podemos importar el plano polar mediante `PolarPlane`, es decir:
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

Podemos personalizar el plano polar según nuestras necesidades, ajustando atributos como `background_line_style`, `radius`, `azimuth_angle`, etc. Además, podemos agregar funciones polares y objetos al plano, similar a cómo lo haríamos en un plano cartesiano.

Concretamente distinguimos los siguientes métodos y atributos:

**Métodos**
| Método                          | Descripción                                                                   |
|---------------------------------|-------------------------------------------------------------------------------|
| `add_coordinates`               | Agrega las coordenadas al plano polar.                                        |
| `get_axes`                      | Obtiene los ejes del plano polar.                                             |
| `get_coordinate_labels`         | Obtiene las etiquetas de las coordenadas.                                     |
| `get_radian_label`              | Obtiene la etiqueta en radianes para el azimut.                               |
| `get_vector`                    | Obtiene el vector que representa el azimut y el radio en un punto específico. |
| `prepare_for_nonlinear_transform`| Prepara para una transformación no lineal.                                    |

**Atributos**
| Atributo               | Descripción                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| `animate`              | Se utiliza para animar la aplicación de cualquier método del propio objeto.    |
| `animation_overrides`  | Configuraciones adicionales para anulación de animaciones.                     |
| `color`                | Color del objeto.                                                               |
| `depth`                | Profundidad del objeto en la escena.                                           |
| `fill_color`           | Si hay múltiples colores (para degradado), devuelve el primero.                 |
| `height`               | Altura del objeto.                                                             |
| `n_points_per_curve`   | Número de puntos por curva para representar el objeto.                         |
| `sheen_factor`         | Factor de brillo para efectos de brillo.                                       |
| `stroke_color`         | Color del contorno del objeto.                                                 |
| `width`                | Ancho del objeto.                                                              |

### ¿Cómo importamos un función polar?
La notación general para una función polar es r=f(θ), donde r es la distancia al origen y θ es el ángulo polar. 

Analicemos las siguientes líneas de código:
```python
# Importamos las clases necesarias de Manim y NumPy
from manim import *
import numpy as np

# Definimos una clase llamada FuncPolar que hereda de la clase Scene
class FuncPolar(Scene):
    # Método para construir la escena
    def construct(self):
        # Creamos una instancia de un plano polar con un radio máximo de 3
        Ejes = PolarPlane(radius_max=3)
        # Añadimos las coordenadas al plano polar
        Ejes.add_coordinates()

        # Definimos una función lambda y graficamos la función polar
        f = Ejes.plot_polar_graph(lambda theta: 2 * np.sin(theta * 5), color=RED)

        # Añadimos el plano polar y la función a la escena
        self.add(Ejes, f)

        # Esperamos 2 segundos antes de finalizar la escena
        self.wait(2)

```
- `lambda theta: 2 * np.sin(theta * 5)`: Aquí se utiliza una expresión lambda para definir una función anónima que toma un parámetro theta y devuelve el valor de la función polar **r=2sin(5θ)**. La estructura general de una función lambda es lambda parámetro: expresión. En este caso, el parámetro es theta y la expresión es **2 * np.sin(theta * 5)**.
- `f = Ejes.plot_polar_graph(...)`: Luego, la función lambda se pasa como argumento al método `plot_polar_graph` del objeto `Ejes` (un plano polar), que se encarga de graficar la función polar. El resultado de esta operación se asigna a la variable f.
  
>![](https://github.com/BrosReys/ManimCE/blob/Images/FuncPolar_ManimCE_v0.18.0.png)





[^1]: Como usar LaTeX: https://manualdelatex.com/
[^2]: Vídeo tutorial de posicionamiento: https://www.youtube.com/watch?v=1Fv0Nu-Tb7Q&t=676s
[^3]: Gráfico lineal con `NumberPlane`en la sección '¿Cómo creamos los ejes utilizando \`Scene\`?' 

