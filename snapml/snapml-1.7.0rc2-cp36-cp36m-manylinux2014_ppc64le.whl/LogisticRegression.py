# *****************************************************************
#
# Licensed Materials - Property of IBM
#
# (C) Copyright IBM Corp. 2017, 2020. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
#
# ******************************************************************

import numpy as np
import sys

from snapml.utils import _is_mpi_enabled, _param_check, _is_data_snapml_partition_type
from snapml._predict_utils import PredictTypes

_mpi_enabled = _is_mpi_enabled()

if sys.version_info[0] < 3:
    if _mpi_enabled:
        import libsnapmlmpi2 as libsnapml
    else:
        import libsnapmllocal2 as libsnapml
else:
    if _mpi_enabled:
        import snapml.libsnapmlmpi3 as libsnapml
    else:
        import snapml.libsnapmllocal3 as libsnapml

from snapml.GeneralizedLinearModelClassifier import GeneralizedLinearModelClassifier

from sklearn.base import BaseEstimator, ClassifierMixin

class LogisticRegression(GeneralizedLinearModelClassifier, BaseEstimator, ClassifierMixin):

    """
    Logistic Regression classifier

    This class implements regularized logistic regression using the IBM Snap ML solver.
    It supports both local and distributed(MPI) methods of the Snap ML solver. It
    can be used for both binary and multi-class classification problems. For multi-class
    classification it predicts only classes (no probabilities). It handles both dense and 
    sparse matrix inputs. Use csr, csc, ndarray, deviceNDArray or SnapML data partition format
    for training and csr, ndarray or SnapML data partition format for prediction.
    DeviceNDArray input data format is currently not supported for training with MPI implementation.
    We recommend the user to first normalize the input values.

    Parameters
    ----------
    max_iter : int, default=1000
        Maximum number of iterations used by the solver to converge.

    regularizer : float, default=1.0
        Regularization strength. It must be a positive float.
        Larger regularization values imply stronger regularization.

    use_gpu : bool, default=False
        Flag for indicating the hardware platform used for training. If True, the training
        is performed using the GPU. If False, the training is performed using the CPU.

    device_ids : array-like of int, default=[]
        If use_gpu is True, it indicates the IDs of the GPUs used for training.
        For single-GPU training, set device_ids to the GPU ID to be used for training, e.g., [0].
        For multi-GPU training, set device_ids to a list of GPU IDs to be used for training, e.g., [0, 1].

    class_weight : {'balanced', None}, default=None
        If set to 'None', all classes will have weight 1.

    dual : bool, default=True
        Dual or primal formulation.
        Recommendation: if n_samples > n_features use dual=True.

    verbose : bool, default=False
        If True, it prints the training cost, one per iteration. Warning: this will increase the
        training time. For performance evaluation, use verbose=False.

    n_jobs : int, default=1
        The number of threads used for running the training. The value of this parameter
        should be a multiple of 32 if the training is performed on GPU (use_gpu=True).

    penalty : {'l1', 'l2'}, default='l2'
        The regularization / penalty type. Possible values are "l2" for L2 regularization (LogisticRegression)
        or "l1" for L1 regularization (SparseLogisticRegression). L1 regularization is possible only for the primal
        optimization problem (dual=False).

    tol : float, default=0.001
        The tolerance parameter. Training will finish when maximum change in model coefficients is less than tol. 

    generate_training_history : {'summary', 'full', None}, default=None
        Determines the level of summary statistics that are generated during training.
        By default no information is generated (None), but this parameter can be set to "summary", to obtain 
        summary statistics at the end of training, or "full" to obtain a complete set of statistics 
        for the entire training procedure. Note, enabling either option will result in slower training.
        generate_training_history is not supported for DeviceNDArray input format.

    privacy : bool, default=False
        Train the model using a differentially private algorithm.
        Currently not supported for MPI implementation.

    eta : float, default=0.3
        Learning rate for the differentially private training algorithm.
        Currently not supported for MPI implementation.

    batch_size : int, default=100
        Mini-batch size for the differentially private training algorithm.
        Currently not supported for MPI implementation.

    privacy_epsilon : float, default=10.0
        Target privacy gaurantee. Learned model will be (privacy_epsilon, 0.01)-private.
        Currently not supported for MPI implementation.

    grad_clip : float, default=1.0
        Gradient clipping parameter for the differentially private training algorithm.
        Currently not supported for MPI implementation.

    fit_intercept : bool, default=False
        Add bias term -- note, may affect speed of convergence, especially for sparse datasets.

    intercept_scaling : float, default=1.0
        Scaling of bias term. The inclusion of a bias term is implemented by appending an additional feature to the 
        dataset. This feature has a constant value, that can be set using this parameter.

    Attributes
    ----------
    coef_ : array-like, shape (n_features, 1) for binary classification or
        (n_features, n_classes) for multi-class classification.
        Coefficients of the features in the trained model.

    support_ : array-like
        Indices of the features that contribute to the decision. (only available for L1)
        Currently not supported for MPI implementation.

    model_sparsity_ : float
        fraction of non-zeros in the model parameters. (only available for L1)
        Currently not supported for MPI implementation.

    training_history_ : dict
        Training history statistics.

    """

    PARAMS = [
        {"name": "max_iter", "attr": [{"type": "int", "ge": 1}]},
        {"name": "regularizer", "attr": [{"type": "float", "gt": 0}]},
        {"name": "device_ids", "attr": [{"type": "list"}]},
        {"name": "verbose", "attr": [{"type": "bool"}]},
        {"name": "class_weight", "attr": [{"values": [None, "balanced"]}]},
        {"name": "use_gpu", "attr": [{"type": "bool"}]},
        {"name": "n_jobs", "attr": [{"type": "int", "ge": 1}]},
        {"name": "dual", "attr": [{"type": "bool"}]},
        {"name": "penalty", "attr": [{"values": ["l1", "l2"]}]},
        {"name": "tol", "attr": [{"type": "float", "ge": 0}]},
        {"name": "generate_training_history", "attr": [{"values": [None, "summary", "full"]}]},
        {"name": "privacy", "attr": [{"type": "bool"}]},
        {"name": "eta", "attr": [{"type": "float", "gt": 0}]},
        {"name": "batch_size", "attr": [{"type": "int", "gt": 0}]},
        {"name": "grad_clip", "attr": [{"type": "float", "ge": 0}]},
        {"name": "privacy_epsilon", "attr": [{"type": "float", "gt": 0}]},
        {"name": "fit_intercept", "attr": [{"type": "bool"}]},
        {"name": "intercept_scaling", "attr": [{"type": "float", "gt": 0}]}
    ]

    def __init__(self,  max_iter = 1000, 
                        regularizer = 1.0, 
                        device_ids = [], 
                        verbose = False, 
                        use_gpu = False, 
                        class_weight = None, 
                        dual = True, 
                        n_jobs = 1, 
                        penalty = "l2",
                        tol = 0.001,
                        generate_training_history = None,
                        privacy = False,
                        eta = 0.3,
                        batch_size = 100,
                        privacy_epsilon = 10,
                        grad_clip = 1,
                        fit_intercept = False,
                        intercept_scaling = 1.0):

        self.max_iter = max_iter 
        self.regularizer = regularizer
        self.device_ids = device_ids
        self.verbose = verbose
        self.use_gpu = use_gpu
        self.class_weight = class_weight
        self.dual = dual
        self.n_jobs = n_jobs
        self.penalty = penalty
        self.tol = tol
        self.generate_training_history = generate_training_history
        self.fit_intercept = fit_intercept
        self.intercept_scaling = intercept_scaling
        self.privacy = privacy
        self.eta = eta
        self.batch_size = batch_size
        self.grad_clip = grad_clip
        self.privacy_epsilon = privacy_epsilon
        self.is_regression = 0
        self.num_train_unique_labs = 0
        self.model_size = 0
        self.labels_flag = False
        self.params = LogisticRegression.PARAMS
        self.standard_predict_type = PredictTypes.linear_classification

    def param_check(self):
        for varname, value in self.__dict__.items():
            if varname not in ['is_regression', 'params', 'standard_predict_type',
                               'num_train_unique_labs', 'model_size', 'labels_flag']:
                _param_check(self.params, varname, value)  

    def c_fit(self,
                    balanced,
                    col_major,
                    num_ex,
                    num_ft,
                    num_nz,
                    indptr,
                    indices,
                    data,
                    labs,
                    gpu_data_ptr,
                    gpu_lab_ptr,
                    gpu_matrix,
                    X_train_ptr_,
                    X_train_type_,
                    generate_training_code):

        # Train the model
        out_fit = libsnapml.lr_fit( self.max_iter,
                                    self.regularizer,
                                    1,
                                    self.verbose,
                                    balanced,
                                    self.use_gpu,
                                    self.n_jobs,
                                    col_major,
                                    num_ex,
                                    num_ft,
                                    num_nz,
                                    indptr,
                                    indices,
                                    data,
                                    labs,
                                    gpu_data_ptr,
                                    gpu_lab_ptr,
                                    gpu_matrix,
                                    self.device_ids,
                                    X_train_ptr_,
                                    X_train_type_,
                                    self.penalty,
                                    self.tol,
                                    generate_training_code,
                                    self.privacy,
                                    self.eta,
                                    self.batch_size,
                                    self.grad_clip,
                                    self.privacy_epsilon,
                                    self.is_regression,
                                    self.fit_intercept,
                                    self.intercept_scaling)

        return out_fit

    def post_training(self, gpu_matrix, training_metadata, X_train, _mpi_enabled, num_ft):
        self.num_train_unique_labs = int(training_metadata['num_uniq_labs'])
        self.classes_ = np.array(training_metadata['uniq_labs'])
        if _is_data_snapml_partition_type(X_train) or _mpi_enabled:
            #For snap-ml-local with non-snap-partition-type 'labels_flag' is set differently
            self.labels_flag = int(training_metadata['labs_converted'])

        self.n_features_in_ = num_ft

    def c_predict(self, n_jobs, pred_vars):


        pred, pred_metadata = \
            libsnapml.lr_predict(pred_vars.num_ex,
                                 pred_vars.num_ft,
                                 pred_vars.indptr,
                                 pred_vars.indices,
                                 pred_vars.data,
                                 self.model_,
                                 pred_vars.X_ptr_,
                                 pred_vars.X_type_,
                                 self.model_size,
                                 pred_vars.num_train_unique_labs,
                                 self.is_regression,
                                 n_jobs,
                                 self.fit_intercept,
                                 self.intercept_scaling)

        return pred, pred_metadata

    def predict_proba(self, X, n_jobs=0):

        """
        Probability estimates

        The returned probability estimates for the two classes.
        Only for binary classification. 

        Parameters
        ----------
        X : Dataset used for predicting probability estimates. Supports the following input data-types :
            1. Sparse matrix (csr_matrix, csc_matrix) or dense matrix (ndarray)
            2. SnapML data partition of type DensePartition, SparsePartition or ConstantValueSparsePartition

        n_jobs : int, default : 0
            Number of threads used to run inference.
            By default inference runs with maximum number of available threads.
            This parameter is ignored for predict_proba of a single observation.

        Returns
        -------
        proba: array-like of shape (n_samples, 2) or (n_samples, 1)
            Probability of the sample of each of the two classes for local implementation.
            Probability of the positive class only for the MPI implementation.

        """
        if (self.num_train_unique_labs > 2):
            raise ValueError("predict_proba is currently not supported for multi-class classification. Use predict to compute the class estimates.")

        is_single, pred, pred_vars = self.pre_predict_is_single(X, _mpi_enabled, self.standard_predict_type)

        if is_single == False:
            # Multi-row or snap-data or MPI
            pred, proba_metadata = libsnapml.lr_predict_proba(pred_vars.num_ex,
                                                               pred_vars.num_ft,
                                                               pred_vars.indptr,
                                                               pred_vars.indices,
                                                               pred_vars.data,
                                                               self.model_,
                                                               pred_vars.X_ptr_,
                                                               pred_vars.X_type_,
                                                               self.model_size,
                                                               pred_vars.num_train_unique_labs,
                                                               self.is_regression,
                                                               n_jobs,
                                                               self.fit_intercept,
                                                               self.intercept_scaling)

        return np.array(pred)

    def predict_log_proba(self, X, n_jobs=0):

        """
        Log of probability estimates

        The returned log-probability estimates for the two classes.
        Only for binary classification.

        Parameters
        ----------
        X : Dataset used for predicting log-probability estimates. Supports the following input data-types :
            1. Sparse matrix (csr_matrix, csc_matrix) or dense matrix (ndarray)
            2. SnapML data partition of type DensePartition, SparsePartition or ConstantValueSparsePartition

        n_jobs : int, default : 0
            Number of threads used to run inference.
            By default inference runs with maximum number of available threads.
            This parameter is ignored for predict_log_proba of a single observation.

        Returns
        -------
        proba: array-like of shape (n_samples, 2) or (n_samples, 1)
            Log-probability of the sample of each of the two classes for local implementation.
            Log-probability of the positive class only for the MPI implementation.
        """

        if (self.num_train_unique_labs > 2):
            raise ValueError("predict_log_proba is currently not supported for multi-class classification. Use predict to compute the class estimates.")

        is_single, pred, pred_vars = self.pre_predict_is_single(X, _mpi_enabled, self.standard_predict_type)

        if is_single == False:
            # Multi-row or snap-data or MPI
            pred, proba_metadata = libsnapml.lr_predict_log_proba(pred_vars.num_ex,
                                                                   pred_vars.num_ft,
                                                                   pred_vars.indptr,
                                                                   pred_vars.indices,
                                                                   pred_vars.data,
                                                                   self.model_,
                                                                   pred_vars.X_ptr_,
                                                                   pred_vars.X_type_,
                                                                   self.model_size,
                                                                   pred_vars.num_train_unique_labs,
                                                                   self.is_regression,
                                                                   n_jobs,
                                                                   self.fit_intercept,
                                                                   self.intercept_scaling)

        return np.array(pred)

