#coding=gbk
#__Author__GCX
import maya.cmds as cmds
import pymel.core as pmel
from functools import partial
import random

class XYZItem(object):
    
    def __init__(self,x,y,z,name='',string_name='',parent=None):
        self.x = x
        self.y = y
        self.z = z
        self.lay = cmds.rowLayout(p=parent,numberOfColumns=8,bgc=[0.4,0.45,0.45])
        cmds.text(l=name,ann=string_name)
        self.lay1 = cmds.rowLayout(p=self.lay,numberOfColumns=6,en=0)
        cmds.text(l='X:')
        self.Xx = cmds.textField(w=40,tx=self.x,en=1,ann='输入需要调整的X轴数值')
        cmds.text(l='Y:')
        self.Yy = cmds.textField(w=40,tx=self.y,en=1,ann='输入需要调整的Y轴数值')
        cmds.text(l='Z:')
        self.Zz = cmds.textField(w=40,tx=self.z,en=1,ann='输入需要调整的Z轴数值')
        cmds.checkBox(p=self.lay,l='Look\nor\nUnlook',onc=partial(self.un_look_text,1),
                      ofc=partial(self.un_look_text,0),
                      ann='解锁需要的控制的属性')
        
    def un_look_text(self,value,*args):
        cmds.rowLayout(self.lay1,e=1,en=value)
        
    def _get_field_value(self,*args):
        x = cmds.textField(self.Xx,q=1,tx=1)
        y = cmds.textField(self.Yy,q=1,tx=1)
        z = cmds.textField(self.Zz,q=1,tx=1)
        return x,y,z
        
class RandomTool(object):
    
    def __init__(self):
       
        self.list_emitter_delete = []
        if cmds.window('main_random_win',q=1,ex=1):
            cmds.deleteUI('main_random_win')
        cmds.window('main_random_win',menuBar=True,t='random_plan    ---GCX',w=300,h=300,s=1)
        cmds.menu(l='help',tearOff=True)
        self.main_lay = cmds.columnLayout(adj=1)
        cmds.separator(style='in' )
        self.title_lay = cmds.rowLayout(p=self.main_lay,numberOfColumns=5,vis=0)
        cmds.button(l='help',vis=0)
        cmds.text(l='    ')
        self.close_emitter_btn = cmds.button(l='CloseEmitter',vis=1,c=partial(self._delete_emitter),ann='清除发射器（一般用不到）')
        cmds.text(l='    ')
        self.ShowNewObjectList = cmds.button(l='ShowNewObjectList',c=partial(self._hide_show_new_list,1),vis=1,ann='显示新创建物体列表')
        cmds.rowLayout(p=self.main_lay,numberOfColumns=3)
        cmds.text(l=' Plan:',ann='地面')
        self.plan_text = cmds.textField(w=200,ed=0,ann='放入需要产生随机点的地面')
        cmds.button(l='SelectPlan', c=partial(self._sel_plan),ann='添加地面')
        scroll_layout = cmds.rowLayout(p=self.main_lay,numberOfColumns = 3)
        cmds.text(l=' OBJ: ',ann='添加的物体列表')
        self.obj_list = cmds.textScrollList(w=200,ann='放入需要进行随机的模型')
        cmds.columnLayout(p=scroll_layout)
        cmds.button(l='+',w=30,c=partial(self._add_obj),ann='添加需要进行随机的模型')
        cmds.text(l='')
        cmds.button(l='-',w=30,c=partial(self._remove_obj),ann='清除列表里选择的模型')
        cmds.text(l='')
        cmds.button(l='clear',w=30, c=partial(self._remove_all),ann='清除列表里所有的模型')
        
        cmds.text(p=self.main_lay,l='')
        self.trans_item_ui = XYZItem(0,0,0,name='Translate:',string_name='位移属性',parent=self.main_lay)
        cmds.text(p=self.main_lay,l='')
        self.rotate_item_ui = XYZItem(0,360,0,name='Rotate:   ',string_name='旋转属性',parent=self.main_lay)
        cmds.text(p=self.main_lay,l='')
        self.scale_item_ui = XYZItem(0,0,0,name='Scale:      ',string_name='缩放属性',parent=self.main_lay)
        cmds.text(p=self.main_lay,l='')
        
        cmds.rowLayout(p=self.main_lay,numberOfColumns=2)
        self.point_number = cmds.intSliderGrp(l='PointNumber:',field=True,cw3=[73,80,130],minValue=2, 
                            maxValue=999, fieldMinValue=0, 
                            fieldMaxValue=99999, value=200,
                            ann='输入需要随机产生的数量 ')
        cmds.button(p=self.main_lay,l='RandomPoint',w=295,c=partial(self._random_point),
                                                    ann='点击在选择的面上随机复制列表里的模型')
        
        self.list_new_obj = cmds.rowLayout(p=self.main_lay,numberOfColumns=3,vis=0)
        cmds.text(l='New\nObject:')
        self.new_obj_list = cmds.textScrollList(w=200,ann='新创建模型列表')
        cmds.columnLayout(p=self.list_new_obj)
        cmds.button(l='Hide',c=partial(self._hide_show_new_list,0),ann='隐藏新创建物体列表')
        cmds.text(l='')
        cmds.button(l='Select\n new \n object', c=partial(self._random_new_obj),ann='选择列表里的模型')
        
        cmds.button(p=self.main_lay,l='test',c=partial(self.test),vis=0)
        self.progress = cmds.progressBar(p=self.main_lay,w=300,vis=0)
        cmds.helpLine(p=self.main_lay,w=300,bgc=[0.1,0.1,0.1])
        cmds.showWindow()

    def _add_obj(self,*args):
        sel_obj = cmds.ls(sl=1)
        if sel_obj:
            exist_list = cmds.textScrollList(self.obj_list,q=1,ai=1)
            if exist_list:
                for sel in sel_obj:
                    if sel not in exist_list:
                        cmds.textScrollList(self.obj_list,e=1,a=sel)
            else:
                cmds.textScrollList(self.obj_list,e=1,a=sel_obj)
        else:
            print 'no select obj'
            
    def _remove_obj(self,*args):
        item = cmds.textScrollList(self.obj_list,q=1,si=1)
        if item:
            cmds.textScrollList(self.obj_list,e=1,ri=item)
        else:
            print 'no select item'
    def _remove_all(self,*args):
        cmds.textScrollList(self.obj_list,e=1,ra=1)
            
    def _sel_plan(self,*args):
        sel_plan = cmds.ls(sl=1)
        if sel_plan:
            print sel_plan
            cmds.textField(self.plan_text,e=1,tx=sel_plan[0])
        else:
            print 'no select obj plan'
            
    def _random_point(self,*args):
        time = pmel.playbackOptions(q=1,min=1)
        
        number = cmds.intSliderGrp(self.point_number,q=1,v=1)
        plan_name = cmds.textField(self.plan_text,q=1,tx=1)
        
        cmds.select(plan_name)
        
        self._create_particle(number)

        #cmds.rowLayout(self.title_lay,e=1,vis=1)
        #cmds.button(self.close_emitter_btn,e=1,vis=1)
        
        for time in range(0,10):
            cmds.currentTime(time)
            
        self._hide_show_new_list(1)
        #cmds.button(self.ShowNewObjectList,e=1,vis=1)
        sel_obj_list = cmds.textScrollList(self.obj_list,q=1,ai=1)
        if sel_obj_list:
            tx = self.trans_item_ui._get_field_value()
            rx = self.rotate_item_ui._get_field_value()
            sy = self.scale_item_ui._get_field_value()
            print type(float(rx[0])),type(float(rx[1])),type(float(rx[2]))
            
            pmel.group(self._create_tree(obj_list=sel_obj_list,
                                         tx=float(tx[0]),
                                         ty=float(tx[1]),
                                         tz=float(tx[2]),
                                         rx=float(rx[0]),
                                         ry=float(rx[1]),
                                         rz=float(rx[2]),
                                         sx=float(sy[0]),
                                         sy=float(sy[0]),
                                         sz=float(sy[0])),
                         n='tree')
            
        self._delete_emitter()
        pmel.currentTime(int(time))
        
    def _delete_emitter(self,*argv):
        pmel.delete(self.list_emitter_delete)
        print 'delete:%s' %self.list_emitter_delete
        self.list_emitter_delete = []
        
        
    def _create_particle(self,value,*argv):
        global n_particle_create
        pmel.emitter( r=value,dx=1, dy=0, dz=0, sp=0, nsp=0, n='myRandomEmitter' ,type='surface')
        n_particle_create = pmel.nParticle( n='emittedParticles' )
        n_particle_create[1].maxCount.set(value)
        nucleus = pmel.listConnections(n_particle_create,t='nucleus')
        nucleus[0].gravity.set(0)
        pmel.connectDynamic( 'emittedParticles', em='myRandomEmitter')
        self.list_emitter_delete.append('myRandomEmitter')
        self.list_emitter_delete.append(n_particle_create)
        self.list_emitter_delete.append(nucleus)
        
    def _create_tree(self,obj_list='',tx=0,ty=0,tz=0,rx=10,ry=10,rz=10,sx=0,sy=0,sz=0,*args):
        cmds.progressBar(self.progress,e=1,step=0,vis=1)
        cmds.textScrollList(self.new_obj_list,e=1,ra=1)
        grp_obj_list = []
        dup_obj_str = []
        pp = pmel.PyNode('emittedParticlesShape')
        priticle_id = range(len(pp.particleIds()))
        sel_obj = obj_list
        if sel_obj:
            for p in priticle_id:
                rand_tx = random.uniform(-tx,tx)
                rand_ty = random.uniform(-ty,ty)
                rand_tz = random.uniform(-tz,tz)
                
                rand_rx = random.uniform(-rx,rx)
                rand_ry = random.uniform(-ry,ry)
                rand_rz = random.uniform(-rz,rz)
                
                rand_sx = random.uniform(0,sx)
                rand_sy = random.uniform(0,sy)
                rand_sz = random.uniform(0,sz)
                
                random_sel_obj = random.randint(0,len(sel_obj)-1)
                
                priticle_trans = pmel.getParticleAttr(n_particle_create[0].pt[p],a=1,at='position')
                obj = pmel.duplicate(sel_obj[random_sel_obj])
                grp_obj_list.append(obj)
                pmel.xform(obj,t=priticle_trans)
                tx_get = obj[0].tx.get()
                ty_get = obj[0].ty.get()
                tz_get = obj[0].tz.get()
                
                rx_get = obj[0].rx.get()
                ry_get = obj[0].ry.get()
                rz_get = obj[0].rz.get()
                
                sx_get = obj[0].sx.get()
                sy_get = obj[0].sy.get()
                sz_get = obj[0].sz.get()
                
                obj[0].tx.set(tx_get+rand_tx)
                obj[0].ty.set(ty_get+rand_ty)
                obj[0].tz.set(tz_get+rand_tz)
                
                obj[0].rx.set(rx_get+rand_rx)
                obj[0].ry.set(ry_get+rand_ry)
                obj[0].rz.set(rz_get+rand_rz)
                
                obj[0].sx.set(sx_get+rand_sx)
                obj[0].sy.set(sy_get+rand_sy)
                obj[0].sz.set(sz_get+rand_sz)
                dup_obj_str.append(str(obj[0]))
                
                cmds.textScrollList(self.new_obj_list,e=1,a=str(obj[0]),si=str(obj[0]))
                cmds.progressBar(self.progress,maxValue=len(priticle_id)-1,e=1,step=1)
                cmds.refresh()
        
            
        return grp_obj_list
        
    def _random_new_obj(self,*args):
        obj_list = cmds.textScrollList(self.new_obj_list,q=1,ai=1)
        if obj_list:
            pmel.select(obj_list)
        else:
            print '列表没有模型'
    def _hide_show_new_list(self,value,*args):
        cmds.rowLayout(self.list_new_obj,e=1,vis=value)
        
    def test(self,*args):
        print self.rotate_item_ui._get_field_value()
        print self.scale_item_ui._get_field_value()
        
def run():
	rt = RandomTool()

