from pyansilove.fonts.font_amiga_microknight import font_amiga_microknight
from pyansilove.fonts.font_amiga_microknight_plus import font_amiga_microknight_plus
from pyansilove.fonts.font_amiga_mosoul import font_amiga_mosoul
from pyansilove.fonts.font_amiga_pot_noodle import font_amiga_pot_noodle
from pyansilove.fonts.font_amiga_topaz_1200 import font_amiga_topaz_1200
from pyansilove.fonts.font_amiga_topaz_1200_plus import font_amiga_topaz_1200_plus
from pyansilove.fonts.font_amiga_topaz_500 import font_amiga_topaz_500
from pyansilove.fonts.font_amiga_topaz_500_plus import font_amiga_topaz_500_plus
from pyansilove.fonts.font_pc_80x25 import font_pc_80x25
from pyansilove.fonts.font_pc_80x50 import font_pc_80x50
from pyansilove.fonts.font_pc_baltic import font_pc_baltic
from pyansilove.fonts.font_pc_cyrillic import font_pc_cyrillic
from pyansilove.fonts.font_pc_french_canadian import font_pc_french_canadian
from pyansilove.fonts.font_pc_greek import font_pc_greek
from pyansilove.fonts.font_pc_greek869 import font_pc_greek_869
from pyansilove.fonts.font_pc_hebrew import font_pc_hebrew
from pyansilove.fonts.font_pc_icelandic import font_pc_icelandic
from pyansilove.fonts.font_pc_latin1 import font_pc_latin1
from pyansilove.fonts.font_pc_latin2 import font_pc_latin2
from pyansilove.fonts.font_pc_nordic import font_pc_nordic
from pyansilove.fonts.font_pc_portuguese import font_pc_portuguese
from pyansilove.fonts.font_pc_russian import font_pc_russian
from pyansilove.fonts.font_pc_spleen import font_pc_spleen
from pyansilove.fonts.font_pc_terminus import font_pc_terminus
from pyansilove.fonts.font_pc_turkish import font_pc_turkish
from pyansilove.schemas import AnsiLoveFontType, AnsiLoveFont


def select_font(font: AnsiLoveFontType):
    if font == AnsiLoveFontType.CP437:
        return AnsiLoveFont(font_data=font_pc_80x50, width=9, height=8)
    elif font == AnsiLoveFontType.CP737:
        return AnsiLoveFont(font_data=font_pc_greek, width=9, height=16)
    elif font == AnsiLoveFontType.CP775:
        return AnsiLoveFont(font_data=font_pc_baltic, width=9, height=16)
    elif font == AnsiLoveFontType.CP850:
        return AnsiLoveFont(font_data=font_pc_latin1, width=9, height=16)
    elif font == AnsiLoveFontType.CP852:
        return AnsiLoveFont(font_data=font_pc_latin2, width=9, height=16)
    elif font == AnsiLoveFontType.CP855:
        return AnsiLoveFont(font_data=font_pc_cyrillic, width=9, height=16)
    elif font == AnsiLoveFontType.CP857:
        return AnsiLoveFont(font_data=font_pc_turkish, width=9, height=16)
    elif font == AnsiLoveFontType.CP860:
        return AnsiLoveFont(font_data=font_pc_portuguese, width=9, height=16)
    elif font == AnsiLoveFontType.CP861:
        return AnsiLoveFont(font_data=font_pc_icelandic, width=9, height=16)
    elif font == AnsiLoveFontType.CP862:
        return AnsiLoveFont(font_data=font_pc_hebrew, width=9, height=16)
    elif font == AnsiLoveFontType.CP863:
        return AnsiLoveFont(font_data=font_pc_french_canadian, width=9, height=16)
    elif font == AnsiLoveFontType.CP865:
        return AnsiLoveFont(font_data=font_pc_nordic, width=9, height=16)
    elif font == AnsiLoveFontType.CP866:
        return AnsiLoveFont(font_data=font_pc_russian, width=9, height=16)
    elif font == AnsiLoveFontType.CP869:
        return AnsiLoveFont(font_data=font_pc_greek_869, width=9, height=16)
    elif font == AnsiLoveFontType.SPLEEN:
        return AnsiLoveFont(font_data=font_pc_spleen, width=9, height=16)
    elif font == AnsiLoveFontType.TERMINUS:
        return AnsiLoveFont(font_data=font_pc_terminus, width=9, height=16)
    elif font == AnsiLoveFontType.MICROKNIGHT:
        return AnsiLoveFont(font_data=font_amiga_microknight, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.MICROKNIGHT_PLUS:
        return AnsiLoveFont(font_data=font_amiga_microknight_plus, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.MOSOUL:
        return AnsiLoveFont(font_data=font_amiga_mosoul, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.POT_NOODLE:
        return AnsiLoveFont(font_data=font_amiga_pot_noodle, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.TOPAZ:
        return AnsiLoveFont(font_data=font_amiga_topaz_1200, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.TOPAZ_PLUS:
        return AnsiLoveFont(font_data=font_amiga_topaz_1200_plus, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.TOPAZ500:
        return AnsiLoveFont(font_data=font_amiga_topaz_500, width=8, height=16, isAmigaFont=True)
    elif font == AnsiLoveFontType.TOPAZ500_PLUS:
        return AnsiLoveFont(font_data=font_amiga_topaz_500_plus, width=8, height=16, isAmigaFont=True)
    else:
        return AnsiLoveFont(font_data=font_pc_80x25, width=9, height=16)
