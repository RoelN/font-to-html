#!/usr/bin/env python3
# Font to HTML 1.0
# @author Roel Nieskens, https://pixelambacht.nl
# MIT license

"""Create HTML page with every character from font, including GSUB."""
import argparse
from fontTools import ttLib


def wrap(char, wrapper):
	"""Wrap a sequence in a custom string."""
	return wrapper.format(char=char)


def get_unicode_value(glyph, font):
	"""Get Unicode value for glyphname from CMAP."""
	cmap = font['cmap'].getBestCmap()
	pamc = dict(map(reversed, cmap.items()))
	if glyph in pamc:
		return str(pamc[glyph])


def get_cmap_chars(font, wrapper):
	"""Return list of Unicode values found in CMAP."""
	chars = ''
	cmap = font['cmap'].getBestCmap()
	for key in cmap:
		char = wrap(key, '&#{char};')
		chars += wrap(char, wrapper)
	return chars, len(cmap)


def get_gsub_chars(font, wrapper):
	"""Get all ligature sequences in the font."""
	chars = ''
	if 'GSUB' in font:
		table = font['GSUB'].table
		if table.LookupList:
			# GSUB present, let's plough through all tables
			for lookup in table.LookupList.Lookup:
				if lookup.LookupType == 4:
					for st in lookup.SubTable:
						ligatures = st.ligatures
						for first_char in ligatures:
							for ligature in ligatures[first_char]:
								char = get_unicode_value(first_char, font)
								sequence = wrap(char, '&#{char};')

								for following_char in ligature.Component:
									char = get_unicode_value(
										following_char, font)
									sequence += wrap(char, '&#{char};')

								chars += wrap(sequence, wrapper)
						return chars, len(ligatures)
	return "", 0


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-i', '--input', help='input font file', required=True)
	parser.add_argument(
		'-o', '--output', help='output HTML file', default='font-to-html.html')
	parser.add_argument(
		'-t', '--template', help='HTML template', default='template.html')
	parser.add_argument(
		'-w', '--wrapper', help='HTML string to wrap char in', default='<div>{char}</div>')
	args = parser.parse_args()

	font = ttLib.TTFont(args.input)

	cmap_html, cmap_len = get_cmap_chars(font, args.wrapper)
	gsub_html, gsub_len = get_gsub_chars(font, args.wrapper)

	stats_html = f'<h1>{args.input} contains {cmap_len} characters and {gsub_len} ligatures.</h1>\n'

	with open('template.html', 'r') as f:
		data = f.read()

	data = data.replace('{fontfile}', args.input)
	data = data.replace('{stats}', stats_html)
	data = data.replace('{content}', cmap_html + gsub_html)

	with open(args.output, mode='wt', encoding='utf-8') as f:
		f.write(data)


if __name__ == '__main__':
	main()
