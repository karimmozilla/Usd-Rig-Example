from pxr import Usd, UsdGeom, UsdSkel, Sdf, Gf
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


def bind_skel_mesh(asset_filepath, skel_filepath, mesh_filepath, skel_path, mesh_path):
    """
    reference and bind a usd skeleton and mesh into usd file

    Args:
        asset_filepath (str): system path where creating a new usd asset file reference skeleton and mesh usd files
        skel_filepath (str): system path for usd skeleton file
        mesh_filepath (str): [system path for usd mesh file
        skel_path (str): the string path of skeleton prim
        mesh_path (str): the string path of mesh prim
    """

    with open_stage(asset_filepath) as stage:

        # define a SkelRoot.
        root_path = Sdf.Path("/{}".format(mesh_path.split("/")[1]))
        root = UsdSkel.Root.Define(stage, root_path)

        # basic configuration
        stage.SetDefaultPrim(root.GetPrim())
        stage.SetStartTimeCode(1)
        stage.SetEndTimeCode(20)
        stage.SetTimeCodesPerSecond(24)

        # reference skeleton usd file into skeleton prim
        stage.DefinePrim(skel_path).GetReferences().AddReference(
            skel_filepath, skel_path
        )
        skeleton = UsdSkel.Skeleton.Define(stage, skel_path)

        # reference mesh usd file into mesh prim
        stage.DefinePrim(mesh_path).GetReferences().AddReference(
            mesh_filepath, mesh_path
        )
        mesh = UsdGeom.Mesh.Define(stage, mesh_path)

        # bind skeleton to mesh
        skin_binding = UsdSkel.BindingAPI.Apply(mesh.GetPrim())
        skin_binding.CreateJointIndicesPrimvar(constant=False, elementSize=1).Set(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        skin_binding.CreateJointWeightsPrimvar(constant=False, elementSize=1).Set(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )
        skin_binding.CreateGeomBindTransformAttr().Set(Gf.Matrix4d())

        skin_binding.CreateSkeletonRel().AddTarget(skeleton.GetPath())
