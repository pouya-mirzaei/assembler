def hex_to_bin(hex_value):
    # Convert hex to decimal
    decimal = int(hex_value, 16)

    return dec_to_bin(decimal)


def generate_output(rs):
    # Initialize an empty list to hold formatted lines
    output_lines = [f"{'Location':<10} {'Content'}", "-" * 30]

    # Iterate over each entry in the array of rs
    for entry in rs:
        # Format each line as 'location content', and append it to the list
        output_lines.append(f"{entry['location']:<10} {entry['Content']}")

    # Join all the lines into a single string with newlines separating them
    return "\n".join(output_lines)


def dec_to_bin(decimal):
    # Check if the number is negative
    if decimal < 0:
        # Two's complement for negative numbers
        binary_value = bin((1 << 16) + decimal)[2:].zfill(16)
    else:
        # Convert the decimal to binary and pad to 16 bits
        binary_value = bin(decimal)[2:].zfill(16)

    return binary_value
