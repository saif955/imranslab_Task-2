from manim import *


def animate_particles(scene: Scene, particles: VGroup):
    scene.play(
        particles.animate.shift(0.3 * UP),
        run_time=4,
        rate_func=linear,
    )


def animate_logo_reveal(scene: Scene, glow, logo, is_vector: bool):
    scene.play(FadeIn(glow, scale=1.05, shift=0.15*UP), run_time=0.6)
    if is_vector:
        scene.play(DrawBorderThenFill(logo), run_time=2.0)
        scene.play(
            ShowPassingFlash(logo.copy().set_stroke(color=YELLOW, width=6)),
            run_time=1.2,
        )
    else:
        scene.play(FadeIn(logo, scale=0.98), run_time=1.2)
        scene.play(glow.animate.set_opacity(0.32), run_time=0.25)
        scene.play(glow.animate.set_opacity(0.18), run_time=0.25)


def animate_title_sequence(scene: Scene, tagline, underline, accent_left, accent_right, title):
    scene.play(Write(tagline), run_time=2.2)
    scene.play(
        Create(underline, rate_func=smooth),
        FadeIn(accent_left, shift=0.1*UP),
        FadeIn(accent_right, shift=0.1*UP),
        run_time=1.2,
    )
    scene.play(Write(title), run_time=1.8)


def animate_outro(scene: Scene, glow, logo, tagline, title, underline, accent_left, accent_right, particles, bg):
    scene.play(
        logo.animate.scale(1.06).set_color_by_gradient(WHITE, "#2c2c2c"),
        tagline.animate.set_opacity(0.9),
        title.animate.scale(1.02),
        accent_left.animate.set_color("#22d3ee"),
        accent_right.animate.set_color("#fca5a5"),
        run_time=1.5,
    )
    scene.wait(1.2)
    scene.play(FadeOut(Group(glow, logo, tagline, title, underline, accent_left, accent_right, particles, bg)), run_time=1.2)


