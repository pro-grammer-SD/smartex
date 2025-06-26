import argparse
from . import smart_latex_to_png

def main():
    parser = argparse.ArgumentParser(
        description="Render LaTeX math to high-quality PNG using Codecogs."
    )
    parser.add_argument("expression", help="LaTeX expression to render")
    parser.add_argument(
        "-o", "--output", default="output", help="Output filename (without .png)"
    )
    parser.add_argument(
        "-s",
        "--size",
        default="huge",
        choices=["tiny", "small", "normalsize", "large", "huge", "Huge"],
        help="LaTeX font size",
    )

    args = parser.parse_args()

    try:
        path = smart_latex_to_png(args.expression, args.output, args.size)
        print(f"✅ Saved image to: {path}")
    except Exception as e:
        print(f"❌ Error: {e}")
