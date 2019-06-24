genes_short = open('genes_w_subunits.txt', 'r').readlines()
genes_long = open('gene_names_ordered.txt','r').readlines()

list_combined = []

for line1, line2 in zip(genes_long, genes_short):
    list_combined.append('{0}({1})'.format(line1,line2.rstrip('\n')))

print list_combined
