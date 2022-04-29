#!/bin/bash
#SBATCH -J create_table
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem=350G
python create_table.py