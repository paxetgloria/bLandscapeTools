import bpy,bgl,blf,bmesh
import subprocess,os,time, struct,sys
from shutil import copy,rmtree
from math import floor, isnan, ceil
from numpy import genfromtxt,vstack,hstack,array,savetxt,delete,ones,zeros,flipud,empty,fromfile,float16,float32,reshape,uint8
from mathutils import Vector, Matrix


def dlsa31meu():
    dma31usle = '{}\lib'.format(dusaem31l()[1])
    sys.path.append(dma31usle)
    import pip
    pip.main(['install', 'opencv-python', '--no-deps'])
    try:
        import cv2
        print('\nbLT_Info: OpenCV installed successfully')
    except:
        print('\nbLT_Info: OpenCV installation problem!!!')
    

    

    
def dl31seamu(self, context):
    dsluae31m = context.scene.demual31s
    
    if dsluae31m != '':
        if dsluae31m.split('.')[-1] in ['png','tif','tiff','jpg','jpeg']:
            context.scene.du31lames = True
            from cv2 import imread as dl31mueas, imwrite as dusea31lm, resize as dlausme31, IMREAD_COLOR as dl31usame
            
            d31lemsau = context.user_preferences.addons["bLandscapeTools-master"].preferences.d31lemsau
            daue31msl = context.scene.daue31msl
            dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
            dasm31eul = deu31alsm(d31lemsau,dsluae31m)
            
            if os.path.exists('{}ProjectData\\Textures\\previewSatTex.png'.format(daue31msl)):
                os.remove('{}ProjectData\\Textures\\previewSatTex.png'.format(daue31msl))

            print('\nbLT_Info: Terrain texture preview creation started {}'.format(time.ctime()))
            if dasm31eul < 5000:
                print(' Input imagery size <= 5000x5000 px, no resizing necessary.')
                copy(context.scene.demual31s,'{}ProjectData\\Textures\\'.format(daue31msl))
                deums31la = context.scene.demual31s.split('\\')[-1]
                os.rename('{}ProjectData\\Textures\\{}'.format(daue31msl,deums31la),'{}ProjectData\\Textures\\previewSatTex.png'.format(daue31msl))
            else:
                print(' Input imagery size > 5000x5000 px, needs to be downscaled.')
                dms31aeul = dl31mueas(dsluae31m, dl31usame)
                delsamu31 = dlausme31(dms31aeul, (5000, 5000))
                dusea31lm(r'{}ProjectData\Textures\previewSatTex.png'.format(daue31msl), delsamu31)
            
                
            if bpy.data.images.get('previewSatTex.png') is None:
                bpy.data.images.load('{}ProjectData\\Textures\\previewSatTex.png'.format(daue31msl))
                bpy.data.images['previewSatTex.png'].use_fake_user = True
            else:
                bpy.data.images['previewSatTex.png'].reload()
                
            daml31sue = bpy.data.scenes['Default_Location']    
            daml31sue["ImageryResolution"] = dasm31eul
            
            bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
            
            print(' Terrain texture preview image created successfully.')
            print('bLT_Info: Terrain texture preview creation finished {}'.format(time.ctime()))    
        else:
            context.scene.du31lames = False
            print('\nbLT_Info: {} is unsupported imagery file format! Use PNG, TIF, TIFF, JPG, JPEG instead.'.format(dsluae31m.split('.')[-1]))
    else:
        context.scene.du31lames = False
        
def dulae31ms(self, context):
    dmealsu31 = context.scene.dumlse31a
    daue31msl = context.scene.daue31msl
    dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
    
    if dmealsu31 != '':
        if dmealsu31.split('.')[-1] in ['png','tif','tiff']:
            context.scene.dml31eaus = True
            bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        else:
            context.scene.dml31eaus = False
            print('\nbLT_Info: {} is unsupported surface mask file format! Use PNG, TIF, TIFF instead.'.format(dmealsu31.split('.')[-1]))
    else:
        context.scene.dml31eaus = False
    
def delmsa31u(self, context):
    
    du31laems = context.scene.dlsumea31
    
    if du31laems !='':
        if du31laems.split('.')[-1] in ['asc','ascii']:
            context.scene.deal31mus = True
            d31lemsau = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.d31lemsau
            daue31msl = bpy.data.scenes["Default_Location"].daue31msl
            dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
            d31samelu = dsma31ule(du31laems)
            print('\nbLT_Info: ASC elevation to bLTe format conversion started {}'.format(time.ctime()))
            dael31usm = genfromtxt(du31laems, delimiter=' ', skip_header=6)
            dslu31mea = '{}ProjectData\\Textures\\elevation.bLTe'.format(daue31msl)
            dael31usm.astype('float32').tofile(dslu31mea)
            print('bLT_Info: ASC elevation to bLTe format conversion finished {}'.format(time.ctime()))
            
            print('\nbLT_Info: Shaded terrain preview creation started {}'.format(time.ctime()))
            dmels31au(du31laems)
            print('bLT_Info: Shaded terrain preview creation finished {}'.format(time.ctime()))
            
            daml31sue = bpy.data.scenes['Default_Location']
            daml31sue["da31mlues"] = d31samelu[0]
            daml31sue["dmaseu31l"] = d31samelu[1]
            daml31sue["dual31sem"] = d31samelu[2]
            daml31sue["ds31uamle"] = d31samelu[3]
            bpy.data.scenes['Default_Location'].d31emusal = dslu31mea

            bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        else:
            context.scene.deal31mus = False
            print('bLT_Info: {} is unsupported elevation file format! Use ASC or ASCII instead.'.format(du31laems.split('.')[-1]))
    else:
        context.scene.deal31mus = False

def dlmeuas31(self, context):
    dlmeusa31 = context.scene.dl31uesma
    daue31msl = bpy.data.scenes["Default_Location"].daue31msl
    dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
    
    if dlmeusa31 != '':
        if dlmeusa31.split('.')[-1] == 'cfg':
            if len(context.scene.dulem31as) != 0:
                for textureBrushName in context.scene.dulem31as:
                    bpy.data.brushes.remove(bpy.data.brushes[textureBrushName.name])
                for daslme31uName in context.scene.dulem31as:
                    context.scene.dulem31as.remove(0)
                    
            
            dus31lema = open(dlmeusa31,encoding="utf8")
            de31sulma = context.scene.de31sulma
            daue31msl = bpy.data.scenes["Default_Location"].daue31msl
            
            surfaces = []
            materials = {}
            colors = {}
            
            for line in dus31lema.readlines():
                line = (line.lstrip()).rstrip('\n')
                if line.split(' ')[0] == 'class' and line.split(' ')[1] not in ['Layers','Legend','Colors']:
                    dsmaule31 = line.split(' ')[1].strip().lower()
                    if '\t' in line.split(' ')[1].strip():
                        dsmaule31 = line.split(' ')[1].strip().split('\t')[0].lower()
                    surfaces.append(dsmaule31)
                if line.split('=')[0].rstrip() == 'material':
                    materials[surfaces[-1]] = line.split('=')[1].split(';')[0].strip()[1:-1]
                if (line.split('=')[0].strip()).rstrip('[]') in surfaces:
                    du31lsmea = list(map(int, line.split('=')[1].strip().split(';')[0].lstrip('{{').rstrip('}}').split(',')))
                    colors[(line.split('=')[0].strip()).rstrip('[]')] = du31lsmea
                    
            dus31lema.close()
            
            from cv2 import imread as dl31mueas, imwrite as dusea31lm, resize as dlausme31, IMREAD_COLOR as dl31usame
            
            print('\nbLT_Info: Surface brushes and previews creation started {}'.format(time.ctime()))
            for dsmaule31, dsm31uale in materials.items():
                f = open('{}\\{}'.format(de31sulma,dsm31uale))
                textures = []
                for line in f.readlines():
                    line = (line.lstrip()).rstrip('\n')
                    if line.split('=')[0] == 'texture':
                        textures.append(line.split('=')[1][1:-2])
                f.close()
                
                dms31aeul = dl31mueas('{}{}'.format(de31sulma,textures[1]), dl31usame)
                delsamu31 = dlausme31(dms31aeul, (128, 128))
                dusea31lm(r'{}ProjectData\Textures\previewIcon_{}.png'.format(daue31msl,dsmaule31), delsamu31)

                dlmseua31 = bpy.data.brushes.new(dsmaule31)
                dlmseua31.use_custom_icon = True
                dlmseua31.icon_filepath = '{}ProjectData\Textures\previewIcon_{}.png'.format(daue31msl,dsmaule31)
                dlmseua31.strength = 1.0
                bpy.context.scene.tool_settings.image_paint.use_normal_falloff = False
                bpy.context.scene.tool_settings.image_paint.seam_bleed = 0
                dlmseua31.color = (0 if colors[dsmaule31][0] == 0 else colors[dsmaule31][0] / 255,
                                      0 if colors[dsmaule31][1] == 0 else colors[dsmaule31][1] / 255,
                                      0 if colors[dsmaule31][2] == 0 else colors[dsmaule31][2] / 255)
                dlmseua31.secondary_color = (0 if colors[dsmaule31][0] == 0 else colors[dsmaule31][0] / 255,
                                                0 if colors[dsmaule31][1] == 0 else colors[dsmaule31][1] / 255,
                                                0 if colors[dsmaule31][2] == 0 else colors[dsmaule31][2] / 255)
                dlmseua31.curve.curves[0].points.remove(dlmseua31.curve.curves[0].points[1])
                dlmseua31.curve.curves[0].points.remove(dlmseua31.curve.curves[0].points[1])
                dlmseua31.curve.curves[0].points[1].location[1] = 1.0
                dlmseua31.curve.update()
                dlmseua31 = context.scene.dulem31as.add()
                dlmseua31.name = dsmaule31
                
            bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
            print('bLT_Info: Surface brushes and previews creation finished {}'.format(time.ctime()))
                
        else:
            print('\nbLT_Info: {} is unsupported config file format! Use CFG instead.'.format(dlmeusa31.split('.')[-1]))
            
def de31smlua(self, context):
    if not os.path.exists(context.scene.de31sulma):
        context.scene.ds31aulem = False
        print('\nbLT_Info: System drive {} doesn\'t exist!'.format(context.scene.de31sulma))
    else:
        context.scene.ds31aulem = True
        daue31msl = bpy.data.scenes["Default_Location"].daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        print('\nbLT_Info: System drive {} does exist.'.format(context.scene.de31sulma))
          
def dmalseu31(self, context):
    if context.scene.dl31aesum:
        bpy.ops.object.select_all(action='DESELECT')
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.select=True
        context.scene.objects.active = dlmsa31ue
        bpy.ops.object.mode_set(mode='SCULPT')
    else:
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        
def d31ausmel(self, context):
    if context.scene.dsem31alu:
        bpy.ops.object.select_all(action='DESELECT')
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.select=True
        context.scene.objects.active = dlmsa31ue
        bpy.ops.object.ds31ealmu()
        dlmsa31ue.material_slots[0].material.use_textures[1] = True
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
    else:
        bpy.context.area.type = 'IMAGE_EDITOR'
        bpy.ops.image.save()
        bpy.context.area.type = 'VIEW_3D'
        context.active_object.material_slots[0].material.use_textures[1] = False
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        
def d31umlesa(self, context):
    dueamls31 = context.active_object
    dmeasul31 = dueamls31.children[0]
    dmeasul31.scale.y = self.dameslu31
    
def dmels31au(du31laems):
    d31lemsau = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.d31lemsau
    daue31msl = bpy.data.scenes["Default_Location"].daue31msl
    
    cmd = '"{}gdaldem.exe" hillshade -az 45 -z 1.3 "{}" "{}ProjectData\Textures\previewTerTex.tif"'.format(d31lemsau,du31laems,daue31msl)
    subprocess.call(cmd)
    
    if bpy.data.images.get('previewTerTex.tif') is None:
        bpy.data.images.load('{}ProjectData\\Textures\\previewTerTex.tif'.format(daue31msl))
        bpy.data.images['previewTerTex.tif'].use_fake_user = True
    else:
        bpy.data.images['previewTerTex.tif'].reload()      
        
def dusaem31l():
    import addon_utils
    addons = [mod for mod in addon_utils.modules(refresh=False)]
    for mod in addons:
        if mod.__name__ == "bLandscapeTools-master":
            dam31usel = mod.__file__
            pass
           
    desula31m = dam31usel[:-12]
    dmseul31a = '{}\\data'.format(desula31m)
    
    return dam31usel,desula31m,dmseul31a
     
def deu31alsm(d31lemsau,dsluae31m):
    ext = dsluae31m.split('.')[-1]
    if ext == 'png':
        d31euasml = 'pgw'
    if ext == 'tif' or ext == 'tiff':
        d31euasml = 'tfw'
    if ext == 'jpg' or ext == 'jpeg':
        d31euasml = 'jgw'
        
    cmd = '{}gdalinfo.exe "{}"'.format(d31lemsau,dsluae31m)
    d31sleamu = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    
    for i in range(0,10):
        line = str(d31sleamu.stdout.readline()).rstrip('\\r\\n\'')
        if line.split(' ')[0][2:] == 'Size':
            info = int(line.split(' ')[3])

    return info
    
def dsma31ule(path):
    info = []
    f = open(path,"r")
    line = f.readline().split(" ")
    for i in range(5):
        info.append( line[-1])
        line = f.readline().split(" ")
    f.close()
    ncols = int(info[0])
    dl31mseau = float(info[4])
    x = float(info[2])
    y = float(info[3])
    return ncols,x,y,dl31mseau

    
    

def dalemsu31(du31almes, dsl31uame):
    bpy.ops.object.lamp_add(type='HEMI')
    hemi = bpy.context.object
    hemi.hide = True
    hemi.name = "Hemi_" + du31almes

    Areas = bpy.context.screen.areas
    for Area in Areas:
        if Area.type == 'VIEW_3D':
            if dsl31uame:
                Area.spaces.active.viewport_shade = 'MATERIAL'
            else:
                Area.spaces.active.viewport_shade = 'SOLID'
                bpy.ops.scene.d31auemls()
            Area.spaces.active.cursor_location = [0,0,0]
            Area.spaces.active.clip_start = 0.1
            Area.spaces.active.clip_end = 20000
            Area.spaces.active.show_world = True
            Area.spaces.active.show_floor = False
            Area.spaces.active.show_axis_x = False
            Area.spaces.active.show_axis_y = False
            Area.spaces.active.fx_settings.use_ssao = True
            Area.spaces.active.fx_settings.ssao.factor = 4.1
            Area.spaces.active.fx_settings.ssao.distance_max = 4.0
            Area.spaces.active.fx_settings.ssao.samples = 70
            Area.spaces.active.fx_settings.use_ssao = False
    
            
def dlm31suea():
    dmseul31a = dusaem31l()[2]
    print('\nbLT_Info: Project created.')
    daue31msl = bpy.context.scene.daue31msl

        
  
    
    
    bpy.ops.wm.read_homefile(use_splash=False, app_template="bLandscapeTools")
    bpy.context.scene.desl31uma = True
    bpy.context.scene.daue31msl = daue31msl
    bpy.context.scene['dlm31saue'] = False

    if not os.path.exists(bpy.context.scene.daue31msl + 'ProjectData'):
	    os.makedirs(bpy.context.scene.daue31msl + 'ProjectData')
    else:
        rmtree(bpy.context.scene.daue31msl + 'ProjectData')
        os.makedirs(bpy.context.scene.daue31msl + 'ProjectData\\Textures')
    if not os.path.exists(bpy.context.scene.daue31msl + 'Output'):
	    os.makedirs(bpy.context.scene.daue31msl + 'Output\\bLTilities')
    else:
        rmtree(bpy.context.scene.daue31msl + 'Output')
        os.makedirs(bpy.context.scene.daue31msl + 'Output\\bLTilities')
        
def demusla31():
    
    bpy.context.area.type = 'IMAGE_EDITOR'
    
    for space in bpy.context.area.spaces:
        if space.type == 'IMAGE_EDITOR':
            space.image = bpy.data.images['previewTerTex.tif']
            if bpy.data.images.get('previewSatTex.png') is not None:
                space.image = bpy.data.images['previewSatTex.png']        

    bpy.ops.image.view_all()
    
    screen = bpy.context.window.screen
    for area in screen.areas:
        if area.type == 'IMAGE_EDITOR':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'window': bpy.context.window, 'screen': screen, 'area': area, 'region': region}
    bpy.ops.view2d.ds31meaul(override,'INVOKE_DEFAULT')

def dsml31eau(self,context):
    region = context.region

    width,height = region.width,region.height
    center = [width / 2, height / 2]
    
    font_id = 0
    blf.size(font_id, 13, 80)
    blf.enable(0, blf.SHADOW)
    blf.shadow_offset(0, 1, -1)
    blf.shadow(0, 3, 0.0, 0.0, 0.0, 1)

    bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.img.bindcode[0])
    bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
    bgl.glEnable(bgl.GL_TEXTURE_2D)
    bgl.glTexEnvf(bgl.GL_TEXTURE_ENV,bgl.GL_TEXTURE_ENV_MODE, bgl.GL_REPLACE)
    bgl.glBegin(bgl.GL_QUADS)
    
    bgl.glTexCoord2f(0, 0)
    bgl.glVertex2f(center[0] - 384, center[1] - 245)

    bgl.glTexCoord2f(0, 1)
    bgl.glVertex2f(center[0] - 384, center[1] + 245)

    bgl.glTexCoord2f(1, 1)
    bgl.glVertex2f(center[0] + 384, center[1] + 245)

    bgl.glTexCoord2f(1, 0)
    bgl.glVertex2f(center[0] + 384, center[1] - 245)

    bgl.glEnd()
    bgl.glDisable(bgl.GL_TEXTURE_2D)
    
    bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
    blf.position(font_id, center[0] - 380, center[1] - 237, 0)
    blf.draw(font_id, 'Version: Bushlurker(Test build: 0.2)')
    
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    blf.disable(0, blf.SHADOW)
    
def daseu31lm(self, context):
    region = context.region

    width,height = region.width,region.height

    font_id = 0
    blf.size(font_id, 12, 72)
    blf.enable(0, blf.SHADOW)
    blf.shadow_offset(0, 2, -2)
    blf.shadow(0, 3, 0.0, 0.0, 0.0, 1)
    
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glLineStipple(2, 0xAAAA)
    bgl.glColor4f(.7, .7, .7, 1.0)
    bgl.glEnable(bgl.GL_LINE_STIPPLE)
    
    if not self.switch:
        bgl.glBegin(bgl.GL_LINES)
        bgl.glVertex2i(0, self.de31amlus)
        bgl.glVertex2i(width, self.de31amlus)
        bgl.glVertex2i(self.dalms31ue, 0)
        bgl.glVertex2i(self.dalms31ue, height)
        bgl.glEnd()
        
    else:
        duems31la = self.desuam31l
        damles31u = list(bpy.context.region.view2d.view_to_region(duems31la[0],duems31la[1],clip=False))
        
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.dalms31ue, self.de31amlus)
        bgl.glVertex2i(damles31u[0], self.de31amlus)
        bgl.glVertex2i(damles31u[0], damles31u[1])
        bgl.glVertex2i(self.dalms31ue, damles31u[1])
        bgl.glEnd()

        bgl.glColor4f(0.0, 1.0, 0.0, 0.3)
        bgl.glBegin(bgl.GL_POLYGON)
        bgl.glVertex2i(self.dalms31ue, self.de31amlus)
        bgl.glVertex2i(damles31u[0], self.de31amlus)
        bgl.glVertex2i(damles31u[0], damles31u[1])
        bgl.glVertex2i(self.dalms31ue, damles31u[1])
        bgl.glEnd()
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.position(font_id, self.dalms31ue - 210, self.de31amlus - 15, 0)
        blf.draw(font_id, self.d31ulaems)
        blf.position(font_id, self.dalms31ue - 210, self.de31amlus - 30, 0)
        blf.draw(font_id, self.dsau31eml)
        blf.position(font_id, self.dalms31ue - 210, self.de31amlus - 45, 0)
        blf.draw(font_id, self.d31lsaeum)      

    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    bgl.glDisable(bgl.GL_LINE_STIPPLE)
    blf.disable(0, blf.SHADOW)
          
def dulmse31a(dmuale31s,da31muesl):
    dula31mse, dmal31seu, demasu31l, d31usamle = dmuale31s[0], dmuale31s[1], da31muesl[0], da31muesl[1]

    if demasu31l < 0:
        demasu31l = 0.0
    elif demasu31l > 1:
        demasu31l = 1.0
        
    if d31usamle < 0:
        d31usamle = 0.0
    elif d31usamle > 1:
        d31usamle = 1.0

    if dula31mse < 0:
        dula31mse = 0.0
    elif dula31mse > 1:
        dula31mse = 1.0
    
    if dmal31seu < 0:
        dmal31seu = 0.0
    elif dmal31seu > 1:
        dmal31seu = 1.0

    if demasu31l < dula31mse:
        dmlsa31eu = demasu31l
        dual31ems = dula31mse
    else:
        dmlsa31eu = dula31mse
        dual31ems = demasu31l

    if d31usamle > dmal31seu:
        dua31smel = d31usamle
        dsmlu31ae = dmal31seu
    else:
        dua31smel = dmal31seu
        dsmlu31ae = d31usamle
  
    return dua31smel,dmlsa31eu,dsmlu31ae,dual31ems
    
def dlu31maes(dl31mseau,dlmuae31s,dua31smel,dmlsa31eu,dsmlu31ae,dual31ems):
    dmselau31 = False
    d31esamlu = False
    
    if isnan(dua31smel):
        dua31smel = 0.0
    if isnan(dmlsa31eu):
        dmlsa31eu = 0.0

    if dua31smel == 1.0:
        duseml31a = 0
        dmselau31 = True
    else:
        duseml31a = floor((1 - dua31smel) * dlmuae31s)
        
    dem31lasu = ceil(dmlsa31eu * dlmuae31s)
    
    if dsmlu31ae == 0.0:
        dmleuas31 = dlmuae31s - 1
    else:
        dmleuas31 = floor((1 - dsmlu31ae) * dlmuae31s) - 1
        
    if dual31ems == 1.0:
         deulm31as = dlmuae31s - 1
         d31esamlu = True
    else:
        deulm31as = ceil(dual31ems * dlmuae31s) - 1
        
    dl31uemsa = deulm31as - dem31lasu + 2 if d31esamlu else deulm31as - dem31lasu + 1
    delas31um = dmleuas31 - duseml31a + 2 if dmselau31 else dmleuas31 - duseml31a + 1
        
    return duseml31a, dem31lasu, dmleuas31, deulm31as, dmselau31, d31esamlu, dl31uemsa, delas31um
    
def dsmu31lea(demsu31al,dlmuae31s,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu):
    print(' Heightfield preparation started {}'.format(time.ctime()))
    dsuale31m = fromfile(demsu31al, dtype=float32)
    demasul31 = reshape(dsuale31m,(dlmuae31s,dlmuae31s))
    dsuale31m = demasul31[duseml31a:dmleuas31 + 1,dem31lasu:deulm31as + 1]
    
    if dmselau31 and d31esamlu:
        dle31aums = dsuale31m[0]
        dsuale31m = vstack((dle31aums,dsuale31m))
        dealus31m = dsuale31m[:,[-1]]
        dsuale31m = hstack((dsuale31m,dealus31m))
    else:
        if dmselau31:
            dle31aums = dsuale31m[0]
            dsuale31m = vstack((dle31aums,dsuale31m))
        if d31esamlu:
            dealus31m = dsuale31m[:,[-1]]
            dsuale31m = hstack((dsuale31m,dealus31m))
    print(' Heightfield preparation finished {}'.format(time.ctime()))
    return dsuale31m

def duam31les(dumea31ls,dlsmue31a,dem31lasu,duseml31aChanged,duase31ml,damsule31,dumse31al,dsmlea31u):
    dal31umes = dlsmue31a * dem31lasu - dumea31ls * duase31ml
    dea31lums = dlsmue31a * duseml31aChanged - dumea31ls * damsule31
    print(' Pixel edge to vertex distance: ', dal31umes,dea31lums)
    d31sameul = 1 / dumea31ls * dal31umes
    dul31esma = 1 / dumea31ls * dea31lums
    print(' Vertex from pixel shift: ', d31sameul,dul31esma)
    
    dmlsuae31 = 1 / dumse31al * d31sameul
    dsul31ame = 1 - (1 / dsmlea31u * dul31esma)
    print(' uvStart at: ', dmlsuae31, dsul31ame)
    
    ds31umale = (dlsmue31a / dumea31ls) * (1 / dumse31al)
    dml31eusa = (dlsmue31a / dumea31ls) * (1 / dsmlea31u)
    print(' terrainUVcellsizeLoc: ', ds31umale, dml31eusa)
    return dmlsuae31, dsul31ame, ds31umale, dml31eusa

def d31leasmu(deu31smal, demasul31, dlumesa31):
    deu31smal[dlumesa31[0]:dlumesa31[0] + demasul31.shape[0], dlumesa31[1]:dlumesa31[1] + demasul31.shape[1]] = demasul31
    return deu31smal
    
def dauslm31e(dlsamue31):
    print('\nbLT_Info: Heightmap export started ', time.ctime())
    d31emausl = bpy.data.scenes['Default_Location']
    demalu31s = d31emausl.d31emusal
    daue31msl = d31emausl.daue31msl
    dlmuae31s,dmaseu31l,dual31sem,dl31mseau = d31emausl["da31mlues"],d31emausl["dmaseu31l"],d31emausl["dual31sem"],d31emausl["ds31uamle"]
    d31saelum = fromfile(demalu31s,dtype=float32)
    dulmaes31 = d31saelum.reshape((dlmuae31s,dlmuae31s))
    
    du31almes = bpy.context.scene.name
    dlmsa31ue = bpy.data.objects.get('Terrain_{}'.format(du31almes))
    deusmla31 = dlmsa31ue.matrix_world
    
    dsuale31m1D = []
    for v in dlmsa31ue.data.vertices:
        dsu31laem = deusmla31 * v.co
        dsuale31m1D.append(round(dsu31laem[2],2))
    
    demasul31 = array(dsuale31m1D).reshape(dlmsa31ue["dms31luea"],dlmsa31ue["dalems31u"])
    
    if dlmsa31ue['dm31sleau']:
        demasul31 = delete(demasul31,0,0)
    if dlmsa31ue['dealsu31m']:
        demasul31 = delete(demasul31,-1,1)
    
    deu31amls = d31leasmu(dulmaes31, demasul31, [dlmsa31ue["dsea31mlu"],dlmsa31ue["dsme31lua"]])
    deu31amls.astype('float32').tofile(demalu31s)
    if dlsamue31:
        daemu31sl = d31emausl.dlsumea31
    else:
        daemu31sl = '{}\\Output\\elevation.asc'.format(daue31msl)
    header = 'ncols         {}\nnrows         {}\ndmaseu31l     {}\ndual31sem     {}\ncellsize      {}\nNODATA_value  -9999'.format(dlmuae31s,dlmuae31s,dmaseu31l,dual31sem,dl31mseau)
    savetxt(daemu31sl,deu31amls,fmt='%.2f',delimiter=' ',comments='',header=header)
    print(' bLT_Info: Shaded terrain preview regeneration started ', time.ctime())
    dmels31au(daemu31sl)
    print(' bLT_Info: Shaded terrain preview regeneration finished ', time.ctime())
    print('bLT_Info: Heightmap export finished ', time.ctime())
    
def dua31mles(dlsamue31):
    dmealsu31 = bpy.data.scenes["Default_Location"].dumlse31a
    if bpy.context.scene.dml31eaus:
        print('\nbLT_Info: Surface map export started ', time.ctime())
        from cv2 import imread as dl31mueas, imwrite as dusea31lm, IMREAD_COLOR as dl31usame
        daue31msl = bpy.data.scenes["Default_Location"].daue31msl
        du31almes = bpy.context.scene.name
        dslemua31 = dl31mueas(bpy.data.scenes["Default_Location"].dumlse31a, dl31usame)
        dleusma31 = dl31mueas(r'{}ProjectData\Textures\TerrainMask_{}.png'.format(daue31msl,du31almes), dl31usame)
        dlmsa31ue = bpy.data.objects.get('Terrain_{}'.format(du31almes))
        dslemua31[dlmsa31ue['MergeTopLeftY']:dlmsa31ue["MergeBottomRightY"],dlmsa31ue["MergeTopLeftX"]:dlmsa31ue["MergeBottomRightX"]] = dleusma31
        if dlsamue31:
            daemu31sl = dmealsu31
        else:
            daemu31sl = '{}\\Output\\d31slmuae.png'.format(daue31msl)
        dusea31lm(daemu31sl, dslemua31)
        print('bLT_Info: Surface map export finished ', time.ctime())
    else:
        print('\nbLT_Info:No surface map data exported!!! Source surface mask path not defined in Data Sources panel.')
    
    
def dslemu31a(du31almes,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu):
    d31ulemas = bpy.data.scenes['Default_Location']
    dlmuae31s = d31ulemas["da31mlues"]
    dl31mseau = d31ulemas["ds31uamle"]
    
    dusae31ml = bpy.data.grease_pencil["OccupiedLocations"].layers.new(du31almes)
    d31lauesm = dusae31ml.frames.new(0)
    dealmu31s = d31lauesm.strokes.new('dealmu31s')
    dealmu31s.colorname = 'Color'
    dealmu31s.draw_mode = '2DSPACE'
    
    d31lsaeum = dlmuae31s * dl31mseau
    
    dsemu31la = (dem31lasu * dl31mseau) / d31lsaeum
    duemsla31 = 1 if dmselau31 else 1 - ((duseml31a + 1) * dl31mseau / d31lsaeum)
    dul31meas = 1 if d31esamlu else (deulm31as * dl31mseau) / d31lsaeum
    dm31esalu = 1 - ((dmleuas31 + 1) * dl31mseau / d31lsaeum)
    
    
    dealmu31s.points.add()
    dealmu31s.points[0].co = Vector((dsemu31la,duemsla31,0))
    dealmu31s.points.add()
    dealmu31s.points[1].co = Vector((dsemu31la,dm31esalu,0))
    dealmu31s.points.add()
    dealmu31s.points[2].co = Vector((dul31meas,dm31esalu,0))
    dealmu31s.points.add()
    dealmu31s.points[3].co = Vector((dul31meas,duemsla31,0))
    
    
def d31smleua(du31almes,dl31uemsa,delas31um,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu):
    d31ulemas = bpy.data.scenes['Default_Location']
    dlmuae31s = d31ulemas["da31mlues"]
    dl31mseau = d31ulemas["ds31uamle"]
    dumel31as = bpy.data.scenes['Default_Location'].d31emusal
    dsluae31m = bpy.data.scenes["Default_Location"].demual31s
    dmealsu31 = bpy.data.scenes["Default_Location"].dumlse31a
    daue31msl = bpy.data.scenes["Default_Location"].daue31msl

    bpy.context.window.screen.scene = bpy.data.scenes["Default_Location"]
    bpy.ops.scene.new(type='FULL_COPY')
    bpy.context.scene.name = du31almes
    bpy.context.scene['dlm31saue'] = True
    
    
    if bpy.data.meshes.get('TerrainMesh_{}'.format(du31almes)) is not None:
        bpy.data.meshes.get('TerrainMesh_{}'.format(du31almes)).user_clear()
        bpy.data.meshes.remove(bpy.data.meshes.get('TerrainMesh_{}'.format(du31almes)))

    dsuaml31e = bpy.data.meshes.new('TerrainMesh_{}'.format(du31almes))
    dlmsa31ue = bpy.data.objects.new('Terrain_{}'.format(du31almes),dsuaml31e)
    bpy.context.scene.objects.link(dlmsa31ue)
    dlmsa31ue.select=True
    bpy.context.scene.objects.active = dlmsa31ue
    
    print('\nbLT_Info: Location creation started ', time.ctime())
    
    if bpy.context.scene.du31lames:
        dsamuel31 = d31ulemas["ImageryResolution"]
        
        dumea31ls = 1 / dsamuel31
        dlsmue31a = 1 / dlmuae31s
        print(' UVCellTexture: ', dumea31ls)
        print(' UVCellTerrain: ', dlsmue31a)
        
        duseml31aChanged = duseml31a
        dal31eusm = deulm31as
        deslaum31 = dmleuas31
        
        if not dmselau31:
            duseml31aChanged += 1
            
        deslaum31 += 1     
            
        
        duase31ml = floor(dem31lasu * dlsmue31a / dumea31ls)
        damsule31 = floor(round(duseml31aChanged * dlsmue31a / dumea31ls,6))

        if d31esamlu:
            dal31eusm += 1
        
        daem31usl = ceil(dal31eusm * dlsmue31a / dumea31ls) - 1
        da31eusml = ceil(round(deslaum31 * dlsmue31a / dumea31ls,6)) - 1
        
        dumse31al = daem31usl - duase31ml + 1
        dsmlea31u = da31eusml - damsule31 + 1
         
        print(' Texture starts at: ', duase31ml, damsule31)
        print(' Texture ends at: ', daem31usl, da31eusml)
        print(' Terrain texture resolution: ', dumse31al,dsmlea31u)
        
        from cv2 import imread as dl31mueas, imwrite as dusea31lm, IMREAD_COLOR as dl31usame
        print(' Location\'s terrain texture extraction started ', time.ctime())
        dms31aeul = dl31mueas(dsluae31m, dl31usame)
        dsuae31lm = dms31aeul[damsule31:da31eusml,duase31ml:daem31usl]
        dusea31lm(r'{}ProjectData\Textures\TerrainImage_{}.png'.format(daue31msl,du31almes), dsuae31lm)
        print(' Location\'s terrain texture extraction finished ', time.ctime())
        dsamu31el= bpy.data.textures.new('TerrainTexture_{}'.format(du31almes), type = 'IMAGE')
        dsamu31el.image = bpy.data.images.load('{}ProjectData\\Textures\\TerrainImage_{}.png'.format(daue31msl,du31almes))
        
        if bpy.context.scene.dml31eaus:
            print(' Location\'s surface mask extraction started ', time.ctime())
            dms31aeul = dl31mueas(dmealsu31, dl31usame)
            dleusma31 = dms31aeul[damsule31:da31eusml,duase31ml:daem31usl]
            dusea31lm(r'{}ProjectData\Textures\TerrainMask_{}.png'.format(daue31msl,du31almes), dleusma31)
            print(' Location\'s surface mask extraction finished ', time.ctime())
            
            dema31usl= bpy.data.textures.new('TerrainMask_{}'.format(du31almes), type = 'IMAGE')
            dema31usl.image = bpy.data.images.load('{}ProjectData\\Textures\\TerrainMask_{}.png'.format(daue31msl,du31almes))
        
    
        #-------------------------- Create new terrain material ----------------------------------------------
        dalm31seu = bpy.data.materials.new('TerrainMaterial_{}'.format(du31almes))
        dalm31seu.specular_intensity = 0
        dalm31seu.texture_slots.add()
        
        da31ulsme = dalm31seu.texture_slots[0]
        da31ulsme.texture = dsamu31el
        da31ulsme.texture_coords = 'UV'
        
        if bpy.context.scene.dml31eaus:
            dalm31seu.texture_slots.add()
            da31ulsme = dalm31seu.texture_slots[1]
            da31ulsme.texture = dema31usl
            da31ulsme.texture_coords = 'UV'
            da31ulsme.diffuse_color_factor = .5
            dalm31seu.use_textures[1] = False
            dalm31seu.paint_active_slot = 1
        
        bpy.ops.object.material_slot_add()
        bpy.data.objects['Terrain_{}'.format(du31almes)].material_slots[0].material = dalm31seu  
    
    bm = bmesh.new() 
    bm.from_mesh(dsuaml31e)
    
    if bpy.context.scene.du31lames:
        dlasem31u = bm.faces.layers.tex.verify()
        d31mluaes = bm.loops.layers.uv.verify()
        
    d31aumlse = dsmu31lea(dumel31as,dlmuae31s,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu)
    damuesl31 = dem31lasu * dl31mseau
    if dmselau31:
        daelums31 = dlmuae31s * dl31mseau
    else:
        daelums31 = (dlmuae31s - 1)  * dl31mseau
    
    print(' Terrain mesh/UVs generation started ', time.ctime())
    dle31usma = daelums31 - (duseml31a * dl31mseau)
    for row in range(delas31um):
        del31amus = d31aumlse[row]
        for col in range(dl31uemsa):
            bm.verts.new((damuesl31,dle31usma,del31amus[col]))
            damuesl31 += dl31mseau
        damuesl31 = dem31lasu * dl31mseau
        dle31usma -= dl31mseau
    bm.verts.ensure_lookup_table()
    
    if bpy.context.scene.du31lames:
        dmlsuae31, dsul31ame, ds31umale, dml31eusa = duam31les(dumea31ls,dlsmue31a,dem31lasu,duseml31aChanged,duase31ml,damsule31,dumse31al,dsmlea31u)
    daue31lms = 0
    for desam31ul in range(0,dl31uemsa * (delas31um - 1), dl31uemsa):
        for dasu31elm in range (0, dl31uemsa - 1):
            d31asumle = desam31ul + dasu31elm
            face = [bm.verts[d31asumle],bm.verts[d31asumle + dl31uemsa],bm.verts[d31asumle + dl31uemsa + 1],bm.verts[d31asumle + 1]]
            d31selamu = bm.faces.new(face)
            
            if bpy.context.scene.du31lames:
                d31selamu[dlasem31u].image = bpy.data.images['TerrainImage_{}.png'.format(du31almes)]
                d31selamu.loops[0][d31mluaes].uv = [dmlsuae31 + dasu31elm * ds31umale, dsul31ame - daue31lms * dml31eusa]
                d31selamu.loops[1][d31mluaes].uv = [dmlsuae31 + dasu31elm * ds31umale, dsul31ame - daue31lms * dml31eusa - dml31eusa]
                d31selamu.loops[2][d31mluaes].uv = [dmlsuae31 + dasu31elm * ds31umale + ds31umale, dsul31ame - daue31lms * dml31eusa - dml31eusa]
                d31selamu.loops[3][d31mluaes].uv = [dmlsuae31 + dasu31elm * ds31umale + ds31umale, dsul31ame - daue31lms * dml31eusa]
        daue31lms += 1
        
    bmesh.ops.triangulate(bm, faces=bm.faces, quad_method=2)
    bm.to_mesh(dsuaml31e)
    bm.free()
    print(' Terrain mesh/UVs generation finished ', time.ctime())
    
    
    dlmsa31ue["dsea31mlu"] = duseml31a
    dlmsa31ue["dsme31lua"] = dem31lasu
    dlmsa31ue["dalems31u"] = dl31uemsa
    dlmsa31ue["dms31luea"] = delas31um
    dlmsa31ue["dm31sleau"] = dmselau31
    dlmsa31ue["dealsu31m"] = d31esamlu
    if bpy.context.scene.dml31eaus:
        dlmsa31ue["MergeTopLeftY"] = damsule31
        dlmsa31ue["MergeTopLeftX"] = duase31ml
        dlmsa31ue["MergeBottomRightY"] = da31eusml
        dlmsa31ue["MergeBottomRightX"] = daem31usl
    dlmsa31ue.lock_location = True,True,True
    dlmsa31ue.lock_rotation = True,True,True
    dlmsa31ue.lock_scale = True,True,True
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    
    print('bLT_Info: Location creation finished {}\n'.format(time.ctime()))
    
    bpy.context.area.type = 'VIEW_3D'
    screen = bpy.context.window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'window': bpy.context.window, 'screen': screen, 'area': area, 'region': region, 'scene': bpy.context.scene, 'edit_object': bpy.context.edit_object}
    
    bpy.ops.view3d.view_selected(override)
    
    dalemsu31(du31almes, dsl31uame = True if bpy.context.scene.du31lames else False)
    
    dlmsa31ue.select = False
    dlmsa31ue.hide_select = True
    
    
def de31smlau(context):
    daulm31es = context.active_object
    d31ausmle = daulm31es.dupli_group['Dimension']
    bpy.ops.mesh.primitive_plane_add(radius=d31ausmle / 2 + (d31ausmle * .1), location=daulm31es.location, rotation=(0.0,0.0,daulm31es.rotation_euler[2]))
    
    d31almseu = context.active_object
    d31almseu.show_x_ray = True
    d31almseu.draw_type = 'WIRE'
    d31almseu.name = 'Flatter_{}'.format(daulm31es.name)
    
    daulm31es.select = True
    bpy.context.scene.objects.active = daulm31es
    bpy.ops.object.parent_set(type='OBJECT')
    
    dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
    dmelus31a = dlmsa31ue.modifiers.new(d31almseu.name, 'SHRINKWRAP')
    dmelus31a.target = d31almseu
    dmelus31a.wrap_method = 'PROJECT'
    dmelus31a.use_project_z = True
    dmelus31a.use_negative_direction = True
    
    daulm31es.select = False
    bpy.context.scene.objects.active = d31almseu
    
def d31luaesm(context):
    bpy.ops.object.select_all(action='DESELECT')
    Areas = bpy.context.screen.areas
    for Area in Areas:
        if Area.type == 'VIEW_3D':
            deula31ms = Area.spaces.active.cursor_location
    bpy.ops.object.empty_add(type='SINGLE_ARROW', radius=1.0, location=deula31ms)
    daemlsu31 = context.active_object
    daemlsu31.lock_scale = True,True,True
    daemlsu31.show_x_ray = True
    daemlsu31.empty_draw_size = 50
    daemlsu31.name = "M_T_M"
    
    bpy.ops.mesh.primitive_plane_add(radius=context.scene['ds31uamle'] * 1.5, location=deula31ms)
    d31almseu = context.active_object
    d31almseu.show_x_ray = True
    d31almseu.draw_type = 'WIRE'
    d31almseu.name = 'Flatter_{}'.format(daemlsu31.name)
    
    daemlsu31.select = True
    bpy.context.scene.objects.active = daemlsu31
    bpy.ops.object.parent_set(type='OBJECT')
    
    dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
    dmelus31a = dlmsa31ue.modifiers.new(d31almseu.name, 'SHRINKWRAP')
    dmelus31a.target = d31almseu
    dmelus31a.wrap_method = 'PROJECT'
    dmelus31a.use_project_z = True
    dmelus31a.use_negative_direction = True
    
    daemlsu31.select = False
    bpy.context.scene.objects.active = d31almseu
  
def dl31uasme(context):
    delm31usas = bpy.context.selected_objects
    
    dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
    bpy.context.scene.objects.active = dlmsa31ue
    
    for delm31usa in delm31usas:
        bpy.ops.object.modifier_apply(modifier=delm31usa.children[0].name)
        context.scene.objects.unlink(delm31usa.children[0])
        delm31usa.children[0].user_clear()
        bpy.data.objects.remove(delm31usa.children[0])
        if delm31usa.dupli_group is None:
            context.scene.objects.unlink(delm31usa)
            delm31usa.user_clear()
            bpy.data.objects.remove(delm31usa)        
            
def d31mlueas(context):
    bpy.ops.object.select_all(action='DESELECT')
    Areas = bpy.context.screen.areas
    for Area in Areas:
        if Area.type == 'VIEW_3D':
            deula31ms = Area.spaces.active.cursor_location
    
    dma31usel = bpy.data.curves.new('TerrainModifierSpline',"CURVE")
    dma31usel.splines.new("BEZIER")
    dma31usel.dimensions = '3D'
    dueamls31 = bpy.data.objects.new("S_T_M", dma31usel)
    dueamls31.lock_scale = True,True,True
    dueamls31.show_x_ray = True
    dma31usel.splines[0].bezier_points[0].co.x = 0
    dma31usel.splines[0].bezier_points[0].co.y = 0
    dma31usel.splines[0].bezier_points[0].handle_right_type = 'ALIGNED'
    dma31usel.splines[0].bezier_points[0].handle_left_type = 'ALIGNED'
    dma31usel.splines[0].bezier_points[0].handle_left = 0,-20,0    
    dma31usel.splines[0].bezier_points[0].handle_right = 0,20,0
    dma31usel.splines[0].bezier_points.add(1)
    dma31usel.splines[0].bezier_points[1].co.x = 0
    dma31usel.splines[0].bezier_points[1].co.y = 80
    dma31usel.splines[0].bezier_points[1].handle_right_type = 'ALIGNED'
    dma31usel.splines[0].bezier_points[1].handle_left_type = 'ALIGNED'
    dma31usel.splines[0].bezier_points[1].handle_left = 0,60,0
    dma31usel.splines[0].bezier_points[1].handle_right = 0,100,0
    dma31usel.splines[0].resolution_u = 20
    dma31usel.twist_mode = 'Z_UP'
    bpy.context.scene.objects.link(dueamls31)
    dueamls31['dameslu31'] = context.scene['ds31uamle'] * 3
    
    bpy.ops.mesh.primitive_plane_add(radius= .5, location=(.5,0,0))
    d31almseu = context.active_object
        
    d31almseu.scale.y = dueamls31['dameslu31']
    d31almseu.name = 'Flatter_{}'.format(dueamls31.name)
    d31almseu.draw_type = 'WIRE'
    d31almseu.hide_select = True
    
    dlse31mua = d31almseu.modifiers.new('Array', 'ARRAY')
    dlse31mua.fit_type = 'FIT_CURVE'
    dlse31mua.curve = dueamls31
    
    dml31seau = d31almseu.modifiers.new('Curve', 'CURVE')
    dml31seau.object = dueamls31
    
    dueamls31.select = True
    bpy.context.scene.objects.active = dueamls31
    bpy.ops.object.parent_set(type='OBJECT')
    dueamls31.location = deula31ms
    
    d31almseu.select = False
    
    dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
    dmelus31a = dlmsa31ue.modifiers.new(d31almseu.name, 'SHRINKWRAP')
    dmelus31a.target = d31almseu
    dmelus31a.wrap_method = 'PROJECT'
    dmelus31a.use_project_z = True
    dmelus31a.use_negative_direction = True

def dlsu31eam(context):
    delm31usas = bpy.context.selected_objects
    
    dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
    bpy.context.scene.objects.active = dlmsa31ue
   
    for obj in delm31usas:
        bpy.ops.object.modifier_apply(modifier=obj.children[0].name)
        context.scene.objects.unlink(obj.children[0])
        context.scene.objects.unlink(obj)
        obj.children[0].user_clear()
        obj.user_clear()
        bpy.data.objects.remove(obj.children[0])
        bpy.data.objects.remove(obj)

def dseamlu31(dl31mseau,desm31ula,dlseau31m):
    dema31lus = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dema31lus
    if dema31lus != '':
        result = ones((desm31ula,desm31ula)) * dlseau31m
        header = 'ncols         {}\nnrows         {}\ndmaseu31l     0\ndual31sem     0\ncellsize      {}\nNODATA_value  -9999'.format(desm31ula,desm31ula,dl31mseau) 
        savetxt('{}\\elevation.asc'.format(dema31lus),result,fmt='%.2f',delimiter=' ',newline='\r\n',comments='',header=header)
        print('Elevation file saved to {}\\elevation.asc'.format(dema31lus))
    
def d31usemla(dmulae31s,dumal31se):
    dema31lus = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dema31lus
    if dema31lus != '':
        from cv2 import imwrite as dusea31lm
        du31eamls = zeros((dmulae31s,dmulae31s,3), uint8)
        du31eamls[:,:,0] = ones([dmulae31s,dmulae31s]) * dumal31se[2] * 255
        du31eamls[:,:,1] = ones([dmulae31s,dmulae31s]) * dumal31se[1] * 255
        du31eamls[:,:,2] = ones([dmulae31s,dmulae31s]) * dumal31se[0] * 255
        dusea31lm('{}\\surface_mask.png'.format(dema31lus), du31eamls)
        print('Surface mask file saved to {}\\surface_mask.png'.format(dema31lus))
        
def dmlas31eu(self, context):
    dua31smle = context.scene.du31slemaPath
    
    if dua31smle != '':
        if dua31smle.split('.')[-1] in ['png','tif','tiff']:
            context.scene.dl31ueasm = True
        else:
            context.scene.dl31ueasm = False
            print('\nbLT_Info: {} is unsupported surface mask file format! Use PNG, TIF, TIFF instead.'.format(dua31smle.split('.')[-1]))
    else:
        context.scene.dl31ueasm = False

def du31slema(context,dl31mseau,desm31ula,dslame31u,dmsauel31):
    def dseluam31(dl31mseau,desm31ula,dslame31u,dmsauel31):
        def dalmse31u( x ):
            return floor(x + 0.5)

        def dasuel31m( x, i ):
            return (abs( x - i ) < 0.000001)

        def check( x ):
            return dasuel31m(x, dalmse31u( x ))

        dlas31emu = dl31mseau * desm31ula  
        dalseum31 = 1
        dalusm31e = 1000000
        d31almsue = -1
        for i in range(0,8):
            duas31elm = dalseum31 * dl31mseau
            dist = abs(40.0 - duas31elm)
            if dist < dalusm31e:
                dalusm31e = dist
                d31almsue = dalseum31
            dalseum31 *= 2

        duesl31ma = d31almsue
        m_duas31elm = duesl31ma * dl31mseau #land grid cell size or _duas31elm
        dams31uel = floor( dlas31emu / m_duas31elm ) #land grid size or _landRange
        duasme31l = duesl31ma * dams31uel #terrain grid size or _terrainRange
        dl31saume = ds31maleu = duasme31l * dl31mseau #final terrain size
        dmsalu31e = 16 # minimum overlap
        dseau31lm = int(dslame31u) - dmsalu31e
        dseau31lmMeters = dmsauel31 * dseau31lm
        daeusl31m = floor( dseau31lmMeters / m_duas31elm )
        daeusl31m -= daeusl31m % 4
        ds31mlaeu = daeusl31m * m_duas31elm
        dsmea31ul = ds31mlaeu / dmsauel31
        de31lumas = int(dslame31u) - dsmea31ul
        dame31sul = ceil( dl31saume / ds31mlaeu )
        return de31lumas, dame31sul
    
    from cv2 import imread as dl31mueas, imwrite as dusea31lm
    
    d31slmuae = dl31mueas(context.scene.du31slemaPath,1)

    
    dea31smlu = dlmsae31u = int((dl31mseau * desm31ula) / dmsauel31)
    rgb = zeros((dea31smlu,dlmsae31u,3), uint8)
    alpha = zeros((dea31smlu,dlmsae31u,1), uint8)

    de31lumas, dame31sul = dseluam31(dl31mseau,desm31ula,dslame31u,dmsauel31)
    
    font = cv2.FONT_HERSHEY_DUPLEX
    
    print(de31lumas, dame31sul)