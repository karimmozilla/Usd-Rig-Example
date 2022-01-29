import os
import apps.maya.lib as mlib
import modules.usd.lib as ulib
import modules.os.lib as olib
import maya.cmds as mc

export_root = "example"

mesh_filepath = olib._fr(os.path.join(export_root, "geo", "cube_geo.usdc"))
skel_filepath = olib._fr(os.path.join(export_root, "skel", "cube_skel.usd"))
asset_filepath = olib._fr(os.path.join(export_root, "cube_asset.usda"))


with mlib.maintain_selection_type():
    # select rig hierarchy
    mc.select(mc.ls(sl=True), r=True, hierarchy=True)

    with mlib.maintain_selection_type(type="joint"):
        skel_node = mc.ls(sl=True, l=True)[0]
        mlib.export_usd(skel_filepath)

    with mlib.maintain_selection_type(type="mesh"):
        mesh_node = mc.ls(sl=True, l=True)[0]
        mlib.export_usd(mesh_filepath)


if os.path.isfile(mesh_filepath) and os.path.isfile(skel_filepath):

    skel_path = "/".join(skel_node.split("|"))
    mesh_path = "/".join(mesh_node.split("|")[:-1])

    ulib.bind_skel_mesh(
        asset_filepath=asset_filepath,
        skel_filepath=skel_filepath,
        mesh_filepath=mesh_filepath,
        skel_path=skel_path,
        mesh_path=mesh_path,
    )
