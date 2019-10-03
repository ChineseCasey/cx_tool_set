#coding=gbk
import maya.cmds as cmds
import pymel.core as pmel
import maya.mel as mel
from functools import partial

#获取当前时间轴起始结束帧
st_frame_time = pmel.playbackOptions(q=1,ast=1)
et_frame_time = pmel.playbackOptions(q=1,aet=1)
#创建aov类型
rs_aov_Type = ["Ambient Occlusion",
                "Background",
                "Bump Normals",
                "Caustics",
                "Caustics Raw",
                "Depth",
                "Diffuse Filter",
                "Diffuse Lighting",
                "Diffuse Lighting Raw",
                "Emission",
                "Global Illumination",
                "Global Illumination Raw",
                "Matte",
                "Motion Vectors",
                "Normals",
                "ObjectID",
                "Object-Space Bump Normals",
                "Object-Space Positions",
                "Puzzle Matte",
                "Reflections",
                "Reflections Filter",
                "Reflections Raw",
                "Refractions",
                "Refractions Filter",
                "Refractions Raw",
                "Shadows",
                "Specular Lighting",
                "Sub Surface Scatter",
                "Sub Surface Scatter Raw",
                "Total Diffuse Lighting Raw",
                "Total Translucency Lighting Raw",
                "Translucency Filter",
                "Translucency GI Raw",
                "Translucency Lighting Raw",
                "Volume Fog Emission",
                "Volume Fog Tint",
                "Volume Lighting",
                "World Position"]
#常用aov列表        
create_rs_aov_type = ["Bump Normals",
                        "Caustics",
                        "Depth",
                        "Diffuse Lighting",
                        "Emission",
                        "Global Illumination",
                        "Motion Vectors",
                        "Normals",
                        "Object-Space Bump Normals",
                        "Reflections",
                        "Refractions",
                        "Shadows",
                        "Specular Lighting",
                        "Sub Surface Scatter",
                        "Volume Lighting",
                        "World Position"
                      ]
        
class RenderSetting(object):

    def final_render_setting(self,*argv):
        rs_op = pmel.ls(type = 'RedshiftOptions')
        if not rs_op:
            mel.eval('nodeEdCreateNodeCommand "RedshiftOptions";')
            #pmel.delete(rs_op)
        else:
            pass
        #mel.eval('unifiedRenderGlobalsWindow;')
        pmel.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")

        #渲染路径设置
        try:
            pmel.setAttr('defaultRenderGlobals.imageFilePrefix', "<Scene>/<RenderLayer>/<RenderLayer>", type="string")
            pmel.setAttr('redshiftOptions.imageFilePrefix', "<Scene>/<RenderLayer>/<RenderLayer>", type="string")
        except:
            pass
        #bit size
        cmds.setAttr("redshiftOptions.exrBits",32)
        cmds.setAttr("redshiftOptions.autocrop",1)
        cmds.setAttr("redshiftOptions.exrMultipart",1)
        cmds.setAttr("redshiftOptions.exrForceMultilayer",1)

        #时间帧
        cmds.setAttr("defaultRenderGlobals.animation",1)
        cmds.setAttr("defaultRenderGlobals.startFrame",st_frame_time)
        cmds.setAttr("defaultRenderGlobals.endFrame",et_frame_time)

        # 图片格式
        pmel.setAttr("redshiftOptions.imageFormat", 1)
        pmel.setAttr("redshiftOptions.exrDwaCompressionLevel", 4)

        #渲染相机
        try:
            cmds.setAttr("final_cam.renderable",1)
        except:
            pass
        #分辨率
        cmds.setAttr('defaultResolution.width',2048)
        cmds.setAttr('defaultResolution.height',1080)
        #采样值
        cmds.setAttr("redshiftOptions.unifiedMinSamples",64)
        cmds.setAttr("redshiftOptions.unifiedMaxSamples",128)
        cmds.setAttr("redshiftOptions.unifiedAdaptiveErrorThreshold",0.001)
        #GI方式
        cmds.setAttr("redshiftOptions.primaryGIEngine",4)
        cmds.setAttr("redshiftOptions.secondaryGIEngine",2)
        cmds.setAttr("redshiftOptions.bruteForceGINumRays",256)
        cmds.setAttr("redshiftOptions.irradiancePointCloudRetraceThreshold",3)
    
    def create_aov(self,*argv):
        #通用aov
        for aov in create_rs_aov_type: #rs_aov_Type:
            create_cus_aov = pmel.rsCreateAov(t=aov)
            node_cus_aov = pmel.PyNode(create_cus_aov)
            node_cus_aov.filePrefix.set("<BeautyPath>/<BeautyFile>.<RenderPass>")
            node_cus_aov.exrBits.set(32)
            
        mel.eval('redshiftUpdateActiveAovList()')
        
    #aov设置界面 
    def aov_win(self,*argv):
        if cmds.window('aov_setting_win', q=1, ex=1):
            cmds.deleteUI('aov_setting_win')
        cmds.window('aov_setting_win',t='aov_setting')
        self.main_lay = cmds.columnLayout()
        rowlay = cmds.rowLayout(p =self.main_lay, numberOfColumns = 2)
        cmds.checkBox(l='on/off', v=0, onc=partial(self.all_sel_aov_sel,1), ofc=partial(self.all_sel_aov_sel,0))
        cmds.checkBox(l='常用aov选择', v=1, onc=partial(self.common_aov_sel,1), ofc=partial(self.common_aov_sel,0))
        
        self.aov_create_lay = cmds.rowColumnLayout(p = self.main_lay,numberOfColumns=3)
        self._create_aov_setting()
        cmds.rowLayout(p=self.main_lay,numberOfColumns=2)
        cmds.button(l='create',w=100, c=partial(self._create_setting_aov))
        cmds.button(l='Close',w=100, c=partial(self.del_win))
        cmds.showWindow()

    def del_win(self,*argv):
        cmds.deleteUI('aov_setting_win')

    #aov创建列表
    def _create_aov_setting(self,*argv):
        self.aov_list = []
        self.common_aov_list = []
        for aov in rs_aov_Type:
            
            if aov in create_rs_aov_type:
                self.check_name = cmds.checkBox(p=self.aov_create_lay,l=aov,v=1)
                self.aov_list.append(self.check_name)
                self.common_aov_list.append(self.check_name)
            else:
                self.check_name = cmds.checkBox(p=self.aov_create_lay,l=aov,v=0)
                self.aov_list.append(self.check_name)
            
    def all_sel_aov_sel(self,value,*argv):
        for i in self.aov_list:
            cmds.checkBox(i,e=1,v=value)
            
    def common_aov_sel(self,value,*argv):
        for i in self.common_aov_list:
                cmds.checkBox(i,e=1,v=value)
                
    #创建自定义aov
    def _create_setting_aov(self,*argv):
        
        for n in self.aov_list:
            if cmds.checkBox(n,q=1,v=1):
                name = cmds.checkBox(n,q=1,l=1)
                create_cus_aov = pmel.rsCreateAov(t=name)
                node_cus_aov = pmel.PyNode(create_cus_aov)
                node_cus_aov.filePrefix.set("<BeautyPath>/<BeautyFile>")

        mel.eval('redshiftUpdateActiveAovList()')
        
def final_setting_run():
    rs = RenderSetting()
    rs.final_render_setting()
    
def create_aov():
    rs = RenderSetting()
    rs.create_aov()
    
def aov_setting_win():  
    rs = RenderSetting()
    rs.aov_win()
            