from manim import *

class MainScene(Scene):
    def construct(self):
        # Palette and background
        ACCENT1 = "#00FFC6"  # aqua
        ACCENT2 = "#8A2BE2"  # blue-violet
        ACCENT3 = "#FF2D95"  # neon pink
        self.camera.background_color = "#0e1116"

        # Title (5s total)
        title = Text("Member 1 — Nasemul", font_size=64, color=ACCENT1, weight=BOLD)
        underline = Line(LEFT * 3.2, RIGHT * 3.2).next_to(title, DOWN, buff=0.2).set_stroke(ACCENT3, 4)
        title_group = VGroup(title, underline).move_to(ORIGIN)
        self.play(FadeIn(title_group, shift=UP, run_time=1.5))
        self.wait(2.5)
        self.play(FadeOut(title_group, shift=UP, run_time=1.0))

        # Slides (3 × 23s = 69s)
        slides = [
            "My name is Nasemul,\nand I am a Computer Science and\n Engineering major.",
            "I have a strong passion for programming\nand enjoy spending time playing video games.",
            "I also love building web applications\nand exploring new technologies.",
        ]

        for s in slides:
            txt = Text(s, font_size=38, color=WHITE, line_spacing=0.9)
            card_width = max(8.8, txt.width + 1.4)
            card_height = txt.height + 1.2
            bg = (
                RoundedRectangle(corner_radius=0.4, width=card_width, height=card_height)
                .set_stroke(ACCENT2, width=3)
                .set_fill(color=[ACCENT2, ACCENT3], opacity=0.12)
            )
            card = VGroup(bg, txt).move_to(ORIGIN)

            self.play(FadeIn(bg, shift=UP, run_time=1.0))
            self.play(Write(txt, run_time=12.0))
            self.wait(8.0)
            self.play(FadeOut(card, shift=DOWN, run_time=2.0))

        # # Outro (16s)
        # outro = Text("Thanks for watching!", font_size=56, color=ACCENT1, weight=BOLD)
        # self.play(Write(outro, run_time=5.0))
        # self.wait(8.0)
        # self.play(FadeOut(outro, run_time=3.0))

    def get_mobjects(self):
        # Stylized cards for the three slides (for potential reuse)
        ACCENT1 = "#00FFC6"
        ACCENT2 = "#8A2BE2"
        ACCENT3 = "#FF2D95"

        slides = [
            "My name is Nasemul,\nand I am a Computer Science and\n Engineering major.",
            "I have a strong passion for programming\nand enjoy spending time playing video games.",
            "I also love building web applications\nand exploring new technologies.",
        ]

        cards = []
        for s in slides:
            txt = Text(s, font_size=36, color=GRAY_A, line_spacing=0.9)
            card_width = max(8.6, txt.width + 1.2)
            card_height = txt.height + 1.0
            bg = (
                RoundedRectangle(corner_radius=0.4, width=card_width, height=card_height)
                .set_stroke(ACCENT2, width=3)
                .set_fill(color=[ACCENT2, ACCENT3], opacity=0.10)
            )
            card = VGroup(bg, txt).move_to(ORIGIN)
            cards.append(card)

        return cards
