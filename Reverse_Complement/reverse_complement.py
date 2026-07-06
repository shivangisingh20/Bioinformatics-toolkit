def reverse_complement(sequence):
    sequence = sequence.upper()

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_seq = sequence[::-1]

    reverse_comp = ""

    for base in reverse_seq:
        reverse_comp += complement[base]

    return reverse_comp


dna = input("Enter DNA sequence: ")

print("Reverse Complement:", reverse_complement(dna))
