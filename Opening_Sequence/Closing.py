from manim import *
from pathlib import Path
from builders import build_background, build_particles, load_brand_mark, build_glow, build_text_elements
from animations import animate_particles, animate_logo_reveal, animate_title_sequence, animate_outro

BRAND_LOGO_SVG = Path("assets/imranslab_logo.svg")
BRAND_LOGO_PNG = Path("assets/imranslab_logo.png")
FALLBACK_IMAGE = Path("assets/branding_image.png")
COLOR_TEXT = "#2c2c2c"
COLOR_BG = ["#e0e0e0", "#c0c0c0"]


class AdvancedOutro(Scene):
    def construct(self):
        # Build
        bg = build_background(COLOR_BG)
        self.add(bg)
        particles = build_particles()
        self.add(particles)
        logo, is_vector = load_brand_mark(BRAND_LOGO_SVG, BRAND_LOGO_PNG, FALLBACK_IMAGE, COLOR_TEXT)
        glow = build_glow(logo, is_vector)
        tagline, title, underline, accent_left, accent_right = build_text_elements(logo, COLOR_TEXT)

        # Animate
        animate_particles(self, particles)
        animate_logo_reveal(self, glow, logo, is_vector)
        animate_title_sequence(self, tagline, title, underline, accent_left, accent_right)
        animate_outro(self, glow, logo, tagline, title, underline, accent_left, accent_right, particles, bg)

    def random_x(self):
        # Only used in legacy flow if needed elsewhere
        return 0.0

    def random_y(self):
        # Only used in legacy flow if needed elsewhere
        return 0.0
