from Bio.Seq import Seq

with open("C:\\Users\\SACHIN.R\\OneDrive\\Desktop\\input.txt") as my_file:
    dna_sequence_from_file = my_file.read().strip()

# Create a Seq object from the DNA sequence
dna_sequence = Seq(dna_sequence_from_file)

# Transcribe the DNA sequence to RNA
rna_sequence = dna_sequence.transcribe()

# Print the resulting RNA sequence
print(rna_sequence)
