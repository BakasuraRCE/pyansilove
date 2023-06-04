from pathlib import Path
from typing import Dict, Tuple, List

from PIL import Image

from pyansilove.constants import (
    ansi_palette_red,
    ansi_palette_green,
    ansi_palette_blue,
    workbench_palette_red,
    workbench_palette_green,
    workbench_palette_blue
)
from pyansilove.font import select_font
from pyansilove.schemas import AnsiLoveOptions, AnsiLoveRenderingMode, AnsiLoveChar, AnsiLoveState
from pyansilove.utils import draw_char


def ansi_loader(
        input_path: Path,
        output_path: Path,
        options=AnsiLoveOptions()
):
    ansi_sequence_max_length = 14
    ansi_buffer_size = 65536

    # Character definitions
    state = AnsiLoveState.TEXT

    # Default color values
    background = 0
    foreground = 7
    background24 = 0
    foreground24 = 0

    # Text attributes
    bold = False
    blink = False
    invert = False

    # Positions
    column = 0
    row = 0
    column_max = 0
    row_max = 0
    saved_row = 0
    saved_column = 0

    # ANSi buffer structure array definition
    struct_index = 0

    ansi_buffer_size = ansi_buffer_size

    if options.bits != 8 and options.bits != 9:
        return -1

    # Default to 80 columns if columns option wasn't set
    options.columns = options.columns if options.columns else 80

    columns = options.columns

    if columns < 1 or columns > 4096:
        return -1

    ced = False
    workbench = False

    # Font selection
    font_data = select_font(options.font)

    if options.mode == AnsiLoveRenderingMode.CED:
        ced = True
    elif options.mode == AnsiLoveRenderingMode.WORKBENCH:
        workbench = True

    # ANSi buffer dynamic memory allocation
    ansi_buffer: Dict[int, AnsiLoveChar] = {}

    content = input_path.read_text(encoding='latin-1')
    content_len = len(content)

    # ANSi interpreter
    loop = 0
    while loop < content_len:
        cursor = content[loop]

        if column == options.columns:
            row += 1
            column = 0

        if state == AnsiLoveState.TEXT:
            if cursor == '\n':  # LF
                row += 1
                column = 0
            elif cursor == '\r':  # CR
                pass
            elif cursor == '\t':  # TAB
                column += 8
            elif cursor == '\x1a':  # SUB
                state = AnsiLoveState.END
            elif cursor == '\x1b':  # ESC
                # ANSi sequence
                if loop + 1 < content_len and content[loop + 1] == '[':
                    state = AnsiLoveState.SEQUENCE
                    loop += 1
            else:
                # Record number of columns and lines used
                if column > column_max:
                    column_max = column

                if row > row_max:
                    row_max = row

                # Reallocate structure array memory
                if struct_index == ansi_buffer_size:
                    ansi_buffer_size += ansi_buffer_size

                ansi_buffer[struct_index] = AnsiLoveChar()

                # Write current character in ansiChar structure
                if invert:
                    ansi_buffer[struct_index].background = foreground % 8
                    ansi_buffer[struct_index].foreground = background + (foreground & 8)
                else:
                    ansi_buffer[struct_index].background = background24 if background24 else background
                    ansi_buffer[struct_index].foreground = foreground24 if foreground24 else foreground

                ansi_buffer[struct_index].character = ord(cursor)
                ansi_buffer[struct_index].column = column
                ansi_buffer[struct_index].row = row

                struct_index += 1
                column += 1
        elif state == AnsiLoveState.SEQUENCE:
            maxlength = min(content_len - loop, ansi_sequence_max_length)

            for ansi_sequence_loop in range(0, maxlength):
                ansi_sequence_character = content[loop + ansi_sequence_loop]

                # Cursor position
                if ansi_sequence_character == 'H' or ansi_sequence_character == 'f':
                    # Create substring from the sequence's content
                    seq_line = 1
                    seq_column = 1
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    if seq_grab.startswith(';'):
                        seq_line = 1
                        seq_tok = seq_grab.split(';')[0]
                        if seq_tok:
                            seq_column = int(seq_tok)
                    else:
                        seq_tok = seq_grab.split(';')
                        if seq_tok:
                            seq_line = int(seq_tok[0])

                        if len(seq_tok) > 1:
                            seq_column = int(seq_tok[1])

                    # Set the positions
                    row = seq_line - 1
                    column = seq_column - 1

                    loop += ansi_sequence_loop
                    break

                # Cursor up
                if ansi_sequence_character == 'A':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    # Now get escape sequence's position value
                    seq_line = int(seq_grab) if seq_grab else 1

                    row -= seq_line if seq_line else 1

                    if row < 0:
                        row = 0

                    loop += ansi_sequence_loop
                    break

                # Cursor down
                if ansi_sequence_character == 'B':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    # Now get escape sequence's position value
                    seq_line = int(seq_grab) if seq_grab else 1

                    row += seq_line if seq_line else 1

                    loop += ansi_sequence_loop
                    break

                # Cursor forward
                if ansi_sequence_character == 'C':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    # Now get escape sequence's position value
                    seq_column = int(seq_grab) if seq_grab else 1

                    column += seq_column if seq_column else 1

                    if column > options.columns:
                        column = options.columns

                    loop += ansi_sequence_loop
                    break

                # Cursor backward
                if ansi_sequence_character == 'D':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    # Now get escape sequence's content length
                    seq_column = int(seq_grab) if seq_grab else 1

                    column -= seq_column if seq_column else 1

                    if column < 0:
                        column = 0

                    loop += ansi_sequence_loop
                    break

                # Save cursor position
                if ansi_sequence_character == 's':
                    saved_row = row
                    saved_column = column

                    loop += ansi_sequence_loop
                    break

                # Restore cursor position
                if ansi_sequence_character == 'u':
                    row = saved_row
                    column = saved_column

                    loop += ansi_sequence_loop
                    break

                # Erase display
                if ansi_sequence_character == 'J':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    # Convert grab to an integer
                    erase_display_int = int(seq_grab) if seq_grab else 0

                    if erase_display_int == 2:
                        column = 0
                        row = 0

                        column_max = 0
                        row_max = 0

                        # Reset ansi buffer
                        struct_index = 0

                    loop += ansi_sequence_loop
                    break

                # Set graphics mode
                if ansi_sequence_character == 'm':
                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    seq_tok = seq_grab.split(';')
                    for seq_tok in seq_tok:
                        seq_value = int(seq_tok) if seq_tok else 0

                        if seq_value == 0:
                            background = 0
                            background24 = 0
                            foreground = 7
                            foreground24 = 0
                            bold = False
                            blink = False
                            invert = False

                        if seq_value == 1:
                            if not workbench:
                                foreground += 8
                            bold = True
                            foreground24 = 0

                        if seq_value == 5:
                            if not workbench and options.icecolors:
                                background += 8

                            blink = True
                            background24 = 0

                        if seq_value == 7:
                            invert = True

                        if seq_value == 27:
                            invert = False

                        if 29 < seq_value < 38:
                            foreground = seq_value - 30
                            foreground24 = 0

                            if bold:
                                foreground += 8

                        if 39 < seq_value < 48:
                            background = seq_value - 40
                            background24 = 0

                            if blink and options.icecolors:
                                background += 8

                    loop += ansi_sequence_loop
                    break

                # Cursor (de)activation (Amiga ANSi)
                if ansi_sequence_character == 'p':
                    loop += ansi_sequence_loop
                    break

                # Skipping set mode and reset mode sequences
                if ansi_sequence_character == 'h' or ansi_sequence_character == 'l':
                    loop += ansi_sequence_loop
                    break

                # Skipping erase in line (EL) sequences
                if ansi_sequence_character == 'K':
                    loop += ansi_sequence_loop
                    break

                # PabloDraw 24-bit ANSI sequences
                if ansi_sequence_character == 't':
                    color_r = 0
                    color_g = 0
                    color_b = 0

                    # Create substring from the sequence's content
                    seq_grab = content[loop:loop + ansi_sequence_loop]
                    seq_grab = seq_grab

                    seq_tok = seq_grab.split(';')
                    if seq_tok:
                        seq_value = int(seq_tok[0]) if seq_tok[0] else 0

                        if len(seq_tok) > 1:
                            color_r = int(seq_tok[1]) & 0xff if seq_tok[1] else 0

                        if len(seq_tok) > 2:
                            color_g = int(seq_tok[2]) & 0xff if seq_tok[2] else 0

                        if len(seq_tok) > 3:
                            color_b = int(seq_tok[3]) & 0xff if seq_tok[3] else 0

                        if seq_value == 0:
                            background24 = (color_r << 16) | (color_g << 8) | color_b
                        elif seq_value == 1:
                            foreground24 = (color_r << 16) | (color_g << 8) | color_b

                        options.truecolor = True

                    loop += ansi_sequence_loop
                    break

            state = AnsiLoveState.TEXT
        elif state == AnsiLoveState.END:
            loop = content_len
        loop += 1

    # Allocate image buffer memory
    column_max += 1
    row_max += 1

    if ced:
        columns = 78

    if options.diz:
        columns = min(column_max, options.columns)

    width = columns * options.bits
    height = row_max * font_data.height

    image_mode = 'RGB' if options.truecolor else 'P'

    # Create image
    canvas = Image.new(image_mode, (width, height))

    colors: List[Tuple[int, int, int]] = [(0, 0, 0)] * 16

    ced_background = 0
    ced_foreground = 0

    if ced:
        ced_background = (170, 170, 170)
        ced_foreground = (0, 0, 0)
        canvas.paste(ced_background, (0, 0, width, height))
    elif workbench:
        for i in range(16):
            colors[i] = (
                workbench_palette_red[i],
                workbench_palette_green[i],
                workbench_palette_blue[i]
            )
    else:
        # Allocate standard ANSi color palette
        for i in range(16):
            colors[i] = (
                ansi_palette_red[i],
                ansi_palette_green[i],
                ansi_palette_blue[i]
            )

    # Render ANSi
    for loop in range(struct_index):
        # Grab ANSi char from our structure array
        background = ansi_buffer[loop].background
        foreground = ansi_buffer[loop].foreground
        character = ansi_buffer[loop].character
        column = ansi_buffer[loop].column
        row = ansi_buffer[loop].row

        if ced:
            background = ced_background
            foreground = ced_foreground
        else:
            if background < 16:
                background = colors[background]

            if foreground < 16:
                foreground = colors[foreground]

        # Draw character
        draw_char(canvas, font_data.font_data, options.bits, font_data.height,
                  column, row, background, foreground, character)

    # Handle DOS aspect ratio
    if options.dos:
        dos = Image.new('RGB', (canvas.width, int(canvas.height * 1.35)))

        # Convert source image to RGB if it's in "P" mode
        if image_mode == 'P':
            canvas = canvas.convert('RGB')

        dos.paste(canvas.resize((dos.width, dos.height), resample=Image.LANCZOS), (0, 0))

        # Convert back to "P" mode if necessary
        if image_mode == 'P':
            dos = dos.convert('P')

        # dos.paste(canvas, (0, 0))
        # dos = dos.resize((dos.width, dos.height), resample=Image.LANCZOS)

        canvas.close()
        canvas = dos

    # Handle resizing
    if options.scale_factor:
        if options.scale_factor < 2 or options.scale_factor > 8:
            raise Exception('scale factor must be between 2 to 8')

        width = canvas.width * options.scale_factor
        height = canvas.height * options.scale_factor

        retina = canvas.resize((width, height), resample=Image.LANCZOS)

        canvas.close()
        canvas = retina

    # Handle transparency
    if options.mode == AnsiLoveRenderingMode.TRANSPARENT:
        transparent_index = canvas.getpixel((0, 0))
        canvas.info['transparency'] = transparent_index

    # Create output image
    canvas.save(str(output_path.absolute()))
