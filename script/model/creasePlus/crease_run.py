import maya.mel as mel
import os


def run():
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    script_path = path+"/script/model/creasePlus/CreasePlus.mel"
    script_path_one = path+"/script/model/creasePlus/CreasePlus_Extension1.mel"

    mel.eval('source "%s";' %script_path)
    mel.eval('source "%s";' %script_path_one)
