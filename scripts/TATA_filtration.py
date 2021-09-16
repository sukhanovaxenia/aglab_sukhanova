

#This script helps to filter potential genes by the length and promoter sequences:

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--fa",
        type = str,
        metavar = 'STRING',
        help = 'fasta file of genome')
parser.add_argumen("--p",
        type = str,
        metavar = 'STRING',
        help = 'list of posiitons of potential start and stop codons')
parser.add_argument("--out",
        type = str,
        metavar = 'STRING',
        help = 'output file of predicted genes after filtration')

args = parser.parse_args()

fFA=args.fa
fPOS=args.p
fOUT=args.out

with open(fFA) as genome:
    first_line = genome.readline()
    seq=genome.read().split('\n')
seq=''.join(seq)

with open(fPOS) as p:
    pos = [each.strip() for each in p]

genes=[]

for i in range(len(pos)):
    if int(pos[i][1]-pos[i][0]) > 60:
        AT_count_1=seq[pos[i][0]-16:position[i][0]-10].count('A') + seq[position[i][0]-16:position[i][0]-10].count('T')
        AT_count_2=seq[position[i][0]-41:position[i][0]-35].count('A') + seq[position[i][0]-41:position[i][0]-35].count('T')
        if 0.5 < ((AT_count_1+AT_count_2)/12) < 0.95:
                genes.append(seq[pos[i][0]:pos[i][1]])

with open(fOUT, 'w') as g:
    for each, i in enumerate(genes):
        g.write('>'+'gene_'+i+'\n')
        g.write(each+'\n')




