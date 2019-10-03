#!/usr/bin/env python
#coding=utf-8
# code by gcx

import pymel.core as pmel
import maya.cmds as cmds
from functools import partial


class LightLinks():
    def __init__(self):
        if pmel.window('LightLinks', q=1, ex=1):
            pmel.deleteUI('LightLinks')
        cmds.window('LightLinks', w=365, h=305, s=0)
        pmel.columnLayout('column')
        
        pmel.formLayout(p='column')
        pmel.rowLayout(nc=4)
        pmel.button(l='添加', w=85, h=25, c=partial(add_sel_lights,0))
        pmel.button(l='移除', w=85, h=25, c=partial(del_lights,0))
        pmel.button(l='移除所有', w=85, h=25, c=partial(del_all_lights,0))
        pmel.button(l='刷新', w=85, h=25, c=partial(refresh_lights,0))
    
        
        pmel.formLayout(p='column')
        pmel.rowLayout(nc=4)
        pmel.textScrollList('light_list', ams=True, w=260, h=200,  da=1)
        pmel.text(l="", w=5)
        pmel.button(l='补光', w=70.5, h=25, c=partial(light_links, "fast_link",0), bgc=(0.6,0.5,0))
        
        pmel.formLayout(p='column')
        pmel.rowLayout(nc=4)
        pmel.button(l='断开所有', w=85, h=25, c=partial(light_links, "global_break",0))
        pmel.button(l='链接所有', w=85, h=25, c=partial(light_links, "global_make",0))
        pmel.button(l='断开选择', w=85, h=25, c=partial(light_links, "local_break",0))
        pmel.button(l='链接选择', w=85, h=25, c=partial(light_links, "local_make",0))
    
        pmel.formLayout(p='column')
        pmel.rowLayout(nc=4)
        pmel.button(l='查看列表里的灯光', w=172.5, h=25, c=partial(check_sel_lights,0))
        pmel.button(l='检查选择的灯光链接', w=172.5, h=25, bgc=(0.3,0.35,0), c=partial(check_light_links,0))
    
        pmel.formLayout('text_form', p='column')
        pmel.columnLayout(p='text_form',bgc=(0.15,0.2,0),w=347,h=20)
        pmel.text('warming:If you selected lights in scene,do first', p='text_form',h=20)
        pmel.showWindow('LightLinks')

def add_sel_lights(*args):
    sel_list = pmel.ls(sl=1)
    exist_list = pmel.textScrollList('light_list', q=1, allItems=1)
    if exist_list:
        for sel in sel_list:
            if sel in exist_list:
                pass
            else:
                pmel.textScrollList('light_list', append=sel,e=1)
    else:
        pmel.textScrollList('light_list', append=sel_list,e=1)
    pmel.select(clear=1)

#---remove the lights selected in form
def remove_item(*args):
    pmel.textScrollList('light_list', removeItem=args, e=1)

#---remove all lights from the form
def del_all_lights(*args):
    pmel.textScrollList('light_list', removeAll=1, e=1)

#---refresh the light in the form (if you have add one light into the form,but delete it later,please refresh the lights)
def refresh_lights(*args):
    exist_list = pmel.textScrollList('light_list', q=1, allItems=1)
    if exist_list:
        for exist in exist_list:
            try:
                PyNode(exist).getShape()
                pass
            except:
                remove_item(exist)
    else:
        pass   
       
#---remove the light from the form
def del_lights(*args):
    sel_lights = pmel.ls(sl=1)
    sel_item = pmel.textScrollList('light_list', q=1, selectItem=1)
    exist_list = pmel.textScrollList('light_list', q=1, allItems=1)
    #--have
    if sel_lights:
        for sel in sel_lights:
            if sel in exist_list:
                remove_item(sel)
            else:
                pass
    #--do not have
    elif exist_list:
        if sel_item: 
            for item in sel_item:
                remove_item(item)
        else:
            pass
    else:
        pass
#---lights that selected in scene do first
def light_links(args,*argv):
    
    all_obj = pmel.ls(type='mesh')
    sel_obj = pmel.ls(sl=1)
    #sel_item = textScrollList('light_list', q=1, selectItem=1)
    exist_list = pmel.textScrollList('light_list', q=1, allItems=1)

    cmds.waitCursor(state=True)
    try:
        if args == 'fast_link':
            if exist_list:
                for exist in exist_list: 
                    pmel.select(exist,all_obj)
                    cmds.BreakLightLinks()
                    cmds.BreakShadowLinks()
                    pmel.select(exist,sel_obj)
                    cmds.MakeLightLinks()
                    cmds.MakeShadowLinks()
                pmel.select(exist_list)
            else:
                pass   
        elif args == 'global_break':
            if sel_obj:
                for sel in sel_obj:
                    pmel.select(sel,all_obj)
                    cmds.BreakLightLinks()
                    cmds.BreakShadowLinks()
                pmel.select(clear=1)
              
            elif exist_list:
                for exist in exist_list:
                    pmel.select(exist,all_obj)
                    cmds.BreakLightLinks()
                    cmds.BreakShadowLinks()
                pmel.select(clear=1)
            else:
                pass                
        elif args == 'global_make':
            if sel_obj:
                for sel in sel_obj:
                    pmel.select(sel,all_obj)
                    cmds.MakeLightLinks()
                    cmds.MakeShadowLinks()
                pmel.select(clear=1)
            elif exist_list:
                for exist in exist_list:
                    pmel.select(exist,all_obj)
                    cmds.MakeLightLinks()
                    cmds.MakeShadowLinks()
                pmel.select(clear=1)
                   
            else:
                pass 
        elif args == 'local_break':
            if exist_list:
                for exist in exist_list:
                    pmel.select(exist,sel_obj)
                    cmds.BreakLightLinks()
                    cmds.BreakShadowLinks()
                pmel.select(exist_list)
            else:
                pass
        elif args == 'local_make':
            if exist_list:
                for exist in exist_list:
                    pmel.select(exist,sel_obj)
                    cmds.MakeLightLinks()
                    cmds.MakeShadowLinks()
                pmel.select(exist_list)
            else:
                pass
        else:
            pass
    except:
        cmds.waitCursor(state=False)
    else:
        cmds.waitCursor(state=False)
        
###---check the select light links
def check_light_links(*args): 
    cmds.SelectObjectsShadowedByLight()

def check_sel_lights(*args):
    exist_list = pmel.textScrollList('light_list', q=1, allItems=1)
    if exist_list:
        pmel.select(exist_list)
    else:
        pass
        
def run():
    links = LightLinks()
