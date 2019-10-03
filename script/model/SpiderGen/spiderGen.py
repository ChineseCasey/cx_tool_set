'''
SPIDER WEB GENERATOR
PROCEDURES
Joe Withers 2016
This script will create a spiderweb in your scene once the user creates 'anchors' that are used to define the shape of the spiderweb.

NOTE: this script requires assets for the animated spider to work correctly, so please ensure that the SpiderGen folder is located at:
	maya/[VERSION]/scripts/SpiderGen
	
'''

import maya.cmds as cmds
import random 

#generate average of points in tuple
def avgPoints(pointList):
	'''
	This function finds the average position for a list of coordinates passed into it, and returns it as a coordinate.
	'''
	length = len(pointList)
	
	#averaging X

	addingX = list()

	for i in range (0,length):				#putting all of the X values in a list
		n = pointList [i][0]
		addingX.append(n)

	avgX = sum(addingX) / length			#summing the list and dividing it to find the average

	#averaging Y

	addingY = list()

	for i in range (0,length):				#putting all of the Y values in a list
		n = pointList [i][1]
		addingY.append(n)

	avgY = sum(addingY)/ length				#summing the list and dividing it to find the average

	#averaging Z

	addingZ = list()

	for i in range (0,length):				#putting all of the Z values in a list
		n = pointList [i][2]
		addingZ.append(n)

	avgZ = sum(addingZ) / length			#summing the list and dividing it to find the average

	avgPoint = avgX, avgY, avgZ				#returning all of the averages as a list, used as a coordinate
	return avgPoint

### select only the shape node function ###
def selectchild(selection):
	'''
	This function is for selecting the shape node of an object. Due to how the rebuildCurve and bezierCurveToNurbs 
	functions work, it is important to ONLY have the shape node selected when using them.
	'''
	cmds.select(selection, hierarchy = True)
	cmds.select(selection, deselect = True)

### generate a curve from positions of selection input###
def generateCurve(segments, name, namespace):
	'''
	This function generates a curve that passes through each item in the user selection.
	It does so by querying xform to get position values of each item in the list, and then
	appending them to a list to be used as CV points on the curve. The curve is then converted
	to NURBS and rebuild, allowing it to be used with Hair dynamics.
	'''
	locators = cmds.ls(selection=True)						#creates a list of the user selection
	numOfLocators = len(locators)  
	locatorPositions = []    								#an empty tuple for storing coordinates
	for locator in locators:  
		pos = cmds.xform(locator, q=True, ws=True, t=True)  #queries the xform coordinates for each item in the list
		locatorPositions.append(tuple(pos))  				#appends the coordinates to a list
	outputCurve = cmds.curve(bezier = True, point = locatorPositions, degree = numOfLocators - 1, name = str(namespace)+'curve#'+str(name))	#uses the list of coordinates for CV points on the curve.
	selectchild(outputCurve)
	cmds.bezierCurveToNurbs()						#the curves need to be converted to NURBS so that they can be rebuilt with uniform spans.
	selectchild(outputCurve)
	cmds.rebuildCurve(spans = segments)				#this is because there needs to be a sufficient number of points on each curve for the attachCurve command to work later on.
	return outputCurve

#randomise spiralpoints
def randomiseSpiralPoints(points, randomness):
	'''
	This function takes in a list of points, changes their position values by a user set random influence.
	'''
	for point in points:
		pos = cmds.xform(point, q=True, ws=True, t=True)	#queries the coordinates of a point
		ranX = random.uniform(-1,1) * randomness			#gives a random number to add to the coordinates
		ranY = random.uniform(-1,1) * randomness
		ranZ = random.uniform(-1,1) * randomness
		cmds.xform(point, t=(pos[0]+ranX,pos[1]+ranY,pos[2]+ranZ)) #changes the coordinates by adding the random number to the original coordinate 

#function for creating a locator between two points, using a distance vector, has inputs for iterative naming and adjusting the position of the locator	
def createIntermediatePoint(start, end, name, ratio, i):
	'''
	This function creates a point between two input points, with a user specified ratio for where
	it should be placed. It also has an input for numerical naming so that it is named correctly.
	'''
	
	pos1 = cmds.xform(start, q=True, ws=True, t=True) 	#queries the start coordinate
	pos2 = cmds.xform(end, q=True, ws=True, t=True)		#queries the end coordinate
	
	#finds a vector between the start and end points, then multiplies it by ratio to find the distance for the intermediate coordinate.
	distance = ratio*(pos2[0]-pos1[0]), ratio*(pos2[1]-pos1[1]), ratio*(pos2[2]-pos1[2]) 
	#finds the coordinate of the intermediate point by adding the distance vector to the start point coordinate.
	intermediate = pos1[0]+distance[0], pos1[1]+distance[1], pos1[2]+distance[2]
	
	intermediateLocator = cmds.spaceLocator(name=str(name)+str(i))
	cmds.xform(intermediateLocator, ws=True , translation=intermediate)
	return intermediateLocator

#spiralling function	
def createSpiralPoints(midPointList, startpoint, step, randomness, spiralling):
	'''
	This function creates the spiral of locators used for building the web. It does so by using the 
	createIntermediatePoint function with the average point as the 'start' point, and iterating through the 
	outer 'mid' points to be used as the 'end' point. The ratio in this function is incremented to achieve
	a spiral.
	'''
	numOfPoints = len(midPointList)									#the 'index' of the spiral, how many rotations it has to perform in the for loop to form a circle of points.
	i = 1															#an integer used for incrementing string names
	increment = startpoint											#so the user can define where the spiraling begins.
	spiralPointList = []											#an empty array for storing the string names of spiral points created.
	
	while (increment < 1):											#while loop so that it can only spiral until it reaches the midPoints.
		for point in midPointList:
			increment = increment+(step/numOfPoints)				#how far from the center the point needs to be
			point = createIntermediatePoint('avgPoint', point, 'spiralPoint', increment, i)
			increment = increment * (spiralling+1)					#multiplies the users 'spiralling' input to the increment to achieve a spiralling effect.
			spiralPointList.append(point)							#appends the created locator name to an array
			i = i+1
	
	randomiseSpiralPoints(spiralPointList, randomness)				#puts the array of points through a function to randomise their positions.
	cmds.select(*spiralPointList)									#selects all of the contents of the list.
		
#creates the boundary for the circular section of the web
def createSecondaryPoints(points, radius, roundness, startpoint, step, randomness, spiralling):
	'''
	This function creates the points that form the boundary of the spiral, called 'mid' points.
	It does so by using the createIntermediatePoint function with the average point and user selection as
	its input, and a user specified ratio used for its overall size.
	'''
	numOfPoints = len(points)
	
	cmds.select(clear=True)
	
	#creates a list of all of the boundary points
	
	for i in range(1, numOfPoints*2, 2):
		cmds.select('ogPoint'+str(i), add=True)
		
	ogList = cmds.ls(selection=True)
	ogList.append(ogList[0])	#ensures it loops correctly, potentially bad form
	
	#creates midpoints between adjacent boundary points
	
	j=2
	
	for i in range(0, numOfPoints):
		createIntermediatePoint(ogList[i],ogList[i+1],'ogPoint',0.5,j)
		j=j+2
	
	#creates a list of all of the boundary points, including the new midpoints
	
	cmds.select(clear=True)
	for i in range(1, (numOfPoints*2)+1):
		cmds.select('ogPoint'+str(i), add=True)
		
	newOgList = cmds.ls(selection=True)
	
	#creates a ring of midpoints
		
	for i in range(0, (numOfPoints*2),2):
		createIntermediatePoint('avgPoint', newOgList[i],'midPoint',radius,i+1)
	
	#offsets the intermediate point of every other one, to give it 'roundness'
	
	for i in range(1, (numOfPoints*2)+1,2):
		createIntermediatePoint('avgPoint', newOgList[i],'midPoint',radius+roundness,i+1)
			
	cmds.select(clear=True)
	
	for i in range(1, (numOfPoints*2)+1):
		cmds.select('midPoint'+str(i), add=True)
		
	midPointList = cmds.ls(selection=True)
	
	cmds.select(clear=True)
	
	#deletes the unused boundary points
	
	for i in range(2, (numOfPoints*2)+1, 2):
		cmds.delete('ogPoint'+str(i))
	
	createSpiralPoints(midPointList,startpoint, step, randomness, spiralling)

#connect radial points
def connectRadialPoints(input_namespace):
	'''
	This function generates curves going outwards from the center in a radial direction. It does this by taking each
	point in the spiral and connecting it to the one a full rotation of the spiral away from it, which is found by
	adding the number of 'midpoints' to it's numerical suffix.
	'''
	cmds.select('midPoint*')
	indexPoints = cmds.ls(selection=True)		#creates a list of the current selection, which is everything in the scene beginning with the string 'midPoint'
	indexPoints = indexPoints[0::2]				#selects every other item in the list, due to how each item appears once for it's xform node and once for it's shape node. e.g. [pSphere1,pSphere1shape]
	index = len(indexPoints)					#returns the number of points make up a full rotation around the web.

	cmds.select('spiralPoint*')					#as above, but for spiralPoints.
	spiralPoints = cmds.ls(selection=True)
	spiralPoints = spiralPoints[0::2]
	numOfPoints = len(spiralPoints)
	
	cmds.select('ogPoint*')
	ogPoints = cmds.ls(selection=True)
	ogPoints = ogPoints[0::2]
	
	for i in range(1, index+1):					#connect the points from the center to the first ring of spiral points
		cmds.select('avgPoint','spiralPoint'+str(i))
		generateCurve(3, 'inner',str(input_namespace))
		cmds.refresh()							#cmds.refresh allows the user to see it being drawn.
	
	for i in range(1, numOfPoints-index):		#connects each spiral point to the one perpendicular to it AWAY from the center, until it reaches the last ring of spiral points.
		cmds.select('spiralPoint'+str(i),'spiralPoint'+str(i+index))
		generateCurve(3, 'radial',str(input_namespace))
		cmds.refresh()
		
	outerConnect = spiralPoints[-index:-1]		#lists the outermost ring of spiral points.
	outerConnect = outerConnect[0::2]			#appends it to every other item in the list, compensating for the fact that there are half as many points created by the user as there are midPoints.
	
	for i in range(index/2):					#connects the points in outerConnect to those created by the user.
		cmds.select(ogPoints[i],(outerConnect[i]))
		generateCurve(3, 'outer',str(input_namespace))
		cmds.refresh()

#make spider
def generateSpider(input_namespace, startTime, endTime):
	'''
	this function attaches all curves together, without replacing the orignal curves, using it as a motion path
	for an animated spider. the animated spider is imported, and a simple expression links the U value of the motion
	path to a rotation attribute on the spider rig, controlling its walk cycle. there is also a custom attribute on
	the controller that appears with the spider rig, controlling the length of its steps as it walks.
	'''
	filePath = cmds.internalVar(usd=True)+'SpiderGen/spider.ma'	#the file path at which the spider model should exist
	fileExists = cmds.file(filePath, q=True, ex=True)			#queries whether the file exists
	
	if fileExists is True:
		#selects all of the spiralling curves and connects them, providing a 'path' for the spiders movement.
		cmds.select(str(input_namespace)+'curve_spiral*')								
		curves = cmds.ls(selection=True)
		path = cmds.attachCurve(curves, n=str(input_namespace)+'spiderpath', rpo=False)
		cmds.rebuildCurve(path, rt=3)
		cmds.hide(path)
		cmds.file(filePath, i=True)
		
		#renames the spider and it's callable controllers so that they are using the current 'namespace'.
		cmds.rename('SPIDER_RIG', str(input_namespace)+'SPIDER_RIG')
		cmds.rename('SCALE_HANDLE', str(input_namespace)+'CONTROLLER_ScaleMe')
		cmds.rename('CONTROLLER', str(input_namespace)+'CONTROLLER')
		
		#selects the scale controller and the path and connects them to a path animation.
		cmds.select(str(input_namespace)+'CONTROLLER_ScaleMe', path)
		cmds.pathAnimation(stu=startTime, etu=endTime, f=True, fa='x', ua='y', name=str(input_namespace)+'motionpath')
		
		#creates a command that links the controller rotation to the 'length' of the animation.
		command = str(input_namespace)+'CONTROLLER.rotateX = '+str(input_namespace)+'motionpath_uValue.output * '+str((endTime-startTime)/10)
		#creates an expression of that command which is used for moving the legs as the spider moves around the path.
		cmds.expression(name=str(input_namespace)+'leg_movement', alwaysEvaluate=True, s=command)
	else:
		#an error window for if the file is not found
		cmds.confirmDialog( title='Error', message='Spider Model not found, please ensure it located at: '+str(filePath), button=['OK'], cancelButton='OK')
		
	return fileExists	#so that the grouping functions know not to expect the spider model or motionpath
		
	
#rules or options that can be used for connecting points
def ruleDict(i,condition,index,input_namespace):
	'''
	this function specifies all of the different ways that points on the spiral can be connected, a simple connection, 
	no connection, and two ways of 'forking' the curve.
	i : the numerical name
	condition : the connection method to be used
	index : the number of midpoints, ensures the forking options select the correct point to fork to
	input namespace : for unique naming of the curves
	'''
	if condition == 1:						###straight connection between two spiral points, a 'perfect' connection.
		cmds.select('spiralPoint'+str(i))
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)
	if condition == 2:						###no connection between two points.
		cmds.refresh()
		cmds.select(clear=True)	
	if condition == 3:						###downward-end-fork, a connection that looks like this: --<
		#creates an intermediate point at a random distance between the points to 'fork' from
		midPoint = createIntermediatePoint('spiralPoint'+str(i),'spiralPoint'+str(i+1),'connectionPoint', random.uniform(0,0.5), i)	
		#connect the first point to the midpoint
		cmds.select('spiralPoint'+str(i))
		cmds.select(midPoint,add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		#connect the midpoint to the second point
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		#connect the midpoint to the spiral point perpendicular TOWARDS the middle of the web to the second point.
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1-index),add=True)
		generateCurve(1, 'connecting',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)	
		cmds.delete(midPoint)				#deletes the midpoint.
	if condition == 4:						###downward-start-fork, a connection that looks like this: >--
		#creates an intermediate point at a random distance between the points to 'fork' from
		midPoint = createIntermediatePoint('spiralPoint'+str(i),'spiralPoint'+str(i+1),'connectionPoint', random.uniform(0.5,1), i)		
		#connect the first point to the midpoint
		cmds.select('spiralPoint'+str(i))
		cmds.select(midPoint,add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		#connect the midpoint to the second point
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		#connect the midpoint to the spiral point perpendicular TOWARDS the middle of the web to the first point.
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i-index),add=True)
		generateCurve(1, 'connecting',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)	
		cmds.delete(midPoint)				#deletes the midpoint.

#not my weighted choice algorithm	
def weighted_choice(weights):
	'''
	a function for doing weighted random choice. http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python i couldn't work out an simple way of doing this myself.
	'''
	rnd = random.random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0:
			return i

#connects the points on the spiral
def connectSpiralPoints(input_namespace,imperfection):
	'''
	this function connects each of the 'spiralpoints' in a rotational direction. It has a user input for 'imperfection' which
	affects the weighting of the random choice used to connect the points in ruleDict.
	'''
	cmds.select('spiralPoint*')
	spiralPoints = cmds.ls(selection=True)
	spiralPoints = spiralPoints[0::2]
	numOfPoints = len(spiralPoints)
	
	cmds.select('midPoint*')
	indexPoints = cmds.ls(selection=True)
	indexPoints = indexPoints[0::2]
	index = len(indexPoints)
	
	cmds.select(clear=True)
	
	for i in range(1, index+1):								#connecting the innermost spiral ring
		randomInput = [1,2]									#i do not want any 'forking' curves as they will have nowhere to 'fork' to at the center of the spiral.
		randomWeight = [1,imperfection]						#hence the random input will only choose from straight connections and no connections.
															#the weighting is always 1 for the straight connection option, and the other options increase in weighting as 'imperfection' is added.
		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)	#this calls the ruleDict to create a curve, given the option returned by the random weighted choice.
			
	for i in range(index+1, numOfPoints-index-1):			#connecting the spiral points to each other
		randomInput = [1,2,3,4]								#can choose from any option of connection.
		randomWeight = [1,imperfection,imperfection,imperfection]	#as above
		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)	#as above
	
	for i in range(numOfPoints-index-1, numOfPoints-1):		#connecting the last ring of spiral points
		randomInput = [1,3,4]								#can perform any kind of connection EXCEPT 'no connection', as it doesn't look very good on the outer ring
		randomWeight = [1,imperfection,imperfection]		#as above
		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)	#as above

#generates locators on user selection, and also a loctator at the midpoint of these	
def createPrimaryPoints(radius, roundness, startpoint, step, randomness, spiralling):
	'''
	this function places a locator at each item in the user selection, and also one at the average of those points.
	the numerical naming is offset to that the naming is consistent.
	it then calls the secondary point command to create the midpoint ring.
	'''
	#generate points for user input
	controlPoints = cmds.ls(selection=True)
	controlPointPositions = []
	#these points need to be named numerically using odd numbers 1,3,5,7 etc as midpoints will be created in between them, and this makes connecting easier later on.
	i = 1   #integer for naming
	for point in controlPoints:  							#creates a list of coordinates from the user input
		pos = cmds.xform(point, q=True, ws=True, t=True)  
		controlPointPositions.append(tuple(pos))
	for pointPosition in controlPointPositions:				#creates a locator and moves it to the coordinates specified in the list.
		outputLocator = cmds.spaceLocator(name='ogPoint'+str(i))
		cmds.xform(outputLocator, ws=True , translation=pointPosition)
		i = i+2		#ensures numerical naming in odd numbers

	avgLocator = cmds.spaceLocator(name='avgPoint')			#creates a locator to be used as the average point
	cmds.xform(avgLocator, ws=True , translation=avgPoints(controlPointPositions))		#calls the averaging points ocmmand 
	createSecondaryPoints(controlPoints, radius, roundness, startpoint, step, randomness, spiralling)	#calls the secondary points command.

#creating named locators
def createAnchor(*args):
	'''
	this function creates a named locator called 'Anchor' to be used to define the shape of the spiderweb.
	'''
	cmds.spaceLocator(n='Anchor1', a=True)
	
#main running function
def createSpiderWeb(radius, roundness, startpoint, step, randomness, spiralling, spider, startTime, endTime, inputImperfection, deleteAnchors):
	'''
	this is the main running function, it has if statements to ensure that the user input is correct, and an error counter that acts as a failsafe to ensure
	that the user input is correct before running. 
	'''
	errors = 0	#error counter
	anchors = cmds.ls('Anchor*')	#creates a list of all of the anchors
	cmds.select(anchors[0::2])		#omits the shape nodes
	if startTime > endTime:			#ensures that the user hasn't put a start time greater than the end time, and alerts them if so
		cmds.confirmDialog( title='Error', message='Animation Start Time cannot be greater than the End Time', button=['OK'], cancelButton='OK')
		errors = 1
	if len(cmds.ls(selection=True)) < 3:	#ensures that the user has created at least 3 points, otherwise the script plots all of its points in a line or on a point
		cmds.confirmDialog( title='Error', message='Please create at least 3 Anchors.', button=['OK'], cancelButton='OK')
		errors = 1
	if step < 0.01:					#ensures the step is always a positive number, theoretically not needed as the UI has limits, but useful when running this function on its own.
		cmds.confirmDialog( title='Error', message='Step is too small.', button=['OK'], cancelButton='OK')
		errors = 1
	elif errors == 0:	
		createPrimaryPoints(radius, roundness/20, startpoint, step/8, randomness/5, spiralling/20)	#create the points
		namespace = cmds.group( em=True, name='spiderweb')+'_'										#create an empty group, the string name is used as a unique namespace
		cmds.hide('ogPoint*','avgPoint','midPoint*','spiralPoint*')									#hides all of the points
		connectSpiralPoints(namespace, inputImperfection)											#connects the spiral points
		connectRadialPoints(namespace)																#connects the radial points
		if spider is True:																			#creates a spider if the user has specified
			spider = generateSpider(namespace, startTime, endTime)									#generateSpider returns whether the spider creation was successful, so the spider variable is replaced with the result
		
		cmds.delete('ogPoint*','avgPoint','midPoint*','spiralPoint*')								#deletes all of the locators
		
		cmds.select(str(namespace)+'curve*')														#selects all curves
	
		if spider is True:																			#selects the spider assets but only if they have been created
			cmds.select(str(namespace)+'spiderpath', add = True)
			cmds.select(str(namespace)+'SPIDER_RIG', add = True)   		
		
		cmds.parent(cmds.ls(selection = True), str(namespace.rstrip('_')))							#parents the curves to the group created at the beginning
		
		if deleteAnchors is True:																	#if the user wants the anchors can be deleted
			cmds.delete('Anchor*')