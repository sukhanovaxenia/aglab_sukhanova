

#This script allows to generate reverse-complement sequence
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--fa",
        type = str,
        metavar = 'STRING',
        help = 'fasta file of your FILTERED genome sequence')

parser.add_argument("--out",
        type = str,
        metavar = 'STRING',
        help = 'output file of fasta with reverse-complement sequence')
args=parser.parse_args()

fFA = args.fa
fOUT = args.out

complement_table = str.maketrans({
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
    })
with open(fFA) as genome:
    first_line = genome.readline()
    lines = genome.read().split('\n')
lines = ''.join(lines)

rev_seq = lines[::-1].translate(complement_table)

with open(fOUT, 'w') as out:
    for i in rev_seq:
        out.write(i)


