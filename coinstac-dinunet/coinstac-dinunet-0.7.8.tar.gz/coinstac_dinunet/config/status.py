from enum import Enum as _Enum


class Phase(str, _Enum):
    INIT_RUNS = 'init_runs'
    INIT_NN = 'init_nn'
    PRE_COMPUTATION = 'pre_computation'
    COMPUTATION = 'computation'
    NEXT_RUN_WAITING = 'next_run_waiting'
    SUCCESS = 'success'


class Mode(str, _Enum):
    PRE_TRAIN = 'pre_train'
    TRAIN = 'train'
    VALIDATION = 'validation'
    TEST = 'test'
    VALIDATION_WAITING = 'validation_waiting'
    TRAIN_WAITING = 'train_waiting'


class Key(str, _Enum):
    TRAIN_LOG = 'train_log'
    TRAIN_METRICS = 'train_metrics'
    TRAIN_SERIALIZABLE = 'serializable_training_log'

    VALIDATION_LOG = 'validation_log'
    VALIDATION_METRICS = "validation_metrics"
    VALIDATION_SERIALIZABLE = 'serializable_validation_log'

    TEST_LOG = 'test_log'
    TEST_METRICS = 'test_metrics'
    TEST_SERIALIZABLE = 'serializable_test_log'

    GLOBAL_TEST_LOG = 'global_test_log'
    GLOBAL_TEST_METRICS = 'global_test_metrics'
    GLOBAL_TEST_SERIALIZABLE = 'serializable_global_test_log'
