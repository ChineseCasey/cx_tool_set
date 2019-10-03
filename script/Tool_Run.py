# -*- coding:utf-8 -*-
import os,sys
import project_path
import json
import maya.cmds as cmds
from functools import partial

#配置文件地址
def file_config_path():
    path = os.path.join(project_path.get_path(),'config_file')
    file_path = os.path.join(path,'tool_config.json')
    return file_path

#打开配置文件
def open_config():
    with open(file_config_path(),'r') as config_path:
        dict = json.load(config_path)
        return dict

class Tool_Set(object):

    def __init__(self):
        pass
    def create_tool_menu(self,*argv):
        self._create_menu_item()
        print '******************'
    def _create_menu_item(self,*argv):
        print '======='
        if cmds.menu('tool_main_menu', q=1 , ex=1):
            cmds.deleteUI('tool_main_menu')
        main_menu = cmds.menu('tool_main_menu', p='MayaWindow', l=u'【CX_Tool_Set】', tearOff=True)
        for fi in open_config():
            cmds.menuItem(p=main_menu, subMenu=True, tearOff=True, l=fi)
            for fc in open_config().get(fi):
                command = open_config().get(fi).get(fc)[0]
                print command
                if open_config().get(fi).get(fc)[1] == True:
                    op_command = open_config().get(fi).get(fc)[2]
                    cmds.menuItem(tearOff=True, l=fc, c=command )
                    cmds.menuItem(optionBox=True, c=op_command)
                else:
                    cmds.menuItem(tearOff=True, l=fc, c=command )

if __name__ == '__main__':
    aa = Tool_Set()
    aa.create_tool_menu()
    #aa._create_menu_item()