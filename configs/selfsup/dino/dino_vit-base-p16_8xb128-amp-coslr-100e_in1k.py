_base_ = [
    '../_base_/models/dino.py',                  # model
    '../_base_/schedules/adamw_coslr-100e_in1k.py',  # training schedule
    '../_base_/dino_runtime.py',                # runtime setting
]

# change to 128 batch size
train_pipeline = [ 
    dict(type='LoadImageFromFile'),
    dict(
        type='DINOMultiCrop',
        global_crops_scale=(0.4, 1.0),
        local_crops_scale=(0.05, 0.4),
        local_crops_number=8),
    dict(type='PackSelfSupInputs', meta_keys=['img_path'])
]
train_dataloader = dict(
    batch_size=128,
    num_workers=16,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type='mmcls.ImageNet',
        data_root='data/imagenet/',
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline,
    ))  
