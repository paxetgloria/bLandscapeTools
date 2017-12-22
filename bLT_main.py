import bpy

from .bLT_utils import *

from bpy.props import StringProperty,FloatProperty,IntProperty,BoolProperty,EnumProperty,CollectionProperty,FloatVectorProperty
from bpy.types import Panel,Scene,AddonPreferences,UIList,PropertyGroup,WindowManager,Object
from bl_ui.properties_paint_common import UnifiedPaintPanel, brush_texture_settings, brush_texpaint_common

class d31lusmea(bpy.types.Operator):
    bl_idname = "a.dlsa31meu"
    bl_label = "Install OpenCV"
    bl_description = 'Installs OpenCV'

    def execute(self, context):
        dlsa31meu()
        return {'FINISHED'}

class dlumae31s(PropertyGroup):
    dmusle31a = BoolProperty(name="",default=False)
    
class daslme31u(PropertyGroup):
    name = StringProperty(name="Brush Name")
            
class dua31mesl(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name", text="", emboss=False)
        
        icon = 'RESTRICT_VIEW_OFF' if item.dmusle31a else 'RESTRICT_VIEW_ON'
        op = layout.operator("scene.dmalsu31e", text="", emboss=False, icon=icon)
        op.dl31esaum = index

class d31lseaum(bpy.types.Operator):
    bl_idname = "scene.dsmle31ua"
    bl_label = "Remove Location"
    bl_options = {'REGISTER'}
    bl_description = 'Removes current location(eye icon) without commiting any changes!!!'

    @classmethod
    def poll(cls, context):
        return context.scene.dl31aesum == False and context.scene.dsem31alu == False
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dmusa31el = scene.dmusa31el
        
        du31almes = context.scene.name
        
        for index, location in enumerate(dmusa31el):
            if location.name == du31almes:
                dl31esaum = index
        
        scene.dmusa31el.remove(dl31esaum)
        bpy.ops.scene.delete()
        
        
        bpy.data.objects.remove(bpy.data.objects['Terrain_{}'.format(du31almes)])
        bpy.data.meshes.remove(bpy.data.meshes['TerrainMesh_{}'.format(du31almes)])
        if bpy.data.materials.get('TerrainMaterial_{}'.format(du31almes)) is not None:
            bpy.data.materials.remove(bpy.data.materials['TerrainMaterial_{}'.format(du31almes)])
        if bpy.data.textures.get('TerrainTexture_{}'.format(du31almes)) is not None:
            bpy.data.textures.remove(bpy.data.textures['TerrainTexture_{}'.format(du31almes)])
        if bpy.data.textures.get('TerrainMask_{}'.format(du31almes)) is not None:
            bpy.data.textures.remove(bpy.data.textures['TerrainMask_{}'.format(du31almes)])
        if bpy.data.images.get('TerrainImage_{}.png'.format(du31almes)) is not None:
            dm31luase = bpy.data.images['TerrainImage_{}.png'.format(du31almes)].filepath
            bpy.data.images.remove(bpy.data.images['TerrainImage_{}.png'.format(du31almes)])    
            if os.path.isfile(dm31luase):
                os.remove(dm31luase)
            
        if bpy.data.images.get('TerrainMask_{}.png'.format(du31almes)) is not None:
            dm31luase = bpy.data.images['TerrainMask_{}.png'.format(du31almes)].filepath
            bpy.data.images.remove(bpy.data.images['TerrainMask_{}.png'.format(du31almes)])
            if os.path.isfile(dm31luase):
                os.remove(dm31luase)
 
        bpy.data.grease_pencil["OccupiedLocations"].layers.remove(bpy.data.grease_pencil["OccupiedLocations"].layers[du31almes])
        
        if len(dmusa31el) != 0:
            dmusa31el[0].dmusle31a = True
            context.window.screen.scene = bpy.data.scenes[dmusa31el[0].name]
            
            dlmsa31ue = bpy.data.objects['Terrain_{}'.format(dmusa31el[0].name)]
            dlmsa31ue.hide_select = False
            dlmsa31ue.select = True
            context.scene.objects.active = dlmsa31ue
            bpy.ops.view3d.view_selected()
            dlmsa31ue.select = False
            dlmsa31ue.hide_select = True
        else:
            context.window.screen.scene = bpy.data.scenes['Default_Location']
            context.scene.due31alms = False
            context.scene.d31mlesau = True
            
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self,event)
        
class duesla31m(bpy.types.Operator):
    bl_idname = "scene.dmalsu31e"
    bl_label = "Switch Locations"
    bl_description = 'Click on a closed eye to switch to selected location'
    
    dl31esaum = IntProperty()
    
    def execute(self, context):
        scene = bpy.data.scenes['Default_Location']
        dmusa31el = scene.dmusa31el
        dl31esaum = self.dl31esaum
        
        for location in dmusa31el:
            location.dmusle31a = False
        dmusa31el[dl31esaum].dmusle31a = True
        
        bpy.context.window.screen.scene = bpy.data.scenes[dmusa31el[dl31esaum].name]
        context.scene.layers[0] = True
        
        dlmsa31ue = bpy.data.objects['Terrain_{}'.format(dmusa31el[dl31esaum].name)]
        dlmsa31ue.hide_select = False
        dlmsa31ue.select = True
        bpy.context.scene.objects.active = dlmsa31ue
        bpy.ops.view3d.view_selected()
        dlmsa31ue.select = False
        dlmsa31ue.hide_select = True
        
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class d31amselu(bpy.types.Operator):
    bl_idname = "scene.dslum31ae"
    bl_label = "Create Project"
    
    def execute(self, context):
        dlm31suea()
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'window': window, 'screen': screen, 'area': area, 'region': region}
        bpy.ops.view3d.dasmuel31(override,'INVOKE_DEFAULT')
        
        context.scene.dlesamu31 = False
        context.scene.d31mlesau = True
        context.scene.dslaeum31 = True
        
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class daes31lum(bpy.types.Operator):
    bl_idname = "scene.dea31ulsm"
    bl_label = "Import Location"
    bl_description = 'Imports a new location'
     
    @classmethod
    def poll(cls, context):
        return (context.scene.dl31aesum == False 
        and context.scene.dsem31alu == False 
        and context.scene.deal31mus 
        and (context.scene.demual31s == '' or context.scene.du31lames)
        and (context.scene.dumlse31a == '' or context.scene.dml31eaus))

    def execute(self, context):
        demusla31()
        return {'FINISHED'}

class du31aseml(bpy.types.Operator):
    bl_idname = "scene.delusma31"
    bl_label = "Create Location"
    
    du31almes = StringProperty(name="Location name:")
    
    def execute(self, context):
        for location in bpy.data.scenes:
            if location.name == self.du31almes:
                self.report({'WARNING'}, "Location with this name already exists! Try a different name.")
                bpy.ops.scene.dea31ulsm()
                return {'CANCELLED'}
        
        if self.du31almes == '':
            self.report({'WARNING'}, "Location must have a name!")
            bpy.ops.scene.dea31ulsm()
            return {'CANCELLED'}
                
        global duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu,dl31uemsa,delas31um
        d31smleua(self.du31almes,dl31uemsa,delas31um,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu)
        
        scene = bpy.data.scenes['Default_Location']
        dmusa31el = scene.dmusa31el
        dals31emu = len(dmusa31el)
        
        d31ualesm = dmusa31el.add()
        d31ualesm.name = self.du31almes
        for location in dmusa31el:
            location.dmusle31a = False
        d31ualesm.dmusle31a = True
        scene.dlaumes31 = dals31emu

        context.scene.due31alms = True
        context.scene.d31mlesau = False
        context.scene.ds31mlaue = True
        if context.scene.du31lames and context.scene.dml31eaus:
            context.scene.dameuls31 = True
            
        dslemu31a(self.du31almes,duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu)
        
        bpy.ops.wm.save_mainfile()
        return {'FINISHED'}
        
    def invoke(self, context, event):
        self.du31almes = ''
        return context.window_manager.invoke_props_dialog(self)
        
    def cancel(self, context):
        context.area.type = 'VIEW_3D'
        return {'CANCELLED'}
        
class dm31easlu(bpy.types.Operator):
    bl_idname = "scene.dume31sal"
    bl_label = "Commit Location"
    bl_description = 'Commits terrain/surface mask changes from the current location'
    
    dlsamue31 = BoolProperty(description="Checked: Data will be written to paths defined in Data Source panel\nUnchecked: Data will be written to the Output folder within the Project folder", name="Overwrite source data",default=False)
    d31eamlus = BoolProperty(description="Commit elevation", name="Elevation",default=True)
    dum31elas = BoolProperty(description="Commit surface mask", name="Surface mask",default=True)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dl31aesum == False and context.scene.dsem31alu == False
    
    def execute(self, context):
        if self.d31eamlus:
            dauslm31e(self.dlsamue31)
        if self.dum31elas:
            dua31mles(self.dlsamue31)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
     
class dse31lmau(bpy.types.Operator):
    bl_idname = "view2d.ds31meaul"
    bl_label = "Pick Location"

    def modal(self, context, event):
        global duseml31a,dem31lasu,dmleuas31,deulm31as,dmselau31,d31esamlu,dl31uemsa,delas31um
        context.area.tag_redraw()
        
        d31ulemas = bpy.data.scenes['Default_Location']
        dlmuae31s = d31ulemas["da31mlues"]
        dl31mseau = d31ulemas["ds31uamle"]
        
        dualme31s = context.region.view2d.region_to_view(self.dalms31ue,self.de31amlus)
        
        dua31smel,dmlsa31eu,dsmlu31ae,dual31ems = dulmse31a(list(dualme31s),list(self.desuam31l))
        
        duseml31a, dem31lasu, dmleuas31, deulm31as, dmselau31, d31esamlu, dl31uemsa, delas31um = dlu31maes(dl31mseau,dlmuae31s,dua31smel,dmlsa31eu,dsmlu31ae,dual31ems)
        
        self.d31ulaems = 'TerrainVerts: {:,}({:,}x{:,})'.format(dl31uemsa * delas31um,dl31uemsa,delas31um)
        dsau31eml = 0  if ((dl31uemsa - 1) * (delas31um - 1)) * 2 <= 0 else ((dl31uemsa - 1) * (delas31um - 1)) * 2
        self.dsau31eml = 'TerrainTris: {:,}'.format(dsau31eml)
        d31lsaeumX = 0 if (dl31uemsa - 1) * dl31mseau <= 0 else (dl31uemsa - 1) * dl31mseau
        self.d31lsaeum = 'MapSize: {:.2f}x{:.2f} m'.format(d31lsaeumX, (delas31um - 1) * dl31mseau)
        
        if event.type == 'MOUSEMOVE':
            self.dalms31ue, self.de31amlus = event.mouse_region_x,event.mouse_region_y
            
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.switch = True
            self.dseul31am += 1
            if self.dseul31am == 2:
                if ((dl31uemsa - 1) * (delas31um - 1)) * 2 <= 0:
                    self.report({'WARNING'}, "No vertices to create a triangle")
                    self.dseul31am = 0
                    self.switch = False
                else:
                    bpy.ops.scene.delusma31('INVOKE_DEFAULT')
                    bpy.types.SpaceImageEditor.draw_handler_remove(self._handle, 'WINDOW')
                    return {'FINISHED'}
                
            self.desuam31l = context.region.view2d.region_to_view(event.mouse_region_x, event.mouse_region_y)
            
        elif event.type == 'BACK_SPACE':
            if bpy.data.images.get('previewSatTex.png') is not None and bpy.data.images.get('previewTerTex.tif') is not None:
                for space in bpy.context.area.spaces:
                    if space.type == 'IMAGE_EDITOR':
                        dme31uasl = space.image.name

                if dme31uasl == 'previewSatTex.png':
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
        self.dalms31ue,self.de31amlus = 0,0
        self.dseul31am = 0
        self.desuam31l = [0,0]
        self.switch = False
        
        if context.area.type == 'IMAGE_EDITOR':
            args = (self, context)
            self._handle = bpy.types.SpaceImageEditor.draw_handler_add(daseu31lm, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Image Editor not found, cannot run operator")
            return {'CANCELLED'}
 
class dsmaul31e(bpy.types.Operator):
    bl_idname = "view3d.dasmuel31"
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
            self._handle = bpy.types.SpaceView3D.draw_handler_add(dsml31eau, args, 'WINDOW', 'POST_PIXEL')
            dmseul31a = dusaem31l()[2]
            if bpy.data.images.get('splash.png') is None:
                bpy.data.images.load('{}\\splash.png'.format(dmseul31a))
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

class dmelsa31u(bpy.types.Operator):
    bl_idname = "object.dlasume31"
    bl_label = "Assign Mesh Terrain Modifier"
    bl_description = 'Assigns a mesh terrain modifier to selected object(only MESH type)'
    
    @classmethod
    def poll(cls, context):
        return (context.active_object is not None
        and context.active_object.dupli_group is not None
        and context.active_object.name.split('_')[0] != 'Flatter'
        and len(context.active_object.children) == 0
        and len(context.selected_objects) == 1
        and context.active_object.mode not in {'SCULPT','EDIT','TEXTURE_PAINT'}
        and context.active_object.type == 'EMPTY')

    def execute(self, context):
        de31smlau(context)
        
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class dle31uams(bpy.types.Operator):
    bl_idname = "object.dau31emsl"
    bl_label = "Add Mesh Terrain Modifier"
    bl_description = 'Adds a mesh terrain modifier at 3D cursor position'
    
    @classmethod
    def poll(cls, context):
        de31lsuam = True
        if context.active_object is not None:
            if context.active_object.mode in {'SCULPT','EDIT','TEXTURE_PAINT'}:
                de31lsuam = False  
        return de31lsuam

    def execute(self, context):
        d31luaesm(context)
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class dlause31m(bpy.types.Operator):
    bl_idname = "object.duaml31se"
    bl_label = "Apply Mesh Terrain Modifier(s)"
    bl_description = 'Applies terrain changes from all selected objects and removes terran modifier from the scene'
    
    @classmethod
    def poll(cls, context):
        d31esumla = True
        dm31lueas = True

        for ob in context.selected_objects:
            if len(ob.children) == 0:
                dm31lueas = False
            if ob.type != 'EMPTY':
                d31esumla = False
        return (len(context.selected_objects) != 0 and d31esumla and dm31lueas)

    def execute(self, context):
        dl31uasme(context)
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class damsul31e(bpy.types.Operator):
    bl_idname = "object.dlsmaeu31"
    bl_label = "Add Spline Terrain Modifier"
    bl_description = 'Adds a spline terrain modifier at 3D cursor location'
    
    @classmethod
    def poll(cls, context):
        de31lsuam = False
        if context.active_object is None:
            de31lsuam = True
        else:
            if context.active_object.mode not in {'SCULPT','EDIT','TEXTURE_PAINT'}:
                de31lsuam = True
        return de31lsuam
        
    def execute(self, context):
        d31mlueas(context)
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class deas31uml(bpy.types.Operator):
    bl_idname = "object.dlsema31u"
    bl_label = "Apply Spline Terrain Modifier(s)"
    bl_description = 'Applies terrain changes and removes terran modifier from the scene'
    
    @classmethod
    def poll(cls, context):
        dauesm31l = True
        
        for ob in context.selected_objects:
            if ob.type != 'CURVE':
                dauesm31l = False
        return (len(context.selected_objects) != 0 and dauesm31l and context.active_object.mode not in 'EDIT')

    def execute(self, context):
        dlsu31eam(context)
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
            
class duame31ls(bpy.types.Operator):
    bl_idname = "object.dmslae31u"
    bl_label = "Textured + Wire overlay"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'TEXTURED'
        
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.show_wire = True
        dlmsa31ue.show_all_edges = True
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}

class da31emslu(bpy.types.Operator):
    bl_idname = "object.ds31ealmu"
    bl_label = "Textured"

    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'TEXTURED'
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.show_wire = False
        dlmsa31ue.show_all_edges = False
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class dmasel31u(bpy.types.Operator):
    bl_idname = "object.dms31laue"
    bl_label = "Smooth"

    
    @classmethod
    def poll(cls, context):
        return not context.scene.dsem31alu
    
    def execute(self, context):
        if context.active_object is not None and context.active_object.mode == 'SCULPT':
            bpy.ops.object.mode_set(mode='OBJECT')
            context.active_object.hide_select = False
            context.active_object.select = True
            bpy.ops.object.shade_smooth()
            context.active_object.select = False
            context.active_object.hide_select = True
            bpy.ops.object.mode_set(mode='SCULPT')
        else:
            daulm31es = context.active_object if context.active_object is not None else None
            bpy.ops.object.select_all(action='DESELECT')
            dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
            dlmsa31ue.hide_select = False
            dlmsa31ue.select = True
            bpy.ops.object.shade_smooth()
            dlmsa31ue.select = False
            dlmsa31ue.hide_select = True
            if daulm31es is not None:
                daulm31es.select = True
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}
        
class dmeas31lu(bpy.types.Operator):
    bl_idname = "object.da31umsle"
    bl_label = "Flat"
    
    @classmethod
    def poll(cls, context):
        return not context.scene.dsem31alu
    
    def execute(self, context):
        if context.active_object is not None and context.active_object.mode == 'SCULPT':
            bpy.ops.object.mode_set(mode='OBJECT')
            context.active_object.hide_select = False
            context.active_object.select = True
            bpy.ops.object.shade_flat()
            context.active_object.select = False
            context.active_object.hide_select = True
            bpy.ops.object.mode_set(mode='SCULPT')
        else:
            daulm31es = context.active_object if context.active_object is not None else None
            bpy.ops.object.select_all(action='DESELECT')
            dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
            dlmsa31ue.hide_select = False
            dlmsa31ue.select = True
            bpy.ops.object.shade_flat()
            dlmsa31ue.select = False
            dlmsa31ue.hide_select = True
            if daulm31es is not None:
                daulm31es.select = True
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}

class dusem31la(bpy.types.Operator):
    bl_idname = "scene.d31auemls"
    bl_label = "MatCap"

    @classmethod
    def poll(cls, context):
        return not context.scene.dsem31alu
    
    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'SOLID'
                Area.spaces.active.use_matcap = True
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.show_wire = False
        dlmsa31ue.show_all_edges = False
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}

class dsaelmu31(bpy.types.Operator):
    bl_idname = "scene.del31umas"
    bl_label = "MatCap + Wire overlay"

    @classmethod
    def poll(cls, context):
        return not context.scene.dsem31alu
    
    def execute(self, context):
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                Area.spaces.active.viewport_shade = 'SOLID'
                Area.spaces.active.use_matcap = True
        dlmsa31ue = bpy.data.objects['Terrain_' + context.scene.name]
        dlmsa31ue.show_wire = True
        dlmsa31ue.show_all_edges = True
        daue31msl = context.scene.daue31msl
        dsm31ueal = 'Project_{}'.format(daue31msl.split('\\')[-2])
        bpy.ops.wm.save_as_mainfile(filepath='{}{}.blend'.format(daue31msl,dsm31ueal))
        return {'FINISHED'}

class dulema31s(bpy.types.Operator):
    bl_idname = "scene.dsl31aume"
    bl_label = "Generate flat terrain"
    bl_description = 'Generates a flat terrain asc file and writes it to\nthe Output folder defined in addon\'s preferences'
    
    dl31mseau = FloatProperty(name="Cell size:",default=1.0,min=.0)
    desm31ula = IntProperty(name="Grid resolution:",default=512,min=0)
    dlseau31m = FloatProperty(name="Default elevation:",default=10.0)
    
    def execute(self, context):
        dseamlu31(self.dl31mseau,self.desm31ula,self.dlseau31m)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
class dmelas31u(bpy.types.Operator):
    bl_idname = "scene.create_surfacemask"
    bl_label = "Generate empty surface mask"
    bl_description = 'Generates a raster filled with a default color in png format and writes it to\nthe Output folder defined in addon\'s preferences'
    
    dmulae31s = IntProperty(name="Image resolution(px):",default=5000,min=0)
    dumal31se = FloatVectorProperty(name="Default color:",min=0.0,max=1.0,subtype='COLOR')
    
    def execute(self, context):
        d31usemla(self.dmulae31s,self.dumal31se)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
class demus31al(bpy.types.Operator):
    bl_idname = "scene.dmules31a"
    bl_label = "Check surface mask"
    bl_description = 'Generates a raster with information about the count of surfaces per texture tile'
    
    dl31mseau = FloatProperty(name="Cell size(m):",default=7.5,min=0.0)
    desm31ula = IntProperty(name="Terrain grid resolution(px):",default=2048,min=0)
    dmsauel31 = FloatProperty(name="Mask resolution(m/px):",default=1.0,min=0.1)
    dslame31uList = [
    ("512", "512", "", 1),
    ("1024", "1024", "", 2),
    ("2048", "2048", "", 3),
    ("4096", "4096", "", 4)]
    dslame31u = EnumProperty(items=dslame31uList,name="Tile size(px):",default='512')

    @classmethod
    def poll(cls, context):
        return context.scene.dl31ueasm or context.scene.dml31eaus
    
    def execute(self, context):
        du31slema(context,self.dl31mseau,self.desm31ula,self.dslame31u,self.dmsauel31)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
class dmea31usl(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Project Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.desl31uma = BoolProperty(name="",
        description="",
        default=False)
    
    Scene.daue31msl = StringProperty(name="",
        attr="projFolderPath",
        description="Path to project folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='')
        
    Scene.d31emusal = StringProperty(name="",
        attr="terrainPath",
        description="Path to bLT internal elevation file",
        maxlen= 1024,
        subtype='FILE_PATH')
        
    dea31muls = [
    ("RVEngine", "RVEngine", "", 1),
    ("Unreal Engine 4", "Unreal Engine 4", "", 2),
    ("CryEngine", "CryEngine", "", 3),
    ("Unity", "Unity", "", 4),
    ("Enfusion", "Enfusion", "", 5)
    ]

    Scene.d31usmale = EnumProperty(items=dea31muls,name="Engine",default='RVEngine')
    
    Scene.dlesamu31 = BoolProperty(default=True)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dlesamu31

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        box = layout.box()
        row = box.column()
        row.label(text="Project Folder")
        row.prop(scene,'daue31msl')
        row.separator()
        row.prop(scene, 'd31usmale')

        row3 = box.column()
        row3.separator()
        row3.operator("scene.dslum31ae",text='Create Project')
        
        if scene.daue31msl is '':
            row3.enabled = False
        else:
            row3.enabled = True
                
class dseaml31u(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Data Source"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    Scene.d31mlesau = BoolProperty(default=False)
    Scene.demual31s = StringProperty(name="Terrain Texture",
        description="Any imagery format supported by GDAL",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=dl31seamu)

    Scene.dlsumea31 = StringProperty(name="Terrain Heightmap",
        description="Supports ARC/INFO ASCII GRID only",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=delmsa31u)
        
    Scene.dumlse31a = StringProperty(name="Terrain Splat Mask",
        description="",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=dulae31ms)
        
    Scene.dl31uesma = StringProperty(name="Surfaces Definition",
        description="",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=dlmeuas31)
        
    Scene.deal31mus = BoolProperty(default=False)
    Scene.du31lames = BoolProperty(default=False)
    Scene.dml31eaus = BoolProperty(default=False)
    Scene.ds31aulem = BoolProperty(default=False)
    
    
    dem31laus = [("", "", "", 0),("A:\\", "A:\\", "", 1),("B:\\", "B:\\", "", 2),("C:\\", "C:\\", "", 3),("D:\\", "D:\\", "", 4),
    ("E:\\", "E:\\", "", 5),("F:\\", "F:\\", "", 6),("G:\\", "G:\\", "", 7),("I:\\", "I:\\", "", 8),("J:\\", "J:\\", "", 9),("K:\\", "K:\\", "", 10),("L:\\", "L:\\", "", 11),("M:\\", "M:\\", "", 12),("N:\\", "N:\\", "", 13),("O:\\", "O:\\", "", 14),
    ("P:\\", "P:\\", "", 15),("Q:\\", "Q:\\", "", 16),("R:\\", "R:\\", "", 17),("S:\\", "S:\\", "", 18),("T:\\", "T:\\", "", 19),("U:\\", "U:\\", "", 20),("V:\\", "V:\\", "", 21),("W:\\", "W:\\", "", 22),("X:\\", "X:\\", "", 23),("Y:\\", "Y:\\", "", 24),
    ("Z:\\", "Z:\\", "", 25)
    ]

    Scene.de31sulma = bpy.props.EnumProperty(items=dem31laus,name="Dev. Drive",description="Sets the letter of the developer's drive",default="",update=de31smlua)

    
    @classmethod
    def poll(cls, context):
        return context.scene.d31mlesau

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        box = layout.box()
        row1 = box.column()
        row1.prop(scene, 'demual31s')
        row1.prop(scene, 'dlsumea31')
        row2 = box.column()
        row2.prop(scene, 'dumlse31a')
        row3 = box.column()
        row3.prop(scene, 'dl31uesma')
        row4 = box.column()
        row4.prop(scene, 'de31sulma')
        
        if not scene.du31lames:
            row2.enabled = False
        if not scene.dml31eaus:
            row4.enabled = False
        if not scene.dml31eaus or not scene.ds31aulem:
            row3.enabled = False
        
class delsmau31(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Locations manager"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    Scene.dlm31saue = BoolProperty(name="",
    description="",
    default=False)
    
    Scene.dslaeum31 = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.dslaeum31

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        col = layout.column()
        
        if context.scene['dlm31saue']:
            if len(bpy.data.objects['Terrain_' + context.scene.name].modifiers) != 0:
                col.label(text='Terrain has modifier(s) assigned, BE CAREFUL!',icon='ERROR')
        row = layout.row()
        if scene.desl31uma:
            row.template_list("dua31mesl", "", bpy.data.scenes['Default_Location'], "dmusa31el", bpy.data.scenes['Default_Location'], "dlaumes31")
        col = row.column()
        row1 = col.row()
        row1.operator("scene.dea31ulsm",icon='ZOOMIN',text="")
        if bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row1.enabled = False
                    
        row2 = col.row()        
        row2.operator("scene.dume31sal",icon='APPEND_BLEND',text="")
        if not scene.dlm31saue:
            row2.enabled = False
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row2.enabled = False    
        
        row3 = col.row()        
        row3.operator("scene.dsmle31ua",icon='ZOOMOUT',text="")
        if not scene.dlm31saue:
            row3.enabled = False
        elif len(bpy.data.scenes["Default_Location"].dmusa31el) == 0:
            row3.enabled = False  
        elif bpy.context.object is not None:
            if bpy.context.object.mode == 'EDIT':
                row3.enabled = False    
       
   
                
            

class View3DPaintPanel(UnifiedPaintPanel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
                
class dea31lsmu(Panel,View3DPaintPanel):
    bl_category = "bLandscape Tools"
    bl_label = "Terrain Editing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.ds31mlaue = BoolProperty(default=False)
    
    Scene.dl31aesum = BoolProperty(default=False,update=dmalseu31)
    
    Scene.dusl31mea = BoolProperty(default=False)
    Scene.dslmeua31 = BoolProperty(default=False)
    Scene.d31uamles = BoolProperty(default=False)
    Object.dameslu31 = FloatProperty(default=1,update=d31umlesa)
    
    @classmethod
    def poll(cls, context):
        return (context.scene.ds31mlaue or cls.paint_settings(context) or context.sculpt_object)

    def draw(self, context):
        scene = context.scene
        object = context.active_object
        layout = self.layout
       
        col = layout.column()
        
        
        if scene.dl31aesum:
            text = 'Disable Terrain Sculpting'     
        else:
            text = 'Enable Terrain Sculpting'
        col.prop(scene, "dl31aesum", text=text, icon="SCULPTMODE_HLT")
        if scene.dsem31alu:
            col.enabled = False
        
        if len(bpy.data.objects['Terrain_' + context.scene.name].modifiers) != 0:
            col.label(text='Terrain has modifier(s) assigned, BE CAREFUL!',icon='ERROR')

        if scene.dl31aesum:
            toolsettings = context.tool_settings
            settings = self.paint_settings(context)
            brush = settings.brush
            
            box = layout.box()            
            col = box.column()
            col.label(text='Brush settings')
            
            if not context.particle_edit_object:
                col.separator()
                col.separator()
                col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)
            
            capabilities = brush.sculpt_capabilities
            col.separator()
            row = col.row(align=True)
            ups = toolsettings.unified_paint_settings
            if ((ups.use_unified_size and ups.use_locked_size) or
                    ((not ups.use_unified_size) and brush.use_locked_size)):
                self.prop_unified_size(row, context, brush, "use_locked_size", icon='LOCKED')
                self.prop_unified_size(row, context, brush, "unprojected_radius", slider=True, text="Radius")
            else:
                self.prop_unified_size(row, context, brush, "use_locked_size", icon='UNLOCKED')
                self.prop_unified_size(row, context, brush, "size", slider=True, text="Radius")
                
            self.prop_unified_size(row, context, brush, "use_pressure_size")

            col.separator()
            row = col.row(align=True)

            if capabilities.has_space_attenuation:
                row.prop(brush, "use_space_attenuation", toggle=True, icon_only=True)

            self.prop_unified_strength(row, context, brush, "strength", text="Strength")

            if capabilities.has_strength_pressure:
                self.prop_unified_strength(row, context, brush, "use_pressure_strength")

            if capabilities.has_auto_smooth:
                col.separator()

                row = col.row(align=True)
                row.prop(brush, "auto_smooth_factor", slider=True)
                row.prop(brush, "use_inverse_smooth_pressure", toggle=True, text="")

            if capabilities.has_sculpt_plane:
                col.separator()
                row = col.row(align=True)

                row.prop(brush, "use_original_normal", toggle=True, icon_only=True)

                row.prop(brush, "sculpt_plane", text="")

            if brush.sculpt_tool == 'MASK':
                col.prop(brush, "mask_tool", text="")
                
            if capabilities.has_plane_offset:
                row = col.row(align=True)
                row.prop(brush, "plane_offset", slider=True)
                row.prop(brush, "use_offset_pressure", text="")

                col.separator()

                row = col.row()
                row.prop(brush, "use_plane_trim", text="Trim")
                row = col.row()
                row.active = brush.use_plane_trim
                row.prop(brush, "plane_trim", slider=True, text="Distance")

            if capabilities.has_height:
                row = col.row()
                row.prop(brush, "height", slider=True, text="Height")
                
            col.separator()
            row = col.row()
            row.prop(brush, "use_frontface", text="Front Faces Only")

            col.separator()
            col.row().prop(brush, "direction", expand=True)

            if capabilities.has_accumulate:
                col.separator()

                col.prop(brush, "use_accumulate")

            if capabilities.has_persistence:
                col.separator()

                ob = context.sculpt_object
                do_persistent = True

                for md in ob.modifiers:
                    if md.type == 'MULTIRES':
                        do_persistent = False
                        break

                if do_persistent:
                    col.prop(brush, "use_persistent")
                    col.operator("sculpt.set_persistent_base")
            
            col = layout.column()
            col.separator()
            
            box = layout.box()            
            col = box.column()
            col.prop(scene, "dusl31mea", text='Sculpt Texture Settings', icon="TEXTURE")
            
            if scene.dusl31mea:
                col.template_ID_preview(brush, "texture", new="texture.new", rows=3, cols=8)
                brush_texture_settings(col, brush, context.sculpt_object)
                
            
            col = layout.column()
            col.separator()

            box = layout.box()            
            col = box.column()
            col.prop(scene, "dslmeua31", text='Stroke Settings', icon="BRUSH_DATA")
            
            if scene.dslmeua31:
                col.label(text="Stroke Method:")
                col.prop(brush, "stroke_method", text="")
                
                if brush.use_anchor:
                    col.separator()
                    col.prop(brush, "use_edge_to_edge", "Edge To Edge")

                if brush.use_airbrush:
                    col.separator()
                    col.prop(brush, "rate", text="Rate", slider=True)

                if brush.use_space:
                    col.separator()
                    row = col.row(align=True)
                    row.prop(brush, "spacing", text="Spacing")
                    row.prop(brush, "use_pressure_spacing", toggle=True, text="")

                if brush.use_line or brush.use_curve:
                    col.separator()
                    row = col.row(align=True)
                    row.prop(brush, "spacing", text="Spacing")

                if brush.use_curve:
                    col.separator()
                    col.template_ID(brush, "paint_curve", new="paintcurve.new")
                    col.operator("paintcurve.draw")

                if context.sculpt_object:
                    if brush.sculpt_capabilities.has_jitter:
                        col.separator()

                        row = col.row(align=True)
                        row.prop(brush, "use_relative_jitter", icon_only=True)
                        if brush.use_relative_jitter:
                            row.prop(brush, "jitter", slider=True)
                        else:
                            row.prop(brush, "jitter_absolute")
                        row.prop(brush, "use_pressure_jitter", toggle=True, text="")

                    if brush.sculpt_capabilities.has_smooth_stroke:
                        col.separator()

                        col.prop(brush, "use_smooth_stroke")

                        sub = col.column()
                        sub.active = brush.use_smooth_stroke
                        sub.prop(brush, "smooth_stroke_radius", text="Radius", slider=True)
                        sub.prop(brush, "smooth_stroke_factor", text="Factor", slider=True)
                else:
                    col.separator()

                    row = col.row(align=True)
                    row.prop(brush, "use_relative_jitter", icon_only=True)
                    if brush.use_relative_jitter:
                        row.prop(brush, "jitter", slider=True)
                    else:
                        row.prop(brush, "jitter_absolute")
                    row.prop(brush, "use_pressure_jitter", toggle=True, text="")

                    col.separator()

                    if brush.brush_capabilities.has_smooth_stroke:
                        col.prop(brush, "use_smooth_stroke")

                        sub = col.column()
                        sub.active = brush.use_smooth_stroke
                        sub.prop(brush, "smooth_stroke_radius", text="Radius", slider=True)
                        sub.prop(brush, "smooth_stroke_factor", text="Factor", slider=True)
                        
                col.prop(settings, "input_samples")
                
            col = layout.column()
            col.separator()
            
            box = layout.box()            
            col = box.column()
            col.prop(scene, "d31uamles", text='Brush Shape Curve', icon="SMOOTHCURVE")
            
            if scene.d31uamles:
                col.template_curve_mapping(brush, "curve", brush=True)
                col = box.column()
                row = col.row(align=True)
                row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
                row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
                row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
                row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
                row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
                row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
                
        if not scene.dl31aesum:
            col.separator()
            col.separator()
            box = layout.box()            
            col = box.column()
            col.label(text='Mesh Based Terrain Editing:')
            col.operator("object.dlasume31", icon='OUTLINER_OB_LATTICE')
            col.operator("object.dau31emsl", icon='OUTLINER_OB_LATTICE')
            col.operator("object.duaml31se", icon='FILE_TICK')
            col.separator()
            col.label(text='Spline Based Terrain Editing:')
            col.operator("object.dlsmaeu31", icon='IPO_BEZIER')
            col.operator("object.dlsema31u", icon='FILE_TICK')
            if context.active_object is not None and context.active_object.type == 'CURVE':
                col.prop(object,'dameslu31',text='Modifier Width')
                
            if context.active_object is not None and context.active_object.type == 'CURVE' and context.active_object.mode == 'EDIT':
                for point in bpy.context.active_object.data.splines.active.bezier_points:
                    if point.select_control_point == True:
                        col.prop(point,'radius',text='Custom Width')
                        col.prop(point,'tilt')
                        break
        
class dsma31lue(Panel,View3DPaintPanel):
    bl_category = "bLandscape Tools"
    bl_label = "Surface Painting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.dameuls31 = BoolProperty(default=False)
    
    Scene.dsem31alu = BoolProperty(default=False,update=d31ausmel)
    Scene.dumae31sl = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        #settings = cls.paint_settings(context)
        return context.scene.dameuls31

    def draw(self, context):
        scene = context.scene
        object = context.active_object
        layout = self.layout
        
        col = layout.column()
        
        if scene.dsem31alu:
            text = 'Disable Surface Painting'
            
        else:
            text = 'Enable Surface Painting'
        col.prop(scene, "dsem31alu", text=text, icon="TPAINT_HLT")
        if scene.dl31aesum:
            col.enabled = False
            
        if scene.dsem31alu:
            toolsettings = context.tool_settings
            settings = self.paint_settings(context)
            brush = settings.brush
            
            box = layout.box()            
            col = box.column()
            col.label(text='Brush settings')
            
            if not context.particle_edit_object:
                col.separator()
                col.separator()
                col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)
                
            capabilities = brush.sculpt_capabilities
            col.separator()
            col.separator()
            row = col.row(align=True)
            
            if context.image_paint_object and brush:
                self.prop_unified_size(row, context, brush, "size", slider=True, text="Radius")
            
            col = layout.column()
            col.separator()
            
            box = layout.box()            
            col = box.column()
            col.prop(scene, "dumae31sl", text='Stroke Settings', icon="BRUSH_DATA")
            
            if scene.dumae31sl:
                col.label(text="Stroke Method:")

                col.prop(brush, "stroke_method", text="")

                if brush.use_anchor:
                    col.separator()
                    col.prop(brush, "use_edge_to_edge", "Edge To Edge")

                if brush.use_airbrush:
                    col.separator()
                    col.prop(brush, "rate", text="Rate", slider=True)

                if brush.use_space:
                    col.separator()
                    row = col.row(align=True)
                    row.prop(brush, "spacing", text="Spacing")
                    row.prop(brush, "use_pressure_spacing", toggle=True, text="")

                if brush.use_line or brush.use_curve:
                    col.separator()
                    row = col.row(align=True)
                    row.prop(brush, "spacing", text="Spacing")

                if brush.use_curve:
                    col.separator()
                    col.template_ID(brush, "paint_curve", new="paintcurve.new")
                    col.operator("paintcurve.draw")

                col.separator()

                row = col.row(align=True)
                row.prop(brush, "use_relative_jitter", icon_only=True)
                if brush.use_relative_jitter:
                    row.prop(brush, "jitter", slider=True)
                else:
                    row.prop(brush, "jitter_absolute")
                row.prop(brush, "use_pressure_jitter", toggle=True, text="")

                col.separator()

                if brush.brush_capabilities.has_smooth_stroke:
                    col.prop(brush, "use_smooth_stroke")
                    sub = col.column()
                    sub.active = brush.use_smooth_stroke
                    sub.prop(brush, "smooth_stroke_radius", text="Radius", slider=True)
                    sub.prop(brush, "smooth_stroke_factor", text="Factor", slider=True)
                col.prop(settings, "input_samples")
                   
class d31emuasl(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Location/Object(s) Appearance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.due31alms = BoolProperty(default=False)
    
    @classmethod
    def poll(cls, context):
        return context.scene.due31alms

    def draw(self, context):
        scene = context.scene
        view = context.space_data
        layout = self.layout
        fx_settings = view.fx_settings
        userPreferences = context.user_preferences
        systemTab = userPreferences.system
        
        dsluae31m = bpy.data.scenes["Default_Location"].demual31s
        
        row = layout.row(align=True)
        row.operator("object.ds31ealmu",icon='TEXTURE')
        row.operator("object.dmslae31u",icon='ASSET_MANAGER')
        if not scene.du31lames:
            row.enabled = False
            
        row2 = layout.row(align=True)
        row2.operator("object.dms31laue", text="Smooth",icon='MOD_SMOOTH')
        row2.operator("object.da31umsle", text="Flat",icon='MOD_DISPLACE')
        
        
        
        row1 = layout.row(align=True)
        row1.operator("scene.d31auemls",icon='MATCAP_13')
        row1.operator("scene.del31umas",icon='MOD_TRIANGULATE')
        
        Areas = context.screen.areas
        for Area in Areas:
            if Area.type == 'VIEW_3D':
                if  Area.spaces.active.use_matcap == True and Area.spaces.active.viewport_shade == 'SOLID':
                    row4 = layout.row(align=False)
                    row4.template_icon_view(view, "matcap_icon")
        
        col = layout.column()
        col.prop(fx_settings, "use_ssao", text="Ambient Occlusion")
        if fx_settings.use_ssao:
                ssao_settings = fx_settings.ssao
                subcol = col.column(align=True)
                subcol.prop(ssao_settings, "factor")
                subcol.prop(ssao_settings, "distance_max")
                subcol.prop(ssao_settings, "attenuation")
                subcol.prop(ssao_settings, "samples")
          
        col = layout.column()
        col.separator()
        
        if scene.dml31eaus:
            d31slmuaeTexture = bpy.data.objects['Terrain_' + context.scene.name].material_slots[0].material.texture_slots[1]
            row3 = layout.row(align=True)
            row3.prop(d31slmuaeTexture,"diffuse_color_factor",text='Surface mask opacity')
            row3.prop(d31slmuaeTexture,"blend_type")
            if not scene.dsem31alu:
                row3.enabled = False
        
        colMipMap = layout.column()
        colMipMap.prop(systemTab, "use_mipmaps",text='Textures mipmaps')
        if not scene.du31lames:
            colMipMap.enabled = False

class d31lusaem(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "Quality Assurance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    Scene.du31slemaPath = StringProperty(name="Surface mask path",
        description="Path to surface mask",
        maxlen= 1024,
        subtype='FILE_PATH',
        update=dmlas31eu)
        
    Scene.dl31ueasm = BoolProperty(default=False)
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout

        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("scene.dmules31a",icon='IMAGE_RGB')
        row.prop(scene,'du31slemaPath',text="")
        row.enabled = False
                 
class dau31mles(Panel):
    bl_category = "bLandscape Tools"
    bl_label = "bLTilities"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout

        col = layout.column(align=True)
        col.operator("scene.dsl31aume",icon='MESH_GRID')
        col.operator("scene.create_surfacemask",icon='COLORSET_03_VEC')
