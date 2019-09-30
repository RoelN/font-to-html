# Font to HTML

Dumps all characters and ligatures in a font to a HTML page, so you can see which [glyphs](https://en.wikipedia.org/wiki/Glyph) the font can produce.

Currently supports normal characters, and ligature substitutions (GSUB LookupType 4, like `ccmp`, `rlig`, `liga`, etc.). Not yet any of the other GSUB lookup types.

## How to use

1. Clone the repo
2. Do a `pip install fonttools`
3. Run `./font-to-html.py -i fontfile.ttf`

This will produce `font-to-html.html` which you can open in the browser.