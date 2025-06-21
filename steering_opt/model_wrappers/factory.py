import torch
from model_wrappers.abstract import ModelWrapper
from model_wrappers.gemma3 import Gemma3Wrapper
from model_wrappers.default import DefaultModelWrapper


def get_model_wrapper(model: torch.nn.Module) -> ModelWrapper:
    if model.config.model_type == "gemma3":
        return Gemma3Wrapper(model)
    else:
        return DefaultModelWrapper(model)
