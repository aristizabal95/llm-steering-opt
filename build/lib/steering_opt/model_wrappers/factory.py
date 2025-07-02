import torch
from steering_opt.model_wrappers.abstract import ModelWrapper
from steering_opt.model_wrappers.gemma3 import Gemma3Wrapper
from steering_opt.model_wrappers.default import DefaultModelWrapper


def get_model_wrapper(model: torch.nn.Module) -> ModelWrapper:
    if model.config.model_type == "gemma3":
        return Gemma3Wrapper(model)
    else:
        return DefaultModelWrapper(model)
