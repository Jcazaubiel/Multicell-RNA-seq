#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
from gtfparse import read_gtf


# In[91]:


# Create file names
nums = [2, 4, 16, 64, 128]
filenames = []

for i in nums:
    for j in range(i):
        name = 'N' + str(i) + 'c' + str(j) + '.kallisto'
        filenames.append(name)


# In[92]:


# Initialize the table with the transcript IDs from the first kallisto output
table = pd.read_csv(filenames[0] + '/abundance.tsv', sep = '\t')
table.drop(['length', 'eff_length', 'tpm', 'est_counts'], axis = 1, inplace = True)

# Remove decimals in the transcript ids
table['target_id'] = table['target_id'].str.split('.').str[0]

# Rename column to transcript_id
table.rename(columns={"target_id": "transcript_id"}, inplace = True)
table.head()


# In[ ]:


# Import gtf file
gtf = read_gtf("Mus_musculus.GRCm39.105.gtf")


# In[93]:


# Create dataframe to map transcript id to gene id, using the gtf file
id2gene = gtf[['gene_id', 'transcript_id']]

# Take the transcripts ids in the mapping file as a list 
transcript_ids = id2gene['transcript_id'].tolist()

# Get the indexes (or NA if there is no match) of the gene ids that match the transcript ids in order
gene_id_index = []
for transcript in table['transcript_id'].tolist():
    try:
        gene_id_index.append(transcript_ids.index(transcript))
    except ValueError:
        gene_id_index.append('NA')

# Create a column of gene IDs to add to the table, using the indexes gotten previously
gene_ids = []
for index in gene_id_index:
    if(index != 'NA'):
        gene_ids.append(id2gene['gene_id'].tolist()[index])
    else:
        gene_ids.append('NA')

# Add gene_id column to table
table['gene_id'] = gene_ids


# In[47]:

# Add columns for bulk and pseudo bulk
df = pd.read_csv('SRR9057198_GSM3767902_C-LTMR_3_Mus_musculus_RNA-Seq.kallisto/abundance.tsv', sep = '\t')
table['bulk'] = df['tpm']

df = pd.read_csv('SN_pseudo_bulk.kallisto/abundance.tsv', sep = '\t')
table['pseudo_bulk'] = df['tpm']


# Add columns for all clusters
for i in range(len(filenames)):
    df = pd.read_csv(filenames[i] + '/abundance.tsv', sep = '\t')
    table[filenames[i].replace('.kallisto', '')] = df['tpm']

table.to_csv('SN_table_tpm.tsv', sep = '\t', index = False)


# In[ ]:




