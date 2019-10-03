import time
import re

time1 = time.time()
def get_all_render_node():
    node = []
    node_list = NodegraphAPI.GetAllNodes()
    for i in node_list:
        if i.getType() == 'Render':
            if re.match('^pass',i.getName().split('_')[-1]):
                node.append(i)
    return node

def get_input_node(node):
    get_node = node.getInputPorts()[0].getConnectedPorts()[0].getNode()
    return get_node

all_node = []
def get_inport_node(node_list):
    n = get_input_node(node_list)
    if n:
        if n.getType() != 'Dot':
            get_inport_node(n)
        all_node.append(n)

for render_node in get_all_render_node():
    get_inport_node(render_node)

for node in all_node:
    node.delete()

time2 = time.time()

time2-time1
