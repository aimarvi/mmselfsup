#!/bin/bash

#SBATCH -t 5-00:00:00
#SBATCH -c 20
#SBATCH --mem=40GB
#SBATCH --mail-user=amarvi@mit.edu
#SBATCH --mail-type=TIME_LIMIT,FAIL,END
#SBATCH --job-name=face-dino
#SBATCH --gres=gpu:a100:1
#SBATCH --constraint=ampere
#SBATCH --output=runlog/run%j.out
#SBATCH --partition=nklab


# test training with a single gpu (this works. now make it work with multi-gpus)
# python tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb64-amp-coslr-100e_mini-obj.py
# python tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb64-amp-coslr-100e_mini-face.py
# python tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb128-amp-coslr-100e_in1k.py
python tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb128-amp-coslr-100e_face.py

# test training with multi-gpu
# python -u tools/train.py configs/selfsup/dino/dino_vit-base-p16_8xb64-amp-coslr-100e_in1k.py --launcher="slurm" --amp
