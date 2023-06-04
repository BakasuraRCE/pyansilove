from dataclasses import dataclass
from enum import Enum
from typing import List

from pydantic import BaseModel


class AnsiLoveState(int, Enum):
    TEXT = 0
    SEQUENCE = 1
    END = 2


class AnsiLoveFont(BaseModel):
    font_data: List[int]
    width: int
    height: int
    isAmigaFont: bool = False


class AnsiLoveFontType(int, Enum):
    # PC Fonts
    DEFAULT = 0
    CP437 = 1
    CP437_80x50 = 2
    CP737 = 3
    CP775 = 4
    CP850 = 5
    CP852 = 6
    CP855 = 7
    CP857 = 8
    CP860 = 9
    CP861 = 10
    CP862 = 11
    CP863 = 12
    CP865 = 13
    CP866 = 14
    CP869 = 15
    TERMINUS = 20
    SPLEEN = 21
    # Amiga fonts
    MICROKNIGHT = 30
    MICROKNIGHT_PLUS = 31
    MOSOUL = 32
    POT_NOODLE = 33
    TOPAZ = 34
    TOPAZ_PLUS = 35
    TOPAZ500 = 36
    TOPAZ500_PLUS = 37


# Rendering modes
class AnsiLoveRenderingMode(int, Enum):
    DEFAULT = 0
    CED = 1
    TRANSPARENT = 2
    WORKBENCH = 3


class AnsiLoveOptions(BaseModel):
    diz: bool = False
    dos: bool = False
    icecolors: bool = False
    truecolor: bool = False
    columns: int = 0
    font: AnsiLoveFontType = AnsiLoveFontType.DEFAULT
    bits: int = 8
    mode: AnsiLoveRenderingMode = AnsiLoveRenderingMode.DEFAULT
    scale_factor: int = 0


@dataclass
class AnsiLoveChar:
    column: int = 0
    row: int = 0
    background: int = 0
    foreground: int = 0
    character: int = 0
