import maya.cmds as cmds
import math
from functools import partial
## EASY STEP STAIR MAKER ######################
# FEB 27, 2017 By Gina Jeon ###################
############################# rvhlu00@gmail.com



#### stair making ####
def make_stair(w_val, h_val):
	

	stairbody = cmds.polyCube(n= 'stair_body*', w = w_val, h=0.4, d=2.5)
	cmds.move(0,0.2, 0)
	cmds.move(0, h_val+0.2 , 0)
	
	stairfoot = cmds.polyCube(n= 'stair_foot*', w=0.1, h=h_val, d=0.5)
	
	cmds.polyExtrudeFacet('stair_foot_.f[1]', kft=True, ltz=0.4)
	cmds.polyExtrudeFacet('stair_foot_.f[8]', kft=True, ltz=2)
	
	cmds.select(stairfoot)
	cmds.move(w_val/2+0.05, h_val/2, 1, r=True)
	stairfoot_dup = cmds.duplicate(stairfoot[0])
	cmds.move(-w_val - 0.1,0,0, r=True)
	
	
	cmds.group(stairbody, stairfoot, stairfoot_dup, name = 'stairs')
	cmds.move(0,0,-1.25)
	cmds.makeIdentity( apply=True )



#### pole making ####
	
def make_pole(w_val, h_val, pole_height):

	if h_val <= 2 :
		tilt_val = 0
		
	if h_val <= 1.5 :
		tilt_val = 0.15
  
	if h_val <= 1 :
		tilt_val = 0.2
		
	if h_val <= 0.5:
		tilt_val = 0.4

	if h_val == 0.1 :
		flexible_height = pole_height
	else :
		flexible_height = pole_height - 0.6
	
	
	stair_pole = cmds.polyCylinder(name = 'stair_pole*', r=0.08, h = flexible_height)
	
	# position the initial pole
	
	cmds.move(0, -(pole_height/2)+0.3, 0, stair_pole[0]+".scalePivot", stair_pole[0]+".rotatePivot",  r=True)
		

	cmds.move(w_val/2 - 0.08,0,0)
	
	
	cmds.move(0,0, -1, r=True)  

 
	cmds.move(0, (pole_height/2) -0.3, 0, r=True)
	

	cmds.move ( 0, h_val + tilt_val , 0, r=True)


	# dulpicate another side
	cmds.duplicate(stair_pole[0])
	cmds.move(-w_val+0.16,0,0,r=True)


	cmds.group('stair_pole*', name='poles')




### rail making ###

def make_rail(w_val, h_val, count, pole_height):
	pole_height = float(pole_height)
	
	rail_len = math.sqrt(math.pow(2,2) + math.pow(h_val+0.4,2)) * count



	stair_angle = math.atan( (h_val+0.4)/2 )

	ang = math.degrees(stair_angle)




	stair_rail = cmds.polyCylinder(name = 'stair_rail*', r=0.2, h = rail_len)
	cmds.rotate( ' 90deg', 0, 0)
	cmds.makeIdentity( apply=True )


	cmds.move(0, 0, rail_len/2, stair_rail[0]+".scalePivot", stair_rail[0]+".rotatePivot",  absolute=True)
	cmds.move(0,0, (-rail_len/2))



	cmds.rotate( "{0}deg".format(ang))
	cmds.move(w_val/2+0.05, 0, 0, r=True)

	##### this 0.2 value is to match the ending of the rail
	cmds.move(-0.2,pole_height,0, r=True)
	cmds.makeIdentity( apply=True )

	cmds.duplicate(stair_rail[0])
	cmds.move(-w_val+0.2,0,0, r=True)


	#stair rail underA

	stair_rail = cmds.polyCylinder(name = 'stair_rail_underA*', r=0.07, h = rail_len)
	cmds.rotate( ' 90deg', 0, 0)
	cmds.makeIdentity( apply=True )


	cmds.move(0, 0, rail_len/2, stair_rail[0]+".scalePivot", stair_rail[0]+".rotatePivot",  absolute=True)
	cmds.move(0,0, (-rail_len/2))



	cmds.rotate( "{0}deg".format(ang))
	cmds.move(w_val/2+0.05, 0, 0, r=True)


	cmds.move(-0.07,(pole_height/5)*2, 0, r=True)
	cmds.makeIdentity( apply=True )

	cmds.duplicate(stair_rail[0])
	cmds.move(-w_val +0.07 ,0,0, r=True)



	#stair rail underB

	stair_rail = cmds.polyCylinder(name = 'stair_rail_underB*', r=0.07, h = rail_len)
	cmds.rotate( ' 90deg', 0, 0)
	cmds.makeIdentity( apply=True )


	cmds.move(0, 0, rail_len/2, stair_rail[0]+".scalePivot", stair_rail[0]+".rotatePivot",  absolute=True)
	cmds.move(0,0, (-rail_len/2))



	cmds.rotate( "{0}deg".format(ang))
	cmds.move(w_val/2+0.05, 0, 0, r=True)


	cmds.move(-0.07,(pole_height/5) * 3 ,0, r=True)
	cmds.makeIdentity( apply=True )

	cmds.duplicate(stair_rail[0])
	cmds.move(-w_val+0.07, 0 ,0 , r=True)



	#stair rail underC

	stair_rail = cmds.polyCylinder(name = 'stair_rail_underB*', r=0.07, h = rail_len)
	cmds.rotate( ' 90deg', 0, 0)
	cmds.makeIdentity( apply=True )


	cmds.move(0, 0, rail_len/2, stair_rail[0]+".scalePivot", stair_rail[0]+".rotatePivot",  absolute=True)
	cmds.move(0,0, (-rail_len/2))



	cmds.rotate( "{0}deg".format(ang))
	cmds.move(w_val/2+0.05, 0, 0, r=True)


	cmds.move(-0.07,(pole_height/5) * 4,0, r=True)
	cmds.makeIdentity( apply=True )

	cmds.duplicate(stair_rail[0])
	cmds.move(-w_val+0.07, 0 ,0 , r=True)



#### make stair, pole, rail ###


def combine_stair(*args):
	
	############### QUERY ################
	
	w_val = cmds.intSliderGrp(width_value, q=True, value=True)
	pole_height = cmds.intSliderGrp(rail_h_value, q=True, value=True)
	count = cmds.intSliderGrp(count_value, q=True, value=True)
	h_val = 0.1
	
	############### QUERY (Heigh value) ###
	
	Angle_List = cmds.textScrollList("AngList", q=True, selectItem=True)
	
	if Angle_List[0] == '  Flat':
		h_val = 0.1
	if Angle_List[0] == '  Gentle':
		h_val = 0.5
	if Angle_List[0] == '  Normal':
		h_val = 1.0
	if Angle_List[0] == '  Steep':
		h_val = 1.5
	if Angle_List[0] == '  Very steep':
		h_val = 2.0
	
	#######################################
  
	w_val = float(w_val)
	pole_height = float(pole_height)
	h_val = float(h_val)
	
	########################################
	
	# copy stairs
	make_stair(w_val, h_val)
	
	for i in range(0,count-1):
	
		cmds.duplicate()
		cmds.move(0, h_val+0.4, -2, r=True)
		
	
	# copy poles
	make_pole(w_val, h_val, pole_height)
	
	i = 1
	while i < count :
		i = i + 3
		if (i<=count) :
			cmds.duplicate()
			cmds.move(0, (h_val+0.4) * 3, -2*3, r=True)
		
		
	# make rail
	make_rail(w_val, h_val, count, pole_height)
	
	
	## group the stairs
	cmds.group('stairs*', name='stairgrp')
	# merge the stairs
	cmds.polyUnite('stairgrp', name='stairmesh*')
	cmds.delete(ch=True)
	selstair = cmds.ls(selection=True)
	
	
	## group the poles
	cmds.group('poles*', name='polegrp')
	# merge the poles
	cmds.polyUnite('polegrp', name='polemesh*')
	cmds.delete(ch=True)
	selpole = cmds.ls(selection=True)
	
		
	## group the rails
	cmds.group('stair_rail*', 'stair_rail_underA*', 'stair_rail_underB*', name='railgrp')
	# merge the rails
	cmds.polyUnite('railgrp', name='railmesh*')
	cmds.delete(ch=True)
	selrails = cmds.ls(selection=True)
	
	cmds.group(selstair, selpole,selrails, n='stair_group')
	
	cmds.select(clear=True)
	
	
	
###############
## Window UI ##
###############
def run():
	global width_value, rail_h_value, count_value
	print '=================================='
	winID = "Mainwindow"

	if cmds.window(winID, exists=True):
		cmds.deleteUI(winID)
		
		
	cmds.window(winID, title="Easy Step 1.0", wh=(130,90), sizeable=1, menuBar=True)

	cmds.columnLayout("mainLayout", adj=True, parent=winID)



	cmds.separator(style=None, h= 9)

	cmds.text(label = " :+:   Easy Step Stair maker 1.0   :+:", fn='boldLabelFont', h = 10)

	#cmds.text(label = ":+:   rvhlu00@gmail.com   :+:" , fn="tinyBoldLabelFont")

	cmds.separator(style=None, h =15 )



	cmds.separator(style=None, bgc = (0.31,0.31,0.31), h=3 )




	cmds.separator(style=None, bgc = (0.31,0.31,0.31), h=3 )

	cmds.text ( label = "   Stair Attributes", align = "left", bgc = (0.31,0.31,0.31) )

	cmds.separator(style=None, bgc = (0.31,0.31,0.31), h=3 )


	width_value = cmds.intSliderGrp(label = 'Stair width  ', min=5, max=20, value=8, field=True)

	rail_h_value = cmds.intSliderGrp(label = 'Rail height  ', min=5, max=12, value=7, field=True)  

	count_value = cmds.intSliderGrp(label = 'Step count  ', min=1, max=50, value= 13, field=True)


	cmds.separator(style=None, bgc = (0.31,0.31,0.31), h=3 )

	cmds.text ( label = "   Stair Angle", align = "left", bgc = (0.31,0.31,0.31) )

	cmds.separator(style=None, bgc = (0.31,0.31,0.31), h=3 )

	cmds.textScrollList("AngList", h=70, append=['  Flat', '  Gentle', '  Normal', '  Steep', '  Very steep'], si='  Normal')

	cmds.button("apply_b", label='Execute', c=partial( combine_stair, 0))






	cmds.showWindow(winID)


	############################################