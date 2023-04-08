from nni.experiment import Experiment
experiment = Experiment('local')

search_space = {
    'features': {'_type': 'choice', '_value': [128, 256, 512, 1024]},
    'lr': {'_type': 'loguniform', '_value': [0.0001, 0.1]},
    'momentum': {'_type': 'uniform', '_value': [0, 1]},
}

experiment.config.trial_command = 'python model.py'
experiment.config.trial_code_directory = '.'
experiment.config.search_space = search_space

experiment.config.tuner.name = 'TPE'
experiment.config.tuner.class_args['optimize_mode'] = 'maximize'

experiment.config.max_trial_number = 10
experiment.config.trial_concurrency = 2

experiment.run(8080)
input('Press enter to quit')