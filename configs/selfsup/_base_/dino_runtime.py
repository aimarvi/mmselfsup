# copied from mmselfsup/projects/dino/

default_scope = 'mmselfsup'
default_hooks = dict(
    runtime_info=dict(type='RuntimeInfoHook'),
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=100),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(type='CheckpointHook', interval=1, max_keep_ckpts=1),
    sampler_seed=dict(type='DistSamplerSeedHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
    dist_cfg=dict(backend='nccl'))
log_processor = dict(
    window_size=10,
    custom_cfg=[dict(data_src='', method='mean', window_size='global')])
vis_backends = [dict(type='LocalVisBackend')]
visualizer = dict(
    type='SelfSupVisualizer',
    vis_backends=[dict(type='LocalVisBackend')],
    name='visualizer')
log_level = 'INFO'
load_from = None
resume = True
randomness = dict(seed=2, diff_rank_seed=True)
custom_hooks = [
    dict(
        type='DINOTeacherTempWarmupHook',
        warmup_teacher_temp=0.04,
        teacher_temp=0.04,
        teacher_temp_warmup_epochs=0,
        max_epochs=100)
]
