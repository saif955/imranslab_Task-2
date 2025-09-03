import sys
from pathlib import Path

# Ensure we can import scene files
ROOT = Path(__file__).parent.resolve()
sys.path.append(str(ROOT / "Opening_Sequence"))
sys.path.append(str(ROOT / "Middle_Sequence"))

from manim import tempconfig  # type: ignore
from Opening import AdvancedIntro  # type: ignore
from intro import IntroScene  # type: ignore
from main import MainScene  # type: ignore


def render_scene(scene_cls):
    with tempconfig(
        {
            "pixel_width": 1920,
            "pixel_height": 1080,
            "frame_rate": 60,
            "media_dir": str(ROOT / "media"),
            "write_to_movie": True,
            "save_last_frame": False,
            "format": "mp4",
        }
    ):
        scene = scene_cls()
        scene.render()


def main():
    # 1) Render all three scenes at 1080p60 into media/videos/... (Manim default layout)
    render_scene(AdvancedIntro)
    render_scene(IntroScene)
    render_scene(MainScene)

    # 2) Concatenate into a single final video using MoviePy
    try:
        # MoviePy < 2
        from moviepy.editor import VideoFileClip, concatenate_videoclips  # type: ignore
    except Exception:
        # MoviePy >= 2 moved editor API to top-level
        from moviepy import VideoFileClip, concatenate_videoclips  # type: ignore

    # Expected Manim output filenames based on file/class names
    # Opening_Sequence/Opening.py -> media/videos/Opening/1080p60/AdvancedIntro.mp4
    # Opening_Sequence/intro.py   -> media/videos/intro/1080p60/IntroScene.mp4
    # Middle_Sequence/main.py -> media/videos/main/1080p60/MainScene.mp4
    clips_map = [
        ROOT / "media" / "videos" /  "1080p60" / "AdvancedIntro.mp4",
        ROOT / "media" / "videos" /  "1080p60" / "IntroScene.mp4",
        ROOT / "media" / "videos"  / "1080p60" / "MainScene.mp4",
    ]

    missing = [p for p in clips_map if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "One or more scene outputs are missing after rendering: "
            + ", ".join(str(m) for m in missing)
        )

    clips = [VideoFileClip(str(p)) for p in clips_map]
    final = concatenate_videoclips(clips, method="compose")

    out_dir = ROOT / "media" / "videos" / "final" / "1080p60"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "final.mp4"
    final.write_videofile(str(out_path), fps=60, audio_codec="aac")

    for c in clips:
        c.close()
    final.close()

    print(f"Final video written to: {out_path}")


if __name__ == "__main__":
    main()


