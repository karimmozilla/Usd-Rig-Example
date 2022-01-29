from pxr import Usd
import os
import contextlib


def get_default_prim(stage):
    """
    Get the default prim for the stage

    Args:
        stage (UsdStage): the usd stage which has default prim

    Returns:
        [UsdPrim]: the prim assigned as default prim for the stage
    """
    return stage.GetDefaultPrim()


def create_open_stage(filepath):
    """
    create stage if not exist or open it

    Args:
        filepath (str): the path of usd file

    Returns:
        stage (UsdStage): the opened or created usd stage
    """
    if os.path.isfile(filepath):
        stage = Usd.Stage.Open(filepath)
    else:
        stage = Usd.Stage.CreateNew(filepath)

    return stage


@contextlib.contextmanager
def open_stage(filepath):
    """
    open stage to make edits and save

    Args:
        filepath (str): system path for usd files

    Yields:
        (UsdStage): usd stage to make edits
    """
    stage = create_open_stage(filepath)
    try:
        yield stage
    finally:
        stage.Save()
