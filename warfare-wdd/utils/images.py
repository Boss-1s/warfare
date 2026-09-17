from pathlib import Path

lazy import cairosvg

def svg_to_png(svg_file_path: Path | str,
              png_file_path: Path | str | None = None,
              *,
              return_file: bool = False) -> bytes | None:
    """
    Convert an SVG file to a PNG file.

    :param `svg_file_path`: Path to the input SVG file.
    :param `png_file_path`: Path to the output PNG file.
    :param `return_file`: If True, returns the PNG file itself.
        Defaults to True if png_file_path is not specified.
    """
    svg_file_path = Path(svg_file_path)
    if png_file_path is None:
        return cairosvg.svg2png(url=svg_file_path)
    png_file_path = Path(png_file_path)
    cairosvg.svg2png(url=svg_file_path, write_to=png_file_path)
    if return_file:
        return png_file_path.read_bytes()



