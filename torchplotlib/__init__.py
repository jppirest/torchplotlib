import torch
import numpy as np
import matplotlib.pyplot as plt
from functools import wraps

def tensor_to_numpy(tensor):
    """Convert a torch tensor to a numpy array."""
    if isinstance(tensor, torch.Tensor):
        if tensor.requires_grad:
            tensor = tensor.detach()
        return tensor.cpu().numpy()
    return tensor

def patch_matplotlib_function(func):
    """Decorator to convert torch tensors to numpy for matplotlib functions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [tensor_to_numpy(arg) for arg in args]
        new_kwargs = {k: tensor_to_numpy(v) for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

def patch_matplotlib():
    """Patch common matplotlib functions to support torch tensors."""
    plotting_functions = [
        'plot', 'imshow', 'scatter', 'bar', 'barh', 'hist', 'hist2d',
        'pie', 'stem', 'stackplot', 'fill', 'fill_between', 'contour',
        'contourf', 'pcolormesh', 'tricontour', 'tricontourf'
    ]
    for func_name in plotting_functions:
        if hasattr(plt, func_name):
            original_func = getattr(plt, func_name)
            setattr(plt, func_name, patch_matplotlib_function(original_func))

patch_matplotlib()
#print("torchplotlib wrapped around matplotlib successfully!")
