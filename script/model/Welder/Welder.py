#coding=utf-8
import maya.cmds as mc
import maya.cmds as cmds
import maya.mel as mel
import script.project_path as sp
import sys, os

maya_path = os.path.dirname(sys.path[0]).replace('\\', '/')
# Select an object if and only if it exists.
# Print a warning if it does not exist.
# shaderPath = mc.internalVar(upd = True)+"scripts/Welder_scripts/Welder_shd.ma"
shaderPath = sp.get_path() + "/script/model/Welder/Welder_scripts/Welder_shd.ma"
print maya_path,shaderPath
if mc.objExists('Welder_shd'):
    print("BELLE")
else:
    mc.file(shaderPath, i=True)

# SET correct brush -------------------------------------------------------------------------
version = mc.about(v=True)  # command to get Maya version you are now running
OS = mc.about(os=True)

if OS == 'win64':
    if version == '2018':
        mel.eval('visorPanelBrushPressCallback files1VisorEd "%s/Examples/Paint_Effects/Trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')
    elif version == '2017':
        mel.eval('visorPanelBrushPressCallback files1VisorEd "%s/Examples/Paint_Effects/Trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')
    elif version == '2016':
        mel.eval('visorPanelBrushPressCallback files1VisorEd "%s/brushes/trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')
    elif version == '2015':
        mel.eval('visorPanelBrushPressCallback files1VisorEd "%s/brushes/trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')
    elif version == '2014':
        mel.eval('visorPanelBrushPressCallback files1VisorEd "%s/brushes/trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')
    elif version == '2019':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "%s/Examples/Paint_Effects/Trees/birchLimb.mel";' % maya_path)
        mel.eval('setToolTo $gMove;')

elif OS == 'mac':
    if version == '2018':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2018/Maya.app/Contents/Examples/Paint_Effects/Trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')
    elif version == '2017':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2017/Maya.app/Contents/Examples/Paint_Effects/Trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')
    elif version == '2016':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2016/Maya.app/Contents/brushes/trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')
    elif version == '2015':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2015/Maya.app/Contents/brushes/trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')
    elif version == '2014':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2014/Maya.app/Contents/brushes/trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')
    elif version == '2019':
        mel.eval(
            'visorPanelBrushPressCallback files1VisorEd "/Applications/Autodesk/maya2019/Maya.app/Contents/Examples/Paint_Effects/Trees/birchLimb.mel";')
        mel.eval('setToolTo $gMove;')


elif OS == 'linux64':
    if version == '2018':
        print ("Linux2018")
    elif version == '2017':
        print ("Linux2017")

# SET default setting for the tube --------------------------------------------------------------
# mel.eval('brushToolSettings;')
mc.setAttr("birchLimb.globalScale", 1)
mc.setAttr("birchLimb.brushWidth", 1)
mc.setAttr("birchLimb.forwardTwist", 0)
mc.setAttr(("birchLimb.color1"), 0.8, 0.067, 0.047, type='double3')
mc.setAttr(("birchLimb.specularColor"), 0, 0, 0, type='double3')
mc.setAttr(("birchLimb.tubeSections"), 8)

## INIT PaintEffectTool
mc.dynWireCtx(displayQuality=100, surfaceOffset=-0.1, pressureMapping1=1, pressureMapping2=0, pressureMapping3=0,
              pressureMin1=0.4)

# UI_______________________________________
if mc.window("Welder", exists=True):
    mc.deleteUI("Welder")

ram = mc.window("Welder", t="Welder v1.0", tlb=True, menuBar=True)
mc.columnLayout(adj=True, w=300, h=280)

mc.menu(label='Info')
mc.menuItem(label='Arstation', annotation='My Website', c="goArtstation(()")
mc.menuItem(label='Gumroad', annotation='Tutorial', c="goGumroad()")
mc.menuItem(label='Contact', annotation='For Any Help', c="goFacebook()")

cH1 = mc.columnLayout(adj=True)
# frameCreate = mc.frameLayout(l = "CREATE", cll =1, cl =0, bgc= [0.302, 0.494, 0.588])
mc.text(l='  > PAINT', al='left', h=18, font='smallPlainLabelFont', bgc=[0.906, 0.286, 0.239])

########################################
# ADDED row column bor icons and buttons
########################################
mc.rowColumnLayout(numberOfRows=1)
# imagePathPaint = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_Paint.png"
imagePathPaint = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_Paint.png"
# imagePathMake = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_MakeP.png"
imagePathMake = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_MakeP.png"
# imagePathUV = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_UVs.png"
imagePathUV = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_UVs.png"

mc.separator(w=50, style='none')
makePaint = mc.symbolButton(image=imagePathUV, c=mc.AutoProjection, ann="Make Paintable")

mc.separator(w=50, style='none')
makePaint = mc.symbolButton(image=imagePathMake, c="makePaint()", ann="Make Paintable")

mc.separator(w=50, style='none')
paintWeld = mc.symbolButton(image=imagePathPaint, c=mc.PaintEffectsTool, ann="Paint Weld")
mc.setParent('..')

mc.separator(h=3, style='none')
brushSize = mc.floatSliderGrp('Slider_BrushS', l="Brush Size", min=0.1, max=10, po=True, field=True, cc="BrushS_Val()",
                              dc="BrushS_Val()", v=1, adj=0, cat=[1, "left", 3], cw=[1, 60], ann="Brush Size")

########################################


mc.setParent(cH1)
mc.separator(h=10, style='none')

cH2 = mc.columnLayout(adj=True)
# frameEdit = mc.frameLayout(l = "EDIT", cll =1, cl =0, bgc= [0.302, 0.494, 0.588])
mc.text(l='  > EDIT', al='left', h=18, font='smallPlainLabelFont', bgc=[0.906, 0.286, 0.239])

mc.separator(h=3, style='none')
slideScale = mc.floatSliderGrp('Slider_Scale', l="Scale", min=0.1, max=100, po=True, field=True, cc="Scale_Val()",
                               dc="Scale_Val()", v=1, adj=0, cat=[1, "left", 3], cw=[1, 60],
                               ann="Configure to scene set in cm")
# slideWidth = mc.floatSliderGrp('Slider_Width', l = "Width",min =0.1, max =1,po =True, field =True, cc="Width_Val()", dc="Width_Val()", v= 0.1, pre= 3, adj =0, cat= [1, "left", 3], cw= [1, 60])
slideDensity = mc.floatSliderGrp('Slider_Density', l="Density", min=0.1, max=5, po=True, field=True, cc="Density_Val()",
                                 dc="Density_Val()", v=1, adj=0, cat=[1, "left", 3], cw=[1, 60])
slideSection = mc.intSliderGrp('Slider_Section', l="Section", min=3, max=12, po=True, field=True, cc="Section_Val()",
                               dc="Section_Val()", v=8, adj=0, cat=[1, "left", 3], cw=[1, 60])
slideSmoothing = mc.floatSliderGrp('Slider_Smoothing', l="Smoothing", min=0, max=10, po=True, field=True,
                                   cc="Smoothing_Val()", dc="Smoothing_Val()", v=0, adj=0, cat=[1, "left", 3],
                                   cw=[1, 60])

mc.setParent(cH2)
mc.separator(h=15, style='none')

cH3 = mc.columnLayout(adj=True)
# frameEdit = mc.frameLayout(l = "CONVERT", cll =1, cl =0, bgc= [0.302, 0.494, 0.588])
mc.text(l='  > CREATE', al='left', h=18, font='smallPlainLabelFont', bgc=[0.906, 0.286, 0.239])

# mc.text(l= "To finish you should convert into Mesh the cable.", al= "left", h= 25, w= 293, backgroundColor= [0.24, 0.24, 0.24])
# mc.text(l= "But once you've bake to geo, you loose Edit possibility", al= "left", h= 25, w= 293, backgroundColor= [0.24, 0.24, 0.24])
mc.separator(h=5, style='none')
mc.rowColumnLayout(numberOfRows=1)
mc.separator(w=1, h=5, style='none')
createWeld = mc.button('buttonCreateWeld', w=290, l="CREATE Weld", c="CreateWeld()", ann="Create Weld")
mc.setParent('..')

mc.setParent(cH3)
mc.separator(h=5, style='none')

cH4 = mc.columnLayout(adj=True)
# frameEdit = mc.frameLayout(l = "CONVERT", cll =1, cl =0, bgc= [0.302, 0.494, 0.588])
mc.text(l='  > SHADER', al='left', h=18, font='smallPlainLabelFont', bgc=[0.906, 0.286, 0.239])

slideDisplace = mc.floatSliderGrp('Slider_Displace', l="Displace", min=0, max=50, po=True, field=True,
                                  cc="Displace_Val()", dc="Displace_Val()", v=2, adj=0, cat=[1, "left", 3], cw=[1, 60],
                                  ann="Configure to scene set in cm")

##______________________________

mc.rowColumnLayout(numberOfRows=1)
# imagePathPlus = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_Plus.png"
# imagePathMin = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_Min.png"
# imagePathWave = mc.internalVar(upd = True)+"icons/Welder_icons/Welder_Wave.png"

imagePathPlus = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_Plus.png"
imagePathMin = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_Min.png"
imagePathWave = sp.get_path() + "/script/model/Welder/Welder_icons/Welder_Wave.png"

mc.separator(w=50, style='none')
WaveMin = mc.symbolButton(image=imagePathMin, c="WaveMin_Val()", ann="Paint Weld")

mc.separator(w=20, style='none')
Wave = mc.image(image=imagePathWave, ann="Make Paintable")

mc.separator(w=20, style='none')
WavePlus = mc.symbolButton(image=imagePathPlus, c="WavePlus_Val()", ann="Make Paintable")
mc.setParent('..')

##______________________________


mc.setParent(cH4)
mc.separator(h=1, style='none')
cH5 = mc.columnLayout(adj=True)

mc.showWindow(ram)

########################################
# ADDED - edit the size of the wwindow to fit new organization
########################################
mc.window(ram, edit=True, h=380)


########################################


###________________________________________PAINT_______________________________###

def makePaint():
    mc.MakePaintable()
    mc.select(d=True)


def BrushS_Val():
    myValueWidght = mc.floatSliderGrp("Slider_BrushS", q=True, value=True)

    mc.setAttr("birchLimb.globalScale", myValueWidght)


###________________________________________INFO_______________________________###

def goArtstation():
    mc.launch(web="https://wizix.artstation.com/")


def goGumroad():
    mc.launch(web="https://gumroad.com/wzx")


def goFacebook():
    mc.launch(web="https://www.facebook.com/WizixPage/")


###________________________________________EDIT_______________________________###

##___________________________________________________PaintEffectControl
# SCALE__________________
def Scale_Val():
    myValueWidght = mc.floatSliderGrp("Slider_Scale", q=True, value=True)

    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    buffer = mc.listConnections(selection, d=True, scn=True, type='brush')

    for each in buffer:
        mc.setAttr(each + ".globalScale", myValueWidght)


# WIDTH__________________
def Width_Val():
    myValueWidght = mc.floatSliderGrp("Slider_Width", q=True, value=True)

    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    buffer = mc.listConnections(selection, d=True, scn=True, type='brush')

    for each in buffer:
        mc.setAttr(each + ".brushWidth", myValueWidght)


# SECTION__________________
def Section_Val():
    myValueWidght = mc.intSliderGrp("Slider_Section", q=True, value=True)

    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    buffer = mc.listConnections(selection, d=True, scn=True, type='brush')

    for each in buffer:
        mc.setAttr(each + ".tubeSections", myValueWidght)


##___________________________________________________Stroke
# DENSITY__________________
def Density_Val():
    myValueWidght = mc.floatSliderGrp("Slider_Density", q=True, value=True)

    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    for each in selection:
        mc.setAttr(each + ".sampleDensity", myValueWidght)


# SMOOTHING__________________
def Smoothing_Val():
    myValueWidght = mc.floatSliderGrp("Slider_Smoothing", q=True, value=True)

    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    for each in selection:
        mc.setAttr(each + ".smoothing", myValueWidght)


###________________________________________CREATE_______________________________###


def CreateWeld():
    selection = mc.ls(sl=True, fl=True, dag=True, type='stroke')

    for each in selection:
        sel1 = mc.ls(sl=True, fl=True, dag=True, )
        sel2 = mc.listConnections(sel1)
        sel3 = mc.listConnections(sel1, type='brush')
        selAll = sel1 + sel3
        import maya.mel as mel
        mel.eval('doPaintEffectsToPoly(1,0,1,1,100000);')
        mel.eval('polyMultiLayoutUV -lm 1 -sc 1 -rbf 0 -fr 1 -ps 0.05 -l 2 -gu 1 -gv 1 -psc 1 -su 1 -sv 1 -ou 0 -ov 0;')
        mc.delete(ch=True)
        mc.parent(w=True)
        sel4 = mc.ls("birchLimb*MeshGroup")
        mc.delete(selAll)
        mc.delete(sel4)
        mc.CenterPivot()
        mc.hyperShade(a="Welder_shd")
        selected_objects = mc.ls(selection=True)
        mc.toggleDisplacement()
        newname = "Weld_"
        for number, object in enumerate(selected_objects):
            print 'Old Name:', object
            print 'New Name:', '%s%02d' % (newname, number)
            mc.setAttr(object + ".aiSubdivType", 1)
            mc.setAttr(object + ".aiSubdivIterations", 2)
            mc.rename(object, ('%s%02d' % (newname, number)))


###________________________________________SHADER_______________________________###


def Displace_Val():
    myValueWidght = mc.floatSliderGrp("Slider_Displace", q=True, value=True)

    mc.setAttr("Large_Noise.alphaGain", myValueWidght)


def WavePlus_Val():
    selection = mc.ls(sl=True, fl=True, dag=True, type='mesh')

    for each in selection:
        mc.select(each + ".map[*]")
        mc.polyEditUV(pu=0.5, pv=0.5, su=1, sv=1.2)
        mc.select(each)


def WaveMin_Val():
    selection = mc.ls(sl=True, fl=True, dag=True, type='mesh')

    for each in selection:
        mc.select(each + ".map[*]")
        mc.polyEditUV(pu=0.5, pv=0.5, su=1, sv=0.8)
        mc.select(each)
