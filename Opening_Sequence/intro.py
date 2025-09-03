from manim import *

class IntroScene(Scene):
    def construct(self):
        # Palette
        ACCENT1 = "#00FFC6"  # aqua
        ACCENT2 = "#8A2BE2"  # blue-violet
        ACCENT3 = "#FF2D95"  # neon pink
        group_name = "Neon Nexus"

        # Intro: logo + title
        ring = Annulus(inner_radius=0.6, outer_radius=1.0).set_stroke(ACCENT1, width=8).set_fill(opacity=0)
        tri = RegularPolygon(3, radius=0.55).rotate(PI / 2).set_fill(ACCENT2, opacity=1).set_stroke(ACCENT3, width=3)
        dots = VGroup(*[Dot(radius=0.06).set_fill(ACCENT3) for _ in range(3)])
        for i, d in enumerate(dots):
            ang = i * TAU / 3
            d.move_to(np.array([np.cos(ang) * 0.85, np.sin(ang) * 0.85, 0]))
        logo = VGroup(ring, tri, dots)
        title = IntroScene().get_mobject().scale(0.9)
        title.set_color_by_gradient(ACCENT1, ACCENT3)

        self.play(
            LaggedStart(
                GrowFromCenter(ring),
                SpinInFromNothing(tri),
                LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.2),
                lag_ratio=0.2,
            ),
            run_time=4,
        )
        self.play(LaggedStart(*[Write(c) for c in title], lag_ratio=0.06), run_time=3)
        self.play(Rotate(ring, angle=TAU / 6), run_time=5, rate_func=smooth)
        self.play(Indicate(title, color=ACCENT3, scale_factor=1.05), run_time=1.8)

    def get_mobject(self):
        return Text("Neon Nexus", font_size=72).set_color_by_gradient(BLUE, PURPLE)
