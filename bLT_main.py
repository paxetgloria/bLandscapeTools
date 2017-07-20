import bpy

from .bLT_utils import *

from bpy.props import StringProperty,FloatProperty,IntProperty,BoolProperty,EnumProperty
from bpy.types import Panel,Scene,AddonPreferences,UIList,PropertyGroup,WindowManager

class dob1p0ql(PropertyGroup):
    dop0bql1 = BoolProperty(name="",default=False)
            
class d1lb0opq(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name", text="", emboss=False)
        
        
        icon = 'RESTRICT_VIEW_OFF' if item.dop0bql1 else 'RESTRICT_VIEW_ON'
        op = layout.operator("scene.dqb0l1po", text="", emboss=False, icon=icon)
        op.d0bpl1qo = index

class doq1pb0l(bpy.types.Operator):
    bl_idname = "scene.doq01blp"
    bl_label = "Remove Location"
    bl_options = {'REGISTER'}
    bl_description = 'Removes current location(eye icon) without commiting any changes!!!'

    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dlop10qb = scene.dlop10qb
        
        dbqp1lo0 = context.scene.name
        print(dbqp1lo0)
        
        for index, location in enumerate(dlop10qb):
            if location.name == dbqp1lo0:
                d0bpl1qo = index
        
        scene.dlop10qb.remove(d0bpl1qo)
        bpy.ops.scene.delete()
        
        if len(dlop10qb) != 0:
            dlop10qb[0].dop0bql1 = True
            context.window.screen.scene = bpy.data.scenes[dlop10qb[0].name]
            
            d0bolq1p = bpy.data.objects['Terrain_{}'.format(dlop10qb[0].name)]
            d0bolq1p.select=True
            context.scene.objects.active = d0bolq1p
            bpy.ops.view3d.view_selected()
        else:
            context.window.screen.scene = bpy.data.scenes['Default_Location']
            context.scene.d1l0qbop = False
            context.scene.doqb1lp0 = True

        
        return {'FINISHED'}
        
    def invoke(self, context, event):

        return context.window_manager.invoke_confirm(self,event)
        
class do1b0qlp(bpy.types.Operator):
    bl_idname = "scene.dqb0l1po"
    bl_label = "Switch Locations"
    bl_description = 'Click on a closed eye to switch to selected location'
    
    d0bpl1qo = IntProperty()
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dlop10qb = scene.dlop10qb
        d0bpl1qo = self.d0bpl1qo
        
        for location in dlop10qb:
            location.dop0bql1 = False
        dlop10qb[d0bpl1qo].dop0bql1 = True
        
        bpy.context.window.screen.scene = bpy.data.scenes[dlop10qb[d0bpl1qo].name]
        
        d0bolq1p = bpy.data.objects['Terrain_{}'.format(dlop10qb[d0bpl1qo].name)]
        d0bolq1p.select=True
        bpy.context.scene.objects.active = d0bolq1p
        bpy.ops.view3d.view_selected()
        
        return {'FINISHED'}
        
class dbql10op(bpy.types.Operator):
    bl_idname = "scene.db0o1lqp"
    bl_label = "Create Project"
    
    def execute(self, context):
        dlq0pob1()
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'window': window, 'screen': screen, 'area': area, 'region': region}
        bpy.ops.view3d.dlqbpo10(override,'INVOKE_DEFAULT')
        
        context.scene.d0q1bopl = False
        context.scene.doqb1lp0 = True
        context.scene.d1bolpq0 = True
        
        return {'FINISHED'}
        
class db0olq1p(bpy.types.Operator):
    bl_idname = "scene.dlop01bq"
    bl_label = "Import Location"
    bl_description = 'Imports a new location'
     
    def execute(self, context):
        d1lp0bqo()
        return {'FINISHED'}

class doplq01b(bpy.types.Operator):
    bl_idname = "scene.dl0bq1po"
    bl_label = "Create Location"
    
    dbqp1lo0 = StringProperty(name="Location name:")
    def execute(self, context):
        for location in bpy.data.scenes:
            if location.name == self.dbqp1lo0:
                self.report({'WARNING'}, "Location with this name already exists! Try a different name.")
                bpy.ops.scene.dlop01bq()
                return {'CANCELLED'}
                
        global d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p,dq0lbp1o,dq10obpl
        do0blp1q(self.dbqp1lo0,dq0lbp1o,dq10obpl,d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p)
        
        scene = bpy.data.scenes['Default_Location']
        dlop10qb = scene.dlop10qb
        dl1qp0bo = len(dlop10qb)
        
        dbq0l1op = dlop10qb.add()
        dbq0l1op.name = self.dbqp1lo0
        for location in dlop10qb:
            location.dop0bql1 = False
        dbq0l1op.dop0bql1 = True
        scene.dlop10qb_index = dl1qp0bo
        
        context.scene.d1l0qbop = True
        context.scene.doqb1lp0 = False
        
        bpy.ops.wm.save_mainfile()
        return {'FINISHED'}
        
    def invoke(self, context, event):
        self.dbqp1lo0 = 'Type location name here...'
        return context.window_manager.invoke_props_dialog(self)
        
    def cancel(self, context):
        context.area.type = 'VIEW_3D'
        return {'CANCELLED'}
        
class dbpoq10l(bpy.types.Operator):
    bl_idname = "scene.dplq1o0b"
    bl_label = "Commit Location"
    bl_description = 'Commits all terrain changes to the elevation.bLTe file'

    def execute(self, context):
        d1lq0opb()
        return {'FINISHED'}
     
class d0qb1lop(bpy.types.Operator):
    bl_idname = "view2d.d10bqpol"
    bl_label = "Pick Location"

    def modal(self, context, event):
        global d0p1oqbl,topLeftColumn,bottomRightRow,bottomRightColumn,dpoql0b1,db1oql0p,dq0lbp1o,dq10obpl
        context.area.tag_redraw()
        
        d0o1qlbp = bpy.data.scenes['Default_Location']
        dloq0b1p = d0o1qlbp["d0l1qpbo"]
        d0op1bql = d0o1qlbp["dqlp0o1b"]
        
        do0qp1bl = context.region.view2d.region_to_view(self.dbplo1q0,self.dpq1b0ol)
        
        d0q1olpb,dqol1bp0,dlq01bop,d1loq0pb = dop1lbq0(list(do0qp1bl),list(self.dpoqbl01))
        
        d0p1oqbl, topLeftColumn, bottomRightRow, bottomRightColumn, dpoql0b1, db1oql0p, dq0lbp1o, dq10obpl = dblqo1p0(d0op1bql,dloq0b1p,d0q1olpb,dqol1bp0,dlq01bop,d1loq0pb)
        
        self.dql1pb0o = 'TerrainVerts: {:,}({:,}x{:,})'.format(dq0lbp1o * dq10obpl,dq0lbp1o,dq10obpl)
        dbpql1o0 = 0  if ((dq0lbp1o - 1) * (dq10obpl - 1)) * 2 <= 0 else ((dq0lbp1o - 1) * (dq10obpl - 1)) * 2
        self.dbpql1o0 = 'TerrainTris: {:,}'.format(dbpql1o0)
        d0bpqlo1X = 0 if (dq0lbp1o - 1) * d0op1bql <= 0 else (dq0lbp1o - 1) * d0op1bql
        self.d0bpqlo1 = 'MapSize: {:.2f}x{:.2f} m'.format(d0bpqlo1X, (dq10obpl - 1) * d0op1bql)
        
        if event.type == 'MOUSEMOVE':
            self.dbplo1q0, self.dpq1b0ol = event.mouse_region_x,event.mouse_region_y
            
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.switch = True
            self.dlp1qbo0 += 1
            if self.dlp1qbo0 == 2:
                if ((dq0lbp1o - 1) * (dq10obpl - 1)) * 2 <= 0:
                    self.report({'WARNING'}, "No vertices to create a triangle")
                    self.dlp1qbo0 = 0
                    self.switch = False
                else:
                    bpy.ops.scene.dl0bq1po('INVOKE_DEFAULT')
                    bpy.types.SpaceImageEditor.draw_handler_remove(self._handle, 'WINDOW')
                    return {'FINISHED'}
                
            self.dpoqbl01 = context.region.view2d.region_to_view(event.mouse_region_x, event.mouse_region_y)
            
        elif event.type == 'BACK_SPACE':
            if bpy.data.images.get('previewSatTex.png') is not None and bpy.data.images.get('previewTerTex.tif') is not None:
                for space in bpy.context.area.spaces:
                    if space.type == 'IMAGE_EDITOR':
                        curPreview = space.image.name

                if curPreview == 'previewSatTex.png':
                    for space in bpy.context.area.spaces:
                        if space.type == 'IMAGE_EDITOR':
                            space.image = bpy.data.images['previewTerTex.tif']
                else:
                    for space in bpy.context.area.spaces:
                        if space.type == 'IMAGE_EDITOR':
                            space.image = bpy.data.images['previewSatTex.png']
                            
            return {'PASS_THROUGH'}
            
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.type = 'VIEW_3D'
            bpy.types.SpaceImageEditor.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
            
        elif event.type in {'WHEELUPMOUSE', 'WHEELDOWNMOUSE','MIDDLEMOUSE','LEFT_SHIFT'}:
            return {'PASS_THROUGH'}
        return {'RUNNING_MODAL'}
  
    def invoke(self, context, event):
        self.dbplo1q0,self.dpq1b0ol = 0,0
        self.dlp1qbo0 = 0
        self.dpoqbl01 = [0,0]
        self.switch = False
        
        if context.area.type == 'IMAGE_EDITOR':
            args = (self, context)
            self._handle = bpy.types.SpaceImageEditor.draw_handler_add(d1b0qlop, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Image Editor not found, cannot run operator")
            return {'CANCELLED'}
 
class dop1lb0q(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.dlqbpo10"
    bl_label = "Draw splash screen"

    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type in {'RIGHTMOUSE', 'LEFTMOUSE', 'ESC'}:
            self.img.gl_free()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            args = (self, context)
            self._handle = bpy.types.SpaceView3D.draw_handler_add(dobql01p, args, 'WINDOW', 'POST_PIXEL')
            dq01plob = dpobq0l1()[2]
            if bpy.data.images.get('splash.png') is None:
                bpy.data.images.load('{}\\splash.png'.format(dq01plob))
                bpy.data.images['splash.png'].use_fake_user = True
            else:
                bpy.data.images['splash.png'].reload()
            self.img = bpy.data.images['splash.png']
            self.img.gl_load()
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}

class dbpol1q0(bpy.types.Operator):
    bl_idname = "object.dbpqlo01"
    bl_label = "Textured + Wire overlay"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'TEXTURED'
        objs = bpy.context.selected_objects
        for obj in objs:
            obj.show_wire = True
            obj.show_all_edges = True
        return {'FINISHED'}

class dl1obp0q(bpy.types.Operator):
    bl_idname = "object.d01lopqb"
    bl_label = "Textured"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'TEXTURED'
        objs = bpy.context.selected_objects
        for obj in objs:
            obj.show_wire = False
            obj.show_all_edges = False
        return {'FINISHED'}

class dlpoq0b1(bpy.types.Operator):
    bl_idname = "scene.d01lbpoq"
    bl_label = "MatCap"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'SOLID'
                Area.spaces.active.use_matcap = True
        objs = bpy.context.selected_objects
        for obj in objs:
            obj.show_wire = False
            obj.show_all_edges = False
        return {'FINISHED'}

class d0lpobq1(bpy.types.Operator):
    bl_idname = "scene.dp0l1obq"
    bl_label = "MatCap + Wire overlay"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'SOLID'
                Area.spaces.active.use_matcap = True
        objs = bpy.context.selected_objects
        for obj in objs:
            obj.show_wire = True
            obj.show_all_edges = True
        return {'FINISHED'}

class dbploq10(bpy.types.Operator):
    bl_idname = "scene.do0lb1pq"
    bl_label = "Generate flat terrain"
    
    d0op1bql = FloatProperty(name="Cell size:",default=1.0)
    d1qbp0lo = IntProperty(name="Grid resolution:",default=512)
    dpl0q1ob = FloatProperty(name="Default height:",default=10.0)
    
    def execute(self, context):
        dqbpol10(self.d0op1bql,self.d1qbp0lo,self.dpl0q1ob)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
class dq0lo1bp(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Project Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.db0opql1 = BoolProperty(name="",
        description="",
        default=False)
    
    Scene.dq1o0pbl = StringProperty(name="",
        attr="projFolderPath",
        description="Path to project folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='')
    
    Scene.doqbpl10 = StringProperty(name="",
        attr="satellitePath",
        description="Path to terrain texture",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=doblqp01)

    Scene.d0bq1olp = StringProperty(name="",
        attr="terrainPath",
        description="Path to terrain heightmap to create 3D terrain",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=d1opl0qb)
        
    Scene.dlq1bpo0 = StringProperty(name="",
        attr="terrainPath",
        description="Path to bLT internal elevation file",
        maxlen= 1024,
        subtype='FILE_PATH')
        
    dqo1pb0l = [
    ("RVEngine", "RVEngine", "", 1),
    ("Unreal Engine 4", "Unreal Engine 4", "", 2),
    ("CryEngine", "CryEngine", "", 3),
    ("Unity", "Unity", "", 4),
    ("Enfusion", "Enfusion", "", 5)
    ]

    Scene.dpbl0o1q = bpy.props.EnumProperty(items=dqo1pb0l,name="Engine",default='RVEngine')
    
    Scene.d0q1bopl = BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d0q1bopl

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        box = layout.box()
        row = box.column()
        row.label(text="Project Folder")
        row.prop(scene,'dq1o0pbl')
        row.separator()
        row.prop(scene, 'dpbl0o1q')

        row3 = box.column()
        row3.separator()
        row3.operator("scene.db0o1lqp",text='Create Project')
        
        if scene.dq1o0pbl is '':
            row3.enabled = False
        else:
            row3.enabled = True
                
class db1lo0qp(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Data Source"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.doqb1lp0 = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.doqb1lp0

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        
        box = layout.box()
        row1 = box.column()
        row1.label(text="Terrain texture")
        row2 = row1.column(align=True)
        row2.prop(scene, 'doqbpl10')
        row2.separator()
        row2.label(text="Terrain Heightmap")
        row2.prop(scene, 'd0bq1olp')
        
        if len(bpy.data.scenes) > 1:
            row1.enabled = False
            row2.enabled = False
                
        
class d1qbo0lp(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Locations manager"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    
    Scene.dolqp1b0 = BoolProperty(name="",
    description="",
    default=False)
    
    Scene.d1bolpq0 = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d1bolpq0

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        if scene.db0opql1:
            row.template_list("d1lb0opq", "", bpy.data.scenes['Default_Location'], "dlop10qb", bpy.data.scenes['Default_Location'], "dlop10qb_index")
        col = row.column()
        row1 = col.row()
        row1.operator("scene.dlop01bq",icon='ZOOMIN',text="")
        if scene.d0bq1olp is '':#would be nice to have also check for supported file types
            row1.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row1.enabled = False
                    
        row2 = col.row()        
        row2.operator("scene.dplq1o0b",icon='APPEND_BLEND',text="")
        if not scene.dolqp1b0:
            row2.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row2.enabled = False    
        
        row3 = col.row()        
        row3.operator("scene.doq01blp",icon='ZOOMOUT',text="")
        if not scene.dolqp1b0:
            row3.enabled = False
        elif len(bpy.data.scenes["Default_Location"].dlop10qb) == 0:
            row3.enabled = False  
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row3.enabled = False    
       
   
                
            

class dq0bplo1(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Location/Object(s) Appearance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.d1l0qbop = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d1l0qbop

    def draw(self, context):
        scene = context.scene
        view = context.space_data
        layout = self.layout
        fx_settings = view.fx_settings
        
        row = layout.row(align=True)
        row.operator("object.d01lopqb",icon='TEXTURE')
        row.operator("object.dbpqlo01",icon='ASSET_MANAGER')
        row2 = layout.row(align=True)
        row2.operator("object.shade_smooth", text="Smooth",icon='MOD_SMOOTH')
        row2.operator("object.shade_flat", text="Flat",icon='MOD_DISPLACE')
        row1 = layout.row(align=True)
        row1.operator("scene.d01lbpoq",icon='MATCAP_13')
        row1.operator("scene.dp0l1obq",icon='MOD_TRIANGULATE')
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                if  Area.spaces.active.use_matcap == True and Area.spaces.active.viewport_shade == 'SOLID':
                    row4 = layout.row(align=False)
                    row4.template_icon_view(view, "matcap_icon")
                    if not scene.dolqp1b0:
                        row4.enabled = False

        col = layout.column()
        col.prop(fx_settings, "use_ssao", text="Ambient Occlusion")
        if fx_settings.use_ssao:
                ssao_settings = fx_settings.ssao
                subcol = col.column(align=True)
                subcol.prop(ssao_settings, "factor")
                subcol.prop(ssao_settings, "distance_max")
                subcol.prop(ssao_settings, "attenuation")
                subcol.prop(ssao_settings, "samples")
                    
        if not scene.dolqp1b0:
            row.enabled = False 
            row1.enabled = False
            row2.enabled = False
            
            col.enabled = False
            
class db1qlp0o(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Create"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout

        row = layout.row(align=True)
        row.operator("scene.do0lb1pq",icon='MESH_GRID')
        
