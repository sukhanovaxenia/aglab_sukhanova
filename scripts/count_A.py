from Bio import SeqIO
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("--fa",
        type = str,
        metavar = "STRING",
        help="fasta file of genome")
args = parser.parse_args()

fFA=args.fa

genome = SeqIO.parse(open(fFA), 'fasta')
counter=0

for read in genome:
    counter+=read.upper().seq.count('A')
print(counter)
