from Katana import NodegraphAPI


obj_dict = {'cube':'hezi','sphere':'qiu','cone':'yuanzui','rig':'dingweidian','torus':'yuanhuan'}
def create_node(nodeType,nodeName,transfrom,position,*args):

    my_node = NodegraphAPI.CreateNode('PrimitiveCreate',NodegraphAPI.GetRootNode())

    NodegraphAPI.SetNodePosition(my_node,position)

    my_node.setName(nodeName)

    my_node.getParameter('name').setValue('/root/world/geo/%s' %(nodeName),0)
        
    my_node.getParameter('type').setValue(nodeType,0)

    my_node.getParameter('transform.translate.x').setValue(transfrom,0)

    return my_node 
   
def create_merge(nodes,*args):
    mergeNode = NodegraphAPI.CreateNode('Merge', NodegraphAPI.GetRootNode())
    NodegraphAPI.SetNodePosition(mergeNode,(600,0))
    id = 0 
    for node in nodes:
        if not node:
            continue
        in_port = mergeNode.addInputPort('i%s' % id).connect(node.getOutputPort('out'))
        id += 1

def create_tools():
    obj_transfrom = 0 
    x=0
    y=100
    node_positon = x,y
    nodes = [] 
    for obj in obj_dict:
        obj_cre = create_node(obj,obj_dict[obj],obj_transfrom,node_positon)
        obj_transfrom += 4
        x += 300
        node_positon = x,y
        nodes.append(obj_cre)

    create_merge(nodes)

create_tools()




