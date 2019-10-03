#coding=utf8
from PySide import QtCore,QtGui
import sys
from ID_uic.main_window import Ui_redshift_IDs
from ID_uic.item_aov import Ui_Dialog
import pymel.core as pmel
import maya.cmds as cmds
import maya.mel as mel
from functools import partial

class ID_Rs_Item(QtGui.QDialog):
    def __init__(self, parent=None, aov_name=''):
        super(ID_Rs_Item, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.aov_name = aov_name
        
        self.ui.ID_Red_btn.setFixedSize(25,25)
        self.ui.ID_Green_btn_.setFixedSize(25,25)
        self.ui.ID_Blue_btn.setFixedSize(25,25)
        #self.ui.item_aov_frame.mousePressEvent = self.test
        self.ui.delete_btn.clicked.connect(self.delete_select_matte_aov)
        # self.setFixedSize(100, 25)
    #删除选择的matte层
    def delete_select_matte_aov(self):
        self.close()
        pmel.delete(self.aov_name)
    def test(self, event):
        self.ui.item_aov_frame.setStyleSheet('background-color: rgb(40, 130, 255)')
        self.ui.aov_name_label.setStyleSheet('color: rgb(255, 170, 80);')
# app = QtGui.QApplication([])
# aa = ID_Rs_Item()
# aa.show()
# app.exec_()
class ID_Rs_Main_Window(QtGui.QDialog,Ui_redshift_IDs):

    def __init__(self,parent=None):
        super(ID_Rs_Main_Window, self).__init__(parent)
        self.setupUi(self)
        self.item_list = []
        self.setWindowTitle('RedShift ID')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.Add_btn.clicked.connect(self.Create_Aov)
        self.sel_obj_id_btn.clicked.connect(self.get_obj_ID)
        
        self.clear_btn.clicked.connect(self.delete_matte_aov)
        self.zero_btn.clicked.connect(partial(self.ovide_ID,0))
        self.refresh_aov_ui()
        
    def Create_Aov(self):
        self.Create_Redshift_Aov()
    #创建一个新的matte层
    def Create_Redshift_Aov(self):
        # global iri
        
        # self.add_item_lay.addWidget(QtGui.QPushButton())
        
        create_rs_aov = pmel.rsCreateAov(t='Puzzle Matte')
        sel_aov_node = pmel.PyNode(create_rs_aov)
        name = pmel.getAttr(sel_aov_node + '.name')
        
        iri = ID_Rs_Item(aov_name=create_rs_aov)
        self.add_item_lay.addWidget(iri)
        self.item_list.append(iri)
        
        sel_aov_node.mode.set(1)
        sel_aov_node.filePrefix.set("<BeautyPath>/<BeautyFile>")
        iri.ui.aov_name_label.setText(name)
        
        if len(name) == 11:
            sel_aov_node.redId.set(1)
            sel_aov_node.greenId.set(2)
            sel_aov_node.blueId.set(3)

            iri.ui.ID_Red_btn.setText(str(1))
            iri.ui.ID_Green_btn_.setText(str(2))
            iri.ui.ID_Blue_btn.setText(str(3))

            # iri.ID_Blue_btn.clicked.connect(self.ovide_ID)
            # iri.ID_Green_btn_.clicked.connect(self.ovide_ID)
            # iri.ID_Blue_btn.clicked.connect(self.ovide_ID)
        else:
            sel_aov_node.redId.set(int(name[len('PuzzleMatte'):]) * 3 + 1)
            sel_aov_node.greenId.set(int(name[len('PuzzleMatte'):]) * 3 + 2)
            sel_aov_node.blueId.set(int(name[len('PuzzleMatte'):]) * 3 + 3)

            iri.ui.ID_Red_btn.setText(str(int(name[len('PuzzleMatte'):]) * 3 + 1))
            iri.ui.ID_Green_btn_.setText(str(int(name[len('PuzzleMatte'):]) * 3 + 2))
            iri.ui.ID_Blue_btn.setText(str(int(name[len('PuzzleMatte'):]) * 3 + 3))

        r = iri.ui.ID_Red_btn.text()
        g = iri.ui.ID_Green_btn_.text()
        b = iri.ui.ID_Blue_btn.text()

        iri.ui.ID_Red_btn.clicked.connect(partial(self.ovide_ID, int(r)))
        iri.ui.ID_Green_btn_.clicked.connect(partial(self.ovide_ID, int(g)))
        iri.ui.ID_Blue_btn.clicked.connect(partial(self.ovide_ID, int(b)))
        self.label.setText('ID:')
        self.update_aov()
        
    #刷新aov列表
    def update_aov(self):
        try:
            mel.eval('redshiftUpdateActiveAovList()')
        except:
            pass
    #读取场景中的Matte层 刷新到界面
    def refresh_aov_ui(self):
        # global iri
        matteList = self.get_all_matte()

        if matteList:
            for i in matteList:
                iri = ID_Rs_Item(aov_name = i)
                # iri.ui.delete_btn.clicked.connect(self.delete_select_matte_aov)
                self.item_list.append(iri)
                name = pmel.getAttr(i + '.name')
                self.add_item_lay.addWidget(iri)
                iri.ui.aov_name_label.setText(name)
                
                a = pmel.PyNode(i)

                iri.ui.ID_Red_btn.setText(str(a.redId.get()))
                iri.ui.ID_Green_btn_.setText(str(a.greenId.get()))
                iri.ui.ID_Blue_btn.setText(str(a.blueId.get()))

                r = iri.ui.ID_Red_btn.text()
                g = iri.ui.ID_Green_btn_.text()
                b = iri.ui.ID_Blue_btn.text()

                iri.ui.ID_Red_btn.clicked.connect(partial(self.ovide_ID,int(r)))
                iri.ui.ID_Green_btn_.clicked.connect(partial(self.ovide_ID,int(g)))
                iri.ui.ID_Blue_btn.clicked.connect(partial(self.ovide_ID,int(b)))

    #获取所有的Matte层
    def get_all_matte(self):
        try:
            all_matte = [str(x) for x in pmel.ls(type="RedshiftAOV") if x.aovType.get() == 'Puzzle Matte']
            return all_matte
        except:
            pass
    #获取选择物体的ID号
    def get_obj_ID(self):
        name = pmel.ls(dag=1,sl=1)
        if name:
            try:
                #objShape = name[0].getShape()
                hairSystem = pmel.listConnections(name, type='hairSystem')
                #print len(name)
                if len(name) > 2:
                    self.label.setText(u'一次只能选择一个模型')
                elif hairSystem:
                    hairSystem_ID = hairSystem[0].rsObjectId.get()
                    self.label.setText('ID:  %s' % hairSystem_ID)
                else:
                    ID_name = name[0].rsObjectId.get()
                    self.label.setText('ID:  %s' % ID_name)
            except:
                ID_name = name[0].rsObjectId.get()
                self.label.setText('ID:  %s' % ID_name)
        else:
            self.label.setText(u'没有选择需要查看的模型')
    #删除所有的matte层
    def delete_matte_aov(self):
        all_matte = self.get_all_matte()
        if all_matte:
            for m in all_matte:
                pmel.delete(m)
        if self.item_list:
            for item in self.item_list:
                item.close()
        self.item_list = []
    def ovide_ID(self,data,*argv):
        obj_name = pmel.ls(dag=1,sl=1,type=['surfaceShape','mesh','pfxHair','hairSystem'])
        if obj_name:
            for i in obj_name:
                print i
                #根据项目添加插件shape
                try:
                    #objShape = i.getShape()
                    hairSystem = pmel.listConnections(i, type='hairSystem')
                    #print hairSystem
                    if hairSystem:
                        hairSystem[0].rsObjectId.set(data)
                        self.label.setText(u'给物体：%s 添加了ID号：%s' %(hairSystem[0],data))
                    else:
                        cmds.setAttr(i+".rsObjectId", data)
                        self.label.setText(u'给物体：%s 添加了ID号：%s' % (i, data))
                except:
                    print i
                    i.rsObjectId.set(data)
                    self.label.setText(u'给物体：%s 添加了ID号：%s' % (i, data))

        else:
            self.label.setText(u'请选择需要赋予ID的模型！')

def run(parent=None):
    global irmw
    try:
        irmw.deleteLater()
        irmw.close()
    except:
        pass
    #app = QtGui.QApplication(sys.argv)
    irmw = ID_Rs_Main_Window(parent)
    irmw.show()
    #app.exec_()
#run()
