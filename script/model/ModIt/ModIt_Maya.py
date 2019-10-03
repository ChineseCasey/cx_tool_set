import maya.cmds as cmds
import maya.cmds as mc
import maya.mel as mel

def createCustomWorkspaceControlModIt(*args):
    #UI_______________________________________

    mc.columnLayout(adj = True, w=250, h=305)
              
    #_________________SUPP ERROR MESSAGE
    mc.warning()
    print '',

        #__________________________________________________________________PRIMITIVES
    #________________
    cH1 = mc.columnLayout(adj =True)
    frameEdit = mc.frameLayout(l = "  PRIMITIVES", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    mc.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,50), (2,50), (3,50), (4,50), (5,50) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )

    imageSphere = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Sphere.png"
    imageCube = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Cube.png"
    imageCylindre = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Cylindre.png"
    imagePlane = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Plane.png"
    imageDisc = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Disc.png"


    PShpere = mc.symbolButton( image= imageSphere, c= "PSphere16()", ann= "Create Sphere")
    mc.popupMenu()
    mc.menuItem(l= 'Sphere sbdv 8', c= 'PSphere8()')
    mc.menuItem(l= 'Sphere sbdv 10', c= 'PSphere10()')
    mc.menuItem(l= 'Sphere sbdv 12', c= 'PSphere12()')
    mc.menuItem(l= 'Sphere sbdv 14', c= 'PSphere14()')
    mc.menuItem(l= 'Sphere sbdv 16', c= 'PSphere16()')
    mc.menuItem(l= 'Sphere sbdv 18', c= 'PSphere18()')
    mc.menuItem(l= 'Sphere sbdv 20', c= 'PSphere20()')

    PCube = mc.symbolButton( image= imageCube, c= "PCube1()", ann= "Create Cube ")
    mc.popupMenu()
    mc.menuItem(l= 'Cube sbdv 1', c= 'PCube1()')
    mc.menuItem(l= 'Cube sbdv 2', c= 'PCube2()')
    mc.menuItem(l= 'Cube sbdv 3', c= 'PCube3()')
    mc.menuItem(l= 'Cube sbdv 4', c= 'PCube4()')
    mc.menuItem(l= 'Cube sbdv 5', c= 'PCube5()')
    mc.menuItem(l= 'Cube sbdv 6', c= 'PCube6()')

    PCylindre = mc.symbolButton( image= imageCylindre, c= "PCylY12()", ann= "Create Cylinder on X with 6 Subdiv)")
    mc.popupMenu()
    mc.menuItem(l= '__________X')
    mc.menuItem(l= 'Cylindre X 6', c= 'PCylX6()')
    mc.menuItem(l= 'Cylindre X 8', c= 'PCylX8()')
    mc.menuItem(l= 'Cylindre X 10', c= 'PCylX10()')
    mc.menuItem(l= 'Cylindre X 12', c= 'PCylX12()')
    mc.menuItem(l= 'Cylindre X 16', c= 'PCylX16()')
    mc.menuItem(l= 'Cylindre X 20', c= 'PCylX20()')
    mc.menuItem(l= 'Cylindre X 28', c= 'PCylX28()')
    mc.menuItem(l= '__________Y')
    mc.menuItem(l= 'Cylindre Y 6', c= 'PCylY6()')
    mc.menuItem(l= 'Cylindre Y 8', c= 'PCylY8()')
    mc.menuItem(l= 'Cylindre Y 10', c= 'PCylY10()')
    mc.menuItem(l= 'Cylindre Y 12', c= 'PCylY12()')
    mc.menuItem(l= 'Cylindre Y 16', c= 'PCylY16()')
    mc.menuItem(l= 'Cylindre Y 20', c= 'PCylY20()')
    mc.menuItem(l= 'Cylindre Y 28', c= 'PCylY28()')
    mc.menuItem(l= '__________Z')
    mc.menuItem(l= 'Cylindre Z 6', c= 'PCylZ6()')
    mc.menuItem(l= 'Cylindre Z 8', c= 'PCylZ8()')
    mc.menuItem(l= 'Cylindre Z 10', c= 'PCylZ10()')
    mc.menuItem(l= 'Cylindre Z 12', c= 'PCylZ12()')
    mc.menuItem(l= 'Cylindre Z 16', c= 'PCylZ16()')
    mc.menuItem(l= 'Cylindre Z 20', c= 'PCylZ20()')
    mc.menuItem(l= 'Cylindre Z 28', c= 'PCylZ28()')


    PPlane = mc.symbolButton( image= imagePlane, c= "PPlaneX()", ann= "Create a Plane on X, Y or Z axis")
    mc.popupMenu()
    mc.menuItem(l= 'Plane X', c= 'PPlaneX()')
    mc.menuItem(l= 'Plane Y', c= 'PPlaneY()')
    mc.menuItem(l= 'Plane Z', c= 'PPlaneZ()')


    mc.setParent(cH1)
    mc.separator(h= 1, style = 'none')


    #________________
    #__________________________________________________________________TOOLS
    #________________


    cH2 = mc.columnLayout(adj =True)
    frameEdit = mc.frameLayout(l = "  TOOLS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    mc.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,48), (2,48), (3,48), (4,48), (5,48) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )

    imageCam = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Camera.png"
    imageHardEdge = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/HardEdge.png"
    imageSym = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Sym.png"

    CamO = mc.symbolButton( image= imageCam, c= "CamOrtho()", ann= "Hide and Lock Orthographique Cameras")


    Sym = mc.symbolButton( image= imageSym, c= "SymX()", ann= "Make Symetrie")
    mc.popupMenu()
    mc.menuItem(l= '________Symmetry Merge')
    mc.menuItem(l= 'Symmetry on X', c= 'SymX()')
    mc.menuItem(l= 'Symmetry on Y', c= 'SymY()')
    mc.menuItem(l= 'Symmetry on Z', c= 'SymZ()')
    mc.menuItem(l= '________Flip Selection')
    mc.menuItem(l= 'Flip on X', c= 'FlipX()')
    mc.menuItem(l= 'Flip on Y', c= 'FlipY()')
    mc.menuItem(l= 'Flip on Z', c= 'FlipZ()')

    HardEdge = mc.symbolButton( image= imageHardEdge, c= "HardEdges()", ann= "Be sure to be in edge mode")
    mc.popupMenu()
    mc.menuItem(l= 'Smooth 30', c= 'mc.polySoftEdge(angle= 30)')
    mc.menuItem(l= 'Smooth 35', c= 'mc.polySoftEdge(angle= 35)')
    mc.menuItem(l= 'Smooth 40', c= 'mc.polySoftEdge(angle= 40)')
    mc.menuItem(l= 'Smooth 45', c= 'mc.polySoftEdge(angle= 45)')

    Align = mc.symbolButton( image= "CenterPivot.png", c= "Align()", ann= "Select at least 3 Vertices, 2 Edges or 1 Face")
    mc.popupMenu()
    mc.menuItem(l= 'A to B', c= 'BtoA()')
    
    UVs = mc.symbolButton( image= "polyAutoProjLarge.png", c= "UVsAuto()", ann= "Auto UVs")
    mc.popupMenu()
    mc.menuItem(l= 'Auto UVs', c= 'UVsAuto()')
    mc.menuItem(l= 'Planar UVs', c= 'UVsPlanar()')
    mc.menuItem(l= 'UVs Shader', c= 'UVs()')

    mc.setParent(cH2)
    mc.separator(h= 1, style = 'none')


    #________________
    #__________________________________________________________________COLORS
    #________________

    cH3 = mc.columnLayout(adj =True)
    frameEdit = mc.frameLayout(l = "  COLORS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    mc.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,40), (2,40), (3,40), (4,40), (5,40), (6,40) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center'), (6, 'center') ] )

    imageColorLambert = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorLambert.png"
    imageColorGreen = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorGreen.png"
    imageColorRed = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorRed.png"
    imageColorBlue = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorBlue.png"
    imageColorYellow = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorYellow.png"
    imageColorDarkGrey = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorDarkGrey.png"

    ColorLambert = mc.symbolButton( image= imageColorLambert, c= "lambert1()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectLambert()')
    mc.menuItem(l= 'Transparancy', c= 'TransLambert()')
    mc.menuItem(l= 'Attribut', c= 'AttributLambert()')

    ColorGreen = mc.symbolButton( image= imageColorGreen, c= "SelGreen()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectGreen()')
    mc.menuItem(l= 'Transparancy', c= 'TransGreen()')
    mc.menuItem(l= 'Attribut', c= 'AttributGreen()')

    ColorRed = mc.symbolButton( image= imageColorRed, c= "SelRed()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectRed()')
    mc.menuItem(l= 'Transparancy', c= 'TransRed()')
    mc.menuItem(l= 'Attribut', c= 'AttributRed()')

    ColorBlue = mc.symbolButton( image= imageColorBlue, c= "SelBlue()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectBlue()')
    mc.menuItem(l= 'Transparancy', c= 'TransBlue()')
    mc.menuItem(l= 'Attribut', c= 'AttributBlue()')

    ColorYellow = mc.symbolButton( image= imageColorYellow, c= "SelYellow()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectYellow()')
    mc.menuItem(l= 'Transparancy', c= 'TransYellow()')
    mc.menuItem(l= 'Attribut', c= 'AttributYellow()')

    ColorDarkGrey = mc.symbolButton( image= imageColorDarkGrey, c= "SelGreyDark()", ann= "Apply Face Color")
    mc.popupMenu()
    mc.menuItem(l= 'Select', c= 'SelectDarkGrey()')
    mc.menuItem(l= 'Transparancy', c= 'TransDarkGrey()')
    mc.menuItem(l= 'Attribut', c= 'AttributDarkGrey()')


    mc.setParent(cH3)
    mc.separator(h= 1, style = 'none')

    #________________
    #__________________________________________________________________SELECTIONS
    #________________

    cH5 = mc.columnLayout(adj =True)
    frameEdit = mc.frameLayout(l = "  SELECTIONS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    mc.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,30), (2,110), (3,30), (4,30), (5,30) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'right'), (4, 'right'), (5, 'right')  ] )

    imageMoins = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Moins.png"
    imagePlus = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Plus.png"
    imageDel = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Del.png"
    imageSetSel = mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelSet.png"

    Moins1 = mc.symbolButton( image= imageMoins, c= "Moins1()", ann= "Remove from Selection 1")
    Store1 = mc.button(l= "Store Selection 1", c= "Store1()", w= 110, bgc= [0.22, 0.22, 0.22])
    Plus1 = mc.symbolButton( image= imagePlus, c= "Plus1()", ann= "Add to Selection 1")
    Del1 = mc.symbolButton( image= imageDel, c= "Del1()", ann= "Delete Selection 1")
    SetSel1 = mc.symbolButton( image= imageSetSel, c= "SetSel1()", ann= "Get Selection 1")

    Moins2 = mc.symbolButton( image= imageMoins, c= "Moins2()", ann= "Remove from Selection 2")
    Store2 = mc.button(l= "Store Selection 2", c= "Store2()", w= 110, bgc= [0.22, 0.22, 0.22])
    Plus2 = mc.symbolButton( image= imagePlus, c= "Plus2()", ann= "Add to Selection 2")
    Del2 = mc.symbolButton( image= imageDel, c= "Del2()", ann= "Delete Selection 2")
    SetSel2 = mc.symbolButton( image= imageSetSel, c= "SetSel2()", ann= "Get Selection 2")


    mc.setParent(cH5)
    mc.separator(h= 1, style = 'none')


   
    #__________________________________________________________________SCREW and BOLTS
    #________________

    cH8 = mc.columnLayout(adj =True)
    frameEdit = mc.frameLayout(l = "  SREWS and BOLTS", cll =1, cl =1, bgc= [0.15, 0.15, 0.15])


    imageCustom= mc.internalVar(upd = True)+"scripts/ShadeIt_script/Icons/Empty.png" 
    imageScrewA= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_A.png"
    imageScrewB= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_B.png"
    imageScrewC= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_C.png"
    imageScrewD= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_D.png"
    imageScrewE= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_E.png"
    imageScrewF= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_F.png"

    imageBoltA= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_A.png"
    imageBoltB= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_B.png"
    imageBoltC= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_C.png"
    imageBoltD= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_D.png"
    imageBoltE= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_E.png"
    imageChainA= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/Chain_A.png"
    
    imageSF1= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_1.png"
    imageSF2= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_2.png"
    imageSF3= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_3.png"
    imageSF4= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_4.png"        
    imageSF5= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_5.png"
    imageSF6= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_6.png"
    imageSF7= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_7.png"
    imageSF8= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_8.png"
    imageSF9= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_9.png"
    imageSF10= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_10.png"        
    imageSF11= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_11.png"
    imageSF12= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_12.png"    
    imageSF13= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_13.png"
    imageSF14= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_14.png"
    imageSF15= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_15.png"
    imageSF16= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_16.png"        
    imageSF17= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_17.png"
    imageSF18= mc.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_18.png"                    
                                    
                                                                    
    mc.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,39), (2,39), (3,39), (4,39), (5,39), (6,39) ] )
    
    ScrewA = mc.symbolButton( image= imageScrewA, c= "ScrewA()", ann= "Add Screw A")
    mc.popupMenu()
    mc.menuItem(l= 'Screw_A_Washer', c= "Screw_A_Washer()")
    ScrewB = mc.symbolButton( image= imageScrewB, c= "ScrewB()", ann= "Add Screw B")
    mc.popupMenu()
    mc.menuItem(l= 'Screw_B_Washer', c= "Screw_B_Washer()")
    ScrewC = mc.symbolButton( image= imageScrewC, c= "ScrewC()", ann= "Add Screw C")
    mc.popupMenu()
    mc.menuItem(l= 'Screw_C_Washer', c= "Screw_C_Washer()")
    ScrewD = mc.symbolButton( image= imageScrewD, c= "ScrewD()", ann= "Add Screw D")
    mc.popupMenu()
    mc.menuItem(l= 'Screw_D_Washer', c= "Screw_D_Washer()")
    ScrewE = mc.symbolButton( image= imageScrewE, c= "ScrewE()", ann= "Add Screw E")
    ScrewF = mc.symbolButton( image= imageScrewF, c= "ScrewF()", ann= "Add Screw F")


    BoltA = mc.symbolButton( image= imageBoltA, c= "BoltA()", ann= "Add Bolt A")
    mc.popupMenu()
    mc.menuItem(l= 'Bolt_A_Washer', c= "Bolt_A_Washer()")
    BoltB = mc.symbolButton( image= imageBoltB, c= "BoltB()", ann= "Add Bolt B")
    mc.popupMenu()
    mc.menuItem(l= 'Bolt_B_Washer', c= "Bolt_B_Washer()")
    BoltC = mc.symbolButton( image= imageBoltC, c= "BoltC()", ann= "Add Bolt C")
    BoltD = mc.symbolButton( image= imageBoltD, c= "BoltD()", ann= "Add Bolt D")
    BoltE = mc.symbolButton( image= imageBoltE, c= "BoltE()", ann= "Add Bolt E")
    ChainA = mc.symbolButton( image= imageChainA, c= "ChainA()", ann= "Add Chain A")
    mc.popupMenu()
    mc.menuItem(l= 'Chain_B', c= "ChainB()")
    mc.setParent( '..' )


    cH9 = mc.columnLayout(adj =True)
    mc.separator(h= 3, style='in')


    mc.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,39), (2,39), (3,39), (4,39), (5,39), (6,39) ] )
    
    SF1 = mc.symbolButton( image= imageSF1, c= "SF1()", ann= "Add SF 1")
    SF2 = mc.symbolButton( image= imageSF2, c= "SF2()", ann= "Add SF 2")
    SF3 = mc.symbolButton( image= imageSF3, c= "SF3()", ann= "Add SF 3")
    SF4 = mc.symbolButton( image= imageSF4, c= "SF4()", ann= "Add SF 4")
    SF5 = mc.symbolButton( image= imageSF5, c= "SF5()", ann= "Add SF 5")
    SF6 = mc.symbolButton( image= imageSF6, c= "SF6()", ann= "Add SF 6")

    SF7 = mc.symbolButton( image= imageSF7, c= "SF7()", ann= "Add SF 7")
    SF8 = mc.symbolButton( image= imageSF8, c= "SF8()", ann= "Add SF 8")
    SF9 = mc.symbolButton( image= imageSF9, c= "SF9()", ann= "Add SF 9")
    SF10 = mc.symbolButton( image= imageSF10, c= "SF10()", ann= "Add SF 10")
    SF11 = mc.symbolButton( image= imageSF11, c= "SF11()", ann= "Add SF 11")
    SF12 = mc.symbolButton( image= imageSF12, c= "SF12()", ann= "Add SF 12")
    
    SF13 = mc.symbolButton( image= imageSF13, c= "SF13()", ann= "Add SF 13")
    SF14 = mc.symbolButton( image= imageSF14, c= "SF14()", ann= "Add SF 14")
    SF15 = mc.symbolButton( image= imageSF15, c= "SF15()", ann= "Add SF 15")
    SF16 = mc.symbolButton( image= imageSF16, c= "SF16()", ann= "Add SF 16")
    SF17 = mc.symbolButton( image= imageSF17, c= "SF17()", ann= "Add SF 17")
    SF18 = mc.symbolButton( image= imageSF18, c= "SF18()", ann= "Add SF 18")
    
    
    mc.setParent(cH8)
    mc.separator(h= 1, style = 'none')
    mc.setParent( '..' )


#mc.workspaceControl("ModIt 2.0 ", retain=False, floating=True, li= True, uiScript="createCustomWorkspaceControlModIt()");




class COMAND():
    def Comand():
        mc.launch(web= "https://wizix.artstation.com/")


###________________________________________PRIMITIVES_______________________________###
###_________SPHERE

def PSphere8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 8, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 8, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 10, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 10, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 12, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 12, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere14():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 14, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 14, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 16, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 16, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 18, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 18, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PSphere20():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polySphere(r= 10, sx= 20, sy= 12, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere_1")

    else: 
    
        name = "Sphere"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polySphere(r= 10, sx= 20, sy= 12, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Sphere")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

###_________CUBE

def PCube1():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 1,sy= 1,sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 1,sy= 1,sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCube2():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 2,sy= 2,sz= 2, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 2,sy= 2,sz= 2, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PCube3():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 3,sy= 3,sz= 3, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 3,sy= 3,sz= 3, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
def PCube4():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 4,sy= 4,sz= 4, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 4,sy= 4,sz= 4, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
def PCube5():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 5,sy= 5,sz= 5, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 5,sy= 5,sz= 5, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")   

def PCube6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCube(w= 20, h= 20, d= 20, sx= 6,sy= 6,sz= 6, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube_1")

    else: 
    
        name = "Cube"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCube(w= 20, h= 20, d= 20, sx= 6,sy= 6,sz= 6, ax= [0, 1, 0], cuv= 4, ch= 1)
        mc.rename("Cube")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
###_________CYLINDRE

def PCylX6():
    
    selection = mc.ls(sl= True)
    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
        

    
def PCylX8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    
def PCylX10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCylX12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCylX16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCylX20():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCylX28():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

def PCylY6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
        

def PCylY8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
        
    
def PCylY10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
    
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
    
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder")

        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    

def PCylY12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    

def PCylY16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
        

def PCylY18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 18)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 18)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
        

def PCylY20():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")


def PCylY28():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    

def PCylZ6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    


def PCylZ8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

    

def PCylZ10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 10)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    

def PCylZ12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 


def PCylZ16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    

def PCylZ18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 18)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 18)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")   


def PCylZ20():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 20)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    

def PCylZ28():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 28)
        mc.rename("Cylinder_1")

    else: 
    
        name = "Cylinder"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyCylinder(r= 10, h= 20, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 6)
        mc.rename("Cylinder")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
        
   
    
    
###_________PLANE

def PPlaneX():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [1, 0, 0], cuv= 2, ch= 1)
        mc.rename("Plane_1")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Plane")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 


def PPlaneY():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Plane_1")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Plane")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 


def PPlaneZ():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [0, 0, 1], cuv= 2, ch= 1)
        mc.rename("Plane_1")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyPlane(w= 20, h= 20, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        mc.rename("Plane")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 

    
###_________DISK

def PDiscX6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscX8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
    
def PDiscX10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscX12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
    
def PDiscX16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

    
def PDiscX18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(0, 0, -90)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
        
        
def PDiscY6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY14():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 14, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 14, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscY18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscZ6():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 6, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscZ8():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")

def PDiscZ10():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 10, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")
    
def PDiscZ12():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")   
    
def PDiscZ14():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 14, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 14, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01") 
    
def PDiscZ16():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")  
    
def PDiscZ18():
    
    selection = mc.ls(sl= True)

    if selection == []:
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        mc.polyDisc(sides= 18, subdivisionMode= 4, subdivisions= 1,radius= 10)
        mc.rotate(90, 0, 0)
        mc.rename("Disc")
        mc.move(pos[0], pos[1], pos[2], name)
        constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        mc.delete(constr)
        mc.rename(name, name + "_01")  
    
    
    
    
    
    
    
        
###________________________________________TOOLS_______________________________###
###_________CAMRRE

def CamOrtho():
    mc.setAttr( "top.visibility", 0)
    mc.setAttr( "top.v", lock= True)

    mc.setAttr( "front.visibility", 0)
    mc.setAttr( "front.v", lock= True)

    mc.setAttr( "side.visibility", 0)
    mc.setAttr( "side.v", lock= True)
    
    print "DONE"



###_________SYM

def SymX():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            mc.FreezeTransformations()
            mc.delete(ch= True)
            mc.duplicate()
            mc.rename("Dupli")
            mc.setAttr("Dupli.scaleX", -1)
            mc.polyUnite(selection, "Dupli", n = "polyTemps")
            mc.delete(ch= True)
            mc.CenterPivot()
            mc.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            mc.rename("Combiningwzx")
        

def SymY():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            mc.FreezeTransformations()
            mc.delete(ch= True)
            mc.duplicate()
            mc.rename("Dupli")
            mc.setAttr("Dupli.scaleY", -1)
            mc.polyUnite(selection, "Dupli", n = "polyTemps")
            mc.delete(ch= True)
            mc.CenterPivot()
            mc.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            mc.rename("Combiningwzx")        

def SymZ():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            mc.FreezeTransformations()
            mc.delete(ch= True)
            mc.duplicate()
            mc.rename("Dupli")
            mc.setAttr("Dupli.scaleZ", -1)
            mc.polyUnite(selection, "Dupli", n = "polyTemps")
            mc.delete(ch= True)
            mc.CenterPivot()
            mc.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            mc.rename("Combiningwzx")    
    
    
def FlipX():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)
    

    for each in selection:
            DupSel = mc.duplicate(rc= True)
            mc.group(em= True, n="DupliF")
            mc.parent(DupSel, 'DupliF')
            mc.setAttr("DupliF.scaleX", -1)
            mc.rename("DupliF", "DupliFlip")

def FlipY():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)
    

    for each in selection:
            DupSel = mc.duplicate(rc= True)
            mc.group(em= True, n="DupliF")
            mc.parent(DupSel, 'DupliF')
            mc.setAttr("DupliF.scaleY", -1)
            mc.rename("DupliF", "DupliFlip")

def FlipZ():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)
    

    for each in selection:
            DupSel = mc.duplicate(rc= True)
            mc.group(em= True, n="DupliF")
            mc.parent(DupSel, 'DupliF')
            mc.setAttr("DupliF.scaleZ", -1)
            mc.rename("DupliF", "DupliFlip")

###___________________________________________________________________________HARDEDGES
def HardEdges():
        mc.polySelectConstraint(m= 3, t= 0x8000, sm= 1)
        mc.polySelectConstraint(m= 0) 


###___________________________________________________________________________UVS

def UVsAuto():   
    selection = mc.ls(sl = True, fl = True, dag = True, type= 'mesh')
    
    for each in selection:
        mc.DeleteHistory()
        mc.polyAutoProjection(lm= 0, pb= 0, ibd= 1, sc= 1, o= 1, p= 3, ps= 0.1, ws= 0)
        mc.polyEditUV(pu= 0.5, pv= 0.5, su= 0.5, sv= 0.5, u= -0.25, v= 0.25)
        mc.select(each)
        mc.DeleteHistory()
        print "UV Done"
    
def UVsPlanar():
    
    selection = mc.ls(sl = True, fl = True, dag = True, type= 'mesh')
    
    for each in selection:
        mc.DeleteHistory()
        mc.polyProjection( each + '.f[*]', ch= 1, type= "planar", ibd= True, kir= True,  md= "c" )
        mc.polyEditUV(pu= 0.5, pv= 0.5, su= 0.5, sv= 0.5, u= -0.25, v= 0.25)
        mc.select(each)
        mc.DeleteHistory()
        print "UV Done"

def UVs():
    
    UVsPath = mc.internalVar(upd = True)+"scripts/ModIt_script/Shaders/Uvs.ma"
    selection = mc.ls(sl = True, fl = True, dag = True)

    if mc.objExists('UVs'):
      print("UVs_EXIST")
      for each in selection:
        mc.hyperShade( a= "UVs")
        mc.select("UVs")
        print "Done"
        
    else:
      mc.sets(n= "Settemps")
      mc.file(UVsPath, i = True)
      mc.binMembership("UVs", addToBin= "Viewport_Shaders")
      mc.select("Settemps")
      mc.ls(selection= True)
      mc.delete("Settemps")
      for each in selection:
        mc.hyperShade( a= "UVs")
        mc.select("UVs")
        print "Done"   

def BtoA():
    mc.MatchTranslation()
    mc.MatchRotation()
 

###________________________________________________________________________FACES COLORS
def lambert1():

    mc.hyperShade( assign= "lambert1" )
    

def SelGreen():

    selection = mc.ls(sl= True)

    if mc.objExists('Sel_Green'):
        mc.hyperShade( assign= "Sel_Green" )
    
    else:
        LambertGreen = mc.shadingNode("lambert",asShader=True)
        mc.setAttr(LambertGreen + ".color", 0.0, 0.7, 0.0, type = 'double3')
        mc.rename("Sel_Green")
        mc.select(selection)
        mc.hyperShade( assign= "Sel_Green" )



def SelRed():

    selection = mc.ls(sl= True)

    if mc.objExists('Sel_Red'):
        mc.hyperShade( assign= "Sel_Red" )
    
    else:
        LambertRed = mc.shadingNode("lambert",asShader=True)
        mc.setAttr(LambertRed + ".color", 0.7, 0.0, 0.0, type = 'double3')
        mc.rename("Sel_Red")
        mc.select(selection)
        mc.hyperShade( assign= "Sel_Red" )

def SelBlue():

    selection = mc.ls(sl= True)

    if mc.objExists('Sel_Blue'):
        mc.hyperShade( assign= "Sel_Blue" )
    
    else:
        LambertBlue = mc.shadingNode("lambert",asShader=True)
        mc.setAttr(LambertBlue + ".color", 0.0, 0.0, 0.7, type = 'double3')
        mc.rename("Sel_Blue")
        mc.select(selection)
        mc.hyperShade( assign= "Sel_Blue" )

def SelYellow():

    selection = mc.ls(sl= True)

    if mc.objExists('Sel_Yellow'):
        mc.hyperShade( assign= "Sel_Yellow" )
    
    else:
        LambertYellow = mc.shadingNode("lambert",asShader=True)
        mc.setAttr(LambertYellow + ".color", 1.0, 0.7, 0.0, type = 'double3')
        mc.rename("Sel_Yellow")
        mc.select(selection)
        mc.hyperShade( assign= "Sel_Yellow" )

def SelGreyDark():

    selection = mc.ls(sl= True)

    if mc.objExists('Sel_GreyDark'):
        mc.hyperShade( assign= "Sel_GreyDark" )
    
    else:
        LambertGreyDark = mc.shadingNode("lambert",asShader=True)
        mc.setAttr(LambertGreyDark + ".color", 0.05, 0.05, 0.05, type = 'double3')
        mc.rename("Sel_GreyDark")
        mc.select(selection)
        mc.hyperShade( assign= "Sel_GreyDark" )    
        

def SelectLambert():

    if mc.objExists('lambert1'):
       mc.hyperShade( objects= "lambert1" )
    
    else:
        print "Please First Create this FaceColor Shader"   


def SelectGreen():

    if mc.objExists('Sel_Green'):
       mc.hyperShade( objects= "Sel_Green" )
    
    else:
        print "Please First Create this FaceColor Shader"         
        
        
def SelectRed():

    if mc.objExists('Sel_Red'):
       mc.hyperShade( objects= "Sel_Red" )
    
    else:
        print "Please First Create this FaceColor Shader"  


def SelectBlue():

    if mc.objExists('Sel_Blue'):
       mc.hyperShade( objects= "Sel_Blue" )
    
    else:
        print "Please First Create this FaceColor Shader"  

def SelectYellow():

    if mc.objExists('Sel_Yellow'):
       mc.hyperShade( objects= "Sel_Yellow" )
    
    else:
        print "Please First Create this FaceColor Shader"  

def SelectDarkGrey():

    if mc.objExists('Sel_GreyDark'):
       mc.hyperShade( objects= "Sel_GreyDark" )
    
    else:
        print "Please First Create this FaceColor Shader"   


def TransGreen():

    if mc.objExists('Sel_Green'):
       mc.window( title='Green Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='Sel_Green.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributGreen():

    if mc.objExists('Sel_Green'):
       mc.select('Sel_Green')
    
    else:
        print "Please First Create this FaceColor Shader" 


def TransLambert():

    if mc.objExists('lambert1'):
       mc.window( title='Lambert Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='lambert1.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributLambert():

    if mc.objExists('lambert1'):
       mc.select('lambert1')
    
    else:
        print "Please First Create this FaceColor Shader" 

def TransRed():

    if mc.objExists('Sel_Red'):
       mc.window( title='Red Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='Sel_Red.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributRed():

    if mc.objExists('Sel_Red'):
       mc.select('Sel_Red')
    
    else:
        print "Please First Create this FaceColor Shader" 


def TransBlue():

    if mc.objExists('Sel_Blue'):
       mc.window( title='Blue Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='Sel_Blue.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributBlue():

    if mc.objExists('Sel_Blue'):
       mc.select('Sel_Blue')
    
    else:
        print "Please First Create this FaceColor Shader" 


def TransYellow():

    if mc.objExists('Sel_Yellow'):
       mc.window( title='Yellow Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='Sel_Yellow.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributYellow():

    if mc.objExists('Sel_Yellow'):
       mc.select('Sel_Yellow')
    
    else:
        print "Please First Create this FaceColor Shader" 


def TransDarkGrey():

    if mc.objExists('Sel_GreyDark'):
       mc.window( title='GreyDark Transparancy' )
       mc.columnLayout()
       mc.attrColorSliderGrp( at='Sel_GreyDark.transparency')
       mc.showWindow()
    
    else:
        print "Please First Create this FaceColor Shader"         
   

def AttributDarkGrey():

    if mc.objExists('Sel_GreyDark'):
       mc.select('Sel_GreyDark')
    
    else:
        print "Please First Create this FaceColor Shader" 


class ALIGN():
    def Comand():
        mc.launch(web= "https://wizix.artstation.com/")
        
        
###________________________________________________________________________ALIGN
def Align():
    mc.setToolTo('Move')
    getPivotPos = mel.eval("float $getPivotPos[] = `manipMoveContext -q -p Move`;")
    mel.eval("ConvertSelectionToVertices;")
    vtxSel=mc.ls(fl=1, sl=1)
    selectedObjectStore= mc.ls(o=1, sl=1)
    objectSelectionStore= mc.listRelatives(selectedObjectStore[0], p=1)
    if len(vtxSel)<3:
        mc.warning("Please select at least 3 Vertices, 2 Edges or 1 Face")
        
    plane=mc.polyPlane(cuv=2, sy=1, sx=1, h=1, n='rotationPlane', ch=1, w=1, ax=(0, 1, 0))
    mc.select((plane[0] + ".vtx[0:2]"), 
        vtxSel[0], vtxSel[1], vtxSel[2])
    mel.eval("snap3PointsTo3Points(0)")
    mc.parent(objectSelectionStore, plane[0])
    mc.makeIdentity(objectSelectionStore, apply=True, s=0, r=1, t=0, n=0)
    mc.xform(ws=1, piv=(getPivotPos[0], getPivotPos[1], getPivotPos[2]))
    mc.parent(objectSelectionStore, world=1)
    mc.delete(plane)








###________________________________________SELECTIONS_______________________________###
###_________STORE1

def Store1():
    
    if mc.objExists('ModSet1'):
       mc.sets(add = "ModSet1")
      
    else :
       newSet1 = mc.sets(n = "ModSet1")


def Plus1():
    mc.sets(add = "ModSet1")


def Moins1():
    mc.sets(rm = "ModSet1")


def Del1():
    mc.delete("ModSet1")


def SetSel1():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)
    
    mc.select( "ModSet1" )
    mc.ls( selection= True )
    import maya.mel as mel    
    mel.eval('setSelectMode components Components; selectType -smp 0 -sme 1 -smf 0 -smu 0 -pv 0 -pe 1 -pf 0 -puv 0; HideManipulators;')


###_________STORE2

def Store2():
    
    if mc.objExists('ModSet2'):
       mc.sets(add = "ModSet2")
      
    else :
       newSet1 = mc.sets(n = "ModSet2")


def Plus2():
    mc.sets(add = "ModSet2")


def Moins2():
    mc.sets(rm = "ModSet2")


def Del2():
    mc.delete("ModSet2")


def SetSel2():
    selection = mc.ls(sl = True, fl = True, dag = True, hd = 1)
    
    mc.select( "ModSet2" )
    mc.ls( selection= True )
    import maya.mel as mel    
    mel.eval('setSelectMode components Components; selectType -smp 0 -sme 1 -smf 0 -smu 0 -pv 0 -pe 1 -pf 0 -puv 0; HideManipulators;')



###________________________________________SCREW AND BOLTS______________________________###
###_________SCREW1

def ScrewA():
    
    name = "Screw_A"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_A.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Screw_A_Washer():
    
    name = "Screw_A_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_A_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def ScrewB():
    
    name = "Screw_B"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_B.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Screw_B_Washer():
    
    name = "Screw_B_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_B_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def ScrewC():
    
    name = "Screw_C"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_C.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Screw_C_Washer():
    
    name = "Screw_C_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_C_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def ScrewD():
    
    name = "Screw_D"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_D.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Screw_D_Washer():
    
    name = "Screw_D_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_D_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def ScrewE():
    
    name = "Screw_E"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_E.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

    
def ScrewF():
    
    name = "Screw_F"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_F.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")    


def BoltA():
    
    name = "Bolt_A"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_A.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Bolt_A_Washer():
    
    name = "Bolt_A_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_A_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def BoltB():
    
    name = "Bolt_B"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_B.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def Bolt_B_Washer():
    
    name = "Bolt_B_Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_B_Washer.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def BoltC():
    
    name = "Bolt_C"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_C.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")



def BoltD():
    
    name = "Bolt_D"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_D.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")



def BoltE():
    
    name = "Bolt_E"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = mc.ls(selection=True)
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_E.ma"
    target = mc.file(fileO, i= True)

    mc.move(pos[0], pos[1], pos[2], name)

    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")



def ChainA():
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Chain_A.ma"
    target = mc.file(fileO, i= True)

    mc.rename("Chain_A", "Chain_A_01")


def ChainB():
    
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Chain_B.ma"
    target = mc.file(fileO, i= True)

    mc.rename("Chain_B", "Chain_B_01")

def SF1():
    
    name = "SF_1"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_1.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF2():
    
    name = "SF_2"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_2.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF3():
    
    name = "SF_3"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_3.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF4():
    
    name = "SF_4"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_4.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF5():
    
    name = "SF_5"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_5.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF6():
    
    name = "SF_6"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_6.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF7():
    
    name = "SF_7"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_7.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF8():
    
    name = "SF_8"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_8.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF9():
    
    name = "SF_9"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_9.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF10():
    
    name = "SF_10"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_10.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF11():
    
    name = "SF_11"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_11.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF12():
    
    name = "SF_12"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_12.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")


def SF13():
    
    name = "SF_13"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_13.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF14():
    
    name = "SF_14"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_14.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF15():
    
    name = "SF_15"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_15.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF16():
    
    name = "SF_16"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_16.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF17():
    
    name = "SF_17"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_17.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

def SF18():
    
    name = "SF_18"
    mel.eval("setToolTo $gMove;")
    pos = mc.manipMoveContext('Move', query=True, position=True) 
    selection = mc.ls(selection=True)
    fileO = mc.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_18.ma"
    target = mc.file(fileO, i= True)
    mc.move(pos[0], pos[1], pos[2], name)
    constr = mc.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    mc.delete(constr)
    mc.rename(name, name + "_01")

