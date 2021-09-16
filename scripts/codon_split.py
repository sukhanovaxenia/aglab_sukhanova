


#For 3-mer extraction, which provide splitting the genome by codons.

def kmer_extraction(seq, ksize):
    with open(seq) as genome:
        first_line = genome.readline()
        lines = genome.read().split('\n')
    lines=''.join(lines)

    
    n_kemrs = len(lines)-ksize+1
    with open('codon_seq.fa', 'w') as c:
        for i in range(n_kmers):
            c.write(lines[i:i+ksize])


