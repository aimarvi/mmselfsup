# copied from mmselfsup/projects/dino/

model = dict(
    type='DINO',
    data_preprocessor=dict(
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True),
    backbone=dict(type='mmcls.VisionTransformer', arch='b', patch_size=16),
    neck=dict(
        type='DINONeck',
        in_channels=768,
        out_channels=65536,
        hidden_channels=2048,
        bottleneck_channels=256),
    head=dict(
        type='DINOHead',
        out_channels=65536,
        num_crops=10,
        student_temp=0.1,
        center_momentum=0.9))
