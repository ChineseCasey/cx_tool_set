import pymel.core as pmel
import maya.mel as mel

#print mel.eval('renderLayerEditorRenderable RenderLayerTab "bb1" "1";')

#pmel.editRenderLayerGlobals(currentRenderLayer='bb')

frame = 10,11,30,50,20
for a in frame:
    pmel.setAttr("defaultRenderGlobals.startFrame",a)
    pmel.setAttr("defaultRenderGlobals.endFrame",a)
    pmel.rsRender(render=1,b=1)
    
help(pmel.rsRender)
def test_run():
    frame = 10,11,12,13,15,30
    layer = pmel.ls(type='renderLayer')
    dir(layer[0].renderable.get())
    
    for f in frame:
        for i in layer:
            if i.renderable.get():
                print '========'
                print str(i)
                pmel.editRenderLayerGlobals(currentRenderLayer = i)
                print f
                print '********'
                
test_run()