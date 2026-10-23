import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    # Your implementation here
    ev      = torch.linalg.eigvals(matrix)   # complex eigenvalues
    ev_real = ev.real                        # real part only
    result  = ev_real.sort(descending=True)  # (values, indices)
    out     = result.values                  # tensor([3., 1.])
    # 1 line ans 
    # return torch.linalg.eigvals(matrix).real.sort(descending=True).values 

    return out
