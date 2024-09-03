#!/usr/bin/env python3

from glob import iglob
import os
from PIL import Image
import sys

DESIRED_DPI = 300
OUTPUT_SUBFOLDER = "fix-dpi-output"


def main():
    filenames = [file for arg in sys.argv[1:] for file in iglob(arg)]
    for ind, filename in enumerate(filenames):
        img = Image.open(filename)
        current_dir, just_filename = os.path.split(filename)
        output_dir = os.path.join(current_dir, OUTPUT_SUBFOLDER)
        if ind == 0:
            print(f"Writing files to {output_dir}")
            os.makedirs(output_dir, exist_ok=True)

        print(just_filename)
        img.save(
            os.path.join(output_dir, just_filename),
            quality="keep" if img.format == "JPEG" else 95,
            dpi=[DESIRED_DPI, DESIRED_DPI],
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filenames>")
        sys.exit(1)

    main()
