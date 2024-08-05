_base_ = [
    '../_base_/models/dino.py',                  # model
    '../_base_/schedules/adamw_coslr-100e_in1k.py',  # training schedule
    '../_base_/datasets/vggface-2_dino.py',     # dataset
    '../_base_/dino_runtime.py',                # runtime setting
]
