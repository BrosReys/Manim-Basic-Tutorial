from manim import *

# Define una clase de escena llamada MyScene
class MyScene(Scene):
    # Método construct donde se define la animación
    def construct(self):

        # Configura los ejes XY
        Ejes = Axes(
            x_range=([0, 10]), y_range=([-1, 15]),
            x_length=10, y_length=5,
            axis_config={"include_tip": False, "color": YELLOW},
            y_axis_config={"include_ticks": False}
        ).move_to([-1, 0, 0])

        # Grafica una función cúbica
        func = Ejes.plot(lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0, 10], color=BLUE)

        # Define una expresión matemática para la derivada
        ecuacion = MathTex(
            r"\frac{d}{dx}f'(x) =", r"\lim_{h \to 0}", r"\frac{f(x + h) - f(x)}{h}"
        ).move_to([-1, 3, 0])

        # Crea rectángulos para resaltar partes de la expresión
        box1 = SurroundingRectangle(ecuacion[0])
        box2 = SurroundingRectangle(ecuacion[1])
        box3 = SurroundingRectangle(ecuacion[2])

        # Value trackers para x y h
        xtracker = ValueTracker(5)
        dx = ValueTracker(4)

        # Crea un grupo de pendiente secante para la visualización
        secante = always_redraw(lambda: Ejes.get_secant_slope_group(
            x=xtracker.get_value(),
            dx=dx.get_value(),
            graph=func,
            dx_label="h",
            dy_label=MathTex("f(x+h)-f(x)").set_scale(0.7),
            secant_line_color=RED
        ))

        # Crea puntos en el gráfico que representan los puntos de interés
        punto1 = always_redraw(
            lambda: Dot(color=GREEN).move_to(Ejes.c2p(xtracker.get_value(), func.underlying_function(xtracker.get_value())))
        )
        punto2 = always_redraw(
            lambda: Dot(color=PURPLE).move_to(Ejes.c2p(xtracker.get_value() + dx.get_value(),
                                                       func.underlying_function(xtracker.get_value() + dx.get_value())))
        )

        # Etiquetas de los ejes
        labels = Ejes.get_axis_labels(x_label="x", y_label="y")

        # Etiqueta de texto
        texto = Text("Derivadas").move_to([-3, 3, 0])

        # Etiquetas para x, x+h, y h
        etiqueta = always_redraw(
            lambda: Ejes.get_T_label(x_val=xtracker.get_value(), graph=func, label="x", line_color=GREEN))
        etiqueta1 = always_redraw(
            lambda: Ejes.get_T_label(x_val=xtracker.get_value() + dx.get_value(), graph=func, label="x+h",
                                     line_color=PURPLE))
        etiqueta3 = always_redraw(
            lambda: Ejes.get_T_label(x_val=xtracker.get_value(), graph=func, label="h=0"))

        # Tracker de variable para h
        variableh = Variable(dx.get_value(), num_decimal_places=3, label=MathTex(r"h")).move_to([0, 2, 0])
        vartracker = variableh.tracker
        var = 0.0001

        # Secuencia de animación
        self.play(DrawBorderThenFill(Ejes), run_time=2)
        self.play(Write(labels))
        self.play(Write(texto))
        self.play(Transform(texto, ecuacion))
        self.wait(2)
        self.play(Create(func))
        self.play(FadeIn(punto1, punto2))
        self.play(FadeIn(etiqueta, etiqueta1, variableh))
        self.play(Create(box1))
        self.play(Create(secante), run_time=2)
        self.play(ReplacementTransform(box1, box3))
        self.play(dx.animate.set_value(0.0001), vartracker.animate.set_value(var), run_time=3)
        self.play(ReplacementTransform(box3, box2))
        self.play(FadeOut(etiqueta, etiqueta1, variableh), FadeIn(etiqueta3))
        self.wait(2)
        self.play(FadeOut(box2))
        self.play(xtracker.animate.set_value(2))
        self.play(xtracker.animate.set_value(6))
        self.wait()
