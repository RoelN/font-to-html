# Font to HTML

Dumps all characters and ligatures in a font to a HTML page, so you can see which [glyphs](https://en.wikipedia.org/wiki/Glyph) the font can produce.

Currently supports normal characters, and ligature substitutions (GSUB LookupType 4, like `ccmp`, `rlig`, `liga`, etc.). Not yet any of the other GSUB lookup types.

## How to use

It's a little Python 3 script, so you'd need that, along with [ttx/FontTools](https://github.com/fonttools/fonttools).

1. Clone the repo
2. Do a `pip install fonttools`, if you don't have it already
3. Run `./font-to-html.py -i fontfile.ttf`

This will produce `font-to-html.html` which you can open in the browser.

Extra optional flags:

- `-o my-output.html` to use different filename for HTML file
- `-t my-template.html` to use different HTML template
- `-w '<p>{char}</p>'` to pass different HTML wrapper for each character

## It worksn't!

Any problems? Open an [issue](https://github.com/RoelN/font-to-html/issues) or ping me over at [Twitter](https://twitter.com/pixelambacht)!