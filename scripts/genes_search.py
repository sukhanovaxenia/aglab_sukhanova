
def gene_search(seq, forward, reverse):
        with open(seq) as genome:
                first_line=genome.readline()
                    lines=genome.read().split('\n')
                    lines=''.join(lines)

        def build_kmers(ksize, sequ):
                kmer=[]
                n_kmers = len(sequ)-ksize+1
                for i in range(n_kmers):
                    kmer.append(sequ[i:i+ksize])
                return(kmer)

        all_kmers = build_kmers(ksize=3, sequ=lines)

        def gene_filt(seq, kmers,out):   
            start = 'ATG'
            stop = ['TAG', 'TGA','TAA']
            pos_dict = {'start': [], 'stop':[]}
            position=[]
            genes=[]
            genes2=[]
            #Filtration of potential genes:    
            for i in range(len(kmers)):
                if kmers[i] != start:
                    continue
                starting=i
                for j in range(starting, len(kmers)):
                    if kmers[j] in stop:
                        ending=j
                        pos_dict['start'].append(starting)
                        pos_dict['stop'].append(ending)
                        position.append((starting,ending))
                        break
            #Search for promoter: 
            for i in range(len(position)):
                if int(position[i][1]-position[i][0]) > 60:
                    genes.append(seq[position[i][0]:position[i][1]])
                    AT_count_1=seq[position[i][0]-16:position[i][0]-10].count('A') + seq[position[i][0]-16:position[i][0]-10].count('T')
                    AT_count_2=seq[position[i][0]-41:position[i][0]-35].count('A') + seq[position[i][0]-41:position[i][0]-35].count('T')
                    #print(AT_count_1+AT_count_2)
                    #print((AT_count_1+AT_count_2)/12)
                    if  0.5 <((AT_count_1+AT_count_2)/12) < 0.95:  
                        genes2.append(seq[position[i][0]:position[i][1]])
            with open(out, 'w') as g:
                for each,i in enumerate(genes2):
                    g.write('>'+'gene_'+i+'\n')
                    g.write(each)
        gene_filt(seq=lines, kmers = all_kmers, out=forward)
        #Get genes for reverse complement strand
        COMPLEMENTARY_TABLE = str.maketrans({
            'A': 'T', 
            'T': 'A', 
            'C': 'G', 
            'G': 'C'
        })

        def reverse(seq):
            return seq[::-1]

        def complement(seq):
            return seq.translate(COMPLEMENTARY_TABLE)
        rev_seq=complement(reverse(lines))

        all_kmers_rev=build_kmers(3, rev_seq)
        gene_filt(seq=rev_seq, kmers=all_lmers_rev, out=reverse)


