from . import smart_latex_to_png

def main():
    latex = input("📥 Enter LaTeX expression: ").strip()
    name = input("💾 Output filename (without .png): ").strip() or "output"
    size = input("🔠 Font size (tiny/small/normalsize/large/huge/Huge) [default=huge]: ").strip() or "huge"

    try:
        file_path = smart_latex_to_png(latex, name, size)
        print(f"✅ Saved: {file_path}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
