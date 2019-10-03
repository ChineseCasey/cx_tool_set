#-*- coding:utf-8 -*-
#######郭晨曦#####
import pymel.core as pmel
import maya.cmds as cmds

class RedshiftMaskSub(object):
    '''
    批量设置Redshift的Mask：
        1.选中模型后执行
    '''
    def __init__(self,cmd,value):
        self.cmd = cmd
        self.value = value
        
    def sel_obj(self,*argv):
        sel = pmel.ls(sl=1)
        if sel:
            return sel
            
    def run_def(self,*argv):
        name = self.sel_obj()
        for n in name:
            self.redshift_on_off(n,self.cmd,self.value)
            
    def redshift_on_off(self,obj_name,cmd,value,*argv):
        print obj_name,cmd,value
        if cmd == 'rsMatteEnable':
            try:
                cmds.editRenderLayerAdjustment('{}.{}'.format(obj_name,cmd),'{}.rsMatteAlpha'.format(obj_name))
                cmds.setAttr('{}.{}'.format(obj_name,cmd),value)
                cmds.setAttr(obj_name+".rsMatteAlpha",0)
            except:
                pass
        else:
            try:
                cmds.setAttr('{}.{}'.format(obj_name,cmd),value)
            except:pass
            
def sub_run(value):
    RM = RedshiftMaskSub('rsEnableSubdivision',value)
    RM.run_def()
    print RM.__doc__
    
def mask_run(value):
    RM = RedshiftMaskSub('rsMatteEnable',value)
    RM.run_def()
    print RM.__doc__
    
if __name__ == '__main__':
    mask_run(1)
    sub_run(1)