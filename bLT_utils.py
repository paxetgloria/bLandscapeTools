import bpy,bgl,blf,bmesh
import subprocess,os,time, struct
from shutil import copy,rmtree
from math import floor, isnan, ceil
from numpy import genfromtxt,vstack,hstack,array,savetxt,delete,ones,flipud,empty,fromfile,float16,float32,reshape
from mathutils import Vector, Matrix

def d01lqobp(self, context):
    doql0b1pPath = bpy.data.scenes["Default_Location"].dlqop10b
    
    dp01lobq = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.dp01lobq
    db0pl1oq = bpy.data.scenes["Default_Location"].db0pl1oq
    do0qpb1l = 'Project_{}'.format(db0pl1oq.split('\\')[-2])
    dl1qpbo0 = d1l0qbpo(dp01lobq,doql0b1pPath)
    
    if os.path.exists('{}ProjectData\\Textures\\previewSatTex.png'.format(db0pl1oq)):
        os.remove('{}ProjectData\\Textures\\previewSatTex.png'.format(db0pl1oq))
    
    if dl1qpbo0 < 5000:
        copy(bpy.context.scene.dlqop10b,'{}ProjectData\\Textures\\'.format(db0pl1oq))
        dopql10b = bpy.context.scene.dlqop10b.split('\\')[-1]
        os.rename('{}ProjectData\\Textures\\{}'.format(db0pl1oq,dopql10b),'{}ProjectData\\Textures\\previewSatTex.png'.format(db0pl1oq))
    else:
        cmd = '"{}gdal_translate.exe" "{}" -of PNG -outsize 5000 5000 "{}ProjectData\Textures\previewSatTex.png"'.format(dp01lobq,doql0b1pPath,db0pl1oq)
        subprocess.call(cmd)
    if bpy.data.images.get('previewSatTex.png') is None:
        bpy.data.images.load('{}ProjectData\\Textures\\previewSatTex.png'.format(db0pl1oq))
        bpy.data.images['previewSatTex.png'].use_fake_user = True
    else:
        bpy.data.images['previewSatTex.png'].reload()
        
    dp10boql = bpy.data.scenes['Default_Location']    
    dp10boql["ImageryResolution"] = dl1qpbo0
    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(db0pl1oq,do0qpb1l))
    
def dlbpo1q0(self, context):
    
    
    dp01lqob = bpy.data.scenes["Default_Location"].dlbo0qp1
    
    dp01lobq = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.dp01lobq
    db0pl1oq = bpy.data.scenes["Default_Location"].db0pl1oq
    do0qpb1l = 'Project_{}'.format(db0pl1oq.split('\\')[-2])
    db0oq1lp = dbop1lq0(dp01lqob)
    dp0bql1o = genfromtxt(dp01lqob, delimiter=' ', skip_header=6)
    do10lqbp = '{}ProjectData\\Textures\\elevation.bLTe'.format(db0pl1oq)
    dp0bql1o.astype('float32').tofile(do10lqbp)

    print('Elevation converted')
    
    dp1b0oql(dp01lqob)
    
    dp10boql = bpy.data.scenes['Default_Location']
    dp10boql["dlqp0o1b"] = db0oq1lp[0]
    dp10boql["dbo0qlp1"] = db0oq1lp[1]
    dp10boql["db0qpol1"] = db0oq1lp[2]
    dp10boql["d01bopql"] = db0oq1lp[3]
    bpy.data.scenes['Default_Location'].doplq0b1 = do10lqbp

    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(db0pl1oq,do0qpb1l))
    
def dp1b0oql(dp01lqob):
    dp01lobq = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.dp01lobq
    db0pl1oq = bpy.data.scenes["Default_Location"].db0pl1oq
    
    cmd = '"{}gdaldem.exe" hillshade -az 45 -z 1.3 "{}" "{}ProjectData\Textures\previewTerTex.tif"'.format(dp01lobq,dp01lqob,db0pl1oq)
    subprocess.call(cmd)
    
    if bpy.data.images.get('previewTerTex.tif') is None:
        bpy.data.images.load('{}ProjectData\\Textures\\previewTerTex.tif'.format(db0pl1oq))
        bpy.data.images['previewTerTex.tif'].use_fake_user = True
    else:
        bpy.data.images['previewTerTex.tif'].reload()


def dob01qpl():
    import addon_utils
    
    addons = [mod for mod in addon_utils.modules(refresh=False)]

    for mod in addons:
        if mod.__name__ == "bLandscapeTools":
            scriptPath = mod.__file__
            pass
           
    scriptFolder = scriptPath[:-12]
    d0lqop1b = '{}\\data'.format(scriptFolder)
    
    return scriptPath,scriptFolder,d0lqop1b
     
def d1l0qbpo(dp01lobq,doql0b1pPath):
    ext = doql0b1pPath.split('.')[-1]
    if ext == 'png':
        dbopql10 = 'pgw'
    if ext == 'tif' or ext == 'tiff':
        dbopql10 = 'tfw'
    if ext == 'jpg' or ext == 'jpeg':
        dbopql10 = 'jgw'
        
    cmd = '{}gdalinfo.exe "{}"'.format(dp01lobq,doql0b1pPath)
    print(cmd)
    dolb0qp1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    
    for i in range(0,10):
        line = str(dolb0qp1.stdout.readline()).rstrip('\\r\\n\'')
        if line.split(' ')[0][2:] == 'Size':
            info = int(line.split(' ')[3])

    return info
    
def dbop1lq0(path):
    info = []
    f = open(path,"r")
    line = f.readline().split(" ")
    for i in range(5):
        info.append( line[-1])
        line = f.readline().split(" ")
    f.close()
    ncols = int(info[0])
    dpoq01bl = float(info[4])
    x = float(info[2])
    y = float(info[3])
    return ncols,x,y,dpoq01bl

    
    

def d1pb0oql(d0oplq1b):
    bpy.ops.object.lamp_add(type='HEMI')
    hemi = bpy.context.object
    hemi.hide = True
    hemi.name = "Hemi_" + d0oplq1b

    Areas = bpy.context.screen.areas
    for Area in Areas:
        if Area.type == 'VIEW_3D':
            Area.spaces.active.viewport_shade = 'MATERIAL'
            Area.spaces.active.cursor_location = [0,0,0]
            Area.spaces.active.clip_start = 0.1
            Area.spaces.active.clip_end = 20000
            Area.spaces.active.show_world = True
            Area.spaces.active.show_floor = False
            Area.spaces.active.show_axis_x = False
            Area.spaces.active.show_axis_y = False
            Area.spaces.active.fx_settings.use_ssao = False
            Area.spaces.active.fx_settings.ssao.factor = 4.1
            Area.spaces.active.fx_settings.ssao.distance_max = 4.0
            Area.spaces.active.fx_settings.ssao.samples = 70
    
            
def dp1q0blo():
    d0lqop1b = dob01qpl()[2]
    db0pl1oq = bpy.context.scene.db0pl1oq
    do0qpb1l = 'Project_{}'.format(db0pl1oq.split('\\')[-2])

        
  
    
    bpy.ops.wm.open_mainfile(filepath='{}\\dummy.blend'.format(d0lqop1b))

    bpy.context.scene.dlo01pqb = True
    bpy.context.scene.db0pl1oq = db0pl1oq
    bpy.context.scene['dq1bplo0'] = False
    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(bpy.context.scene.db0pl1oq,do0qpb1l),copy=False)

    if not os.path.exists(bpy.context.scene.db0pl1oq + 'ProjectData'):
	    os.makedirs(bpy.context.scene.db0pl1oq + 'ProjectData')
    if not os.path.exists(bpy.context.scene.db0pl1oq + 'ProjectData\\Textures'):
	    os.makedirs(bpy.context.scene.db0pl1oq + 'ProjectData\\Textures')
    else:
        rmtree(bpy.context.scene.db0pl1oq + 'ProjectData\\Textures')
        os.makedirs(bpy.context.scene.db0pl1oq + 'ProjectData\\Textures')
    if not os.path.exists(bpy.context.scene.db0pl1oq + 'Output'):
	    os.makedirs(bpy.context.scene.db0pl1oq + 'Output')

        
def d1qlo0pb():
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
    bpy.ops.view2d.d0bqp1ol(override,'INVOKE_DEFAULT')

def d1bl0opq(self,context):
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
    bgl.glVertex2f(center[0] - 384, center[1] - 192)

    bgl.glTexCoord2f(0, 1)
    bgl.glVertex2f(center[0] - 384, center[1] + 192)

    bgl.glTexCoord2f(1, 1)
    bgl.glVertex2f(center[0] + 384, center[1] + 192)

    bgl.glTexCoord2f(1, 0)
    bgl.glVertex2f(center[0] + 384, center[1] - 192)

    bgl.glEnd()
    bgl.glDisable(bgl.GL_TEXTURE_2D)
    
    bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
    blf.position(font_id, center[0] - 380, center[1] - 184, 0)
    blf.draw(font_id, 'Version: Bushlurker(Test build: 0.1)')
    
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    blf.disable(0, blf.SHADOW)
    
def d10qlobp(self, context):
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
        bgl.glVertex2i(0, self.dbql0p1o)
        bgl.glVertex2i(width, self.dbql0p1o)
        bgl.glVertex2i(self.dqlbp1o0, 0)
        bgl.glVertex2i(self.dqlbp1o0, height)
        bgl.glEnd()
        
    else:
        dopb1l0q = self.d0bqlop1
        dqlop0b1 = list(bpy.context.region.view2d.view_to_region(dopb1l0q[0],dopb1l0q[1],clip=False))
        
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.dqlbp1o0, self.dbql0p1o)
        bgl.glVertex2i(dqlop0b1[0], self.dbql0p1o)
        bgl.glVertex2i(dqlop0b1[0], dqlop0b1[1])
        bgl.glVertex2i(self.dqlbp1o0, dqlop0b1[1])
        bgl.glEnd()

        bgl.glColor4f(0.0, 1.0, 0.0, 0.3)
        bgl.glBegin(bgl.GL_POLYGON)
        bgl.glVertex2i(self.dqlbp1o0, self.dbql0p1o)
        bgl.glVertex2i(dqlop0b1[0], self.dbql0p1o)
        bgl.glVertex2i(dqlop0b1[0], dqlop0b1[1])
        bgl.glVertex2i(self.dqlbp1o0, dqlop0b1[1])
        bgl.glEnd()
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.position(font_id, self.dqlbp1o0 - 210, self.dbql0p1o - 15, 0)
        blf.draw(font_id, self.d0lo1qbp)
        blf.position(font_id, self.dqlbp1o0 - 210, self.dbql0p1o - 30, 0)
        blf.draw(font_id, self.do1q0bpl)
        blf.position(font_id, self.dqlbp1o0 - 210, self.dbql0p1o - 45, 0)
        blf.draw(font_id, self.dlp1qb0o)      

    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    bgl.glDisable(bgl.GL_LINE_STIPPLE)
    blf.disable(0, blf.SHADOW)
          
def dobl1p0q(dpl0bo1q,dpl1oq0b):
    d0plb1oq, d1qlpo0b, dqblop10, dbpl01oq = dpl0bo1q[0], dpl0bo1q[1], dpl1oq0b[0], dpl1oq0b[1]

    if dqblop10 < 0:
        dqblop10 = 0.0
    elif dqblop10 > 1:
        dqblop10 = 1.0
        
    if dbpl01oq < 0:
        dbpl01oq = 0.0
    elif dbpl01oq > 1:
        dbpl01oq = 1.0

    if d0plb1oq < 0:
        d0plb1oq = 0.0
    elif d0plb1oq > 1:
        d0plb1oq = 1.0
    
    if d1qlpo0b < 0:
        d1qlpo0b = 0.0
    elif d1qlpo0b > 1:
        d1qlpo0b = 1.0

    if dqblop10 < d0plb1oq:
        dlo0qbp1 = dqblop10
        dl0qopb1 = d0plb1oq
    else:
        dlo0qbp1 = d0plb1oq
        dl0qopb1 = dqblop10

    if dbpl01oq > d1qlpo0b:
        dlqobp10 = dbpl01oq
        d0plboq1 = d1qlpo0b
    else:
        dlqobp10 = d1qlpo0b
        d0plboq1 = dbpl01oq
  
    return dlqobp10,dlo0qbp1,d0plboq1,dl0qopb1
    
def dlbp0oq1(dpoq01bl,dbl0qpo1,dlqobp10,dlo0qbp1,d0plboq1,dl0qopb1):
    d1lbpq0o = False
    d1olq0pb = False
    
    if isnan(dlqobp10):
        dlqobp10 = 0.0
    if isnan(dlo0qbp1):
        dlo0qbp1 = 0.0

    if dlqobp10 == 1.0:
        dqlbpo10 = 0
        d1lbpq0o = True
    else:
        dqlbpo10 = floor((1 - dlqobp10) * dbl0qpo1)
        
    topLeftColumn = ceil(dlo0qbp1 * dbl0qpo1)
    
    if d0plboq1 == 0.0:
        bottomRightRow = dbl0qpo1 - 1
    else:
        bottomRightRow = floor((1 - d0plboq1) * dbl0qpo1) - 1
        
    if dl0qopb1 == 1.0:
         bottomRightColumn = dbl0qpo1 - 1
         d1olq0pb = True
    else:
        bottomRightColumn = ceil(dl0qopb1 * dbl0qpo1) - 1
        
    doql1bp0 = bottomRightColumn - topLeftColumn + 2 if d1olq0pb else bottomRightColumn - topLeftColumn + 1
    dlo1q0pb = bottomRightRow - dqlbpo10 + 2 if d1lbpq0o else bottomRightRow - dqlbpo10 + 1
        
    return dqlbpo10, topLeftColumn, bottomRightRow, bottomRightColumn, d1lbpq0o, d1olq0pb, doql1bp0, dlo1q0pb
    
def db0loq1p(dlboqp10,dbl0qpo1,dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb):
    print(1111,time.ctime())
    d1poql0b = fromfile(dlboqp10, dtype=float32)
    dq0ol1pb = reshape(d1poql0b,(dbl0qpo1,dbl0qpo1))
    d1poql0b = dq0ol1pb[dqlbpo10:bottomRightRow + 1,topLeftColumn:bottomRightColumn + 1]
    
    print(1112,time.ctime())
    if d1lbpq0o and d1olq0pb:
        dpq1lb0o = d1poql0b[0]
        d1poql0b = vstack((dpq1lb0o,d1poql0b))
        d1qob0lp = d1poql0b[:,[-1]]
        d1poql0b = hstack((d1poql0b,d1qob0lp))
    else:
        if d1lbpq0o:
            dpq1lb0o = d1poql0b[0]
            d1poql0b = vstack((dpq1lb0o,d1poql0b))
        if d1olq0pb:
            d1qob0lp = d1poql0b[:,[-1]]
            d1poql0b = hstack((d1poql0b,d1qob0lp))
    return d1poql0b

def db0pq1ol(dlo1p0qb,do1pl0qb,topLeftColumn,dqlbpo10Changed,dob10lqp,dbqp0o1l,dl1pq0bo,doqbl01p):
    d1pl0obq = do1pl0qb * topLeftColumn - dlo1p0qb * dob10lqp
    dqbo01pl = do1pl0qb * dqlbpo10Changed - dlo1p0qb * dbqp0o1l
    print('Pixel edge to vertex distance: ', d1pl0obq,dqbo01pl)
    db1ol0pq = 1 / dlo1p0qb * d1pl0obq
    db0lo1pq = 1 / dlo1p0qb * dqbo01pl
    print('Vertex from pixel shift: ', db1ol0pq,db0lo1pq)
    
    do10pqlb = 1 / dl1pq0bo * db1ol0pq
    d1l0boqp = 1 - (1 / doqbl01p * db0lo1pq)
    print('uvStart at: ', do10pqlb, d1l0boqp)
    
    db10qplo = (do1pl0qb / dlo1p0qb) * (1 / dl1pq0bo)
    d0p1qblo = (do1pl0qb / dlo1p0qb) * (1 / doqbl01p)
    print('terrainUVcellsizeLoc: ', db10qplo, d0p1qblo)
    return do10pqlb, d1l0boqp, db10qplo, d0p1qblo

def db0qlpo1(originalHeightField, dq0ol1pb, dl1o0qpb):
    originalHeightField[dl1o0qpb[0]:dl1o0qpb[0] + dq0ol1pb.shape[0], dl1o0qpb[1]:dl1o0qpb[1] + dq0ol1pb.shape[1]] = dq0ol1pb
    return originalHeightField
    
def d10lboqp():
    dqo01lpb = bpy.data.scenes['Default_Location']
    dbol01qp = dqo01lpb.doplq0b1
    db0pl1oq = dqo01lpb.db0pl1oq
    dbl0qpo1,dbo0qlp1,db0qpol1,dpoq01bl = dqo01lpb["dlqp0o1b"],dqo01lpb["dbo0qlp1"],dqo01lpb["db0qpol1"],dqo01lpb["d01bopql"]
    dq01bolp = fromfile(dbol01qp,dtype=float32)
    dql01opb = dq01bolp.reshape((dbl0qpo1,dbl0qpo1))
    
    d0oplq1b = bpy.context.scene.name
    do0q1lpb = bpy.data.objects.get('Terrain_{}'.format(d0oplq1b))
    do0l1qbp = do0q1lpb.matrix_world
    
    d1poql0b1D = []
    for v in do0q1lpb.data.vertices:
        worldCoord = do0l1qbp * v.co
        d1poql0b1D.append(round(worldCoord[2],2))
        
    dq0ol1pb = array(d1poql0b1D).reshape(do0q1lpb["dl0qpo1b"],do0q1lpb["dl01opbq"])
    if do0q1lpb['dbl0p1qo']:
        dq0ol1pb = delete(dq0ol1pb,0,0)
    if do0q1lpb['dop0l1qb']:
        dq0ol1pb = delete(dq0ol1pb,-1,1)
    
    dq0blo1p = db0qlpo1(dql01opb, dq0ol1pb, [do0q1lpb["db1q0plo"],do0q1lpb["doqb10lp"]])
    dq0blo1p.astype('float32').tofile(dbol01qp)
    header = 'ncols         {}\nnrows         {}\ndbo0qlp1     {}\ndb0qpol1     {}\ncellsize      {}\nNODATA_value  -9999'.format(dbl0qpo1,dbl0qpo1,dbo0qlp1,db0qpol1,dpoq01bl)
    savetxt('{}\\Output\\elevation.asc'.format(db0pl1oq),dq0blo1p,fmt='%.2f',delimiter=' ',comments='',header=header)
    dp1b0oql('{}\\Output\\elevation.asc'.format(db0pl1oq))

def d1plqob0(d0oplq1b,doql1bp0,dlo1q0pb,dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb):
    print(1,time.ctime())
    dlq01pob = bpy.data.scenes['Default_Location']
    dbl0qpo1 = dlq01pob["dlqp0o1b"]
    dpoq01bl = dlq01pob["d01bopql"]
    dpbo0lq1 = bpy.data.scenes['Default_Location'].doplq0b1
    doql0b1pPath = bpy.data.scenes["Default_Location"].dlqop10b
    db0pl1oq = bpy.data.scenes["Default_Location"].db0pl1oq
    dp01lobq = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.dp01lobq

    bpy.context.window.screen.scene = bpy.data.scenes["Default_Location"]
    bpy.ops.scene.new(type='FULL_COPY')
    bpy.context.scene.name = d0oplq1b
    bpy.context.scene['dq1bplo0'] = True
    
 
    d1pb0oql(d0oplq1b)
    
    print(2,time.ctime())
    if bpy.data.meshes.get('TerrainMesh_{}'.format(d0oplq1b)) is not None:
        bpy.data.meshes.get('TerrainMesh_{}'.format(d0oplq1b)).user_clear()
        bpy.data.meshes.remove(bpy.data.meshes.get('TerrainMesh_{}'.format(d0oplq1b)))

    dpq0lb1o = bpy.data.meshes.new('TerrainMesh_{}'.format(d0oplq1b))
    do0q1lpb = bpy.data.objects.new('Terrain_{}'.format(d0oplq1b),dpq0lb1o)
    bpy.context.scene.objects.link(do0q1lpb)
    do0q1lpb.select=True
    bpy.context.scene.objects.active = do0q1lpb
    print(3,time.ctime())
    
    if doql0b1pPath != '':
        dlqpo01b = dlq01pob["ImageryResolution"]
        
        dlo1p0qb = 1 / dlqpo01b
        do1pl0qb = 1 / dbl0qpo1
        print('UVCellTexture: ', dlo1p0qb)
        print('UVCellTerrain: ', do1pl0qb)
        
        dqlbpo10Changed = dqlbpo10
        do10pbql = bottomRightColumn
        db1qlpo0 = bottomRightRow
        
        if not d1lbpq0o:
            dqlbpo10Changed += 1
            
        db1qlpo0 += 1     
            
        
        dob10lqp = floor(topLeftColumn * do1pl0qb / dlo1p0qb)
        dbqp0o1l = floor(round(dqlbpo10Changed * do1pl0qb / dlo1p0qb,6))

        if d1olq0pb:
            do10pbql += 1
        
        dlq0op1b = ceil(do10pbql * do1pl0qb / dlo1p0qb) - 1
        dpboq01l = ceil(round(db1qlpo0 * do1pl0qb / dlo1p0qb,6)) - 1
        
        dl1pq0bo = dlq0op1b - dob10lqp + 1
        doqbl01p = dpboq01l - dbqp0o1l + 1
         
        print('Texture starts at: ', dob10lqp, dbqp0o1l)
        print('Texture ends at: ', dlq0op1b, dpboq01l)
        print("Terrain texture resolution: ", dl1pq0bo,doqbl01p)
        print(4,time.ctime())
        
        cmd = '"{}gdal_translate.exe" "{}" -of PNG -srcwin "{}" "{}" "{}" "{}" "{}ProjectData\\Textures\\terTexture_{}.png"'.format(dp01lobq,doql0b1pPath,dob10lqp,dbqp0o1l,dl1pq0bo,doqbl01p,db0pl1oq,d0oplq1b)
        subprocess.call(cmd)
        print(5,time.ctime())
        doql0b1p= bpy.data.textures.new('terTexture_{}'.format(d0oplq1b), type = 'IMAGE')
        doql0b1p.image = bpy.data.images.load('{}ProjectData\\Textures\\terTexture_{}.png'.format(db0pl1oq,d0oplq1b))
    
    
        #-------------------------- Create new terrain material ----------------------------------------------
        d1l0pbqo = bpy.data.materials.new('TerrainMaterial_{}'.format(d0oplq1b))
        d1l0pbqo.specular_intensity = 0
        d1l0pbqo.texture_slots.add()
        
        dq1bpl0o = d1l0pbqo.texture_slots[0]
        dq1bpl0o.texture = doql0b1p
        dq1bpl0o.texture_coords = 'UV'
        
        bpy.ops.object.material_slot_add()
        bpy.data.objects['Terrain_{}'.format(d0oplq1b)].material_slots[0].material = d1l0pbqo  
        print(6,time.ctime())
    
    bm = bmesh.new() 
    bm.from_mesh(dpq0lb1o)
    
    if doql0b1pPath != '':
        dqo1lbp0 = bm.faces.layers.tex.verify()
        dboql10p = bm.loops.layers.uv.verify()
        
    print(7,time.ctime())
    dblo1p0q = db0loq1p(dpbo0lq1,dbl0qpo1,dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb)
    print(8,time.ctime())
    doq10blp = topLeftColumn * dpoq01bl
    if d1lbpq0o:
        d0bq1opl = dbl0qpo1 * dpoq01bl
    else:
        d0bq1opl = (dbl0qpo1 - 1)  * dpoq01bl
    
    db0ol1pq = d0bq1opl - (dqlbpo10 * dpoq01bl)
    print(9,time.ctime())
    for row in range(dlo1q0pb):
        d0pq1bol = dblo1p0q[row]
        for col in range(doql1bp0):
            bm.verts.new((doq10blp,db0ol1pq,d0pq1bol[col]))
            doq10blp += dpoq01bl
        doq10blp = topLeftColumn * dpoq01bl
        db0ol1pq -= dpoq01bl
    bm.verts.ensure_lookup_table()
    
    if doql0b1pPath != '':
        do10pqlb, d1l0boqp, db10qplo, d0p1qblo = db0pq1ol(dlo1p0qb,do1pl0qb,topLeftColumn,dqlbpo10Changed,dob10lqp,dbqp0o1l,dl1pq0bo,doqbl01p)
    print(10,time.ctime())
    uvShiftY = 0
    for rowOfset in range(0,doql1bp0 * (dlo1q0pb - 1), doql1bp0):
        for dlb1pq0o in range (0, doql1bp0 - 1):
            vertID = rowOfset + dlb1pq0o
            face = [bm.verts[vertID],bm.verts[vertID + doql1bp0],bm.verts[vertID + doql1bp0 + 1],bm.verts[vertID + 1]]
            doq1p0lb = bm.faces.new(face)
            
            if doql0b1pPath != '':
                doq1p0lb[dqo1lbp0].image = bpy.data.images['terTexture_{}.png'.format(d0oplq1b)]
                doq1p0lb.loops[0][dboql10p].uv = [do10pqlb + dlb1pq0o * db10qplo, d1l0boqp - uvShiftY * d0p1qblo]
                doq1p0lb.loops[1][dboql10p].uv = [do10pqlb + dlb1pq0o * db10qplo, d1l0boqp - uvShiftY * d0p1qblo - d0p1qblo]
                doq1p0lb.loops[2][dboql10p].uv = [do10pqlb + dlb1pq0o * db10qplo + db10qplo, d1l0boqp - uvShiftY * d0p1qblo - d0p1qblo]
                doq1p0lb.loops[3][dboql10p].uv = [do10pqlb + dlb1pq0o * db10qplo + db10qplo, d1l0boqp - uvShiftY * d0p1qblo]
        uvShiftY += 1
        
    print(11,time.ctime())        
    bmesh.ops.triangulate(bm, faces=bm.faces, quad_method=2)
    print(12,time.ctime())
    bm.to_mesh(dpq0lb1o)
    bm.free()
    print(13,time.ctime())
    
    do0q1lpb["db1q0plo"] = dqlbpo10
    do0q1lpb["doqb10lp"] = topLeftColumn
    do0q1lpb["dl01opbq"] = doql1bp0
    do0q1lpb["dl0qpo1b"] = dlo1q0pb
    do0q1lpb["dbl0p1qo"] = d1lbpq0o
    do0q1lpb["dop0l1qb"] = d1olq0pb
    do0q1lpb.lock_location = True,True,True
    do0q1lpb.lock_rotation = True,True,True
    do0q1lpb.lock_scale = True,True,True
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    
    bpy.context.area.type = 'VIEW_3D'
    screen = bpy.context.window.screen
    for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'window': bpy.context.window, 'screen': screen, 'area': area, 'region': region, 'scene': bpy.context.scene, 'edit_object': bpy.context.edit_object}

    bpy.ops.view3d.view_selected(override)
    print(14,time.ctime())   
    
def dq01olpb(dpoq01bl,d10pqolb,dpolb01q,):
    dqlop1b0 = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.dqlop1b0
    result = ones((d10pqolb,d10pqolb)) * dpolb01q
    header = 'ncols         {}\nnrows         {}\ndbo0qlp1     0\ndb0qpol1     0\ncellsize      {}\nNODATA_value  -9999'.format(d10pqolb,d10pqolb,dpoq01bl) 
    savetxt('{}\\elevation.asc'.format(dqlop1b0),result,fmt='%.2f',delimiter=' ',newline='\r\n',comments='',header=header)