from Katana import NodegraphAPI


obj_dict = {'cube':'hezi','sphere':'qiu','cone':'yuanzui','rig':'dingweidian','torus':'yuanhuan'} #{物体类型：名字}
def create_node(nodeType,nodeName,transfrom,position,*args):

    my_node = NodegraphAPI.CreateNode('PrimitiveCreate',NodegraphAPI.GetRootNode()) #创建物体节点

    NodegraphAPI.SetNodePosition(my_node,position) #修改节点位置

    my_node.setName(nodeName) #修改节点名称

    my_node.getParameter('name').setValue('/root/world/geo/%s' %(nodeName),0) #修改物体名字
        
    my_node.getParameter('type').setValue(nodeType,0) #修改物体的类型

    my_node.getParameter('transform.translate.x').setValue(transfrom,0) #修改物体的位移

    return my_node 
   
def create_merge(nodes,*args):
    mergeNode = NodegraphAPI.CreateNode('Merge', NodegraphAPI.GetRootNode()) #创建合并节点
    NodegraphAPI.SetNodePosition(mergeNode,(600,0)) #修改节点位置
    id = 0 #合并节点的输入口
    for node in nodes:
        if not node:
            continue
        in_port = mergeNode.addInputPort('i%s' % id).connect(node.getOutputPort('out')) #增加合并节点的输入口并连入节点
        id += 1

def create_tools():
    obj_transfrom = 0 #物体位移
    x=0               #节点x位置  
    y=100             #节点y位置
    node_positon = x,y
    nodes = [] #创建的节点列表
    for obj in obj_dict:
        obj_cre = create_node(obj,obj_dict[obj],obj_transfrom,node_positon)
        obj_transfrom += 4
        x += 300
        node_positon = x,y
        nodes.append(obj_cre)

    create_merge(nodes)

create_tools()

'''
rootNode = NodegraphAPI.GetRootNode()
mergeNode = NodegraphAPI.CreateNode('Merge', rootNode)
for i in range(10):
    mergeNode.addInputPort('i%s' %i)

mergeNode.getInputPort('i0').connect(my_node.getOutputPort('out'))
my_node = NodegraphAPI.CreateNode('PrimitiveCreate',NodegraphAPI.GetRootNode())'''







