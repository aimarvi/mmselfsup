import argparse
import os
import pdb
import importlib
import setuptools
import torch
from torch import distributed as dist

rank = int(os.environ['RANK'])
print(rank)

num_gpus = torch.cuda.device_count()
print(num_gpus)

torch.cuda.set_device(rank % num_gpus)
dist.init_process_group(backend='nccl')

