#!/bin/bash

#SBATCH -t 2-00:00:00
#SBATCH -c 20
#SBATCH --mem=50GB
#SBATCH --mail-user=amarvi@mit.edu
#SBATCH --mail-type=TIME_LIMIT,FAIL,END
#SBATCH --job-name=mmselfsup_test
#SBATCH --gres=gpu:2
#SBATCH --constraint=ampere
#SBATCH --output=runlog/run%j.out
#SBATCH --partition=normal

# python -m torch.distributed.launch --nnodes=1 --node_rank=X --master_addr=X --nproc_per_node=X --master_port=X tools/train.py $CONFIG --launcher pytorch

# test training with a single gpu
python tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb64-amp-coslr-100e_in1k.py
