"""Módulo onde armazeno meus aprendizados em pandas."""
import pandas as pd
from pathlib import Path

def ler_csv(caminho: Path) -> pd.DataFrame:
    """
    Lê um arquivo csv.
    
    Parameters
    ----------
    caminho : Path
        O caminho do arquivo csv.

    Returns
    -------
    pd.DataFrame
        Um dataframe do pandas.
    """
    return pd.read_csv(caminho)