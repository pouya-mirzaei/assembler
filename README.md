# Basic Assembler

A Python-based assembler that converts assembly language code into binary machine code. This project implements a two-pass assembler supporting Memory-Reference Instructions (MRI) and non-MRI operations.

## Features

- Two-pass assembly process
- Support for Memory-Reference Instructions (MRI)
- Support for non-MRI operations
- Handles pseudo-instructions (ORG, END, DEC, HEX)
- Symbol table generation
- Binary and hexadecimal conversion utilities

## Supported Instructions

### Memory-Reference Instructions (MRI)

- AND: AND memory to accumulator
- ADD: Add memory to accumulator
- LDA: Load accumulator from memory
- STA: Store accumulator to memory
- BUN: Branch unconditionally
- BSA: Branch and save return address
- ISZ: Increment and skip if zero

### Non-MRI Instructions

- Register operations (CLA, CLE, CMA, CME)
- Circular shift operations (CIR, CIL)
- Skip operations (SPA, SNA, SZA, SZE)
- I/O operations (INP, OUT, SKI, SKO)
- Control operations (HLT, ION, IOF)

## Project Structure

```
.
├── input/          # Input assembly files (.in)
├── output/         # Generated binary files (.out)
├── src/
│   ├── assembler.py    # Main assembler logic
│   └── utils.py        # Utility functions
└── main.py        # Entry point
```

## Usage

1. Place your assembly code files with `.in` extension in the `input` directory
2. Run the assembler:
   ```bash
   python main.py
   ```
3. Find the generated binary output files in the `output` directory

## Input File Format

Assembly code should follow this format:

```assembly
ORG 100    / Set origin
LDA X      / Load value from X
ADD Y      / Add Y to accumulator
STA Z      / Store result in Z
HLT        / Halt program
X, DEC 5   / Variable X with decimal value 5
Y, HEX A   / Variable Y with hex value A
Z, DEC 0   / Variable Z initialized to 0
END        / End of program
```

## Output Format

The assembler generates binary machine code files with the same name as the input files but with `.out` extension.

## Requirements

- Python 3.6 or higher
- pathlib library (included in Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/basic-assembler.git
   ```
2. Navigate to the project directory:
   ```bash
   cd basic-assembler
   ```
