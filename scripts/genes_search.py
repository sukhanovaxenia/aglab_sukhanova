

with open('/mnt/c/Users/sukha/Downloads/ecoli_10K.fasta') as genome:
        first_line=genome.readline()
            lines=genome.read().split('\n')
            lines=''.join(lines)

def build_kmers(ksize, seq):
        kmer=[]
        n_kmers = len(seq)-ksize+1
        for i in range(n_kmers):
            kmer.append(seq[i:i+ksize])
        return(kmer)

all_kmers = build_kmers(ksize=3, seq=lines)

start = 'ATG'
stop = ['TAG', 'TGA','TAA']
pos_dict = {'start': [], 'stop':[]}
position=[]
genes=[]
genes2=[]
for i in range(len(all_kmers)):
    if all_kmers[i] != start:
        continue
    starting=i
    for j in range(starting, len(all_kmers)):
        if all_kmers[j] in stop:
            ending=j
            pos_dict['start'].append(starting)
            pos_dict['stop'].append(ending)
            position.append((starting,ending))
            break
for i in range(len(position)):
    if int(position[i][1]-position[i][0]) > 60:
        genes.append(lines[position[i][0]:position[i][1]])
        AT_count=lines[position[i][0]-35:position[i][1]-10].count('A') + lines[position[i][0]-35:position[i][1]-10].count('T')
        if  0.5 <(AT_count/len(lines[position[i][0]-35:position[i][1]-10])) < 0.8:  
            genes2.append(lines[position[i][0]:position[i][1]])
with open('genes_unTATA.fa', 'w') as f:
    for each in genes:
        f.write('gene_1'+'\n')
        f.write(each)

with open('genes_TATA.fa', 'w') as g:
    for each in genes2:
        g.write('gene_1'+'\n')
        g.write(each)
