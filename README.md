# torchplotlib 

**torchplotlib** is a simple wrapper that **patches matplotlib** to support plotting of **pytorch tensors** — no more manual `.cpu().detach().numpy()` calls.

This is especially useful for deep learning workflows and experiments where you want to quickly visualize tensor data without worrying about device or gradient issues.

## Installation

### Option 1: Install directly via pip

```bash
pip install git+https://github.com/jppirest/torchplotlib.git
```

### Option 2: Clone and install locally

```bash
git clone https://github.com/yourusername/torchplotlib.git
cd torchplotlib
pip install .
```

## Usage

```python
import torchplotlib  
import matplotlib.pyplot as plt
import torch

# Create a tensor on GPU with requires_grad=True
device = 'cuda' if torch.cuda.is_available() else 'cpu'
x = torch.randn((128, 128), device="cuda", requires_grad=True)

# Plot it directly — no need for .detach().cpu().numpy()
plt.imshow(x)
plt.title("No Detach Needed 🚀")
plt.colorbar()
plt.show()
```
