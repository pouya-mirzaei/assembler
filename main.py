import os
from pathlib import Path
from src.assembler import parse_assembly_code

# Paths
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)


def process_files():
    for input_file in INPUT_DIR.glob("*.in"):
        # Extract the number from the file name
        file_number = input_file.stem

        # Read the content of the input file
        with input_file.open("r") as file:
            file_content = file.read()

        # Parse the assembly code
        compiled_code = parse_assembly_code(file_content)

        output_file = OUTPUT_DIR / f"{file_number}.out"
        with output_file.open("w") as file:
            file.write(compiled_code)

        print(f"Processed {input_file} -> {output_file}")


if __name__ == "__main__":
    process_files()
