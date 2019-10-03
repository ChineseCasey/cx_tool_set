#coding=utf-8


def run(*args):
	from  script.model.SpiderGen import gui
	reload(gui)
	gui.createUI()
