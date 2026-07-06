def gc_content(sequence):
    sequence = sequence.upper().strip()

    valid_bases = {"A", "T", "G", "C"}

    if not all(base in valid_bases for base in sequence):
        print("Error: Invalid DNA sequence.")
        return

    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100

    print(f"\nSequence Length : {len(sequence)}")
    print(f"GC Count        : {gc_count}")
    print(f"GC Content      : {gc_percentage:.2f}%")

dna_sequence = input("Enter DNA sequence: ")

gc_content(dna_sequence)
