import bpy,bgl,blf,bmesh
import subprocess,os,time, struct
from shutil import copy,rmtree
from math import floor, isnan, ceil
from numpy import genfromtxt,vstack,hstack,array,savetxt,delete,ones,flipud,empty,fromfile,float16,float32,reshape
from mathutils import Vector, Matrix

def doblqp01(self, context):
    dl10qobp = bpy.data.scenes["Default_Location"].doqbpl10
    
    d0oqpbl1 = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.d0oqpbl1
    dq1o0pbl = bpy.data.scenes["Default_Location"].dq1o0pbl
    dpboql01 = 'Project_{}'.format(dq1o0pbl.split('\\')[-2])
    dq01blpo = d0o1blpq(d0oqpbl1,dl10qobp)
    
    if os.path.exists('{}ProjectData\\Textures\\previewSatTex.png'.format(dq1o0pbl)):
        os.remove('{}ProjectData\\Textures\\previewSatTex.png'.format(dq1o0pbl))
    
    if dq01blpo < 5000:
        copy(bpy.context.scene.doqbpl10,'{}ProjectData\\Textures\\'.format(dq1o0pbl))
        dq01lbop = bpy.context.scene.doqbpl10.split('\\')[-1]
        os.rename('{}ProjectData\\Textures\\{}'.format(dq1o0pbl,dq01lbop),'{}ProjectData\\Textures\\previewSatTex.png'.format(dq1o0pbl))
    else:
        cmd = '"{}gdal_translate.exe" "{}" -of PNG -outsize 5000 5000 "{}ProjectData\Textures\previewSatTex.png"'.format(d0oqpbl1,dl10qobp,dq1o0pbl)
        subprocess.call(cmd)
    if bpy.data.images.get('previewSatTex.png') is None:
        bpy.data.images.load('{}ProjectData\\Textures\\previewSatTex.png'.format(dq1o0pbl))
        bpy.data.images['previewSatTex.png'].use_fake_user = True
    else:
        bpy.data.images['previewSatTex.png'].reload()
        
    do10pqlb = bpy.data.scenes['Default_Location']    
    do10pqlb["ImageryResolution"] = dq01blpo
    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(dq1o0pbl,dpboql01))
    
def d1opl0qb(self, context):
    
    
    doql10pb = bpy.data.scenes["Default_Location"].d0bq1olp
    
    d0oqpbl1 = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.d0oqpbl1
    dq1o0pbl = bpy.data.scenes["Default_Location"].dq1o0pbl
    dpboql01 = 'Project_{}'.format(dq1o0pbl.split('\\')[-2])
    dqlpb1o0 = d0bqop1l(doql10pb)
    d01lbpqo = genfromtxt(doql10pb, delimiter=' ', skip_header=6)
    dpq10lbo = '{}ProjectData\\Textures\\elevation.bLTe'.format(dq1o0pbl)
    d01lbpqo.astype('float32').tofile(dpq10lbo)

    print('Elevation converted')
    
    db0opq1l(doql10pb)
    
    do10pqlb = bpy.data.scenes['Default_Location']
    do10pqlb["d0l1qpbo"] = dqlpb1o0[0]
    do10pqlb["dblq0po1"] = dqlpb1o0[1]
    do10pqlb["d0l1obqp"] = dqlpb1o0[2]
    do10pqlb["dqlp0o1b"] = dqlpb1o0[3]
    bpy.data.scenes['Default_Location'].dlq1bpo0 = dpq10lbo

    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(dq1o0pbl,dpboql01))
    
def db0opq1l(doql10pb):
    d0oqpbl1 = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.d0oqpbl1
    dq1o0pbl = bpy.data.scenes["Default_Location"].dq1o0pbl
    
    cmd = '"{}gdaldem.exe" hillshade -az 45 -z 1.3 "{}" "{}ProjectData\Textures\previewTerTex.tif"'.format(d0oqpbl1,doql10pb,dq1o0pbl)
    subprocess.call(cmd)
    
    if bpy.data.images.get('previewTerTex.tif') is None:
        bpy.data.images.load('{}ProjectData\\Textures\\previewTerTex.tif'.format(dq1o0pbl))
        bpy.data.images['previewTerTex.tif'].use_fake_user = True
    else:
        bpy.data.images['previewTerTex.tif'].reload()


def dpobq0l1():
    import addon_utils
    
    addons = [mod for mod in addon_utils.modules(refresh=False)]

    for mod in addons:
        if mod.__name__ == "bLandscapeTools":
            dlobp10q = mod.__file__
            pass
           
    dlpq1b0o = dlobp10q[:-12]
    dq01plob = '{}\\data'.format(dlpq1b0o)
    
    return dlobp10q,dlpq1b0o,dq01plob
     
def d0o1blpq(d0oqpbl1,dl10qobp):
    ext = dl10qobp.split('.')[-1]
    if ext == 'png':
        dq1p0bol = 'pgw'
    if ext == 'tif' or ext == 'tiff':
        dq1p0bol = 'tfw'
    if ext == 'jpg' or ext == 'jpeg':
        dq1p0bol = 'jgw'
        
    cmd = '{}gdalinfo.exe "{}"'.format(d0oqpbl1,dl10qobp)
    print(cmd)
    dl0bo1pq = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    
    for i in range(0,10):
        line = str(dl0bo1pq.stdout.readline()).rstrip('\\r\\n\'')
        if line.split(' ')[0][2:] == 'Size':
            info = int(line.split(' ')[3])

    return info
    
def d0bqop1l(path):
    info = []
    f = open(path,"r")
    line = f.readline().split(" ")
    for i in range(5):
        info.append( line[-1])
        line = f.readline().split(" ")
    f.close()
    ncols = int(info[0])
    d0op1bql = float(info[4])
    x = float(info[2])
    y = float(info[3])
    return ncols,x,y,d0op1bql

    
    

def dbp0oql1(dbqp1lo0):
    bpy.ops.object.lamp_add(type='HEMI')
    hemi = bpy.context.object
    hemi.hide = True
    hemi.name = "Hemi_" + dbqp1lo0

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
    
            
def dlq0pob1():
    dq01plob = dpobq0l1()[2]
    dq1o0pbl = bpy.context.scene.dq1o0pbl
    dpboql01 = 'Project_{}'.format(dq1o0pbl.split('\\')[-2])

        
  
    
    bpy.ops.wm.open_mainfile(filepath='{}\\dummy.blend'.format(dq01plob))

    bpy.context.scene.db0opql1 = True
    bpy.context.scene.dq1o0pbl = dq1o0pbl
    bpy.context.scene['dolqp1b0'] = False
    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(bpy.context.scene.dq1o0pbl,dpboql01),copy=False)

    if not os.path.exists(bpy.context.scene.dq1o0pbl + 'ProjectData'):
	    os.makedirs(bpy.context.scene.dq1o0pbl + 'ProjectData')
    if not os.path.exists(bpy.context.scene.dq1o0pbl + 'ProjectData\\Textures'):
	    os.makedirs(bpy.context.scene.dq1o0pbl + 'ProjectData\\Textures')
    else:
        rmtree(bpy.context.scene.dq1o0pbl + 'ProjectData\\Textures')
        os.makedirs(bpy.context.scene.dq1o0pbl + 'ProjectData\\Textures')
    if not os.path.exists(bpy.context.scene.dq1o0pbl + 'Output'):
	    os.makedirs(bpy.context.scene.dq1o0pbl + 'Output')

        
def d1lp0bqo():
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
    bpy.ops.view2d.d10bqpol(override,'INVOKE_DEFAULT')

def dobql01p(self,context):
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
    blf.draw(font_id, 'Version: Bushlurker')
    
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    blf.disable(0, blf.SHADOW)
    
def d1b0qlop(self, context):
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
        bgl.glVertex2i(0, self.dpq1b0ol)
        bgl.glVertex2i(width, self.dpq1b0ol)
        bgl.glVertex2i(self.dbplo1q0, 0)
        bgl.glVertex2i(self.dbplo1q0, height)
        bgl.glEnd()
        
    else:
        d1p0lboq = self.dpoqbl01
        d1bpolq0 = list(bpy.context.region.view2d.view_to_region(d1p0lboq[0],d1p0lboq[1],clip=False))
        
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.dbplo1q0, self.dpq1b0ol)
        bgl.glVertex2i(d1bpolq0[0], self.dpq1b0ol)
        bgl.glVertex2i(d1bpolq0[0], d1bpolq0[1])
        bgl.glVertex2i(self.dbplo1q0, d1bpolq0[1])
        bgl.glEnd()

        bgl.glColor4f(0.0, 1.0, 0.0, 0.3)
        bgl.glBegin(bgl.GL_POLYGON)
        bgl.glVertex2i(self.dbplo1q0, self.dpq1b0ol)
        bgl.glVertex2i(d1bpolq0[0], self.dpq1b0ol)
        bgl.glVertex2i(d1bpolq0[0], d1bpolq0[1])
        bgl.glVertex2i(self.dbplo1q0, d1bpolq0[1])
        bgl.glEnd()
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.position(font_id, self.dbplo1q0 - 210, self.dpq1b0ol - 15, 0)
        blf.draw(font_id, self.dql1pb0o)
        blf.position(font_id, self.dbplo1q0 - 210, self.dpq1b0ol - 30, 0)
        blf.draw(font_id, self.dbpql1o0)
        blf.position(font_id, self.dbplo1q0 - 210, self.dpq1b0ol - 45, 0)
        blf.draw(font_id, self.d0bpqlo1)      

    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    bgl.glDisable(bgl.GL_LINE_STIPPLE)
    blf.disable(0, blf.SHADOW)
          
def dop1lbq0(dbp1olq0,dblq0o1p):
    dl0q1opb, dopbql01, d0lb1poq, dbq0pl1o = dbp1olq0[0], dbp1olq0[1], dblq0o1p[0], dblq0o1p[1]

    if d0lb1poq < 0:
        d0lb1poq = 0.0
    elif d0lb1poq > 1:
        d0lb1poq = 1.0
        
    if dbq0pl1o < 0:
        dbq0pl1o = 0.0
    elif dbq0pl1o > 1:
        dbq0pl1o = 1.0

    if dl0q1opb < 0:
        dl0q1opb = 0.0
    elif dl0q1opb > 1:
        dl0q1opb = 1.0
    
    if dopbql01 < 0:
        dopbql01 = 0.0
    elif dopbql01 > 1:
        dopbql01 = 1.0

    if d0lb1poq < dl0q1opb:
        dqol1bp0 = d0lb1poq
        d1loq0pb = dl0q1opb
    else:
        dqol1bp0 = dl0q1opb
        d1loq0pb = d0lb1poq

    if dbq0pl1o > dopbql01:
        d0q1olpb = dbq0pl1o
        dlq01bop = dopbql01
    else:
        d0q1olpb = dopbql01
        dlq01bop = dbq0pl1o
  
    return d0q1olpb,dqol1bp0,dlq01bop,d1loq0pb
    
def dblqo1p0(d0op1bql,dloq0b1p,d0q1olpb,dqol1bp0,dlq01bop,d1loq0pb):
    dpoql0b1 = False
    db1oql0p = False
    
    if isnan(d0q1olpb):
        d0q1olpb = 0.0
    if isnan(dqol1bp0):
        dqol1bp0 = 0.0

    if d0q1olpb == 1.0:
        d0p1oqbl = 0
        dpoql0b1 = True
    else:
        d0p1oqbl = floor((1 - d0q1olpb) * dloq0b1p)
        
    topLeftColumn = ceil(dqol1bp0 * dloq0b1p)
    
    if dlq01bop == 0.0:
        bottomRightRow = dloq0b1p - 1
    else:
        bottomRightRow = floor((1 - dlq01bop) * dloq0b1p) - 1
        
    if d1loq0pb == 1.0:
         bottomRightColumn = dloq0b1p - 1
         db1oql0p = True
    else:
        bottomRightColumn = ceil(d1loq0pb * dloq0b1p) - 1
        
    dq0lbp1o = bottomRightColumn - topLeftColumn + 2 if db1oql0p else bottomRightColumn - topLeftColumn + 1
    dq10obpl = bottomRightRow - d0p1oqbl + 2 if dpoql0b1 else bottomRightRow - d0p1oqbl + 1
        
    return d0p1oqbl, topLeftColumn, bottomRightRow, bottomRightColumn, dpoql0b1, db1oql0p, dq0lbp1o, dq10obpl
    
def d1lob0qp(dqb1p0lo,dloq0b1p,d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p):
    print(1111,time.ctime())
    db01lopq = fromfile(dqb1p0lo, dtype=float32)
    doq0p1lb = reshape(db01lopq,(dloq0b1p,dloq0b1p))
    db01lopq = doq0p1lb[d0p1oqbl:bottomRightRow + 1,topLeftColumn:bottomRightColumn + 1]
    
    print(1112,time.ctime())
    if dpoql0b1 and db1oql0p:
        d0oqp1lb = db01lopq[0]
        db01lopq = vstack((d0oqp1lb,db01lopq))
        dlq0bpo1 = db01lopq[:,[-1]]
        db01lopq = hstack((db01lopq,dlq0bpo1))
    else:
        if dpoql0b1:
            d0oqp1lb = db01lopq[0]
            db01lopq = vstack((d0oqp1lb,db01lopq))
        if db1oql0p:
            dlq0bpo1 = db01lopq[:,[-1]]
            db01lopq = hstack((db01lopq,dlq0bpo1))
    return db01lopq

def do0qbpl1(d0bqlp1o,dpqbl0o1,topLeftColumn,d1olb0pq,dq0bpol1,d10bqopl,dbo01plq,dp0qlbo1):
    dl0p1obq = dpqbl0o1 * topLeftColumn - d0bqlp1o * dq0bpol1
    dpo0b1lq = dpqbl0o1 * d1olb0pq - d0bqlp1o * d10bqopl
    print('Pixel edge to vertex distance: ', dl0p1obq,dpo0b1lq)
    doql0bp1 = 1 / d0bqlp1o * dl0p1obq
    dql1opb0 = 1 / d0bqlp1o * dpo0b1lq
    print('Vertex from pixel shift: ', doql0bp1,dql1opb0)
    
    dpoqb01l = 1 / dbo01plq * doql0bp1
    dqo10plb = 1 - (1 / dp0qlbo1 * dql1opb0)
    print('uvStart at: ', dpoqb01l, dqo10plb)
    
    dobp10lq = (dpqbl0o1 / d0bqlp1o) * (1 / dbo01plq)
    dlp01oqb = (dpqbl0o1 / d0bqlp1o) * (1 / dp0qlbo1)
    print('terrainUVcellsizeLoc: ', dobp10lq, dlp01oqb)
    return dpoqb01l, dqo10plb, dobp10lq, dlp01oqb

def dl0ob1pq(originalHeightField, doq0p1lb, d0l1pboq):
    originalHeightField[d0l1pboq[0]:d0l1pboq[0] + doq0p1lb.shape[0], d0l1pboq[1]:d0l1pboq[1] + doq0p1lb.shape[1]] = doq0p1lb
    return originalHeightField
    
def d1lq0opb():
    dl10qbpo = bpy.data.scenes['Default_Location']
    dob0q1pl = dl10qbpo.dlq1bpo0
    dq1o0pbl = dl10qbpo.dq1o0pbl
    dloq0b1p,dblq0po1,d0l1obqp,d0op1bql = dl10qbpo["d0l1qpbo"],dl10qbpo["dblq0po1"],dl10qbpo["d0l1obqp"],dl10qbpo["dqlp0o1b"]
    dopbl1q0 = fromfile(dob0q1pl,dtype=float32)
    d1qlpb0o = dopbl1q0.reshape((dloq0b1p,dloq0b1p))
    
    dbqp1lo0 = bpy.context.scene.name
    d0bolq1p = bpy.data.objects.get('Terrain_{}'.format(dbqp1lo0))
    d0o1qblp = d0bolq1p.matrix_world
    
    db01lopq1D = []
    for v in d0bolq1p.data.vertices:
        worldCoord = d0o1qblp * v.co
        db01lopq1D.append(round(worldCoord[2],2))
        
    doq0p1lb = array(db01lopq1D).reshape(d0bolq1p["d1qol0pb"],d0bolq1p["d1olqp0b"])
    if d0bolq1p['dblo0qp1']:
        doq0p1lb = delete(doq0p1lb,0,0)
    if d0bolq1p['do0q1plb']:
        doq0p1lb = delete(doq0p1lb,-1,1)
    
    dbqo0pl1 = dl0ob1pq(d1qlpb0o, doq0p1lb, [d0bolq1p["dobp1l0q"],d0bolq1p["dlob1q0p"]])
    dbqo0pl1.astype('float32').tofile(dob0q1pl)
    header = 'ncols         {}\nnrows         {}\ndblq0po1     {}\nd0l1obqp     {}\ncellsize      {}\nNODATA_value  -9999'.format(dloq0b1p,dloq0b1p,dblq0po1,d0l1obqp,d0op1bql)
    savetxt('{}\\Output\\elevation.asc'.format(dq1o0pbl),dbqo0pl1,fmt='%.2f',delimiter=' ',comments='',header=header)
    db0opq1l('{}\\Output\\elevation.asc'.format(dq1o0pbl))

def do0blp1q(dbqp1lo0,dq0lbp1o,dq10obpl,d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p):
    print(1,time.ctime())
    d0o1qlbp = bpy.data.scenes['Default_Location']
    dloq0b1p = d0o1qlbp["d0l1qpbo"]
    d0op1bql = d0o1qlbp["dqlp0o1b"]
    db1lq0op = bpy.data.scenes['Default_Location'].dlq1bpo0
    dl10qobp = bpy.data.scenes["Default_Location"].doqbpl10
    dq1o0pbl = bpy.data.scenes["Default_Location"].dq1o0pbl
    d0oqpbl1 = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.d0oqpbl1

    bpy.context.window.screen.scene = bpy.data.scenes["Default_Location"]
    bpy.ops.scene.new(type='FULL_COPY')
    bpy.context.scene.name = dbqp1lo0
    bpy.context.scene['dolqp1b0'] = True
    
 
    dbp0oql1(dbqp1lo0)
    
    print(2,time.ctime())
    if bpy.data.meshes.get('TerrainMesh_{}'.format(dbqp1lo0)) is not None:
        bpy.data.meshes.get('TerrainMesh_{}'.format(dbqp1lo0)).user_clear()
        bpy.data.meshes.remove(bpy.data.meshes.get('TerrainMesh_{}'.format(dbqp1lo0)))

    dlpqbo10 = bpy.data.meshes.new('TerrainMesh_{}'.format(dbqp1lo0))
    d0bolq1p = bpy.data.objects.new('Terrain_{}'.format(dbqp1lo0),dlpqbo10)
    bpy.context.scene.objects.link(d0bolq1p)
    d0bolq1p.select=True
    bpy.context.scene.objects.active = d0bolq1p
    print(3,time.ctime())
    
    if dl10qobp != '':
        dp10lqob = d0o1qlbp["ImageryResolution"]
        
        d0bqlp1o = 1 / dp10lqob
        dpqbl0o1 = 1 / dloq0b1p
        print('UVCellTexture: ', d0bqlp1o)
        print('UVCellTerrain: ', dpqbl0o1)
        
        d1olb0pq = d0p1oqbl
        dlbp01qo = bottomRightColumn
        d0obqpl1 = bottomRightRow
        
        if not dpoql0b1:
            d1olb0pq += 1
            
        d0obqpl1 += 1     
            
        
        dq0bpol1 = floor(topLeftColumn * dpqbl0o1 / d0bqlp1o)
        d10bqopl = floor(round(d1olb0pq * dpqbl0o1 / d0bqlp1o,6))

        if db1oql0p:
            dlbp01qo += 1
        
        d0plq1bo = ceil(dlbp01qo * dpqbl0o1 / d0bqlp1o) - 1
        dp1lqbo0 = ceil(round(d0obqpl1 * dpqbl0o1 / d0bqlp1o,6)) - 1
        
        dbo01plq = d0plq1bo - dq0bpol1 + 1
        dp0qlbo1 = dp1lqbo0 - d10bqopl + 1
         
        print('Texture starts at: ', dq0bpol1, d10bqopl)
        print('Texture ends at: ', d0plq1bo, dp1lqbo0)
        print("Terrain texture resolution: ", dbo01plq,dp0qlbo1)
        print(4,time.ctime())
        
        cmd = '"{}gdal_translate.exe" "{}" -of PNG -srcwin "{}" "{}" "{}" "{}" "{}ProjectData\\Textures\\terTexture_{}.png"'.format(d0oqpbl1,dl10qobp,dq0bpol1,d10bqopl,dbo01plq,dp0qlbo1,dq1o0pbl,dbqp1lo0)
        subprocess.call(cmd)
        print(5,time.ctime())
        dl1q0bop= bpy.data.textures.new('terTexture_{}'.format(dbqp1lo0), type = 'IMAGE')
        dl1q0bop.image = bpy.data.images.load('{}ProjectData\\Textures\\terTexture_{}.png'.format(dq1o0pbl,dbqp1lo0))
    
    
        #-------------------------- Create new terrain material ----------------------------------------------
        d1qlbpo0 = bpy.data.materials.new('TerrainMaterial_{}'.format(dbqp1lo0))
        d1qlbpo0.specular_intensity = 0
        d1qlbpo0.texture_slots.add()
        
        d0olq1bp = d1qlbpo0.texture_slots[0]
        d0olq1bp.texture = dl1q0bop
        d0olq1bp.texture_coords = 'UV'
        
        bpy.ops.object.material_slot_add()
        bpy.data.objects['Terrain_{}'.format(dbqp1lo0)].material_slots[0].material = d1qlbpo0  
        print(6,time.ctime())
    
    bm = bmesh.new() 
    bm.from_mesh(dlpqbo10)
    
    if dl10qobp != '':
        dbp01loq = bm.faces.layers.tex.verify()
        dlbo0pq1 = bm.loops.layers.uv.verify()
        
    print(7,time.ctime())
    dlbqp0o1 = d1lob0qp(db1lq0op,dloq0b1p,d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p)
    print(8,time.ctime())
    dqbp1ol0 = topLeftColumn * d0op1bql
    if dpoql0b1:
        do0l1pbq = dloq0b1p * d0op1bql
    else:
        do0l1pbq = (dloq0b1p - 1)  * d0op1bql
    
    do0lqpb1 = do0l1pbq - (d0p1oqbl * d0op1bql)
    print(9,time.ctime())
    for row in range(dq10obpl):
        dp0q1lbo = dlbqp0o1[row]
        for col in range(dq0lbp1o):
            bm.verts.new((dqbp1ol0,do0lqpb1,dp0q1lbo[col]))
            dqbp1ol0 += d0op1bql
        dqbp1ol0 = topLeftColumn * d0op1bql
        do0lqpb1 -= d0op1bql
    bm.verts.ensure_lookup_table()
    
    if dl10qobp != '':
        dpoqb01l, dqo10plb, dobp10lq, dlp01oqb = do0qbpl1(d0bqlp1o,dpqbl0o1,topLeftColumn,d1olb0pq,dq0bpol1,d10bqopl,dbo01plq,dp0qlbo1)
    print(10,time.ctime())
    uvShiftY = 0
    for rowOfset in range(0,dq0lbp1o * (dq10obpl - 1), dq0lbp1o):
        for dlq1o0pb in range (0, dq0lbp1o - 1):
            vertID = rowOfset + dlq1o0pb
            face = [bm.verts[vertID],bm.verts[vertID + dq0lbp1o],bm.verts[vertID + dq0lbp1o + 1],bm.verts[vertID + 1]]
            d0bl1qpo = bm.faces.new(face)
            
            if dl10qobp != '':
                d0bl1qpo[dbp01loq].image = bpy.data.images['terTexture_{}.png'.format(dbqp1lo0)]
                d0bl1qpo.loops[0][dlbo0pq1].uv = [dpoqb01l + dlq1o0pb * dobp10lq, dqo10plb - uvShiftY * dlp01oqb]
                d0bl1qpo.loops[1][dlbo0pq1].uv = [dpoqb01l + dlq1o0pb * dobp10lq, dqo10plb - uvShiftY * dlp01oqb - dlp01oqb]
                d0bl1qpo.loops[2][dlbo0pq1].uv = [dpoqb01l + dlq1o0pb * dobp10lq + dobp10lq, dqo10plb - uvShiftY * dlp01oqb - dlp01oqb]
                d0bl1qpo.loops[3][dlbo0pq1].uv = [dpoqb01l + dlq1o0pb * dobp10lq + dobp10lq, dqo10plb - uvShiftY * dlp01oqb]
        uvShiftY += 1
        
    print(11,time.ctime())        
    bmesh.ops.triangulate(bm, faces=bm.faces, quad_method=2)
    print(12,time.ctime())
    bm.to_mesh(dlpqbo10)
    bm.free()
    print(13,time.ctime())
    
    d0bolq1p["dobp1l0q"] = d0p1oqbl
    d0bolq1p["dlob1q0p"] = topLeftColumn
    d0bolq1p["d1olqp0b"] = dq0lbp1o
    d0bolq1p["d1qol0pb"] = dq10obpl
    d0bolq1p["dblo0qp1"] = dpoql0b1
    d0bolq1p["do0q1plb"] = db1oql0p
    d0bolq1p.lock_location = True,True,True
    d0bolq1p.lock_rotation = True,True,True
    d0bolq1p.lock_scale = True,True,True
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
    
def dqbpol10(d0op1bql,d1qbp0lo,dpl0q1ob,):
    d1qo0pbl = bpy.context.user_preferences.addons["bLandscapeTools"].preferences.d1qo0pbl
    result = ones((d1qbp0lo,d1qbp0lo)) * dpl0q1ob
    header = 'ncols         {}\nnrows         {}\ndblq0po1     0\nd0l1obqp     0\ncellsize      {}\nNODATA_value  -9999'.format(d1qbp0lo,d1qbp0lo,d0op1bql) 
    savetxt('{}\\elevation.asc'.format(d1qo0pbl),result,fmt='%.2f',delimiter=' ',newline='\r\n',comments='',header=header)