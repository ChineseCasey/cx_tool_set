#coding=gbk
import sys
from PySide import QtGui,QtCore


class FRender(QtGui.QWidget):

    def __init__(self,parent=None):
        super(FRender, self).__init__(parent)
        self.setWindowTitle(u'ǰ̨��Ⱦ')
        self.main_lay = QtGui.QVBoxLayout()

        self.hbox_lay_one = QtGui.QHBoxLayout()
        self.seq_render_sel = QtGui.QRadioButton(u'������Ⱦ')
        self.seq_render_sel.setChecked(1)
        self.seq_render_sel.toggled.connect(self._set_itt_state)

        self.hbox_lay_two = QtGui.QHBoxLayout()
        self.st_tex = QtGui.QLabel(U'��ʼ֡��')
        self.st_edit = QtGui.QLineEdit()
        self.st_edit.setFixedWidth(60)
        self.en_tex = QtGui.QLabel(U'����֡��')
        self.en_edit = QtGui.QLineEdit()
        self.en_edit.setFixedWidth(60)

        self.hbox_lay_there = QtGui.QHBoxLayout()
        self.itt_render_sel = QtGui.QRadioButton(u'������Ⱦ')
        self.itt_render_sel.toggled.connect(self._set_seq_state)

        self.hbox_lay_four = QtGui.QHBoxLayout()
        self.itt_render_tex = QtGui.QLabel(u'����֡��')
        self.itt_render_edit = QtGui.QTextEdit()
        self.itt_render_edit.setFixedHeight(80)



        self.hbox_lay_five = QtGui.QHBoxLayout()
        self.sel_frame = QtGui.QFrame()
        #self.sel_frame.setStyleSheet("background-color: rgb(255, 0, 0);")
        #self.sel_frame.setFixedWidth(300)
        #self.sel_frame.setFixedHeight(40)
        self.frme_lay = QtGui.QHBoxLayout(self.sel_frame)
        self.layer_radio = QtGui.QRadioButton(u'������')
        self.layer_radio.setChecked(1)
        self.frame_radio = QtGui.QRadioButton(U'֡����')


        self.render_button = QtGui.QPushButton(u'��Ⱦ ')
        self.render_button.clicked.connect(self._render)

        self.progress = QtGui.QProgressBar()
        self.progress.setFixedWidth(300)

        self.hbox_lay_one.addWidget(self.seq_render_sel)
        self.hbox_lay_two.addWidget(self.st_tex)
        self.hbox_lay_two.addWidget(self.st_edit)
        self.hbox_lay_two.addWidget(self.en_tex)
        self.hbox_lay_two.addWidget(self.en_edit)
        self.hbox_lay_there.addWidget(self.itt_render_sel)
        self.hbox_lay_four.addWidget(self.itt_render_tex)
        self.hbox_lay_four.addWidget(self.itt_render_edit)
        self.hbox_lay_five.addWidget(self.sel_frame)
        self.frme_lay.addWidget(self.layer_radio)
        self.frme_lay.addWidget(self.frame_radio)

        #self.hbox_lay_five.addWidget(self.buttonGroup)
        #self.hbox_lay_five.addWidget(self.frame_radio)

        self.main_lay.addLayout(self.hbox_lay_one)
        self.main_lay.addLayout(self.hbox_lay_two)
        self.main_lay.addLayout(self.hbox_lay_there)
        self.main_lay.addLayout(self.hbox_lay_four)
        self.main_lay.addLayout(self.hbox_lay_five)

        self.main_lay.addWidget(self.render_button)
        self.main_lay.addWidget(self.progress)

        self.setLayout(self.main_lay)
        self._set_itt_state()
    # ����ѡ��״̬�޸�
    def _set_itt_state(self):
        if self.seq_render_sel.isChecked():
            self._iff_enable_on_off(False)
        else:
            self._iff_enable_on_off(True)

    def _set_seq_state(self):
        if self.itt_render_sel.isChecked():
            self._seq_enable_on_off(False)
        else:
            self._seq_enable_on_off(True)

    def _iff_enable_on_off(self,value):
        self.itt_render_tex.setEnabled(value)
        self.itt_render_edit.setEnabled(value)

    def _seq_enable_on_off(self,value):
        self.st_edit.setEnabled(value)
        self.en_edit.setEnabled(value)

    def _render(self):
        if self.seq_render_sel.isChecked():
            start = self.st_edit.text()
            end = self.en_edit.text()
            if start and end:
                self.render_scene(range(int(start),int(end)+1))
            else:
                print u'��������ʼ����֡'

        elif self.itt_render_sel.isChecked():
            frame = self.itt_render_edit.toPlainText()
            if frame:
                self.render_scene(frame,True)
            else:
                print u'��������Ҫ��Ⱦ��֡'
    #solt == ������Ⱦ
    def render_scene(self,frame,slot=False):
        #����д��Ⱦ����
        if slot == True:
            frame_str = frame.split(',')
            self.progress.setMaximum(len(frame_str))
            for f,v in zip(frame_str,range(1,len(frame_str)+1)):
                if '-' in f:
                    frame_split = f.split('-')
                    len1 = range(int(frame_split[0]),int(frame_split[1])+1)
                    frame_str.append(len1)
                    print frame_str
                else:
                    print f,v
                    self.progress.setValue(v)
        else:
            self.progress.setMaximum(len(frame))
            for i in frame:
                self.progress.setValue(i)
                print i

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fr = FRender()
    fr.show()
    app.exec_()