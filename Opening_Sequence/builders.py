from manim import *
import numpy as np
from pathlib import Path


def build_background(color_bg):
    bg = Rectangle(width=14, height=8)
    bg.set_fill(color=color_bg, opacity=1)
    bg.set_stroke(width=0)
    return bg


def build_particles(count: int = 60) -> VGroup:
    particles = VGroup(*[
        Dot(radius=0.05, color=GRAY, fill_opacity=0.15).shift(
            [float(np.random.uniform(-6, 6)), float(np.random.uniform(-3.5, 3.5)), 0]
        )
        for _ in range(count)
    ])
    return particles


def load_brand_mark(svg_path: Path, png_path: Path, fallback_image: Path, color_text: str):
    if svg_path and svg_path.exists():
        logo = SVGMobject(str(svg_path)).set_height(2.6)
        logo.set_color(color_text)
        return logo, True
    if png_path and png_path.exists():
        logo = ImageMobject(str(png_path)).scale(0.85)
        return logo, False
    if fallback_image and fallback_image.exists():
        logo = ImageMobject(str(fallback_image)).scale(0.9)
        return logo, False
    logo = Text("Imran's Lab", weight=BOLD).scale(1.2).set_color(color_text)
    return logo, True


def build_glow(logo, is_vector: bool):
    if is_vector:
        glow = logo.copy().set_stroke(color=YELLOW, width=18, opacity=0.18)
    else:
        glow = logo.copy().set_opacity(0.25).scale(1.06)
    glow.move_to(logo.get_center())
    return glow


def build_text_elements(logo, color_text: str):
    tagline = Text(
        "Innovating Education & Technology",
        font_size=28,
        color=color_text
    ).next_to(logo, DOWN, buff=0.5)

    title = Text("IMRAN'S LAB", weight=BOLD, font_size=54, color=color_text)
    title.set_color_by_gradient("#1f2937", "#334155", "#64748b")
    title.next_to(tagline, DOWN, buff=0.6)
    underline = Line(LEFT*2.8, RIGHT*2.8).set_stroke(color="#94a3b8", width=4)
    underline.next_to(title, DOWN, buff=0.25)
    accent_left = Dot(radius=0.05, color="#60a5fa").next_to(underline, LEFT, buff=0.15)
    accent_right = Dot(radius=0.05, color="#f472b6").next_to(underline, RIGHT, buff=0.15)
    return tagline, title, underline, accent_left, accent_right


