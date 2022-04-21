import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from scipy import linalg
from scipy import sparse
from scipy.sparse.linalg import svds

def svd_decompose(X, n_component):
  
    n, m = X.shape
    # Compute full SVD
    U, S, V = svds(X)
    S = S[::-1]
    U = U[:, ::-1]
    V = V[::-1]
    X_svd = np.dot(U, np.diag(S))

    return X_svd[:,:n_component]

def svd_visual(out):
    x_df2 = pd.DataFrame(out, columns=['X1', 'X2'])
    plt.figure(figsize = (6,6))
    sb.scatterplot(data = x_df2 , x = 'X1',y = 'X2')