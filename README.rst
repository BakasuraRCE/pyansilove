===============
Python Ansilove
===============

pyansilove is a port of the libansilove_ library to convert ANSi and artscene related file formats into PNG images.

* Free software: BSD-2-Clause license


Features
--------

The following formats are supported:

- .ANS - ANSi (ANSI escape sequences: ANSI X3.64 standard)

TODO
----

Port support of formats:

- .PCB - PCBoard Bulletin Board System (BBS) own file format
- .BIN - Binary format (raw memory copy of text mode video memory)
- .ADF - Artworx format, supporting custom character sets and palettes
- .IDF - iCE Draw format, supporting custom character sets and palettes
- .TND - TundraDraw format, supporting 24-bit color mode
- .XB - The eXtended Binary XBin format, supporting custom character sets and palettes

Documentation
-------------

Usage
-----

.. code:: python

    from pathlib import Path

    from pyansilove.ansilove import AnsiLove
    from pyansilove.schemas import AnsiLoveOptions, AnsiLoveRenderingMode

    # https://16colo.rs/pack/break_05/h7-lark.nfo
    AnsiLove.ansi(
        Path('nfo.nfo'),
        Path('nfo.png'),
        options=AnsiLoveOptions(
            # truecolor=True,
            # diz=True,
            # dos=True,
            # mode=AnsiLoveRenderingMode.TRANSPARENT
        )
    )

    # https://16colo.rs/pack/fire-36/US-TREMR.ANS
    AnsiLove.ansi(
        Path('US-TREMR.ANS'),
        Path('US-TREMR.png'),
        options=AnsiLoveOptions(
            # diz=True,
            # dos=True,
            bits=9,
            scale_factor=2,
            # mode=AnsiLoveRenderingMode.TRANSPARENT,
        )
    )



License
-------

pyansilove is released under the BSD 2-Clause license. See the file LICENSE for details.

Credits
-------

Original code written by libansilove_

Port to python by Bakasura_

.. _libansilove: https://github.com/ansilove/libansilove
.. _Bakasura: https://github.com/BakasuraRCE
