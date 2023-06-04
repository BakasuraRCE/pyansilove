from typing import List

from PIL import ImageDraw


def draw_char(im, font_data: List[int], bits, height, column, row, background, foreground, character):
    x_start = column * bits
    y_start = row * height
    x_end = x_start + bits - 1
    y_end = y_start + height - 1

    draw = ImageDraw.Draw(im)
    draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=background)

    for y in range(height):
        for x in range(bits):
            if font_data[y + character * height] & (0x80 >> x):
                draw.point((x_start + x, y_start + y), fill=foreground)

                if bits == 9 and x == 7 and 191 < character < 224:
                    draw.point((x_start + 8, y_start + y), fill=foreground)
