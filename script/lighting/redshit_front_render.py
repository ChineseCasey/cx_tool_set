import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

def front_render(renderFrame):
    strf = cmds.getAttr("defaultRenderGlobals.startFrame")
    endf = cmds.getAttr("defaultRenderGlobals.endFrame")
    for r in render_frame:
        if r.find('-') != -1:
            fa = r.split('-')
            for i in range(int(fa[0]),int(fa[1])+1):
                cmds.setAttr("defaultRenderGlobals.startFrame",i)
                cmds.setAttr("defaultRenderGlobals.endFrame",i)
                cmds.currentTime(i)
                cmds.rsRender(r=1,blk=1,rv=1)
    
        else:
            cmds.setAttr("defaultRenderGlobals.startFrame",r)
            cmds.setAttr("defaultRenderGlobals.endFrame",r)
            cmds.currentTime(i)
            cmds.rsRender(r=1,blk=1,rv=1)
            
    cmds.setAttr("defaultRenderGlobals.startFrame",strf)
    cmds.setAttr("defaultRenderGlobals.endFrame",endf)
    
def run_front_render():
    render_layer = pm.ls(type='renderLayer')
    for rlayer in render_layer:
        if rlayer.renderable.get():
            cmds.editRenderLayerGlobals(crl=rlayer.name())
            front_render(render_frame)
if __name__ == '__main__':
    render_frame = '1-10',       #101,102,105,108-110,
    run_front_render()