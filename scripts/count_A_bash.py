import os
import sys
from argparse import ArgumentParser

parser=ArgumentParser()

parser.add_argument("--fa",
        type = str,
        metavar="STRING",
        help="fasta file of genome")

args=parser.parse_args()

fFA=args.fa

os.system(f"sed -e '/^>/d' {fFA} | tr a A| grep -o 'A' | wc -l") 
