def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100

dna = input("Enter DNA sequence: ")

gc = gc_content(dna)

print(f"GC Content: {gc:.2f}%")
