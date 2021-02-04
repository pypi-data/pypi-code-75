#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 10/07/2020
           """

import torch

from draugr import PROJECT_APP_PATH
from draugr.torch_utilities.writers.tensorboard import TensorBoardPytorchWriter
from draugr.writers import HistogramWriterMixin

__all__ = ["weight_bias_histograms"]

from warg import passes_kws_to


@passes_kws_to(TensorBoardPytorchWriter.histogram)
def weight_bias_histograms(
    writer: HistogramWriterMixin,
    model: torch.nn.Module,
    *,
    prefix: str = "",
    step: int = 0,
    recurse: bool = True,
    **kwargs
) -> None:
    """

  :param recurse:
  :param writer:
  :type writer:
  :param model:
  :type model:
  :param prefix:
  :type prefix:
  :param step:
  :type step:
  :param kwargs:
  :type kwargs:"""
    for name, param in model.named_parameters(prefix=prefix, recurse=recurse):
        writer.histogram(name, param.clone().cpu().data.numpy(), step, **kwargs)


if __name__ == "__main__":

    def a():
        with TensorBoardPytorchWriter(
            PROJECT_APP_PATH.user_log / "Tests" / "Writers"
        ) as writer:
            input_f = 4
            n_classes = 10

            model = torch.nn.Sequential(
                torch.nn.Linear(input_f, 20),
                torch.nn.ReLU(),
                torch.nn.Linear(20, n_classes),
                torch.nn.LogSoftmax(-1),
            )
            weight_bias_histograms(writer, model)

    a()
