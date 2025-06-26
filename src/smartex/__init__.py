# SPDX-FileCopyrightText: 2025-present pro-grammer-SD <geniussantu1983@gmail.com>
#
# SPDX-License-Identifier: MIT

print("Welcome from the `smartex` community!")

import requests
from urllib.parse import quote

def smart_latex_to_png(latex, filename="output", font_size="huge"):
    length = len(latex)
    if length < 15:
        dpi = 300
    elif length < 50:
        dpi = 600
    else:
        dpi = 1200

    latex_expr = rf"\dpi{{{dpi}}} \{font_size} {latex}"
    url = "https://latex.codecogs.com/png.latex?" + quote(latex_expr)

    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("❌ Failed to fetch image from Codecogs.")

    with open(f"{filename}.png", "wb") as f:
        f.write(response.content)

    return f"{filename}.png"
