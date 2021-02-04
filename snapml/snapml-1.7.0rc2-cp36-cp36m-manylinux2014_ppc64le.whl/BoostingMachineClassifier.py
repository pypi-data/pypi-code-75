from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.class_weight import compute_sample_weight
from snapml import BoostingMachine
import numpy as np

class BoostingMachineClassifier(BaseEstimator, ClassifierMixin):

    """
    Boosting machine for binary classification tasks.

    A heterogeneous boosting machine that mixes binary decision trees (of
    stochastic max_depth) with linear models with random fourier features
    (approximation of kernel ridge regression).

    Parameters
    ----------
    num_round : int, default=100
        Number of boosting iterations.

    learning_rate : float, default=0.1
        Learning rate / shrinkage factor.

    random_state : int, default=0
        Random seed.

    colsample_bytree : float, default=1.0
        Fraction of feature columns used at each boosting iteration.

    subsample : float, default=1.0
        Fraction of training examples used at each boosting iteration.

    verbose : bool, default=False
        Print off information during training.

    lambda_l2 : float, default=0.0
        L2-reguralization penalty used during tree-building.

    early_stopping_rounds : int, default=10
        When a validation set is provided, training will stop if the
        validation loss does not increase after a fixed number of rounds.

    compress_trees : bool, default=False
        Compress trees after training for fast inference.

    base_score : float, default=None
        Base score to initialize boosting algorithm.
        If None then the algorithm will initialize the base score to be the 
        average target (regression) or the logit of the probability of the positive 
        class (binary classification).

    class_weight : {'balanced', None}, default=None
        If set to 'balanced' samples weights will be applied to
        account for class imbalance, otherwise no sample weights will be used.

    max_depth : int, default=None
        If set, will set min_max_depth = max_depth = max_max_depth

    min_max_depth : int, default=1
        Minimum max_depth of trees in the ensemble.

    max_max_depth : int, default=5
        Maximum max_depth of trees in the ensemble.

    n_jobs : int, default=1
        Number of threads to use during training.

    use_histograms : bool, default=True
        Use histograms to accelerate tree-building.

    hist_nbins : int, default=256
        Number of histogram bins.

    use_gpu : bool, default=False
        Use GPU for tree-building.

    gpu_id : int, default=0
        Device ID for GPU to use during training.

    tree_select_probability : float, default=1.0
        Probability of selecting a tree (rather than a kernel ridge regressor) at each boosting iteration.

    regularizer : float, default=1.0
        L2-regularization penality for the kernel ridge regressor.

    fit_intercept : bool, default=False
        Include intercept term in the kernel ridge regressor.

    gamma : float, default=1.0
        Guassian kernel parameter.

    n_components : int, default=10
        Number of components in the random projection.

    """

    def __init__(self, num_round=100, learning_rate=0.1, random_state=0, colsample_bytree=1.0,
                 subsample=1.0, verbose=False, lambda_l2=0.0, early_stopping_rounds=10,
                 compress_trees=False, base_score=None, class_weight=None, max_depth=None, 
                 min_max_depth=1, max_max_depth=5,
                 n_jobs=1, use_histograms=True, hist_nbins=256, use_gpu=False, gpu_id=0,
                 tree_select_probability=1.0, regularizer=1.0, fit_intercept=False, gamma=1.0,
                 n_components=10):

        self.num_round = num_round
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.colsample_bytree = colsample_bytree
        self.subsample = subsample
        self.verbose = verbose
        self.lambda_l2 = lambda_l2
        self.early_stopping_rounds = early_stopping_rounds
        self.compress_trees = compress_trees
        self.base_score = base_score
        self.class_weight = class_weight
        self.max_depth = max_depth
        self.min_max_depth = min_max_depth
        self.max_max_depth = max_max_depth
        self.n_jobs = n_jobs
        self.use_histograms = use_histograms
        self.hist_nbins = hist_nbins
        self.use_gpu = use_gpu
        self.gpu_id = gpu_id
        self.tree_select_probability = tree_select_probability
        self.regularizer = regularizer
        self.fit_intercept = fit_intercept
        self.gamma = gamma
        self.n_components = n_components


    def fit(self, X, y, sample_weight=None, X_val=None, y_val=None, sample_weight_val=None):

        """
        Fit the model according to the given train data.

        Parameters
        ----------
        X : dense matrix (ndarray)
            Train dataset

        y : array-like, shape = (n_samples,)
            The target vector corresponding to X.

        sample_weight : array-like, shape = (n_samples,)
            Training sample weights

        X_val : dense matrix (ndarray)
            Validation dataset

        y_val : array-like, shape = (n_samples,)
            The target vector corresponding to X_val.

        sample_weight_val : array-like, shape = (n_samples,)
            Validation sample weights

        Returns
        -------
        self : object
        """
        params = {
            'boosting_params': {
                'objective': 'logloss',
                'num_round': self.num_round,
                'learning_rate': self.learning_rate,
                'random_state': self.random_state,
                'colsample_bytree': self.colsample_bytree,
                'subsample': self.subsample,
                'verbose': self.verbose,
                'lambda_l2': self.lambda_l2,
                'early_stopping_rounds': self.early_stopping_rounds,
                'compress_trees': self.compress_trees,
                'base_score': self.base_score
            },
            'tree_params': {
                'min_max_depth': self.min_max_depth if self.max_depth is None else self.max_depth,
                'max_max_depth': self.max_max_depth if self.max_depth is None else self.max_depth,
                'num_threads': self.n_jobs,
                'use_histograms': self.use_histograms,
                'hist_nbins': self.hist_nbins,
                'use_gpu': self.use_gpu,
                'gpu_id': self.gpu_id,
                'select_probability': self.tree_select_probability
            },
            'ridge_params': {
                'regularizer': self.regularizer,
                'fit_intercept': self.fit_intercept,
                'num_threads': self.n_jobs
            },
            'kernel_params': {
                'gamma': self.gamma,
                'n_components': self.n_components,
                'num_threads': self.n_jobs
            }
        }

        self.classes_ = np.unique(y)

        if len(self.classes_) > 2:
            raise ValueError("Multiclass classification not supported for boosting.")

        y_snap = np.zeros_like(y, dtype=np.float32)
        y_val_snap = np.zeros_like(y_val, dtype=np.float32)

        self.ind2class_ = {}
        for i, c in enumerate(self.classes_):
            self.ind2class_[i] = c
            y_snap[y == c] = i
            y_val_snap[y_val == c] = i

        if self.class_weight == 'balanced':
            sample_weight = compute_sample_weight("balanced", y_snap)
            if y_val is not None:
                sample_weight_val = compute_sample_weight("balanced", y_val_snap)

        self.booster_ = BoostingMachine(params)
        self.booster_.fit(X, y_snap, sample_weight, X_val, y_val_snap, sample_weight_val)

    def predict(self, X, n_jobs=1):

        """
        Predict class labels


        Parameters
        ----------
        X : dense matrix (ndarray)
            Dataset used for predicting class estimates.

        n_jobs : int
            Number of threads to use for prediction.

        Returns
        -------
        pred: array-like, shape = (n_samples,)
            Returns the predicted class labels

        """

        pred = self.booster_.predict(X, n_jobs)

        for i, c in self.ind2class_.items():
            pred[(pred > 0) == i] = c

        return pred

    def predict_proba(self, X, n_jobs=1):

        """
        Predict class label probabilities


        Parameters
        ----------
        X : dense matrix (ndarray)
            Dataset used for predicting class estimates.

        n_jobs : int
            Number of threads to use for prediction.

        Returns
        -------
        proba: array-like, shape = (n_samples, 2)
            Returns the predicted class probabilities

        """

        return self.booster_.predict_proba(X, n_jobs)
