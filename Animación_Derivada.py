from manim import *
import numpy as np 
class MyScene(Scene):
    def construct(self):

        # establecer los EjesXY

        Ejes = Axes(x_range=([0,10]), y_range=([-1,15]),
                    x_length=10, y_length=5,
                    axis_config = {"include_tip": False, "color": YELLOW},
                    y_axis_config={"include_ticks":False}
                    ).move_to([-1,0,0])

        func = Ejes.plot(lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0,10], color=BLUE)
        
        ecuacion = MathTex(r"\frac{d}{dx}f'(x) =", r"\lim_{h \to 0}", r"\frac{f(x + h) - f(x)}{h}").move_to([-1, 3, 0])

        box1 = SurroundingRectangle(ecuacion[0])
        box2 = SurroundingRectangle(ecuacion[1])
        box3 = SurroundingRectangle(ecuacion[2])

        xtracker = ValueTracker(5)
        dx = ValueTracker(4)

        secante = always_redraw(lambda: Ejes.get_secant_slope_group(x=xtracker.get_value(),
                                                                    dx=dx.get_value(),
                                                                    graph=func,
                                                                    dx_label="h",
                                                                    dy_label=MathTex("f(x+h)-f(x)").set_scale(0.7),
                                                                    secant_line_color=RED
                                                                    ))

        punto1 = always_redraw(lambda: Dot(color=GREEN).move_to(Ejes.c2p(xtracker.get_value(), func.underlying_function(xtracker.get_value()))))
        punto2 = always_redraw(lambda: Dot(color=PURPLE).move_to(Ejes.c2p(xtracker.get_value() + dx.get_value(), func.underlying_function(xtracker.get_value() + dx.get_value()))))
        
        labels = Ejes.get_axis_labels(x_label="x", y_label="y")

        texto = Text("Derivadas").move_to([-3,3,0])

        etiqueta = always_redraw(lambda: Ejes.get_T_label(x_val=xtracker.get_value(), graph=func, label="x", line_color=GREEN))
        etiqueta1 = always_redraw(lambda: Ejes.get_T_label(x_val=xtracker.get_value() + dx.get_value(), graph=func, label="x+h", line_color=PURPLE))    
        etiqueta3 = always_redraw(lambda: Ejes.get_T_label(x_val=xtracker.get_value(), graph=func, label="h=0"))
        
       
        variableh = Variable(dx.get_value(), num_decimal_places=3, label=MathTex(r"h")).move_to([0,2,0])


        vartracker = variableh.tracker
        var = 0.0001

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
