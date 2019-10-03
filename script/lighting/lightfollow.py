#!/usr/bin/env python
#coding=gbk
#__Auther__Casey(gcx)
from PySide import QtGui,QtCore
import maya.cmds as cmds

class LightFollow(QtGui.QWidget):
    '''
    
    灯光跟随控制器移动使用帮助:
        1.先选择需要跟随的物体点击“sel”。
        2.再选择灯光，选择跟随模式。
        3.点击“创建跟随”。
        
    '''
    def __init__(self,parent=None):
        super(LightFollow,self).__init__(parent)
        self.setWindowTitle('LightFollow       ---guochenxi')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #self.setFixedSize(450,120)
        #主lay
        self._main_window = QtGui.QVBoxLayout()
        self._main_window.setContentsMargins(1,1,1,1)
        self._main_label = QtGui.QLabel(u'------先选择需要跟随的物体点击“sel”，再选择灯光，选择跟随模式，点击“创建跟随”。------')
        self._main_label.setStyleSheet('color: yellow')
        #横向lay第一行
        self._lay_one = QtGui.QHBoxLayout()
        self._lay_one.setContentsMargins(0,0,0,0)
        
        self._sel_tex = QtGui.QLabel(u' 选择跟随的物体:')
        self._sel_tex.setStyleSheet("font: 90 9pt \"\351\273\221\344\275\223\";")
        self._sel_obj_name = QtGui.QLineEdit()
        self._sel_obj_name.setEnabled(False)
        self._sel_btn = QtGui.QPushButton('sel')
        self._sel_btn.setFixedWidth(30)
        self._sel_btn.clicked.connect(self._Select_Controller)
        self._lay_one.addWidget(self._sel_tex)
        self._lay_one.addWidget(self._sel_obj_name)
        self._lay_one.addWidget(self._sel_btn)
        #横向lay第二行
        self._lay_two = QtGui.QHBoxLayout()
        self._type_follow = QtGui.QLabel(u' 跟随类型: ')
        self._type_follow.setStyleSheet("font: 90 9pt \"\351\273\221\344\275\223\";")
        self._radio_btn_one = QtGui.QRadioButton(u'父子关系')
        self._radio_btn_two = QtGui.QRadioButton(u'位移跟随')
        self._radio_btn_two.setChecked(True)
        self._radio_btn_three = QtGui.QRadioButton(u'跟随旋转')
        self._radio_btn_four = QtGui.QRadioButton(u'灯光旋转跟随物体位移')

        self._lay_two.addWidget(self._type_follow)
        self._lay_two.addWidget(self._radio_btn_one)
        self._lay_two.addWidget(self._radio_btn_two)
        self._lay_two.addWidget(self._radio_btn_three)
        self._lay_two.addWidget(self._radio_btn_four)

        self._follow_btn = QtGui.QPushButton(u'创建跟随')
        self._follow_btn.setStyleSheet('color: rgb(50,255,255);font: 75 9pt;')
        self._follow_btn.clicked.connect(self._Controller_type)
        #self._main_window.addWidget(self._main_label)
        self._main_window.addLayout(self._lay_one)
        self._main_window.addLayout(self._lay_two)
        self._main_window.addWidget(self._follow_btn)
        self.setLayout(self._main_window)
        
    def _Select_Controller(self,*argv):
        select_obj = cmds.ls(sl=1)
        if select_obj:
            if len(select_obj) < 2:
                self._sel_obj_name.setText(select_obj[0])
                
            else:
                print u'只能选择一个物体'
        else:
            print u'没有选择物体'
            
    def _Select_light(self,*argv):
        select_light = cmds.ls(sl=1)
        if select_light:
            return select_light
        else:
            print u'没有选择灯光'
            
    def _Controller_type(self,*argv):
        obj_name = self._sel_obj_name.text()
        light_name = self._Select_light()
        if self._radio_btn_one.isChecked():
            self._Parent_Controller(light_name,obj_name)
            
        elif self._radio_btn_two.isChecked():
            self._point_Controller(light_name,obj_name)
            
        elif self._radio_btn_three.isChecked():
            self._orient_Controller(light_name,obj_name)
            
        elif self._radio_btn_four.isChecked():
            self._aim_Controller(light_name,obj_name)
        
    def _Parent_Controller(self,light,obj,*argv):
        print 'parent',light,obj
        if light:
            for l in light:
                cmds.parentConstraint(obj,l,mo=1)
                
    def _point_Controller(self,light,obj,*argv):
        print 'point',light,obj
        if light:
            for l in light:
                cmds.pointConstraint(obj,l,mo=1)
                
    def _orient_Controller(self,light,obj,*argv):
        print 'orient',light,obj
        if light:
            for l in light:
                cmds.orientConstraint(obj,l,mo=1)
    def _aim_Controller(self,light,obj,*argv):
        print 'aim',light,obj
        if light:
            for l in light:
                cmds.aimConstraint(obj,l,mo=1)
def run():
    global lf
    try:
        lf.deletelater()
        lf.close()
    except:
        pass
    lf = LightFollow()
    lf.show()
    print lf.__doc__
    
if __name__ == '__main__':
    run()