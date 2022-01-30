import hou


geo = hou.node("obj").createNode("geo")
geo.moveToGoodPosition()

# # create USD Character Importer node
char_n = geo.createNode("usdcharacterimport")
char_n.moveToGoodPosition()
# set import node to file instead of lop
char_n.parm("usdsource").set(1)
# set usd file path
asset_filepath = (
    "example/cube_asset.usda"
)
char_n.parm("usdfile").set(asset_filepath)


# # create Rig Pose node
pose_n = geo.createNode("rigpose")
pose_n.moveToGoodPosition()
pose_n.setInput(0, char_n, output_index=1)

# # create Bone Deform node
deform_n = geo.createNode("bonedeform")
deform_n.moveToGoodPosition()
deform_n.setInput(0, char_n, output_index=0)
deform_n.setInput(1, char_n, output_index=1)
deform_n.setInput(2, pose_n)

# display deformed object
deform_n.setDisplayFlag(True)
deform_n.setRenderFlag(True)

# select deformed object and frame it
deform_n.setCurrent(True, clear_all_selected=True)
scene_viewer = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.SceneViewer)
scene_viewer.curViewport().frameSelected()

# select pose node
pose_n.setCurrent(True, clear_all_selected=True)

# select pose handler
scene_viewer.enterCurrentNodeState()
