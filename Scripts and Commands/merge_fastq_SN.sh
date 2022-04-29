#!/bin/bash
#SBATCH -J run_kallisto
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem=300G

cat *fastq.gz > SN_pseudo_bulk.fastq.gz
