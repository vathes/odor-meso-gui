import datajoint as dj

odor = dj.create_virtual_module('odor', 'pipeline_odor')
mice = dj.create_virtual_module('mice', 'pipeline_mice')
experiment = dj.create_virtual_module('experiment', 'pipeline_experiment')
meso = dj.create_virtual_module('meso', 'pipeline_meso')
