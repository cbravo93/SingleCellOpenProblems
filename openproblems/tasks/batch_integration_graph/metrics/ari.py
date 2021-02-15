import numpy as np

from ....tools.decorators import metric
from scIB.metrics import ari
from scIB.clustering import opt_louvain


@metric(
    metric_name="ARI",
    maximize=True,
    # image="openproblems-template-image" # only if required
)
def ari(adata):
    res_max, nmi_max, nmi_all = opt_louvain(adata,
                label_key='labels', cluster_key='cluster', function=nmi,
                plot=False, verbose=verbose, inplace=True, force=True)
    return ari(adata, group1='cluster', group2='labels')