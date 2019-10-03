import maya.cmds as cmds
from functools import partial
import pymel.core as pmel
import os 

class SpToMaya(object):
    def __init__(self):

        self.main_win = cmds.window(t='SpToMaya')
        main_lay = cmds.columnLayout()
        lay_one = cmds.rowLayout(p=main_lay,numberOfColumns=4)
        cmds.radioCollection()
        self.vray_radio = cmds.radioButton(l='Vray',sl=1)
        self.redshift_radio = cmds.radioButton(l='Redshift',onc=partial(self._create_flip_check),ofc=partial(self._del_flip_check),ed=1)
        self.arnold4_radio = cmds.radioButton(l='Arnold4',ed=0)
        self.arnold5_radio = cmds.radioButton(l='Arnold5',ed=0)
        
        lay_two = cmds.rowLayout(p=main_lay,numberOfColumns=3)
        cmds.text(l='Path: ')
        self.path_text = cmds.textField(w=200)
        cmds.button(l='...',c=partial(self._sel_file))
        
        self.lay_there = cmds.rowLayout(p=main_lay,numberOfColumns=3)
        cmds.text(l='shader:')
        self.shade_name = cmds.optionMenu()
        
        cmds.text(p=main_lay,l=' ')
        self.custom_lay = cmds.rowLayout(p=main_lay,numberOfColumns=3)
        self.all_shader = cmds.checkBox(l='Create_all',ed=1)
        self.display_sel = cmds.checkBox(l='Displayment')
        cmds.text(p=main_lay,l=' \n')
        lay_five = cmds.rowLayout(p=main_lay,numberOfColumns=3)
        cmds.text(l='              ')
        
        cmds.button(l='create_shader',c=partial(self.on_clicked_create))

    def show(self):
        cmds.showWindow(self.main_win)
    #deleteUI
    def _deleteUI(self):
        if cmds.window(self.main_win,q=1,ex=1):
            cmds.deleteUI(self.main_win)
    def _create_flip_check(self,*argv):
        self.flip_btn = cmds.checkBox(p=self.custom_lay,l='Normal FlipY',ed=1)
        
    def _del_flip_check(self,*argv):
        cmds.deleteUI(self.flip_btn)
    #select file path
    def _sel_file(self,*arg):
        path_str = cmds.fileDialog2(fm=2,ff='select file')
        if path_str:
            cmds.textField(self.path_text,e=1,tx=path_str[0])
            self.global_path = os.listdir(path_str[0])
            for a in self.get_file_name_number(self.global_path):
                cmds.menuItem(p=self.shade_name,l=a)
    #get path file type number
    def get_file_name_number(self,file_name_list,*argv):
        
        file_list = []
        for name in file_name_list:
            names = name.split('_')
            try:
                file_list.append(names[-2])
            except:
                pass
            
        return set(file_list)
    #create shader
    def create_shade_mtl(self,sname,mtl_type,*argv):
        shader = pmel.shadingNode(mtl_type,n=sname,asShader=True)
        SG = pmel.sets(renderable=True,noSurfaceShader=True , name=sname)
        pmel.connectAttr(shader.outColor,SG.surfaceShader,f=1)
        return shader,SG

    
    #create redshift_normal 
    def create_redshift_normal(self,file_path,*argv):
        normal = pmel.shadingNode('RedshiftNormalMap',asShader=True)
        normal.tex0.set(file_path)
        normal.flipY.set(0)
        return normal
    def create_2dtexture(self,tex_file,*argv):
        tex = tex_file
        uv = pmel.shadingNode('place2dTexture',asUtility=1)
        pmel.connectAttr(uv.coverage,tex.coverage,f=1)
        pmel.connectAttr(uv.translateFrame,tex.translateFrame,f=1)
        pmel.connectAttr(uv.rotateFrame,tex.rotateFrame,f=1)
        pmel.connectAttr(uv.mirrorU,tex.mirrorU,f=1)
        pmel.connectAttr(uv.mirrorV,tex.mirrorV,f=1)
        pmel.connectAttr(uv.stagger,tex.stagger,f=1)
        pmel.connectAttr(uv.wrapU,tex.wrapU,f=1)
        pmel.connectAttr(uv.wrapV,tex.wrapV,f=1)
        pmel.connectAttr(uv.repeatUV,tex.repeatUV,f=1)
        pmel.connectAttr(uv.offset,tex.offset,f=1)
        pmel.connectAttr(uv.rotateUV,tex.rotateUV,f=1)
        pmel.connectAttr(uv.noiseUV,tex.noiseUV,f=1)
        pmel.connectAttr(uv.vertexUvOne,tex.vertexUvOne,f=1)
        pmel.connectAttr(uv.vertexUvTwo,tex.vertexUvTwo,f=1)
        pmel.connectAttr(uv.vertexUvThree,tex.vertexUvThree,f=1)
        pmel.connectAttr(uv.vertexCameraOne,tex.vertexCameraOne,f=1)
        pmel.connectAttr(uv.outUV,tex.uv)
        pmel.connectAttr(uv.outUvFilterSize,tex.uvFilterSize)
        return 

    #text file link
    def create_tex(self,path,*argv):
        tex = pmel.shadingNode('file',asTexture=1,isColorManaged=1)
        tex.fileTextureName.set(path)
        return tex

    #vray link
    def link_vray_shader(self,shade_name,file_path,file_name_list,*argv):
        global vray_shader
        vray_shader = self.create_shade_mtl(shade_name,'VRayMtl')
        for file_name in file_name_list:
            file_type = file_name.split('_')[-1].split('.')
            try:
                names = file_name.split('_')[-2]
                if file_type[0] == 'Diffuse':
                    if shade_name == names:
                        diff = os.path.join(file_path,file_name)
                        dif_tex = self.create_tex(diff)
                        dif_tex.colorSpace.set('sRGB')
                        pmel.connectAttr(dif_tex.outColor,vray_shader[0].color,f=1)
                        
                elif file_type[0] == 'Glossiness':
                    if shade_name == names:
                        gloss = os.path.join(file_path,file_name)
                        gloss_tex = self.create_tex(gloss)
                        gloss_tex.colorSpace.set('Raw')
                        
                        pmel.connectAttr(gloss_tex.outAlpha,vray_shader[0].reflectionGlossiness,f=1)
    
                elif file_type[0] == 'Reflection':
                    if shade_name == names:
                        ref = os.path.join(file_path,file_name)
                        ref_tex = self.create_tex(ref)
                        ref_tex.colorSpace.set('Raw')
                        
                        pmel.connectAttr(ref_tex.outColor,vray_shader[0].reflectionColor,f=1)
                        
                elif file_type[0] == 'ior':
                    if shade_name == names:
                        ior = os.path.join(file_path,file_name)
                        ior_tex = self.create_tex(ior)
                        ior_tex.colorSpace.set('Raw')
                        vray_shader[0].lockFresnelIORToRefractionIOR.set(0)
                        pmel.connectAttr(ior_tex.outAlpha,vray_shader[0].fresnelIOR,f=1)
    
                elif file_type[0] == 'Normal':
                    if shade_name == names:
                        nor = os.path.join(file_path,file_name)
                        nor_tex = self.create_tex(nor)
                        nor_tex.colorSpace.set('Raw')
                        vray_shader[0].bumpMapType.set(1)
                        pmel.connectAttr(nor_tex.outColor,vray_shader[0].bumpMap,f=1)
    
                elif file_type[0] == 'Height':
                    if shade_name == names:
                        Height = os.path.join(file_path,file_name)
                        if cmds.checkBox(self.display_sel,q=1,v=1):
                            Height_tex = self.create_tex(Height)
                            Height_tex.colorSpace.set('Raw')
                            Height_tex.alphaIsLuminance.set(True)
                            Height_tex.alphaGain.set(0.03)
                            display_shader = pmel.shadingNode('displacementShader',n='%sDis' %vray_shader[0],asShader=True)
                            pmel.connectAttr(Height_tex.outAlpha,display_shader.displacement,f=1)
                            pmel.connectAttr(display_shader.displacement,vray_shader[1].displacementShader)
                            #
                        else:
                            pass
            except:
                pass
                
    #vray run()
    def vray_on_clicked_create(self,*argv):
        
        main_file_path = cmds.textField(self.path_text,q=1,tx=1)
        shade_tex_name = cmds.optionMenu(self.shade_name,q=1,v=1)
        
        if cmds.checkBox(self.all_shader,q=1,v=1):
            for name in self.get_file_name_number(self.global_path):
                
                self.link_vray_shader(name,main_file_path,self.global_path)
                
        else:
            sel_obj = cmds.ls(sl=1)
            if sel_obj:
                self.link_vray_shader(shade_tex_name, main_file_path, self.global_path)
                aa = vray_shader[0].getName()
                pmel.select(sel_obj)
                pmel.hyperShade(assign=aa)
            else:
                self.link_vray_shader(shade_tex_name, main_file_path, self.global_path)
                
    def link_redshift_shader(self, shade_name, file_path, file_name_list,*argv):
        global rs_shader
        rs_2dtexture_list = []
        rs_shader = self.create_shade_mtl(shade_name,'RedshiftMaterial')
        rs_shader[0].refl_brdf.set(1)
        rs_shader[0].refl_fresnel_mode.set(1)
        for file_name in file_name_list:
            file_type = file_name.split('_')[-1].split('.')
            try:
                names = file_name.split('_')[-2]
                if file_type[0] == 'Diffuse':
                    if shade_name == names:
                        diff = os.path.join(file_path,file_name)
                        dif_tex = self.create_tex(diff)
                        dif_tex.colorSpace.set('sRGB')
                        pmel.connectAttr(dif_tex.outColor,rs_shader[0].diffuse_color,f=1)
                        rs_2dtexture_list.append(dif_tex)

                elif file_type[0] == 'Glossiness':
                    if shade_name == names:
                        gloss = os.path.join(file_path,file_name)
                        gloss_tex = self.create_tex(gloss)
                        gloss_tex.colorSpace.set('Raw')
                        gloss_tex.invert.set(1)
                        pmel.connectAttr(gloss_tex.outAlpha,rs_shader[0].refl_roughness,f=1)
                        rs_2dtexture_list.append(gloss_tex)
                elif file_type[0] == 'Reflection':
                    if shade_name == names:
                        ref = os.path.join(file_path,file_name)
                        ref_tex = self.create_tex(ref)
                        ref_tex.colorSpace.set('Raw')
                        
                        pmel.connectAttr(ref_tex.outColor,rs_shader[0].refl_color,f=1)
                        rs_2dtexture_list.append(ref_tex)
                elif file_type[0] == 'f0':
                    if shade_name == names:
                        ior = os.path.join(file_path,file_name)
                        ior_tex = self.create_tex(ior)
                        ior_tex.colorSpace.set('Raw')
                        pmel.connectAttr(ior_tex.outColor,rs_shader[0].refl_reflectivity,f=1)
                        rs_2dtexture_list.append(ior_tex)
                elif file_type[0] == 'Normal':
                    if shade_name == names:
                        nor = os.path.join(file_path,file_name)
                        nor_tex = self.create_redshift_normal(nor)
                        if cmds.checkBox(self.flip_btn,q=1,v=1):
                            nor_tex.flipY.set(1)
                        pmel.connectAttr(nor_tex.outDisplacementVector,rs_shader[0].bump_input,f=1)
                        rs_2dtexture_list.append(nor_tex)
                elif file_type[0] == 'Height':
                    if shade_name == names:
                        Height = os.path.join(file_path,file_name)
                        if cmds.checkBox(self.display_sel,q=1,v=1):
                            Height_tex = self.create_tex(Height)
                            Height_tex.colorSpace.set('Raw')
                            display_shader = pmel.shadingNode('RedshiftDisplacement',n='%sDis' %rs_shader[0],asShader=True)
                            pmel.connectAttr(Height_tex.outColor,display_shader.texMap,f=1)
                            pmel.connectAttr(display_shader.out,rs_shader[1].rsDisplacementShader)
                            rs_2dtexture_list.append(Height_tex)
                            #
                        else:
                            pass
            except:
                pass
        for twoD in rs_2dtexture_list:
            self.create_2dtexture(twoD)

    def redshift_on_clicked_create(self,*argv):
        main_file_path = cmds.textField(self.path_text,q=1,tx=1)
        shade_tex_name = cmds.optionMenu(self.shade_name,q=1,v=1)
        
        if cmds.checkBox(self.all_shader,q=1,v=1):
            for name in self.get_file_name_number(self.global_path):
                
                self.link_redshift_shader(name,main_file_path,self.global_path)
        else:
            sel_obj = cmds.ls(sl=1)
            if sel_obj:
                self.link_redshift_shader(shade_tex_name, main_file_path, self.global_path)
                name = rs_shader[0].getName()
                pmel.select(sel_obj)
                pmel.hyperShade(assign=name)
            else:
                self.link_redshift_shader(shade_tex_name, main_file_path, self.global_path)

     
    #run
    def on_clicked_create(self,*argv):
        if cmds.radioButton(self.vray_radio,q=1,sl=1):
           self.vray_on_clicked_create()
        elif cmds.radioButton(self.redshift_radio,q=1,sl=1):
           self.redshift_on_clicked_create()

    
def run():
    sptomaya = SpToMaya()
    sptomaya.show()


