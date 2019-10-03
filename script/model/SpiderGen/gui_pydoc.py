'''
SPIDER WEB GENERATOR
	GUI
Joe Withers 2016

This script will create a spiderweb in your scene once the user creates 'anchors' that are used to define the shape of the spiderweb.

NOTE: this script requires assets for the animated spider to work correctly, so please ensure that the SpiderGen folder is located at:
	maya/[VERSION]/scripts/SpiderGen
	
'''

import maya.cmds as cmds
import spiderGen ### this imports all of the non-UI functions, so I can have the GUI and functions in two different files for organisation purposes.

def createUI(*args):
	''' This function creates the UI '''
	#window
	windowID = 'spiderGenUI90'
	if cmds.window(windowID, exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID, title='Spider Web Generator', resizeToFitChildren=True, sizeable=False)
	
	#header image
	cmds.rowColumnLayout(w=400)

	cmds.image(image=cmds.internalVar(usd=True)+"SpiderGen/UIheader.png")
	cmds.setParent("..")
	
	#controls
	cmds.frameLayout(label="Spiderweb Options", collapsable=False, mw=5, mh=5)
	
	cmds.text(label='Please create a ring of Anchors to define the shape of the spiderweb.', align='center', height = 20)
	cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,200),(2,10),(3,190)])
	cmds.button(label='Create Anchor', command = spiderGen.createAnchor, w=200)
	cmds.text(label='')
	deleteAnchors = cmds.checkBox(label='Delete Anchors after use')
	cmds.setParent("..")
	
	cmds.separator(height=10)
	
	secondaryRadiusControl = cmds.floatSliderGrp(label='Web Radius', minValue=0, maxValue=1, value=0.5, field=True)
	secondaryRoundnessControl = cmds.floatSliderGrp(pre=2,label='Web Roundness', minValue=-1, maxValue=1, value=0.5, field=True)
	spiralStartRadiusControl = cmds.floatSliderGrp(label='Spiral Start Radius', minValue=0, maxValue=0.5, value=0.1, field=True)
	spiralStepControl = cmds.floatSliderGrp(pre=2,label='Spiral Step Distance', minValue=0.1, maxValue=1, value=0.5, field=True)
	spirallingControl = cmds.floatSliderGrp(pre=2,label='Spiralling Amount', minValue=0, maxValue=1, value=0, field=True)
	randomControl = cmds.floatSliderGrp(pre=2,label='Random Influence', minValue=0, maxValue=1, value=0.1, field=True)
	perfection = cmds.floatSliderGrp(pre=2,label='Web Imperfections', minValue=0, maxValue=1, value=0.5, field=True)
	
	cmds.separator(height=10)
	
	cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,100),(1,150),(1,150)])
	
	cmds.text(label='Animated Spider:', align='right')
	animatedSpider = cmds.checkBox(label='')
	cmds.separator(height=20, vis=False)
	cmds.text(label='Frame Range:', align='right')
	animStart = cmds.intField(value=cmds.playbackOptions(q=True, minTime=True))
	animEnd = cmds.intField(value=(cmds.playbackOptions(q=True, maxTime=True)))
	
	cmds.setParent("..")
	
	#tooltips
	cmds.text(label='Adjust the spiders size by scaling the rectangular controller.', align='center')
	cmds.text(label='The animation can also be adjusted under the Extra Attributes tab.', align='center')

	cmds.separator(height=20)
	
	cmds.rowColumnLayout(nc=3, cw=[(1,150),(2,150),(3,100)])

	cmds.button(label='Generate Spider Web', height=30, command = lambda *args: spiderGen.createSpiderWeb(cmds.floatSliderGrp(secondaryRadiusControl, query=True, value=True),
	cmds.floatSliderGrp(secondaryRoundnessControl, query=True, value=True),
	cmds.floatSliderGrp(spiralStartRadiusControl, query=True, value=True),
	cmds.floatSliderGrp(spiralStepControl, query=True, value=True),
	cmds.floatSliderGrp(randomControl, query=True, value=True),
	cmds.floatSliderGrp(spirallingControl, query=True, value=True),
	cmds.checkBox(animatedSpider, query=True, value=True),
	cmds.intField(animStart, query=True, value=True),
	cmds.intField(animEnd, query=True, value=True),
	cmds.floatSliderGrp(perfection, query=True, value=True),
	cmds.checkBox(deleteAnchors, query=True, value=True)))
	
	cmds.button(label = 'Add to Custom shelf', command = shelfButton)
	cmds.button(label = 'Reset', command = createUI)
	
	cmds.setParent("..")
	
	#text
	cmds.text(l='Joe Withers - 2016', w=400, h=30, ww=True, fn="smallPlainLabelFont")
	
	cmds.showWindow()

def shelfButton(*args):
	"""
	adds a shelf button for the script under the 'Custom' tab
	"""
	cmds.shelfButton(annotation='Spiderweb Generator - Joe Withers', image = "commandButton.png", l='SpiderWeb', p='Custom', imageOverlayLabel='Spider', overlayLabelBackColor=(.6, .6, .6, .6), command=str("from SpiderGen import gui;reload(gui);gui.createUI()"))
