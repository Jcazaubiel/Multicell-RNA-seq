#!/bin/bash
#SBATCH -J run_kallisto
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem=350G
python Cluster_merger.py