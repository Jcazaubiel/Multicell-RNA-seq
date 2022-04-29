#!/bin/bash
#SBATCH -J run_kallisto
#SBATCH -N 1
#SBATCH -n 8
module load kallisto/gcc-8.2.0/0.45.1
for file in *.fastq.gz
do
outname="${file%.fastq.gz}.kallisto"
kallisto quant -t $SLURM_NTASKS -i our_index.idx --single -l 300 -s 20 -b 50 -o $outname  $file
done
