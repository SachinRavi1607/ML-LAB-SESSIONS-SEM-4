from Bio import pairwise2
from Bio.pairwise2 import format_alignment
seq1="AGTACGACAGCTCGAT"
seq2="TATGCT"
seq3="ATCGTACGATC"
seq4="GCTAGGGATC"
seq5="TGTCATAGTC"
seq6="CTAGCTAATCTC"
seq7="GGCTAGCTAG"
seq8="ACTGCTAATCG"
seq9="GACTGCAGCT"
seq10="CGATCGATC"
alignments=pairwise2.align.globalxx(seq1,seq2,seq3,seq4,seq5)
for alignment in alignments:
    print(format_alignment(*alignment))
    