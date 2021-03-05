# from ....tools.normalize import log_cpm
from .....tools.decorators import method
from .....tools.utils import check_version


@method(
    method_name="Scanorama",
    paper_name="Sc",
    paper_url="temp",
    paper_year=2020,
    code_url="",
    code_version=check_version("scanorama"),
    image="openproblems-python-batch-integration" # only if required
)
def scanorama_embed_full_unscaled(adata):
    from scIB.integration import runScanorama
    from scIB.preprocessing import hvg_batch
    from scIB.preprocessing import reduce_data
    from scIB.preprocessing import scale_batch
    adata = runScanorama(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    # Complete the result in-place
    return adata


def scanorama_embed_hvg_unscaled(adata):
    from scIB.integration import runScanorama
    from scIB.preprocessing import hvg_batch
    from scIB.preprocessing import reduce_data
    from scIB.preprocessing import scale_batch
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = runScanorama(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata


def scanorama_embed_hvg_scaled(adata):
    from scIB.integration import runScanorama
    from scIB.preprocessing import hvg_batch
    from scIB.preprocessing import reduce_data
    from scIB.preprocessing import scale_batch
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = scale_batch(adata, "batch")
    adata = runScanorama(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata


def scanorama_embed_full_scaled(adata):
    from scIB.integration import runScanorama
    from scIB.preprocessing import hvg_batch
    from scIB.preprocessing import reduce_data
    from scIB.preprocessing import scale_batch
    adata = scale_batch(adata, "batch")
    adata = runScanorama(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata