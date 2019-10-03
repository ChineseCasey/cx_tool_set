import pymel.core as pmel
import maya.cmds as cmds
import maya.mel as mel

pmel.PyNode()

pmel.listAttr(cmds.rsCreateAov())
sel = cmds.textScrollList('rsControl_availableAovsTsl',q=1,selectItem =1 )
sel = "Puzzle Matte"

a = pmel.rsCreateAov(t = 'Puzzle Matte')
b = pmel.PyNode(a)
b.mode.set(1)
b.redId.set(1)
b.greenId.set(2)
b.blueId.set(3)

aov_list = cmds.ls(type="RedshiftAOV")

