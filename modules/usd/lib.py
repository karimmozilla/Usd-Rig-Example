from pxr import Usd


def get_default_prim(stage):
    """
    Get the default prim for the stage

    Args:
        stage (UsdStage): the usd stage which has default prim

    Returns:
        [UsdPrim]: the prim assigned as default prim for the stage
    """
    return stage.GetDefaultPrim()


