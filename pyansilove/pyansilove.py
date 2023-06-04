from pathlib import Path

from pyansilove.loaders.ansi import ansi_loader
from pyansilove.schemas import AnsiLoveOptions


class AnsiLove:
    @staticmethod
    def ansi(
            input_path: Path,
            output_path: Path,
            options: AnsiLoveOptions = AnsiLoveOptions()
    ):
        ansi_loader(
            Path(input_path),
            Path(output_path),
            options=options
        )
