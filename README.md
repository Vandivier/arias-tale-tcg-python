# arias-tale-tcg-python

a trading card game built in python

## Usage

1. Run `python build.py`
2. Drag and drop the `dist/index.html` file into a browser

## Design Goals

This game should always be open source and prioritize low cost.
It is intended to be web-based and educational.
It should be embedded in the [ariastale.com](https://ariastale.com) website at some point.
Additional short term and long term goals are below.
We will anchor to the Chrome browser.

### Short Run

1. Browser-based experience
2. PVE Support

### Long Run (Ordered)

1. Integrate user accounts for collection and achievements features with ariastale.com
2. PVP Support
3. Cross-platform support. Mainly: Mobile can play against desktop (Chrome browser).

### Non-Goals

1. Supporting old versions of Python or many browsers.
2. Supporting cross-platform play with closed systems like Nintendo Switch.

## Tech Stack

1. Python 3.11+
   1. I'm noticing at https://pyodide.org/en/latest/console.html it uses Python 3.12
2. [pygame](https://www.pygame.org/)
3. PyScript OR Pyodide - TBD
   1. Pyodide supports Pygame in v0.26.0.dev0+: https://pyodide.org/en/latest/usage/packages-in-pyodide.html
4. Deploy on [Cloudflare workers](https://blog.cloudflare.com/python-workers), Vercel Python functions, or AWS via [Flightcontrol](https://www.flightcontrol.dev/).

## Related Projects

https://ariastale.com/

Phaser JavaScript/TypeScript clone of this game (TODO/forthcoming)

## Notes + Issues

1. https://github.com/pyodide/pyodide/issues/289
2. https://pyscript.com/@examples/fractals-with-numpy-and-canvas/latest
3. https://pyodide.org/en/stable/usage/index.html
   1. Pyodide runs Python "through" JavaScript. I can't just <script type="py">
4. If you format the HTML file, this might break Python bc indentation. So, remove any whitespace around `<!-- PYTHON_SCRIPT_PLACEHOLDER -->`.
