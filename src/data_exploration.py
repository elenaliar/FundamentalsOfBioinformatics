import numpy as np
import pandas as pd
import os
# Data inspection 

# Exercise 1

# How many HGVS ids does each dataset have?

vep_path = 'data/vep'
files = os.listdir(vep_path)
for i,file in enumerate(files):
    df_t = pd.read_csv(os.path.join(vep_path,file),sep="\t")
    n = len(pd.unique(df_t['# ID']))
    print(n)
    print(f"file: {i} {file}")
    print(df_t.head())
    #print(f"The file contains {num_ids} IDs")



df_bench = pd.read_csv("data/HGVS_2020_benchmark.tsv",sep="\t")
num_ids_bench = len(pd.unique(df_bench['# ID']))
print(f"Benchmark data contains {num_ids_bench} IDs")

#print(df_bench.head())


num_labels = df_bench['Label'].value_counts()
#print(f"There are: {num_labels}")
        