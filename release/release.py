from subprocess import run

tag = input("📌 Enter tag version (e.g. v0.0.1): ").strip()
title = input("📝 Enter release title [default: same as tag]: ").strip() or tag
notes = input("🧾 Enter release notes [default: SmartEx package upload]: ").strip() or "SmartEx package upload"

command = f'git tag {tag} && git push origin {tag} && gh release create {tag} --title "{title}" --notes "{notes}"'
run(command, shell=True, check=True)
