

#This script allows to search for start and stop codons positions with limitation on the order (NOT stop befor start, OT nested codons)


from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--k",
        type = str,
        metavar = 'STRING',
        help = 'file with kmers')
parser.add_argument("--out",
        type = str,
        metavar = 'STRING',
        help = 'output file')

args = parser.parse_args()

fK=args.k
fOUT=args.out

start='ATG'
stop = ['TAG', 'TGA', 'TAA']

with open(fK) as k:
    kmers = [each.strip() for each in k]

position=[]

for i in range(len(kmers)):
    if kmers[i] != start:
        continue
    starting=i
    for j in range(starting, len(kmers)):
        if kmers[j] in stop:
            ending = j
            position.append((starting, ending))
            break
with open(fOUT, 'w') as out:
    out.write('\n'.join('%s %s' % x for x in position))
