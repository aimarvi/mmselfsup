_base_ = [ 
    '../_base_/models/dino.py',                  # model
    '../_base_/datasets/imagenet_dino.py',       # data
    '../_base_/schedules/adamw_coslr-100e_in1k.py',  # training schedule
    '../_base_/dino_runtime.py',                # runtime setting
]

# custom dataset config

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
    batch_size=64,
    num_workers=16,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type='mmcls.CustomDataset',
        data_root='/om2/group/nklab/shared/datasets/vgg_face2/jpgs/train/',
        ann_file='/om2/user/amarvi/mmselfsup/data/mini_face_train_label.txt',
        data_prefix=dict(img_path='./'),
        pipeline=train_pipeline,
    ))  
