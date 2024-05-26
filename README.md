# arias-tale-tcg-python

a trading card game built in python

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

## Tech Stack

1. Python 3.11+
2. [pygame](https://www.pygame.org/)
3. PyScript OR Pyodide - TBD
4. Deploy on [Cloudflare workers](https://blog.cloudflare.com/python-workers), Vercel Python functions, or AWS via [Flightcontrol](https://www.flightcontrol.dev/).

## Related Projects

https://ariastale.com/

Phaser JavaScript/TypeScript clone of this game (TODO/forthcoming)
