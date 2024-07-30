_base_ = [
    '../_base_/models/dino.py',                  # model
    '../_base_/datasets/imagenet_dino.py',       # data
    '../_base_/schedules/adamw_coslr-100e_in1k.py',  # training schedule
    '../_base_/dino_runtime.py',                # runtime setting
]
