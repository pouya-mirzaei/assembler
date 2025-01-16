INSTRUCTION_TABLE = {
    "AND": {"opcode": "0000", "description": "AND M to AC"},
    "ADD": {"opcode": "0001", "description": "Add M to AC, carry to E"},
    "LDA": {"opcode": "0010", "description": "Load AC from M"},
    "STA": {"opcode": "0011", "description": "Store AC in M"},
    "BUN": {"opcode": "0100", "description": "Branch unconditionally to M"},
    "BSA": {
        "opcode": "0101",
        "description": "Save return address in M and branch to M+1",
    },
    "ISZ": {"opcode": "0110", "description": "Increment M and skip if zero"},
    "CLA": {"opcode": "7800", "description": "Clear AC"},
    "CLE": {"opcode": "7400", "description": "Clear E"},
    "CMA": {"opcode": "7200", "description": "Complement AC"},
    "CME": {"opcode": "7100", "description": "Complement E"},
    "CIR": {"opcode": "7080", "description": "Circulate right E and AC"},
    "CIL": {"opcode": "7040", "description": "Circulate left E and AC"},
    "INC": {"opcode": "7020", "description": "Increment AC"},
    "SPA": {"opcode": "7010", "description": "Skip if AC is positive"},
    "SNA": {"opcode": "7008", "description": "Skip if AC is negative"},
    "SZA": {"opcode": "7004", "description": "Skip if AC is zero"},
    "SZE": {"opcode": "7002", "description": "Skip if E is zero"},
    "HLT": {"opcode": "7001", "description": "Halt computer"},
    "INP": {"opcode": "F800", "description": "Input information and clear flag"},
    "OUT": {"opcode": "F400", "description": "Output information and clear flag"},
    "SKI": {"opcode": "F200", "description": "Skip if input flag is on"},
    "SKO": {"opcode": "F100", "description": "Skip if output flag is on"},
    "ION": {"opcode": "F080", "description": "Turn interrupt on"},
    "IOF": {"opcode": "F040", "description": "Turn interrupt off"},
}


def parse_assembly_code(assembly_code):
    # Parse the assembly code and return a list of instructions
    return "Hello World"
