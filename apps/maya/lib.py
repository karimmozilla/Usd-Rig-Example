import maya.cmds as mc
import contextlib


@contextlib.contextmanager
def maintain_selection_type(*args, **kwargs):
    """
    Maintain selection while filter selection by type
    """
    sel = mc.ls(sl=1)
    try:
        sel_by_type = mc.ls(sel, *args, **kwargs)
        mc.select(sel_by_type, replace=True)
        yield
    finally:
        mc.select(sel, replace=True)


def export_usd(filepath):
    """
    export usd file with default options

    Args:
        filepath (str): system path where usd file export
    """
    mc.mayaUSDExport(
        file=filepath,
        selection=True,
        exportSkels="auto",
        convertMaterialsTo="none",
    )
