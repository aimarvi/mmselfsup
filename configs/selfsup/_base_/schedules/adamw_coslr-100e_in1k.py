# copied from mmselfsup/projects/dino/

optimizer = dict(type='AdamW', lr=0.0024, betas=(0.9, 0.95), weight_decay=0.05)
optim_wrapper = dict(
    type='AmpOptimWrapper',
    optimizer=dict(
        type='AdamW', lr=0.0024, betas=(0.9, 0.95), weight_decay=0.05),
    paramwise_cfg=dict(
        custom_keys=dict(
            ln=dict(decay_mult=0.0),
            bias=dict(decay_mult=0.0),
            pos_embed=dict(decay_mult=0.0),
            mask_token=dict(decay_mult=0.0),
            cls_token=dict(decay_mult=0.0))),
    loss_scale='dynamic')
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=1e-09,
        by_epoch=True,
        begin=0,
        end=10,
        convert_to_iter_based=True),
    dict(
        type='CosineAnnealingLR',
        T_max=90,
        by_epoch=True,
        begin=10,
        end=100,
        convert_to_iter_based=True)
]
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=100)
