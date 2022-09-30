from pathlib import Path
import cispa
import click
import logging
from rich.logging import RichHandler
import numpy as np
from cispa import FrameTransform, pivot_calibration

logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
log = logging.getLogger(__name__)


@click.command()
@click.option("--data-dir", "-d", default="data", help="Input data directory")
@click.option("--output-dir", "-o", default="output", help="Output directory")
@click.option("--name", "-n", default="pa1-debug-a", help="Name of the output file")
def main(data_dir, output_dir, name):
    data_dir = Path(data_dir).expanduser()
    output_dir = Path(output_dir).expanduser()

    cal_path = data_dir / f"{name}-calbody.txt"
    # cal_body = read_cal_data(cal_path)

    if not output_dir.exists():
        output_dir.mkdir()

    F = FrameTransform(np.eye(3), np.zeros(3))
    log.info(f"F = {F}")

    ...

    tip_in_tool, post_in_world = pivot_calibration(frames)


if __name__ == "__main__":
    main()
