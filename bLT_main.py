import bpy

from .bLT_utils import *

from bpy.props import StringProperty,FloatProperty,IntProperty,BoolProperty,EnumProperty
from bpy.types import Panel,Scene,AddonPreferences,UIList,PropertyGroup,WindowManager

class dplq01bo(PropertyGroup):
    d0blo1qp = BoolProperty(name="",default=False)

class dpq0bl1o(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name", text="", emboss=False)
        
        icon = 'RESTRICT_VIEW_OFF' if item.d0blo1qp else 'RESTRICT_VIEW_ON'
        op = layout.operator("scene.dq10polb", text="", emboss=False, icon=icon)
        op.dol0qpb1 = index

class d1qoplb0(bpy.types.Operator):
    bl_idname = "scene.dbq0olp1"
    bl_label = "Remove Location"
    bl_options = {'REGISTER'}
    bl_description = 'Removes current location(eye icon) without commiting any changes!!!'
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        d0obpql1 = scene.d0obpql1
        
        db10qolp = context.scene.name
        print(db10qolp)
        
        for index, location in enumerate(d0obpql1):
            if location.name == db10qolp:
                dol0qpb1 = index
        
        scene.d0obpql1.remove(dol0qpb1)
        bpy.ops.scene.delete()
        
        if len(d0obpql1) != 0:
            d0obpql1[0].d0blo1qp = True
            context.window.screen.scene = bpy.data.scenes[d0obpql1[0].name]
            
            doq01bpl = bpy.data.objects['Terrain_{}'.format(d0obpql1[0].name)]
            doq01bpl.select=True
            context.scene.objects.active = doq01bpl
            bpy.ops.view3d.view_selected()
        else:
            context.window.screen.scene = bpy.data.scenes['Default_Location']
            context.scene.dbq0po1l = False
            context.scene.dlqbo01p = True
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self,event)

class dbq10plo(bpy.types.Operator):
    bl_idname = "scene.dq10polb"
    bl_label = "Switch Locations"
    bl_description = 'Click on a closed eye to switch to selected location'
    
    dol0qpb1 = IntProperty()
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        d0obpql1 = scene.d0obpql1
        dol0qpb1 = self.dol0qpb1
        
        for location in d0obpql1:
            location.d0blo1qp = False
        d0obpql1[dol0qpb1].d0blo1qp = True
        
        bpy.context.window.screen.scene = bpy.data.scenes[d0obpql1[dol0qpb1].name]
        
        doq01bpl = bpy.data.objects['Terrain_{}'.format(d0obpql1[dol0qpb1].name)]
        doq01bpl.select=True
        bpy.context.scene.objects.active = doq01bpl
        bpy.ops.view3d.view_selected()
        
        return {'FINISHED'}

class dobqlp01(bpy.types.Operator):
    bl_idname = "scene.do0lbq1p"
    bl_label = "Create Project"
    
    def execute(self, context):
        dplq01ob()
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'window': window, 'screen': screen, 'area': area, 'region': region}
        bpy.ops.view3d.d1lp0obq(override,'INVOKE_DEFAULT')
        
        context.scene.dlpb1qo0 = False
        context.scene.dlqbo01p = True
        context.scene.d0blop1q = True
        
        return {'FINISHED'}

class d0qobl1p(bpy.types.Operator):
    bl_idname = "scene.d1bqpo0l"
    bl_label = "Import Location"
    bl_description = 'Imports a new location'
    
    def execute(self, context):
        db0lqo1p()
        return {'FINISHED'}

class dlob0p1q(bpy.types.Operator):
    bl_idname = "scene.d1ob0plq"
    bl_label = "Create Location"
    
    db10qolp = StringProperty(name="Location name:")
    def execute(self, context):
        for location in bpy.data.scenes:
            if location.name == self.db10qolp:
                self.report({'WARNING'}, "Location with this name already exists! Try a different name.")
                bpy.ops.scene.d1bqpo0l()
                return {'CANCELLED'}
        
        global d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b,dbl1o0qp,d01pqlob
        dq0b1plo(self.db10qolp,dbl1o0qp,d01pqlob,d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b)
        
        scene = bpy.data.scenes['Default_Location']
        d0obpql1 = scene.d0obpql1
        d1b0qlop = len(d0obpql1)
        
        dq1l0bop = d0obpql1.add()
        dq1l0bop.name = self.db10qolp
        for location in d0obpql1:
            location.d0blo1qp = False
        dq1l0bop.d0blo1qp = True
        scene.dq0p1bol = d1b0qlop
        
        context.scene.dbq0po1l = True
        context.scene.dlqbo01p = False
        
        bpy.ops.wm.save_mainfile()
        return {'FINISHED'}
    
    def invoke(self, context, event):
        self.db10qolp = 'Type location name here...'
        return context.window_manager.invoke_props_dialog(self)
    
    def cancel(self, context):
        context.area.type = 'VIEW_3D'
        return {'CANCELLED'}

class d0o1plqb(bpy.types.Operator):
    bl_idname = "scene.dqpolb01"
    bl_label = "Commit Location"
    bl_description = 'Commits all terrain changes to elevation.bLTe\nand elevation.asc(Project\\Output)'
    
    def execute(self, context):
        dbpo1ql0()
        return {'FINISHED'}

class dp0qbl1o(bpy.types.Operator):
    bl_idname = "view2d.dp0ql1bo"
    bl_label = "Pick Location"
    
    def modal(self, context, event):
        global d0bp1qol,topLeftColumn,bottomRightRow,bottomRightColumn,d1qbpo0l,dlpo0q1b,dbl1o0qp,d01pqlob
        context.area.tag_redraw()
        
        d1oqlb0p = bpy.data.scenes['Default_Location']
        d0pqol1b = d1oqlb0p["db1lp0oq"]
        d1oqlpb0 = d1oqlb0p["dboqp1l0"]
        
        d0pob1lq = context.region.view2d.region_to_view(self.do1qpbl0,self.dqo0p1lb)
        
        db1pqo0l,dlbp1o0q,d1bq0olp,d0qbpol1 = dlpoqb10(list(d0pob1lq),list(self.dlp01qbo))
        
        d0bp1qol, topLeftColumn, bottomRightRow, bottomRightColumn, d1qbpo0l, dlpo0q1b, dbl1o0qp, d01pqlob = dpbq01ol(d1oqlpb0,d0pqol1b,db1pqo0l,dlbp1o0q,d1bq0olp,d0qbpol1)
        
        self.doqblp01 = 'TerrainVerts: {:,}({:,}x{:,})'.format(dbl1o0qp * d01pqlob,dbl1o0qp,d01pqlob)
        dp1qb0lo = 0  if ((dbl1o0qp - 1) * (d01pqlob - 1)) * 2 <= 0 else ((dbl1o0qp - 1) * (d01pqlob - 1)) * 2
        self.dp1qb0lo = 'TerrainTris: {:,}'.format(dp1qb0lo)
        dplo1bq0X = 0 if (dbl1o0qp - 1) * d1oqlpb0 <= 0 else (dbl1o0qp - 1) * d1oqlpb0
        self.dplo1bq0 = 'MapSize: {:.2f}x{:.2f} m'.format(dplo1bq0X, (d01pqlob - 1) * d1oqlpb0)
        
        if event.type == 'MOUSEMOVE':
            self.do1qpbl0, self.dqo0p1lb = event.mouse_region_x,event.mouse_region_y
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.switch = True
            self.dqbo0pl1 += 1
            if self.dqbo0pl1 == 2:
                if ((dbl1o0qp - 1) * (d01pqlob - 1)) * 2 <= 0:
                    self.report({'WARNING'}, "No vertices to create a triangle")
                    self.dqbo0pl1 = 0
                    self.switch = False
                else:
                    bpy.ops.scene.d1ob0plq('INVOKE_DEFAULT')
                    bpy.types.SpaceImageEditor.draw_handler_remove(self._handle, 'WINDOW')
                    return {'FINISHED'}
            self.dlp01qbo = context.region.view2d.region_to_view(event.mouse_region_x, event.mouse_region_y)
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
        self.do1qpbl0,self.dqo0p1lb = 0,0
        self.dqbo0pl1 = 0
        self.dlp01qbo = [0,0]
        self.switch = False
        
        if context.area.type == 'IMAGE_EDITOR':
            args = (self, context)
            self._handle = bpy.types.SpaceImageEditor.draw_handler_add(dqob0lp1, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Image Editor not found, cannot run operator")
            return {'CANCELLED'}

class dpbo10ql(bpy.types.Operator):
    bl_idname = "view3d.d1lp0obq"
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
            self._handle = bpy.types.SpaceView3D.draw_handler_add(dql0o1pb, args, 'WINDOW', 'POST_PIXEL')
            dboplq01 = dqolbp10()[2]
            if bpy.data.images.get('splash.png') is None:
                bpy.data.images.load( os.path.join(dboplq01, 'splash.png') )
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

class dp10bqol(bpy.types.Operator):
    bl_idname = "object.dlpoq0b1"
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

class dol1pbq0(bpy.types.Operator):
    bl_idname = "object.dlb0pq1o"
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

class dp1oqb0l(bpy.types.Operator):
    bl_idname = "scene.dlobq0p1"
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

class d0qo1lbp(bpy.types.Operator):
    bl_idname = "scene.dlob10pq"
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

class dq0po1bl(bpy.types.Operator):
    bl_idname = "scene.dl10qbpo"
    bl_label = "Generate flat terrain"
    
    d1oqlpb0 = FloatProperty(name="Cell size:",default=1.0)
    db1l0opq = IntProperty(name="Grid resolution:",default=512)
    dq01lobp = FloatProperty(name="Default height:",default=10.0)
    
    def execute(self, context):
        dlb0o1pq(self.d1oqlpb0,self.db1l0opq,self.dq01lobp)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class dblqo0p1(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Project Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.dqlob01p = BoolProperty(name="",
        description="",
        default=False)
    
    Scene.dblo0p1q = StringProperty(name="",
        attr="projFolderPath",
        description="Path to project folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='')
    
    Scene.dp0l1boq = StringProperty(name="",
        attr="satellitePath",
        description="Path to terrain texture",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=d0lbqop1)
    
    Scene.dlp1qo0b = StringProperty(name="",
        attr="terrainPath",
        description="Path to terrain heightmap to create 3D terrain",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=d1qpbo0l)
    
    Scene.d10bqlop = StringProperty(name="",
        attr="terrainPath",
        description="Path to bLT internal elevation file",
        maxlen= 1024,
        subtype='FILE_PATH')
    
    d0p1lqob = [
    ("RVEngine", "RVEngine", "", 1),
    ("Unreal Engine 4", "Unreal Engine 4", "", 2),
    ("CryEngine", "CryEngine", "", 3),
    ("Unity", "Unity", "", 4),
    ("Enfusion", "Enfusion", "", 5)
    ]
    
    Scene.db1q0opl = bpy.props.EnumProperty(items=d0p1lqob,name="Engine",default='RVEngine')
    
    Scene.dlpb1qo0 = BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dlpb1qo0
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        box = layout.box()
        row = box.column()
        row.label(text="Project Folder")
        row.prop(scene,'dblo0p1q')
        row.separator()
        row.prop(scene, 'db1q0opl')
        
        row3 = box.column()
        row3.separator()
        row3.operator("scene.do0lbq1p",text='Create Project')
        
        if scene.dblo0p1q is '':
            row3.enabled = False
        else:
            row3.enabled = True

class d0bpqol1(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Data Source"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.dlqbo01p = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dlqbo01p
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        box = layout.box()
        row1 = box.column()
        row1.label(text="Terrain texture")
        row2 = row1.column(align=True)
        row2.prop(scene, 'dp0l1boq')
        row2.separator()
        row2.label(text="Terrain Heightmap")
        row2.prop(scene, 'dlp1qo0b')
        
        if len(bpy.data.scenes) > 1:
            row1.enabled = False
            row2.enabled = False

class dbolpq10(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Locations manager"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.d0b1olqp = BoolProperty(name="",
    description="",
    default=False)
    
    Scene.d0blop1q = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d0blop1q
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        if scene.dqlob01p:
            row.template_list("dpq0bl1o", "", bpy.data.scenes['Default_Location'], "d0obpql1", bpy.data.scenes['Default_Location'], "dq0p1bol")
        col = row.column()
        row1 = col.row()
        row1.operator("scene.d1bqpo0l",icon='ZOOMIN',text="")
        if scene.dlp1qo0b is '':#would be nice to have also check for supported file types
            row1.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row1.enabled = False
        
        row2 = col.row()        
        row2.operator("scene.dqpolb01",icon='APPEND_BLEND',text="")
        if not scene.d0b1olqp:
            row2.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row2.enabled = False    
        
        row3 = col.row()        
        row3.operator("scene.dbq0olp1",icon='ZOOMOUT',text="")
        if not scene.d0b1olqp:
            row3.enabled = False
        elif len(bpy.data.scenes["Default_Location"].d0obpql1) == 0:
            row3.enabled = False  
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row3.enabled = False    

class d0ob1lpq(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Location/Object(s) Appearance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.dbq0po1l = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dbq0po1l
    
    def draw(self, context):
        scene = context.scene
        view = context.space_data
        layout = self.layout
        fx_settings = view.fx_settings
        
        row = layout.row(align=True)
        row.operator("object.dlb0pq1o",icon='TEXTURE')
        row.operator("object.dlpoq0b1",icon='ASSET_MANAGER')
        row2 = layout.row(align=True)
        row2.operator("object.shade_smooth", text="Smooth",icon='MOD_SMOOTH')
        row2.operator("object.shade_flat", text="Flat",icon='MOD_DISPLACE')
        row1 = layout.row(align=True)
        row1.operator("scene.dlobq0p1",icon='MATCAP_13')
        row1.operator("scene.dlob10pq",icon='MOD_TRIANGULATE')
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                if  Area.spaces.active.use_matcap == True and Area.spaces.active.viewport_shade == 'SOLID':
                    row4 = layout.row(align=False)
                    row4.template_icon_view(view, "matcap_icon")
                    if not scene.d0b1olqp:
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
        
        if not scene.d0b1olqp:
            row.enabled = False 
            row1.enabled = False
            row2.enabled = False
            
            col.enabled = False

class dpqol01b(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Create"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator("scene.dl10qbpo",icon='MESH_GRID')

