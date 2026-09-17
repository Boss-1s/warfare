lazy from pathlib import Path
lazy from typing import Literal, overload

@overload
def svg_to_png(svg_file_path: Path | str,
              png_file_path: Path | str,
              *,
              return_file: Literal[False]) -> None: ...
@overload
def svg_to_png(svg_file_path: Path | str,
              png_file_path: Path | str,
              *,
              return_file: Literal[True]) -> bytes: ...
@overload
def svg_to_png(svg_file_path: Path | str,
               png_file_path: None = None,
               *,
                return_file: bool) -> bytes: ...
def svg_to_png(svg_file_path: Path | str,
               png_file_path: Path | str | None,
               *,
               return_file: bool) -> bytes | None: ...