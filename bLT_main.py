import bpy

from .bLT_utils import *

from bpy.props import StringProperty,FloatProperty,IntProperty,BoolProperty,EnumProperty
from bpy.types import Panel,Scene,AddonPreferences,UIList,PropertyGroup,WindowManager

class d0q1bolp(PropertyGroup):
    d1b0oplq = BoolProperty(name="",default=False)
            
class d1bp0qol(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name", text="", emboss=False)
        
        
        icon = 'RESTRICT_VIEW_OFF' if item.d1b0oplq else 'RESTRICT_VIEW_ON'
        op = layout.operator("scene.d1lpobq0", text="", emboss=False, icon=icon)
        op.d1q0pbol = index

class d0qp1olb(bpy.types.Operator):
    bl_idname = "scene.dl01boqp"
    bl_label = "Remove Location"
    bl_options = {'REGISTER'}
    bl_description = 'Removes current location(eye icon) without commiting any changes!!!'

    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dlp1qbo0 = scene.dlp1qbo0
        
        d0oplq1b = context.scene.name
        print(d0oplq1b)
        
        for index, location in enumerate(dlp1qbo0):
            if location.name == d0oplq1b:
                d1q0pbol = index
        
        scene.dlp1qbo0.remove(d1q0pbol)
        bpy.ops.scene.delete()
        
        if len(dlp1qbo0) != 0:
            dlp1qbo0[0].d1b0oplq = True
            context.window.screen.scene = bpy.data.scenes[dlp1qbo0[0].name]
            
            do0q1lpb = bpy.data.objects['Terrain_{}'.format(dlp1qbo0[0].name)]
            do0q1lpb.select=True
            context.scene.objects.active = do0q1lpb
            bpy.ops.view3d.view_selected()
        else:
            context.window.screen.scene = bpy.data.scenes['Default_Location']
            context.scene.d1bplq0o = False
            context.scene.d1obqpl0 = True

        
        return {'FINISHED'}
        
    def invoke(self, context, event):

        return context.window_manager.invoke_confirm(self,event)
        
class doq0blp1(bpy.types.Operator):
    bl_idname = "scene.d1lpobq0"
    bl_label = "Switch Locations"
    bl_description = 'Click on a closed eye to switch to selected location'
    
    d1q0pbol = IntProperty()
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dlp1qbo0 = scene.dlp1qbo0
        d1q0pbol = self.d1q0pbol
        
        for location in dlp1qbo0:
            location.d1b0oplq = False
        dlp1qbo0[d1q0pbol].d1b0oplq = True
        
        bpy.context.window.screen.scene = bpy.data.scenes[dlp1qbo0[d1q0pbol].name]
        
        do0q1lpb = bpy.data.objects['Terrain_{}'.format(dlp1qbo0[d1q0pbol].name)]
        do0q1lpb.select=True
        bpy.context.scene.objects.active = do0q1lpb
        bpy.ops.view3d.view_selected()
        
        return {'FINISHED'}
        
class dlpb10oq(bpy.types.Operator):
    bl_idname = "scene.dqb01lop"
    bl_label = "Create Project"
    
    def execute(self, context):
        dp1q0blo()
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'window': window, 'screen': screen, 'area': area, 'region': region}
        bpy.ops.view3d.dolq10pb(override,'INVOKE_DEFAULT')
        
        context.scene.dop1bql0 = False
        context.scene.d1obqpl0 = True
        context.scene.d0p1lqbo = True
        
        return {'FINISHED'}
        
class dl1p0obq(bpy.types.Operator):
    bl_idname = "scene.dbp0oq1l"
    bl_label = "Import Location"
    bl_description = 'Imports a new location'
     
    def execute(self, context):
        d1qlo0pb()
        return {'FINISHED'}

class d01lqpob(bpy.types.Operator):
    bl_idname = "scene.dlp01oqb"
    bl_label = "Create Location"
    
    d0oplq1b = StringProperty(name="Location name:")
    def execute(self, context):
        for location in bpy.data.scenes:
            if location.name == self.d0oplq1b:
                self.report({'WARNING'}, "Location with this name already exists! Try a different name.")
                bpy.ops.scene.dbp0oq1l()
                return {'CANCELLED'}
                
        global dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb,doql1bp0,dlo1q0pb
        d1plqob0(self.d0oplq1b,doql1bp0,dlo1q0pb,dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb)
        
        scene = bpy.data.scenes['Default_Location']
        dlp1qbo0 = scene.dlp1qbo0
        db10ploq = len(dlp1qbo0)
        
        dop0qlb1 = dlp1qbo0.add()
        dop0qlb1.name = self.d0oplq1b
        for location in dlp1qbo0:
            location.d1b0oplq = False
        dop0qlb1.d1b0oplq = True
        scene.d1ol0pbq = db10ploq
        
        context.scene.d1bplq0o = True
        context.scene.d1obqpl0 = False
        
        bpy.ops.wm.save_mainfile()
        return {'FINISHED'}
        
    def invoke(self, context, event):
        self.d0oplq1b = 'Type location name here...'
        return context.window_manager.invoke_props_dialog(self)
        
    def cancel(self, context):
        context.area.type = 'VIEW_3D'
        return {'CANCELLED'}
        
class dp0obq1l(bpy.types.Operator):
    bl_idname = "scene.do0lpb1q"
    bl_label = "Commit Location"
    bl_description = 'Commits all terrain changes to the elevation.bLTe file'

    def execute(self, context):
        d10lboqp()
        return {'FINISHED'}
     
class d1qopbl0(bpy.types.Operator):
    bl_idname = "view2d.d0bqp1ol"
    bl_label = "Pick Location"

    def modal(self, context, event):
        global dqlbpo10,topLeftColumn,bottomRightRow,bottomRightColumn,d1lbpq0o,d1olq0pb,doql1bp0,dlo1q0pb
        context.area.tag_redraw()
        
        dlq01pob = bpy.data.scenes['Default_Location']
        dbl0qpo1 = dlq01pob["dlqp0o1b"]
        dpoq01bl = dlq01pob["d01bopql"]
        
        dlb01qop = context.region.view2d.region_to_view(self.dqlbp1o0,self.dbql0p1o)
        
        dlqobp10,dlo0qbp1,d0plboq1,dl0qopb1 = dobl1p0q(list(dlb01qop),list(self.d0bqlop1))
        
        dqlbpo10, topLeftColumn, bottomRightRow, bottomRightColumn, d1lbpq0o, d1olq0pb, doql1bp0, dlo1q0pb = dlbp0oq1(dpoq01bl,dbl0qpo1,dlqobp10,dlo0qbp1,d0plboq1,dl0qopb1)
        
        self.d0lo1qbp = 'TerrainVerts: {:,}({:,}x{:,})'.format(doql1bp0 * dlo1q0pb,doql1bp0,dlo1q0pb)
        do1q0bpl = 0  if ((doql1bp0 - 1) * (dlo1q0pb - 1)) * 2 <= 0 else ((doql1bp0 - 1) * (dlo1q0pb - 1)) * 2
        self.do1q0bpl = 'TerrainTris: {:,}'.format(do1q0bpl)
        dlp1qb0oX = 0 if (doql1bp0 - 1) * dpoq01bl <= 0 else (doql1bp0 - 1) * dpoq01bl
        self.dlp1qb0o = 'MapSize: {:.2f}x{:.2f} m'.format(dlp1qb0oX, (dlo1q0pb - 1) * dpoq01bl)
        
        if event.type == 'MOUSEMOVE':
            self.dqlbp1o0, self.dbql0p1o = event.mouse_region_x,event.mouse_region_y
            
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.switch = True
            self.db1lpoq0 += 1
            if self.db1lpoq0 == 2:
                if ((doql1bp0 - 1) * (dlo1q0pb - 1)) * 2 <= 0:
                    self.report({'WARNING'}, "No vertices to create a triangle")
                    self.db1lpoq0 = 0
                    self.switch = False
                else:
                    bpy.ops.scene.dlp01oqb('INVOKE_DEFAULT')
                    bpy.types.SpaceImageEditor.draw_handler_remove(self._handle, 'WINDOW')
                    return {'FINISHED'}
                
            self.d0bqlop1 = context.region.view2d.region_to_view(event.mouse_region_x, event.mouse_region_y)
            
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
        self.dqlbp1o0,self.dbql0p1o = 0,0
        self.db1lpoq0 = 0
        self.d0bqlop1 = [0,0]
        self.switch = False
        
        if context.area.type == 'IMAGE_EDITOR':
            args = (self, context)
            self._handle = bpy.types.SpaceImageEditor.draw_handler_add(d10qlobp, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Image Editor not found, cannot run operator")
            return {'CANCELLED'}
 
class d01poqlb(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.dolq10pb"
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
            self._handle = bpy.types.SpaceView3D.draw_handler_add(d1bl0opq, args, 'WINDOW', 'POST_PIXEL')
            d0lqop1b = dob01qpl()[2]
            if bpy.data.images.get('splash.png') is None:
                bpy.data.images.load('{}\\splash.png'.format(d0lqop1b))
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

class dqp0lob1(bpy.types.Operator):
    bl_idname = "object.dolpb0q1"
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

class dpblo1q0(bpy.types.Operator):
    bl_idname = "object.dlb10opq"
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

class doq10lbp(bpy.types.Operator):
    bl_idname = "scene.d1lq0pbo"
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

class db0op1lq(bpy.types.Operator):
    bl_idname = "scene.dbol1pq0"
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

class dlpo01qb(bpy.types.Operator):
    bl_idname = "scene.d0obql1p"
    bl_label = "Generate flat terrain"
    
    dpoq01bl = FloatProperty(name="Cell size:",default=1.0)
    d10pqolb = IntProperty(name="Grid resolution:",default=512)
    dpolb01q = FloatProperty(name="Default height:",default=10.0)
    
    def execute(self, context):
        dq01olpb(self.dpoq01bl,self.d10pqolb,self.dpolb01q)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
class dopblq10(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Project Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.dlo01pqb = BoolProperty(name="",
        description="",
        default=False)
    
    Scene.db0pl1oq = StringProperty(name="",
        attr="projFolderPath",
        description="Path to project folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='')
    
    Scene.dlqop10b = StringProperty(name="",
        attr="satellitePath",
        description="Path to terrain texture",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=d01lqobp)

    Scene.dlbo0qp1 = StringProperty(name="",
        attr="terrainPath",
        description="Path to terrain heightmap to create 3D terrain",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=dlbpo1q0)
        
    Scene.doplq0b1 = StringProperty(name="",
        attr="terrainPath",
        description="Path to bLT internal elevation file",
        maxlen= 1024,
        subtype='FILE_PATH')
        
    db1l0opq = [
    ("RVEngine", "RVEngine", "", 1),
    ("Unreal Engine 4", "Unreal Engine 4", "", 2),
    ("CryEngine", "CryEngine", "", 3),
    ("Unity", "Unity", "", 4),
    ("Enfusion", "Enfusion", "", 5)
    ]

    Scene.dq0b1pol = bpy.props.EnumProperty(items=db1l0opq,name="Engine",default='RVEngine')
    
    Scene.dop1bql0 = BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dop1bql0

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        box = layout.box()
        row = box.column()
        row.label(text="Project Folder")
        row.prop(scene,'db0pl1oq')
        row.separator()
        row.prop(scene, 'dq0b1pol')

        row3 = box.column()
        row3.separator()
        row3.operator("scene.dqb01lop",text='Create Project')
        
        if scene.db0pl1oq is '':
            row3.enabled = False
        else:
            row3.enabled = True
                
class d1bo0qpl(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Data Source"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.d1obqpl0 = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d1obqpl0

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        
        box = layout.box()
        row1 = box.column()
        row1.label(text="Terrain texture")
        row2 = row1.column(align=True)
        row2.prop(scene, 'dlqop10b')
        row2.separator()
        row2.label(text="Terrain Heightmap")
        row2.prop(scene, 'dlbo0qp1')
        
        if len(bpy.data.scenes) > 1:
            row1.enabled = False
            row2.enabled = False
                
        
class d1qpbo0l(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Locations manager"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    
    Scene.dq1bplo0 = BoolProperty(name="",
    description="",
    default=False)
    
    Scene.d0p1lqbo = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d0p1lqbo

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        if scene.dlo01pqb:
            row.template_list("d1bp0qol", "", bpy.data.scenes['Default_Location'], "dlp1qbo0", bpy.data.scenes['Default_Location'], "d1ol0pbq")
        col = row.column()
        row1 = col.row()
        row1.operator("scene.dbp0oq1l",icon='ZOOMIN',text="")
        if scene.dlbo0qp1 is '':#would be nice to have also check for supported file types
            row1.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row1.enabled = False
                    
        row2 = col.row()        
        row2.operator("scene.do0lpb1q",icon='APPEND_BLEND',text="")
        if not scene.dq1bplo0:
            row2.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row2.enabled = False    
        
        row3 = col.row()        
        row3.operator("scene.dl01boqp",icon='ZOOMOUT',text="")
        if not scene.dq1bplo0:
            row3.enabled = False
        elif len(bpy.data.scenes["Default_Location"].dlp1qbo0) == 0:
            row3.enabled = False  
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row3.enabled = False    
       
   
                
            

class d10qbolp(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Location/Object(s) Appearance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.d1bplq0o = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.d1bplq0o

    def draw(self, context):
        scene = context.scene
        view = context.space_data
        layout = self.layout
        fx_settings = view.fx_settings
        
        row = layout.row(align=True)
        row.operator("object.dlb10opq",icon='TEXTURE')
        row.operator("object.dolpb0q1",icon='ASSET_MANAGER')
        row2 = layout.row(align=True)
        row2.operator("object.shade_smooth", text="Smooth",icon='MOD_SMOOTH')
        row2.operator("object.shade_flat", text="Flat",icon='MOD_DISPLACE')
        row1 = layout.row(align=True)
        row1.operator("scene.d1lq0pbo",icon='MATCAP_13')
        row1.operator("scene.dbol1pq0",icon='MOD_TRIANGULATE')
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                if  Area.spaces.active.use_matcap == True and Area.spaces.active.viewport_shade == 'SOLID':
                    row4 = layout.row(align=False)
                    row4.template_icon_view(view, "matcap_icon")
                    if not scene.dq1bplo0:
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
                    
        if not scene.dq1bplo0:
            row.enabled = False 
            row1.enabled = False
            row2.enabled = False
            
            col.enabled = False
            
class dql0pb1o(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Create"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout

        row = layout.row(align=True)
        row.operator("scene.d0obql1p",icon='MESH_GRID')
        
