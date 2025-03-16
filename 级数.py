from manim import *
import numpy as np


class Test(Scene):
    def construct(self):
        text = Text('要求')
        text2 = Text('的值')
        original_sum = MathTex(r"\sum_{n=0}^{\infty} (n+1)\left(\frac{1}{2}\right)^n")
        
        # 使用VGroup将text和original_sum组合在一起
        combined = VGroup(text, original_sum, text2)
        
        # 使用arrange方法将它们排列
        combined.arrange(RIGHT)
        
        self.play(Write(combined))
        self.wait(2)
         # 删除text和text2
        self.play(FadeOut(text), FadeOut(text2))
        self.wait(1)
        # 将original_sum移动到左上角
        self.play(original_sum.animate.to_edge(UL))
        self.wait(1)

        text3 = Text('只需求幂级数：')
        sum2 = MathTex(r"\sum_{n=0}^{\infty} (n+1)x^n")
        
        # 使用VGroup将text和original_sum组合在一起
        combined2 = VGroup(text3, sum2)
        combined2.arrange(RIGHT)
        self.play(Write(combined2))
        self.wait(2)
        # 将combined2整体往上移动一点
        self.play(combined2.animate.shift(UP))
        self.wait(1)
        
        # 添加求sum2的收敛半径
        radius_formula = MathTex(r"R = \lim_{n \to \infty} \left| \frac{n+1}{n+2} \right| = 1")
        radius_formula.next_to(combined2, DOWN*1.2)
        self.play(Write(radius_formula))
        self.wait(2)

        divergence_text = Text("当 x 等于 ±1 时，级数发散，因此此幂级数收敛区间为 (-1, 1)").scale(0.7)
        divergence_text.next_to(radius_formula, DOWN*1.2)
        self.play(Write(divergence_text))
        self.wait(2)
        conclusion_text = Text("因此，当 x = 1/2 时，幂级数收敛").scale(
            0.7)
        conclusion_text.next_to(divergence_text, DOWN*1.2)
        self.play(Write(conclusion_text))
        self.wait(2)

        # 让除了original_sum以外的部分全部消失
        self.play(FadeOut(combined2), FadeOut(radius_formula), FadeOut(divergence_text), FadeOut(conclusion_text))
        self.wait(1)

        text4 = Text("观察到：")
        integral_expr = MathTex(
            r"\int_{0}^{x} (n+1)t^n \, dt = x^{n+1}")
        combined3 = VGroup(text4, integral_expr)
        combined3.arrange(RIGHT-UP*0.5)
        self.play(Write(combined3))
        self.wait(2)

        sum3 = MathTex(r"\int_{0}^{x} \sum_{n=0}^{\infty} (n+1)t^n \, dt = \sum_{n=0}^{\infty} \int_{0}^{x} (n+1)t^n \, dt = \sum_{n=0}^{\infty} x^{(n+1)}")
        sum3.next_to(combined3, DOWN*1.2)
        self.play(Write(sum3))
        self.wait(2)

        # 让除了original_sum以外的部分全部消失
        self.play(FadeOut(combined3))   
        self.wait(1)

        # 将sum3往上平移
        self.play(sum3.animate.shift(UP*2.5))
        self.wait(2)
        
        # 添加等式右边的展开形式
        expanded_sum = MathTex(r"x + x^2 + x^3 + \cdots + x^{n+1}")
        equals_sign = MathTex("=")
        expanded_group = VGroup(equals_sign, expanded_sum).arrange(RIGHT)
        expanded_group.next_to(sum3, DOWN*2)
        self.play(Write(expanded_group))
        self.wait(2)

        # 添加等式右边的分式形式
        fraction_form = MathTex(r"= \frac{x}{1-x}")
        fraction_form.next_to(expanded_group, DOWN*1.5)
        self.play(Write(fraction_form))
        self.wait(2)

        # 让除了original_sum以外的部分全部消失
        self.play(FadeOut(sum3), FadeOut(expanded_group), FadeOut(fraction_form))
        self.wait(1)

        # 添加对 x 微分后的等式
        differentiated_sum = MathTex(r"\frac{d}{dx} \left( \sum_{n=0}^{\infty} x^{(n+1)} \right) = \frac{d}{dx} \left( \frac{x}{1-x} \right)")
        differentiated_sum.move_to(ORIGIN+UP*1)
        self.play(Write(differentiated_sum))
        self.wait(2)

        # 添加微分后的结果
        differentiated_result = MathTex(r"\sum_{n=0}^{\infty} (n+1)x^n = \frac{1}{(1-x)^2}")
        differentiated_result.next_to(differentiated_sum, DOWN*1.5)
        self.play(Write(differentiated_result))
        self.wait(2)

        # 让除了original_sum以外的部分全部消失
        self.play(FadeOut(differentiated_sum), FadeOut(differentiated_result))
        self.wait(1)    

        # 添加结论
        conclusion_text2 = Text("只需令 x = 1/2，有：").scale(0.7)
        conclusion_text2.move_to(ORIGIN+UP*1)
        self.play(Write(conclusion_text2))
        self.wait(2)

        final_result = MathTex(r"\sum_{n=0}^{\infty} (n+1)\left(\frac{1}{2}\right)^n = \frac{1}{(1-\frac{1}{2})^2} = 4")
        final_result.next_to(conclusion_text2, DOWN)
        self.play(Write(final_result))
        self.wait(3)
