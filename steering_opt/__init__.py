"""
A library for optimizing steering vectors in LLMs.
"""

from .steering_opt import (
    TrainingDatapoint,
    optimize_vector,
    optimize_vectors,
    make_steering_hook_hf,
    make_steering_hook_tflens,
    make_abl_mat,
    hf_hooks_contextmanager,
    get_completion_logprob,
    get_completion_logprob_hf,
    sample_most_likely_completions_hf,
    optimize_vector_minibatch_hf,
    make_melbo_loss_funcs
)

__version__ = "0.1" 