#!/bin/bash

#SBATCH -t 5-00:00:00
#SBATCH -c 20
#SBATCH --mem=100GB
#SBATCH --mail-user=amarvi@mit.edu
#SBATCH --mail-type=TIME_LIMIT,FAIL,END
#SBATCH --job-name=in1k-dino
#SBATCH --gres=gpu:a100:1
#SBATCH --constraint=ampere
#SBATCH --output=runlog/run%j.out
#SBATCH --partition=nklab

NNODES=1 bash projects/dino/tools/dist_train.sh projects/dino/config/dino_vit-base-p16_8xb64-amp-coslr-100e_in1k.py 1 --amp
