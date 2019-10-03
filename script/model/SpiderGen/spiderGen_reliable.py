import maya.cmds as cmds
import random 

#generate average of points in tuple
def avgPoints(pointList):
	'''
	this function finds the average position for a list of coordinates passed into it.
	'''
	length = len(pointList)
	
	#averaging X

	addingX = list()

	for i in range (0,length):
		n = pointList [i][0]
		addingX.append(n)

	avgX = sum(addingX) / length

	#averaging Y

	addingY = list()

	for i in range (0,length):
		n = pointList [i][1]
		addingY.append(n)

	avgY = sum(addingY)/ length

	#averaging Z

	addingZ = list()

	for i in range (0,length):
		n = pointList [i][2]
		addingZ.append(n)

	avgZ = sum(addingZ) / length

	avgPoint = avgX, avgY, avgZ
	return avgPoint

### select only the shape node function ###
def selectchild(selection):
	'''
	due to how the rebuildCurve and bezierCurveToNurbs functions work, it is important
	to ONLY have the shape node selected when using them.
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
	locators = cmds.ls(selection=True)
	numOfLocators = len(locators)  
	locatorPositions = []    
	for locator in locators:  
		pos = cmds.xform(locator, q=True, ws=True, t=True)  
		locatorPositions.append(tuple(pos))  
	outputCurve = cmds.curve(bezier = True, point = locatorPositions, degree = numOfLocators - 1, name = str(namespace)+'curve#'+str(name))
	selectchild(outputCurve)
	cmds.bezierCurveToNurbs()
	selectchild(outputCurve)
	cmds.rebuildCurve(spans = segments)
	return outputCurve

#randomise spiralpoints
def randomiseSpiralPoints(points, randomness):
	'''
	This function takes in a list of points, changes their position values by a user set random influence.
	'''
	for point in points:
		pos = cmds.xform(point, q=True, ws=True, t=True)
		ranX = random.uniform(-1,1) * randomness
		ranY = random.uniform(-1,1) * randomness
		ranZ = random.uniform(-1,1) * randomness
		cmds.xform(point, t=(pos[0]+ranX,pos[1]+ranY,pos[2]+ranZ))

#function for creating a locator between two points, using a distance vector, has inputs for iterative naming and adjusting the position of the locator	
def createIntermediatePoint(start, end, name, ratio, i):
	'''
	This function creates a point between two input points, with a user specified ratio for where
	it should be placed. It also has an input for numerical naming so that it is named correctly.
	'''
	
	pos1 = cmds.xform(start, q=True, ws=True, t=True) 
	pos2 = cmds.xform(end, q=True, ws=True, t=True)
	
	distance = ratio*(pos2[0]-pos1[0]), ratio*(pos2[1]-pos1[1]), ratio*(pos2[2]-pos1[2])
	intermediate = pos1[0]+distance[0], pos1[1]+distance[1], pos1[2]+distance[2]
	
	intermediateLocator = cmds.spaceLocator(name=str(name)+str(i))
	cmds.xform(intermediateLocator, ws=True , translation=intermediate)
	return intermediateLocator

#spiralling function here	
def createSpiralPoints(midPointList, startpoint, step, randomness, spiralling):
	'''
	This function creates the spiral of locators used for building the web. It does so by using the 
	createIntermediatePoint function with the average point as the 'start' point, and iterating through the 
	outer 'mid' points to be used as the 'end' point. The ratio in this function is incremented to achieve
	a spiral.
	'''
	numOfPoints = len(midPointList)
	i = 1
	increment = startpoint
	spiralPointList = []
	
	while (increment < 1):
		for point in midPointList:
			increment = increment+(step/numOfPoints)
			point = createIntermediatePoint('avgPoint', point, 'spiralPoint', increment, i)
			increment = increment * (spiralling+1)
			spiralPointList.append(point)
			i = i+1
	
	randomiseSpiralPoints(spiralPointList, randomness)
	cmds.select(*spiralPointList)
		
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
	indexPoints = cmds.ls(selection=True)
	indexPoints = indexPoints[0::2]
	index = len(indexPoints)

	cmds.select('spiralPoint*')
	spiralPoints = cmds.ls(selection=True)
	spiralPoints = spiralPoints[0::2]
	numOfPoints = len(spiralPoints)
	
	for i in range(1, index+1):
		cmds.select('avgPoint','spiralPoint'+str(i))
		generateCurve(3, 'inner',str(input_namespace))
		cmds.refresh()
	
	for i in range(1, numOfPoints-index):
		cmds.select('spiralPoint'+str(i),'spiralPoint'+str(i+index))
		generateCurve(3, 'radial',str(input_namespace))
		cmds.refresh()
		
	cmds.select('ogPoint*')
	ogPoints = cmds.ls(selection=True)
	ogPoints = ogPoints[0::2]
	
	outerConnect = spiralPoints[-index:-1]
	outerConnect = outerConnect[0::2]
	
	for i in range(index/2):
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
	filePath = cmds.internalVar(usd=True)+'SpiderGen/spider.ma'	
	fileExists = cmds.file(filePath, q=True, ex=True)
	
	if fileExists is True:
		cmds.select(str(input_namespace)+'curve_spiral*')
		curves = cmds.ls(selection=True)
		path = cmds.attachCurve(curves, n=str(input_namespace)+'spiderpath', rpo=False)
		cmds.rebuildCurve(path, rt=3)
		cmds.hide(path)
		cmds.file(filePath, i=True)
		
		cmds.rename('SPIDER_RIG', str(input_namespace)+'SPIDER_RIG')
		cmds.rename('SCALE_HANDLE', str(input_namespace)+'CONTROLLER_ScaleMe')
		cmds.rename('CONTROLLER', str(input_namespace)+'CONTROLLER')
		
		cmds.select(str(input_namespace)+'CONTROLLER_ScaleMe', path)
		cmds.pathAnimation(stu=startTime, etu=endTime, f=True, fa='x', ua='y', name=str(input_namespace)+'motionpath')
		
		command = str(input_namespace)+'CONTROLLER.rotateX = '+str(input_namespace)+'motionpath_uValue.output * '+str((endTime-startTime)/10)
		
		cmds.expression(name=str(input_namespace)+'leg_movement', alwaysEvaluate=True, s=command)
	else:
		cmds.confirmDialog( title='Error', message='Spider Model not found, please ensure it located at: '+str(filePath), button=['OK'], cancelButton='OK')
		
	return fileExists
		
	
#rules or options that can be used for connecting points
def ruleDict(i,condition,index,input_namespace):
	'''
	this function specifies all of the different ways that points on the spiral can be connected, a simple connection, 
	no connection, and two ways of 'forking' the curve.
	'''
	if condition == 1:						###straight connection
		cmds.select('spiralPoint'+str(i))
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)
	if condition == 2:						###no connection
		cmds.refresh()
		cmds.select(clear=True)	
	if condition == 3:						###downward-end-fork	
		midPoint = createIntermediatePoint('spiralPoint'+str(i),'spiralPoint'+str(i+1),'connectionPoint', random.uniform(0,0.5), i)		
		cmds.select('spiralPoint'+str(i))
		cmds.select(midPoint,add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1-index),add=True)
		generateCurve(1, 'connecting',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)	
		cmds.delete(midPoint)
	if condition == 4:						###downward-start-fork	
		midPoint = createIntermediatePoint('spiralPoint'+str(i),'spiralPoint'+str(i+1),'connectionPoint', random.uniform(0.5,1), i)		
		cmds.select('spiralPoint'+str(i))
		cmds.select(midPoint,add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i+1),add=True)
		generateCurve(1, 'spiral',str(input_namespace))
		
		cmds.select(midPoint)
		cmds.select('spiralPoint'+str(i-index),add=True)
		generateCurve(1, 'connecting',str(input_namespace))
		cmds.refresh()
		cmds.select(clear=True)	
		cmds.delete(midPoint)

#not my weighted choice algorithm	
def weighted_choice(weights): ###http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python
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
	
	for i in range(1, index+1):
		randomInput = [1,2]
		randomWeight = [1,imperfection]

		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)
			
	for i in range(index+1, numOfPoints-index-1):
		randomInput = [1,2,3,4]
		randomWeight = [1,imperfection,imperfection,imperfection]
		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)
	
	for i in range(numOfPoints-index-1, numOfPoints-1):
		randomInput = [1,3,4]
		randomWeight = [1,imperfection,imperfection]
		ruleDict(i,randomInput[weighted_choice(randomWeight)],index,input_namespace)

#generates locators on user selection, and also a loctator at the midpoint of these	
def createPrimaryPoints(radius, roundness, startpoint, step, randomness, spiralling):
	'''
	this function places a locator at each item in the user selection, and also creates a locator between each of neighboring point.
	the numerical naming is offset to that the naming is consistent.
	'''
	#generate points for user input
	controlPoints = cmds.ls(selection=True)
	controlPointPositions = []
	
	i = 1    
	for point in controlPoints:  
		pos = cmds.xform(point, q=True, ws=True, t=True)  
		controlPointPositions.append(tuple(pos))
	for pointPosition in controlPointPositions:
		outputLocator = cmds.spaceLocator(name='ogPoint'+str(i))
		cmds.xform(outputLocator, ws=True , translation=pointPosition)
		i = i+2

	avgLocator = cmds.spaceLocator(name='avgPoint')
	cmds.xform(avgLocator, ws=True , translation=avgPoints(controlPointPositions))
	createSecondaryPoints(controlPoints, radius, roundness, startpoint, step, randomness, spiralling)

#creating named locators
def createAnchor(*args):
	cmds.spaceLocator(n='Anchor1', a=True)
	
#main running function
def createSpiderWeb(radius, roundness, startpoint, step, randomness, spiralling, spider, startTime, endTime, inputImperfection, deleteAnchors):
	'''
	this is the main running function.
	'''
	errors = 0
	anchors = cmds.ls('Anchor*')
	cmds.select(anchors[0::2])
	if startTime > endTime:
		cmds.confirmDialog( title='Error', message='Animation Start Time cannot be greater than the End Time', button=['OK'], cancelButton='OK')
		errors = 1
	if len(cmds.ls(selection=True)) < 3:
		cmds.confirmDialog( title='Error', message='Please create at least 3 Anchors.', button=['OK'], cancelButton='OK')
		errors = 1
	if step < 0.01:
		cmds.confirmDialog( title='Error', message='Step is too small.', button=['OK'], cancelButton='OK')
		errors = 1
	elif errors == 0:
		
		createPrimaryPoints(radius, roundness/20, startpoint, step/8, randomness/5, spiralling/20)
		namespace = cmds.group( em=True, name='spiderweb')+'_'
		cmds.hide('ogPoint*','avgPoint','midPoint*','spiralPoint*')
		connectSpiralPoints(namespace, inputImperfection)	
		connectRadialPoints(namespace)
		if spider is True:
			spider = generateSpider(namespace, startTime, endTime)
		
		cmds.delete('ogPoint*','avgPoint','midPoint*','spiralPoint*')
	
		cmds.select(str(namespace)+'curve*')
	
		if spider is True:
			cmds.select(str(namespace)+'spiderpath', add = True)
			cmds.select(str(namespace)+'SPIDER_RIG', add = True)   		
		
		cmds.parent(cmds.ls(selection = True), str(namespace.rstrip('_')))
		
		if deleteAnchors is True:
			cmds.delete('Anchor*')
