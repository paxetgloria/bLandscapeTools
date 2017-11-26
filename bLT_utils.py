import bpy,bgl,blf,bmesh
import subprocess,os,time, struct
from shutil import copy,rmtree
from math import floor, isnan, ceil
from numpy import genfromtxt,vstack,hstack,array,savetxt,delete,ones,flipud,empty,fromfile,float16,float32,reshape
from mathutils import Vector, Matrix

def d0lbqop1(self, context):
    dl10pqob = bpy.data.scenes["Default_Location"].dp0l1boq
    
    dboqpl01 = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dboqpl01
    dblo0p1q = bpy.data.scenes["Default_Location"].dblo0p1q
    do1bq0pl = 'Project_{}'.format(dblo0p1q.split(os.path.sep)[-2])
    dbp1loq0 = dp0l1obq(dboqpl01,dl10pqob)
    
    if os.path.exists( os.path.join( dblo0p1q, "ProjectData", "Textures", "previewSatTex.png" ) ):
        os.remove( os.path.join(dblo0p1q, "ProjectData", "Textures", "previewSatTex.png") )
    
    if dbp1loq0 < 5000:
        copy(bpy.context.scene.dp0l1boq, os.path.join(dblo0p1q, "ProjectData", "Textures") )
        dq1olbp0 = bpy.context.scene.dp0l1boq.split(os.path.sep)[-1]
        os.rename( os.path.join(dblo0p1q, "ProjectData", "Textures", dq1olbp0) , os.path.join(dblo0p1q, "ProjectData", "Textures", "previewSatTex.png") )
    else:
        prev = os.path.join(dblo0p1q, "ProjectData", "Textures", "previewSatTex.png")
        if os.name == "posix":
            gdal = "gdal_translate"
            cmd = "{} {} -of PNG -outsize 5000 5000 '{}'".format(gdal, dl10pqob, prev)
        else:
            gdal = os.path.join(dboqpl01, "gdal_translate.exe" )
            cmd = '"{}" "{}" -of PNG -outsize 5000 5000 "{}"'.format(gdal,dl10pqob,prev)
        subprocess.call(cmd)
    if bpy.data.images.get('previewSatTex.png') is None:
        bpy.data.images.load( os.path.join(dblo0p1q, "ProjectData", "Textures", "previewSatTex.png") )
        bpy.data.images['previewSatTex.png'].use_fake_user = True
    else:
        bpy.data.images['previewSatTex.png'].reload()
    
    dpq1lb0o = bpy.data.scenes['Default_Location']    
    dpq1lb0o["ImageryResolution"] = dbp1loq0
    
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(dblo0p1q,"{}.blend".format(do1bq0pl)))

def d1qpbo0l(self, context):
    d1bplo0q = bpy.data.scenes["Default_Location"].dlp1qo0b
    
    dboqpl01 = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dboqpl01
    dblo0p1q = bpy.data.scenes["Default_Location"].dblo0p1q
    do1bq0pl = 'Project_{}'.format(dblo0p1q.split(os.path.sep)[-2])
    dl1p0oqb = dpbqo01l(d1bplo0q)
    dq1ob0lp = genfromtxt(d1bplo0q, delimiter=' ', skip_header=6)
    dq1bl0op = os.path.join(dblo0p1q, "ProjectData", "Textures", "elevation.bLTe")
    dq1ob0lp.astype('float32').tofile(dq1bl0op)
    
    print('Elevation converted')
    
    dqlbo0p1(d1bplo0q)
    
    dpq1lb0o = bpy.data.scenes['Default_Location']
    dpq1lb0o["db1lp0oq"] = dl1p0oqb[0]
    dpq1lb0o["xllcorner"] = dl1p0oqb[1]
    dpq1lb0o["yllcorner"] = dl1p0oqb[2]
    dpq1lb0o["dboqp1l0"] = dl1p0oqb[3]
    bpy.data.scenes['Default_Location'].d10bqlop = dq1bl0op
    
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(dblo0p1q,"{}.blend".format(do1bq0pl)))

def dqlbo0p1(d1bplo0q):
    dboqpl01 = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dboqpl01
    dblo0p1q = bpy.data.scenes["Default_Location"].dblo0p1q
    
    prev = os.path.join( dblo0p1q, "ProjectData", "Textures", "previewTerTex.tif")
    if os.name == "posix":
       gdal = "gdaldem"
       cmd = '{} hillshade -az 45 -z 1.3 "{}" "{}"'.format(gdal,d1bplo0q,prev)
    else:
       gdal = os.path.join(dboqpl01, "gdaldem.exe")
       cmd = '"{}" hillshade -az 45 -z 1.3 "{}" "{}"'.format(gdal,d1bplo0q,prev)
    subprocess.call(cmd)
    
    if bpy.data.images.get('previewTerTex.tif') is None:
        bpy.data.images.load( os.path.join(dblo0p1q, "ProjectData", "Textures", "previewTerTex.tif" ))
        bpy.data.images['previewTerTex.tif'].use_fake_user = True
    else:
        bpy.data.images['previewTerTex.tif'].reload()

def dqolbp10():
    import addon_utils
    
    addons = [mod for mod in addon_utils.modules(refresh=False)]

    for mod in addons:
        if mod.__name__ == "bLandscapeTools-master":
            dpo0qbl1 = mod.__file__
            pass
    
    dlq1obp0 = dpo0qbl1[:-12]
    dboplq01 = os.path.join(dlq1obp0, "data")
    
    return dpo0qbl1,dlq1obp0,dboplq01

def dp0l1obq(dboqpl01,dl10pqob):
    ext = dl10pqob.split('.')[-1]
    if ext == 'png':
        d01qbopl = 'pgw'
    if ext == 'tif' or ext == 'tiff':
        d01qbopl = 'tfw'
    if ext == 'jpg' or ext == 'jpeg':
        d01qbopl = 'jgw'
    
    if os.name == "posix":
        cmd = 'gdalinfo "{}"'.format(dl10pqob)
    else:
        gdal = os.path.join(dboqpl01, "gdalinfo.exe")
        cmd = '"{}" "{}"'.format(gdal,dl10pqob)
    print(cmd)
    dbol1p0q = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    
    for i in range(0,10):
        line = str(dbol1p0q.stdout.readline()).rstrip('\\r\\n\'')
        if line.split(' ')[0][2:] == 'Size':
            info = int(line.split(' ')[3])
    
    return info

def dpbqo01l(path):
    info = []
    f = open(path,"r")
    line = f.readline().split(" ")
    for i in range(5):
        info.append( line[-1])
        line = f.readline().split(" ")
    f.close()
    ncols = int(info[0])
    d1oqlpb0 = float(info[4])
    x = float(info[2])
    y = float(info[3])
    return ncols,x,y,d1oqlpb0

def d1qp0lob(db10qolp):
    bpy.ops.object.lamp_add(type='HEMI')
    hemi = bpy.context.object
    hemi.hide = True
    hemi.name = "Hemi_" + db10qolp
    
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

def dplq01ob():
    dboplq01 = dqolbp10()[2]
    dblo0p1q = bpy.context.scene.dblo0p1q
    do1bq0pl = 'Project_{}'.format(dblo0p1q.split(os.path.sep)[-2])
    
    bpy.ops.wm.open_mainfile(filepath=os.path.join(dboplq01, "dummy.blend"))
    
    bpy.context.scene.dqlob01p = True
    bpy.context.scene.dblo0p1q = dblo0p1q
    bpy.context.scene['d0b1olqp'] = False
    
    bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(bpy.context.scene.dblo0p1q,do1bq0pl),copy=False)
    
    if not os.path.exists(bpy.context.scene.dblo0p1q + 'ProjectData'):
	    os.makedirs(bpy.context.scene.dblo0p1q + 'ProjectData')
    if not os.path.exists(os.path.join(bpy.context.scene.dblo0p1q + 'ProjectData', 'Textures')):
	    os.makedirs(os.path.join(bpy.context.scene.dblo0p1q + 'ProjectData', 'Textures'))
    else:
        rmtree(os.path.join( bpy.context.scene.dblo0p1q + 'ProjectData', 'Textures') )
        os.makedirs(os.path.join( bpy.context.scene.dblo0p1q + 'ProjectData', 'Textures') )
    if not os.path.exists(bpy.context.scene.dblo0p1q + 'Output'):
	    os.makedirs(bpy.context.scene.dblo0p1q + 'Output')


def db0lqo1p():
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
    bpy.ops.view2d.dp0ql1bo(override,'INVOKE_DEFAULT')

def dql0o1pb(self,context):
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

def dqob0lp1(self, context):
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
        bgl.glVertex2i(0, self.dqo0p1lb)
        bgl.glVertex2i(width, self.dqo0p1lb)
        bgl.glVertex2i(self.do1qpbl0, 0)
        bgl.glVertex2i(self.do1qpbl0, height)
        bgl.glEnd()
    
    else:
        dlb0o1qp = self.dlp01qbo
        dob10lpq = list(bpy.context.region.view2d.view_to_region(dlb0o1qp[0],dlb0o1qp[1],clip=False))
        
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.do1qpbl0, self.dqo0p1lb)
        bgl.glVertex2i(dob10lpq[0], self.dqo0p1lb)
        bgl.glVertex2i(dob10lpq[0], dob10lpq[1])
        bgl.glVertex2i(self.do1qpbl0, dob10lpq[1])
        bgl.glEnd()
        
        bgl.glColor4f(0.0, 1.0, 0.0, 0.3)
        bgl.glBegin(bgl.GL_POLYGON)
        bgl.glVertex2i(self.do1qpbl0, self.dqo0p1lb)
        bgl.glVertex2i(dob10lpq[0], self.dqo0p1lb)
        bgl.glVertex2i(dob10lpq[0], dob10lpq[1])
        bgl.glVertex2i(self.do1qpbl0, dob10lpq[1])
        bgl.glEnd()
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.position(font_id, self.do1qpbl0 - 210, self.dqo0p1lb - 15, 0)
        blf.draw(font_id, self.doqblp01)
        blf.position(font_id, self.do1qpbl0 - 210, self.dqo0p1lb - 30, 0)
        blf.draw(font_id, self.dp1qb0lo)
        blf.position(font_id, self.do1qpbl0 - 210, self.dqo0p1lb - 45, 0)
        blf.draw(font_id, self.dplo1bq0)      
    
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    bgl.glDisable(bgl.GL_LINE_STIPPLE)
    blf.disable(0, blf.SHADOW)

def dlpoqb10(do0lbqp1,dpbo0ql1):
    dp10loqb, d1p0lqob, dlbp0oq1, d01olpbq = do0lbqp1[0], do0lbqp1[1], dpbo0ql1[0], dpbo0ql1[1]
    
    if dlbp0oq1 < 0:
        dlbp0oq1 = 0.0
    elif dlbp0oq1 > 1:
        dlbp0oq1 = 1.0
    
    if d01olpbq < 0:
        d01olpbq = 0.0
    elif d01olpbq > 1:
        d01olpbq = 1.0
    
    if dp10loqb < 0:
        dp10loqb = 0.0
    elif dp10loqb > 1:
        dp10loqb = 1.0
    
    if d1p0lqob < 0:
        d1p0lqob = 0.0
    elif d1p0lqob > 1:
        d1p0lqob = 1.0
    
    if dlbp0oq1 < dp10loqb:
        dlbp1o0q = dlbp0oq1
        d0qbpol1 = dp10loqb
    else:
        dlbp1o0q = dp10loqb
        d0qbpol1 = dlbp0oq1
    
    if d01olpbq > d1p0lqob:
        db1pqo0l = d01olpbq
        d1bq0olp = d1p0lqob
    else:
        db1pqo0l = d1p0lqob
        d1bq0olp = d01olpbq
    
    return db1pqo0l,dlbp1o0q,d1bq0olp,d0qbpol1

def dpbq01ol(d1oqlpb0,d0pqol1b,db1pqo0l,dlbp1o0q,d1bq0olp,d0qbpol1):
    d1qbpo0l = False
    dlpo0q1b = False
    
    if isnan(db1pqo0l):
        db1pqo0l = 0.0
    if isnan(dlbp1o0q):
        dlbp1o0q = 0.0
    
    if db1pqo0l == 1.0:
        d0bp1qol = 0
        d1qbpo0l = True
    else:
        d0bp1qol = floor((1 - db1pqo0l) * d0pqol1b)
    
    topLeftColumn = ceil(dlbp1o0q * d0pqol1b)
    
    if d1bq0olp == 0.0:
        bottomRightRow = d0pqol1b - 1
    else:
        bottomRightRow = floor((1 - d1bq0olp) * d0pqol1b) - 1
    
    if d0qbpol1 == 1.0:
         bottomRightColumn = d0pqol1b - 1
         dlpo0q1b = True
    else:
        bottomRightColumn = ceil(d0qbpol1 * d0pqol1b) - 1
    
    dbl1o0qp = bottomRightColumn - topLeftColumn + 2 if dlpo0q1b else bottomRightColumn - topLeftColumn + 1
    d01pqlob = bottomRightRow - d0bp1qol + 2 if d1qbpo0l else bottomRightRow - d0bp1qol + 1
    
    return d0bp1qol, topLeftColumn, bottomRightRow, bottomRightColumn, d1qbpo0l, dlpo0q1b, dbl1o0qp, d01pqlob

def dq0ol1pb(dopql1b0,d0pqol1b,d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b):
    print(1111,time.ctime())
    dqlp01bo = fromfile(dopql1b0, dtype=float32)
    d1blqop0 = reshape(dqlp01bo,(d0pqol1b,d0pqol1b))
    dqlp01bo = d1blqop0[d0bp1qol:bottomRightRow + 1,topLeftColumn:bottomRightColumn + 1]
    
    print(1112,time.ctime())
    if d1qbpo0l and dlpo0q1b:
        dolq10bp = dqlp01bo[0]
        dqlp01bo = vstack((dolq10bp,dqlp01bo))
        d1qlo0pb = dqlp01bo[:,[-1]]
        dqlp01bo = hstack((dqlp01bo,d1qlo0pb))
    else:
        if d1qbpo0l:
            dolq10bp = dqlp01bo[0]
            dqlp01bo = vstack((dolq10bp,dqlp01bo))
        if dlpo0q1b:
            d1qlo0pb = dqlp01bo[:,[-1]]
            dqlp01bo = hstack((dqlp01bo,d1qlo0pb))
    return dqlp01bo

def d1qlpob0(do0bq1lp,d0bolqp1,topLeftColumn,d0bp1qolChanged,dpo0b1lq,d1opblq0,dblpqo01,dq10bpol):
    dl1op0qb = d0bolqp1 * topLeftColumn - do0bq1lp * dpo0b1lq
    doqbl10p = d0bolqp1 * d0bp1qolChanged - do0bq1lp * d1opblq0
    print('Pixel edge to vertex distance: ', dl1op0qb,doqbl10p)
    do1lq0bp = 1 / do0bq1lp * dl1op0qb
    dploq01b = 1 / do0bq1lp * doqbl10p
    print('Vertex from pixel shift: ', do1lq0bp,dploq01b)
    
    dlboqp01 = 1 / dblpqo01 * do1lq0bp
    d1qobl0p = 1 - (1 / dq10bpol * dploq01b)
    print('uvStart at: ', dlboqp01, d1qobl0p)
    
    db0p1olq = (d0bolqp1 / do0bq1lp) * (1 / dblpqo01)
    d1p0qlbo = (d0bolqp1 / do0bq1lp) * (1 / dq10bpol)
    print('terrainUVcellsizeLoc: ', db0p1olq, d1p0qlbo)
    return dlboqp01, d1qobl0p, db0p1olq, d1p0qlbo

def dbqop1l0(originalHeightField, d1blqop0, dopblq10):
    originalHeightField[dopblq10[0]:dopblq10[0] + d1blqop0.shape[0], dopblq10[1]:dopblq10[1] + d1blqop0.shape[1]] = d1blqop0
    return originalHeightField

def dbpo1ql0():
    dq1bolp0 = bpy.data.scenes['Default_Location']
    dobpl1q0 = dq1bolp0.d10bqlop
    dblo0p1q = dq1bolp0.dblo0p1q
    d0pqol1b,xllcorner,yllcorner,d1oqlpb0 = dq1bolp0["db1lp0oq"],dq1bolp0["xllcorner"],dq1bolp0["yllcorner"],dq1bolp0["dboqp1l0"]
    dbqpo01l = fromfile(dobpl1q0,dtype=float32)
    dpol0bq1 = dbqpo01l.reshape((d0pqol1b,d0pqol1b))
    
    db10qolp = bpy.context.scene.name
    doq01bpl = bpy.data.objects.get('Terrain_{}'.format(db10qolp))
    do01bpql = doq01bpl.matrix_world
    
    dqlp01bo1D = []
    for v in doq01bpl.data.vertices:
        worldCoord = do01bpql * v.co
        dqlp01bo1D.append(round(worldCoord[2],2))
    
    d1blqop0 = array(dqlp01bo1D).reshape(doq01bpl["d0blqp1o"],doq01bpl["dqo1lpb0"])
    if doq01bpl['dlbpo1q0']:
        d1blqop0 = delete(d1blqop0,0,0)
    if doq01bpl['do01bplq']:
        d1blqop0 = delete(d1blqop0,-1,1)
    
    dobl01qp = dbqop1l0(dpol0bq1, d1blqop0, [doq01bpl["dqp1b0lo"],doq01bpl["dqlbp10o"]])
    dobl01qp.astype('float32').tofile(dobpl1q0)
    header = 'ncols         {}\nnrows         {}\nxllcorner     {}\nyllcorner     {}\ncellsize      {}\nNODATA_value  -9999'.format(d0pqol1b,d0pqol1b,xllcorner,yllcorner,d1oqlpb0)
    savetxt(os.path.join(dblo0p1q, 'Output', 'elevation.asc'),dobl01qp,fmt='%.2f',delimiter=' ',comments='',header=header)
    dqlbo0p1(os.path.join(dblo0p1q, 'Output', 'elevation.asc') )

def dq0b1plo(db10qolp,dbl1o0qp,d01pqlob,d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b):
    print(1,time.ctime())
    d1oqlb0p = bpy.data.scenes['Default_Location']
    d0pqol1b = d1oqlb0p["db1lp0oq"]
    d1oqlpb0 = d1oqlb0p["dboqp1l0"]
    dpoqlb01 = bpy.data.scenes['Default_Location'].d10bqlop
    dl10pqob = bpy.data.scenes["Default_Location"].dp0l1boq
    dblo0p1q = bpy.data.scenes["Default_Location"].dblo0p1q
    dboqpl01 = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.dboqpl01
    
    bpy.context.window.screen.scene = bpy.data.scenes["Default_Location"]
    bpy.ops.scene.new(type='FULL_COPY')
    bpy.context.scene.name = db10qolp
    bpy.context.scene['d0b1olqp'] = True
    
    d1qp0lob(db10qolp)
    
    print(2,time.ctime())
    if bpy.data.meshes.get('TerrainMesh_{}'.format(db10qolp)) is not None:
        bpy.data.meshes.get('TerrainMesh_{}'.format(db10qolp)).user_clear()
        bpy.data.meshes.remove(bpy.data.meshes.get('TerrainMesh_{}'.format(db10qolp)))
    
    dq1lpo0b = bpy.data.meshes.new('TerrainMesh_{}'.format(db10qolp))
    doq01bpl = bpy.data.objects.new('Terrain_{}'.format(db10qolp),dq1lpo0b)
    bpy.context.scene.objects.link(doq01bpl)
    doq01bpl.select=True
    bpy.context.scene.objects.active = doq01bpl
    print(3,time.ctime())
    
    if dl10pqob != '':
        dol0qbp1 = d1oqlb0p["ImageryResolution"]
        
        do0bq1lp = 1 / dol0qbp1
        d0bolqp1 = 1 / d0pqol1b
        print('UVCellTexture: ', do0bq1lp)
        print('UVCellTerrain: ', d0bolqp1)
        
        d0bp1qolChanged = d0bp1qol
        d1qobp0l = bottomRightColumn
        d01olqbp = bottomRightRow
        
        if not d1qbpo0l:
            d0bp1qolChanged += 1
        
        d01olqbp += 1     
        
        dpo0b1lq = floor(topLeftColumn * d0bolqp1 / do0bq1lp)
        d1opblq0 = floor(round(d0bp1qolChanged * d0bolqp1 / do0bq1lp,6))
        
        if dlpo0q1b:
            d1qobp0l += 1
        
        dqp1olb0 = ceil(d1qobp0l * d0bolqp1 / do0bq1lp) - 1
        dopl1b0q = ceil(round(d01olqbp * d0bolqp1 / do0bq1lp,6)) - 1
        
        dblpqo01 = dqp1olb0 - dpo0b1lq + 1
        dq10bpol = dopl1b0q - d1opblq0 + 1
         
        print('Texture starts at: ', dpo0b1lq, d1opblq0)
        print('Texture ends at: ', dqp1olb0, dopl1b0q)
        print("Terrain texture resolution: ", dblpqo01,dq10bpol)
        print(4,time.ctime())
        
        prev = os.join.path(dblo0p1q, "ProjectData", "Textures", "terTexture_{}.png".format(db10qolp) )
        if os.name == "posix":
            cmd = 'gdal_translate "{}" -of PNG -srcwin "{}" "{}" "{}" "{}" "{}"'.format(dl10pqob,dpo0b1lq,d1opblq0,dblpqo01,dq10bpol,prev)
        else:
            gdal = os.join.path(dboqpl01, "gdal_translate.exe")
            cmd = '"{}" "{}" -of PNG -srcwin "{}" "{}" "{}" "{}" "{}"'.format(gdal,dl10pqob,dpo0b1lq,d1opblq0,dblpqo01,dq10bpol,prev)
        
        subprocess.call(cmd)
        print(5,time.ctime())
        dq10lpob= bpy.data.textures.new('terTexture_{}'.format(db10qolp), type = 'IMAGE')
        dq10lpob.image = bpy.data.images.load( os.path.join(dblo0p1q, 'ProjectData', 'Textures', 'terTexture_{}.png'.format(db10qolp)))
        
        #-------------------------- Create new terrain material ----------------------------------------------
        d0qpol1b = bpy.data.materials.new('TerrainMaterial_{}'.format(db10qolp))
        d0qpol1b.specular_intensity = 0
        d0qpol1b.texture_slots.add()
        
        dp1qobl0 = d0qpol1b.texture_slots[0]
        dp1qobl0.texture = dq10lpob
        dp1qobl0.texture_coords = 'UV'
        
        bpy.ops.object.material_slot_add()
        bpy.data.objects['Terrain_{}'.format(db10qolp)].material_slots[0].material = d0qpol1b  
        print(6,time.ctime())
    
    bm = bmesh.new() 
    bm.from_mesh(dq1lpo0b)
    
    if dl10pqob != '':
        do1p0qbl = bm.faces.layers.tex.verify()
        d0olp1qb = bm.loops.layers.uv.verify()
    
    print(7,time.ctime())
    d0pblq1o = dq0ol1pb(dpoqlb01,d0pqol1b,d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b)
    print(8,time.ctime())
    d1p0oqbl = topLeftColumn * d1oqlpb0
    if d1qbpo0l:
        dol1p0bq = d0pqol1b * d1oqlpb0
    else:
        dol1p0bq = (d0pqol1b - 1)  * d1oqlpb0
    
    dpb0lqo1 = dol1p0bq - (d0bp1qol * d1oqlpb0)
    print(9,time.ctime())
    for row in range(d01pqlob):
        dqlb10op = d0pblq1o[row]
        for col in range(dbl1o0qp):
            bm.verts.new((d1p0oqbl,dpb0lqo1,dqlb10op[col]))
            d1p0oqbl += d1oqlpb0
        d1p0oqbl = topLeftColumn * d1oqlpb0
        dpb0lqo1 -= d1oqlpb0
    bm.verts.ensure_lookup_table()
    
    if dl10pqob != '':
        dlboqp01, d1qobl0p, db0p1olq, d1p0qlbo = d1qlpob0(do0bq1lp,d0bolqp1,topLeftColumn,d0bp1qolChanged,dpo0b1lq,d1opblq0,dblpqo01,dq10bpol)
    print(10,time.ctime())
    uvShiftY = 0
    for rowOfset in range(0,dbl1o0qp * (d01pqlob - 1), dbl1o0qp):
        for d10polqb in range (0, dbl1o0qp - 1):
            vertID = rowOfset + d10polqb
            face = [bm.verts[vertID],bm.verts[vertID + dbl1o0qp],bm.verts[vertID + dbl1o0qp + 1],bm.verts[vertID + 1]]
            d1lpboq0 = bm.faces.new(face)
            
            if dl10pqob != '':
                d1lpboq0[do1p0qbl].image = bpy.data.images['terTexture_{}.png'.format(db10qolp)]
                d1lpboq0.loops[0][d0olp1qb].uv = [dlboqp01 + d10polqb * db0p1olq, d1qobl0p - uvShiftY * d1p0qlbo]
                d1lpboq0.loops[1][d0olp1qb].uv = [dlboqp01 + d10polqb * db0p1olq, d1qobl0p - uvShiftY * d1p0qlbo - d1p0qlbo]
                d1lpboq0.loops[2][d0olp1qb].uv = [dlboqp01 + d10polqb * db0p1olq + db0p1olq, d1qobl0p - uvShiftY * d1p0qlbo - d1p0qlbo]
                d1lpboq0.loops[3][d0olp1qb].uv = [dlboqp01 + d10polqb * db0p1olq + db0p1olq, d1qobl0p - uvShiftY * d1p0qlbo]
        uvShiftY += 1
    
    print(11,time.ctime())        
    bmesh.ops.triangulate(bm, faces=bm.faces, quad_method=2)
    print(12,time.ctime())
    bm.to_mesh(dq1lpo0b)
    bm.free()
    print(13,time.ctime())
    
    doq01bpl["dqp1b0lo"] = d0bp1qol
    doq01bpl["dqlbp10o"] = topLeftColumn
    doq01bpl["dqo1lpb0"] = dbl1o0qp
    doq01bpl["d0blqp1o"] = d01pqlob
    doq01bpl["dlbpo1q0"] = d1qbpo0l
    doq01bpl["do01bplq"] = dlpo0q1b
    doq01bpl.lock_location = True,True,True
    doq01bpl.lock_rotation = True,True,True
    doq01bpl.lock_scale = True,True,True
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

def dlb0o1pq(d1oqlpb0,db1l0opq,dq01lobp,):
    d0p1olqb = bpy.context.user_preferences.addons["bLandscapeTools-master"].preferences.d0p1olqb
    result = ones((db1l0opq,db1l0opq)) * dq01lobp
    header = 'ncols         {}\nnrows         {}\nxllcorner     0\nyllcorner     0\ncellsize      {}\nNODATA_value  -9999'.format(db1l0opq,db1l0opq,d1oqlpb0) 
    savetxt( os.path.join(d0p1olqb, 'elevation.asc'),result,fmt='%.2f',delimiter=' ',newline='\r\n',comments='',header=header)
