# smartex

[![PyPI - Version](https://img.shields.io/pypi/v/smartex.svg)](https://pypi.org/project/smartex)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/smartex.svg)](https://pypi.org/project/smartex)

Convert LaTeX math expressions into high-quality PNG images, intelligently choosing DPI based on expression length. Built for developers, bloggers, students, and markdown warriors who want sharp math renderings fast.

---

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)

  * [Command Line](#command-line)
  * [Python API](#python-api)
* [Examples](#examples)
* [License](#license)

---

## Installation

```bash
pip install smartex
```

---

## Usage

### ✅ Command Line

Once installed, you can use `smartex` directly from your terminal:

```bash
smartex "\\int_0^1 x^2 dx" -o integral -s Huge
```

**Options:**

| Flag | Description                                                              | Default |
| ---- | ------------------------------------------------------------------------ | ------- |
| `-o` | Output filename (without `.png`)                                         | output  |
| `-s` | LaTeX font size (`tiny`, `small`, `normalsize`, `large`, `huge`, `Huge`) | huge    |

---

### 🐍 Python API

```python
from smartex import smart_latex_to_png

smart_latex_to_png(r"\frac{a}{b} = c", filename="frac", font_size="large")
```

Automatically picks DPI based on LaTeX length:

* Short: `300dpi`
* Medium: `600dpi`
* Long: `1200dpi`

Returns the full path to the saved PNG.

---

## Examples

**Render an integral:**

```bash
smartex "\\int_0^\\infty e^{-x} dx" -o integral
```

**Render inline fraction with custom size:**

```bash
smartex "\\frac{1}{2}" -o half -s small
```

---

## License

`smartex` is distributed under the terms of the [MIT License](https://spdx.org/licenses/MIT.html).
