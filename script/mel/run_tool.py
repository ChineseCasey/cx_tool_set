#coding=gbk
import os,sys
import maya.mel as mel


def global_path():
    p = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    path = p + '/script/mel/'
    return path


#name = 需要打开的mel名称
def run(name):
    path = global_path() + name
    print path
    mel.eval('source "%s";' %path)
