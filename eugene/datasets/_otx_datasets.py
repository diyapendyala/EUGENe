from pathlib import Path
import pandas as pd
import pyranges as pr
from .._compat import Literal
from ..dataloading._io import read
from ..dataloading import SeqData

HERE = Path(__file__).parent
pkg_resources = None


def get_dataset_info():
    """
    Return DataFrame with info about builtin datasets.
    Returns
        Info about builtin datasets indexed by dataset name as dataframe.
    """
    global pkg_resources
    if pkg_resources is None:
        import pkg_resources
    stream = pkg_resources.resource_stream(__name__, "datasets.csv")
    return pd.read_csv(stream, index_col=0)


def ols(**kwargs: dict) -> pd.DataFrame:
    """
    reads the OLS dataset.
    """
    filename = "/cellar/users/aklie/projects/EUGENE/data/2021_OLS_Library/2021_OLS_Library.tsv"
    data = read(filename, seq_col="SEQ", name_col="NAME", target_col="ACTIVITY_SUMRNA_NUMDNA", **kwargs)
    return data


def Khoueiry10(**kwargs: dict) -> pd.DataFrame:
    """
    Reads the Khoueiry10 dataset.
    """
    filename = "/cellar/users/aklie/projects/EUGENE/data/2010_Khoueiry_CellPress/2010_Khoueiry_CellPress.tsv"
    data = read(filename, seq_col="SEQ", name_col="NAME", target_col="FXN_LABEL", **kwargs)
    return data