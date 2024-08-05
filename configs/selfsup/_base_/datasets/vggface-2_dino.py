# copied from mmselfsup/projects/dino/

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
        type='mmcls.CustomDataset',
        data_root='data/vggface/',
        ann_file='meta/vggface2_train_label.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline,
    ))
