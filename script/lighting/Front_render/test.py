from PySide import QtGui,QtCore


class test(QtGui.QWidget):
    def __init__(self,parent=None):
        super(test, self).__init__(parent)
        main_lay = QtGui.QVBoxLayout()
        self.progress = QtGui.QProgressBar()
        self.button = QtGui.QPushButton('ok')
        self.button.clicked.connect(self.progress_test)
        main_lay.addWidget(self.progress)
        main_lay.addWidget(self.button)
        self.setLayout(main_lay)

    def progress_test(self):
        num = int(20000)
        self.progress.setMinimum(0)
        self.progress.setMaximum(num)
        for i in range(num+1):
            print i
            self.progress.setValue(i)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    t = test()
    t.show()
    app.exec_()