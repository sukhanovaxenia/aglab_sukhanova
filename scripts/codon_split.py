


#For 3-mer extraction, which provide splitting the genome by codons.

from argparse import ArgumentParser

parser=ArgumentParser()

parser.add_argument("--fa",
        type = str,
        metavar = 'STRING',
        help = 'fasta file of genome sequence')
parser.add_argumen("--k",
        type = int,
        metavar = 'INT',
        help = 'size of kmers')
parser.add_argument("--out",
        type = str,
        metavar = 'STRING',
        help = "output fasta file of codons")

args = parser.parse_args()

fFA=args.fa
ksize=args.k
fOUT=args.out

with open(fFA) as genome:
    first_line = genome.readline()
    lines = genome.read().split('\n')
lines=''.join(lines)

    
n_kemrs = len(lines)-ksize+1
with open(fOUT, 'w') as c:
    for i in range(n_kmers):
        c.write(lines[i:i+ksize])


