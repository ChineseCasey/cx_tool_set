#coding=gbk
import os,sys
import maya.mel as mel


def global_path():
    p = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    path = p + '/script/mel/'
    return path


#name = ��Ҫ�򿪵�mel����
def run(name):
    path = global_path() + name
    print path
    mel.eval('source "%s";' %path)
