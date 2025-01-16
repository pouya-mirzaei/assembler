from .utils import hex_to_bin, generate_output, dec_to_bin

MRI_TABLE = {
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
}


NON_MRI_TABLE = {
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


PSEUDO_INSTRUCTION_TABLE = ["ORG", "END", "DEC", "HEX"]

SYMBOL_TABLE = {}


LC = 0


def first_pass(assembly_code):
    global LC
    SYMBOL_TABLE = {}
    LC = 0

    lines = assembly_code.split("\n")
    for line in lines:
        line = line.strip().split()

        if len(line) == 0:
            continue

        if line[0] in PSEUDO_INSTRUCTION_TABLE:
            if line[0] == "ORG":
                LC = int(line[1])
                continue
            elif line[0] == "END":
                break
        else:
            if line[0].endswith(","):
                SYMBOL_TABLE[line[0][:-1]] = LC

        LC += 1
    return SYMBOL_TABLE


def second_pass(assembly_code, SYMBOL_TABLE):
    global LC
    LC = 0

    results = []
    rs = {}

    lines = assembly_code.split("\n")
    for i, line in enumerate(lines):
        line = line.strip().split()

        if len(line) == 0:
            continue

        if line[0] in PSEUDO_INSTRUCTION_TABLE or (
            len(line) > 1 and line[1] in PSEUDO_INSTRUCTION_TABLE
        ):
            if line[0] == "ORG":
                LC = int(line[1])
                continue
            elif line[0] == "END":
                break
            else:
                # dec or hex instruction
                if line[0][:-1] not in SYMBOL_TABLE:
                    return f"Error: Symbol {line[1][:-1]} not found on line {i+1}"

                if line[1] == "DEC":
                    rs = {"location": LC, "Content": dec_to_bin(int(line[2]))}
                elif line[1] == "HEX":
                    rs = {"location": LC, "Content": hex_to_bin(line[2])}
                else:
                    return (
                        f"Error: Pseudo instruction {line[1]} not found on line {i+1}"
                    )
        else:
            # MRI instruction
            if line[0] == "HLT":
                rs = {
                    "location": LC,
                    "Content": hex_to_bin(NON_MRI_TABLE["HLT"]["opcode"]),
                }
            elif line[0] in MRI_TABLE:
                opcode = MRI_TABLE[line[0]]["opcode"]
                if line[1] not in SYMBOL_TABLE:
                    return f"Error: Symbol {line[1]} not found on line {i+1}"

                address = SYMBOL_TABLE[line[1]]

                if len(line) > 2 and line[2] == "I":
                    opcode[0] = "1"
                address = f"{address:04b}"
                address = address.zfill(12)
                word = f"{opcode}{address}"

                rs = {"location": LC, "Content": word}

            else:
                if line[0] in NON_MRI_TABLE:
                    # non MRI instruction
                    opcode = NON_MRI_TABLE[line[0]]["opcode"]
                    word = f"{hex_to_bin(opcode)}"

                    rs = {"location": LC, "Content": word}
                else:
                    # error
                    return f"Error: Instruction {line[0]} not found on line {i+1}"

        results.append(rs)
        LC += 1

    return generate_output(results)


def parse_assembly_code(assembly_code):
    SYMBOL_TABLE = first_pass(assembly_code)
    return second_pass(assembly_code, SYMBOL_TABLE)
