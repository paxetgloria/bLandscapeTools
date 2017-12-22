bl_info= {
    "name": "bLandscape Tools",
    "author": "Miroslav Horvath",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "View3D > Properties > bLandscape Tools",
    "description": "Tools for virtual landscaping",
    "warning": "",
    "wiki_url": "https://github.com/paxetgloria/bLandscapeTools/wiki",
    "tracker_url": "https://github.com/paxetgloria/bLandscapeTools/issues",
    "support" : "COMMUNITY",
    "category": "3D View"}

import sys
import os
if "bpy" in locals():
    import imp

    imp.reload(bLT_main)
    imp.reload(bLT_utils)
    print("bLT: Reloaded multifiles")
else:
    from . import bLT_main
    from . import bLT_utils

    print("bLT: Imported multifiles")
    
import bpy

from bpy.types import AddonPreferences
from bpy.props import StringProperty,CollectionProperty,IntProperty,BoolProperty,PointerProperty

class dumsela31(AddonPreferences):
    bl_idname = __name__

    d31lemsau = StringProperty(name="GDAL path",
        description="Path to GDAL",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='c:\Program Files\GDAL\\')
        
        
    dema31lus = StringProperty(name="Output path",
        description="Path to Output folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='{}\\Documents\\'.format(os.environ['USERPROFILE']))
    
    def draw(self, context):
        layout = self.layout   
        box = layout.box()
        box.prop(self, "d31lemsau")
        box.prop(self, "dema31lus")
        box.operator("a.dlsa31meu",icon='TEXTURE')
        
classes = (
    bLT_main.d31lusmea,
    bLT_main.dlumae31s,
    bLT_main.daslme31u,
    bLT_main.dua31mesl,
    bLT_main.duesla31m,
    bLT_main.d31lseaum,
    bLT_main.dmea31usl,
    bLT_main.dseaml31u,
    bLT_main.delsmau31,
    bLT_main.dea31lsmu,
    bLT_main.dsma31lue,
    bLT_main.d31emuasl,
    bLT_main.d31lusaem,
    bLT_main.dau31mles,
    bLT_main.d31amselu,
    bLT_main.daes31lum,
    bLT_main.du31aseml,
    bLT_main.dm31easlu,
    bLT_main.dse31lmau,
    bLT_main.dsmaul31e,
    bLT_main.dmelsa31u,
    bLT_main.dle31uams,
    bLT_main.dlause31m,
    bLT_main.damsul31e,
    bLT_main.deas31uml,
    bLT_main.duame31ls,
    bLT_main.da31emslu,
    bLT_main.dmasel31u,
    bLT_main.dmeas31lu,
    bLT_main.dusem31la,
    bLT_main.dsaelmu31,
    bLT_main.dulema31s,
    bLT_main.dmelas31u,
    bLT_main.demus31al,
    dumsela31  
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    os.environ['PATH'] = ''.join(('{}\lib;'.format(bLT_utils.dusaem31l()[1]),os.environ['PATH']))
    
    bpy.types.Scene.dmusa31el = CollectionProperty(type=bLT_main.dlumae31s)
    bpy.types.Scene.dlaumes31 = IntProperty(default=-1)
    bpy.types.Scene.dulem31as = CollectionProperty(type=bLT_main.daslme31u)
    
    dmseul31a = bLT_utils.dusaem31l()[2]
    import zipfile
    zip_ref = zipfile.ZipFile('{}\\bLandscapeTools.zip'.format(dmseul31a), 'r')
    zip_ref.extractall('{}\\AppData\\Roaming\\Blender Foundation\\Blender\\{}.{}\\scripts\\startup\\bl_app_templates_user'.format(os.environ['USERPROFILE'],bpy.app.version[0],bpy.app.version[1]))
    zip_ref.close()
    
    bpy.context.user_preferences.filepaths.use_relative_paths = False
    bpy.context.user_preferences.filepaths.show_thumbnails = True
    bpy.context.user_preferences.system.use_mipmaps = False
    bpy.context.user_preferences.view.use_mouse_depth_navigate = True
    bpy.context.user_preferences.view.use_zoom_to_mouse = True
    bpy.context.user_preferences.view.use_rotate_around_active = True
    bpy.context.user_preferences.view.use_auto_perspective = True
    bpy.context.user_preferences.system.use_select_pick_depth = True
    bpy.context.user_preferences.system.select_method = 'GL_QUERY'


    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.dmusa31el
    del bpy.types.Scene.dlaumes31
    del bpy.types.Scene.dulem31as

if __name__ == "__main__":
    register()
