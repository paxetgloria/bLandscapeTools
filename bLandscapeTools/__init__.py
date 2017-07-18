bl_info= {
    "name": "bLandscape Tools",
    "author": "Miroslav Horvath",
    "version": (0, 1),
    "blender": (2, 7, 8),
    "location": "View3D > Properties > Landscape Tools",
    "description": "Tools for virtual landscaping",
    "warning": "",
    "wiki_url": "https://github.com/paxetgloria/BlenderLandscapeTools/wiki",
    "tracker_url": "https://github.com/paxetgloria/BlenderLandscapeTools/issues",
    "support" : "COMMUNITY",
    "category": "3D View"}

import sys
import os
# ----------------------------------------------
# Import modules
# ----------------------------------------------
if "bpy" in locals():
    import imp

    imp.reload(bLT_main)
    print("BTT: Reloaded multifiles")
else:
    from . import bLT_main

    print("BTT: Imported multifiles")


    
import bpy
from . import bLT_utils
from bpy.types import AddonPreferences
from bpy.props import StringProperty

        
class AddonPref_bLT(AddonPreferences):
    bl_idname = __name__

    GDALPath = StringProperty(name="",
        attr="GDALPath",
        description="Path to GDAL",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='c:\Program Files\GDAL\\')
    
    def draw(self, context):
        layout = self.layout
        
        #External tools
        box = layout.box()
        box.label('External Tools')
        box.prop(self, "GDALPath")

    
def register():
    bpy.utils.register_class(bLT_main.VIEW3D_ProjectSettings)
    bpy.utils.register_class(bLT_main.VIEW3D_LocationsManager)
    
    bpy.utils.register_class(bLT_main.OP_CreateProject)
    bpy.utils.register_class(bLT_main.OP_ImportLocation)
    bpy.utils.register_class(bLT_main.OP_CreateLocation)
    bpy.utils.register_class(bLT_main.OP_CommitLocation)
    bpy.utils.register_class(bLT_main.OP_PickLocation)
    bpy.utils.register_class(bLT_main.OP_DrawSplashScreen)
    
    bpy.utils.register_class(AddonPref_bLT)
    
    # turn off relative paths and use absolute instead
    bpy.context.user_preferences.filepaths.use_relative_paths = False
    
    

def unregister():
    bpy.utils.unregister_class(bLT_main.VIEW3D_ProjectSettings)
    bpy.utils.unregister_class(bLT_main.VIEW3D_LocationsManager)
    
    bpy.utils.unregister_class(bLT_main.OP_CreateProject)
    bpy.utils.unregister_class(bLT_main.OP_ImportLocation)
    bpy.utils.unregister_class(bLT_main.OP_CreateLocation)
    bpy.utils.unregister_class(bLT_main.OP_CommitLocation)
    bpy.utils.unregister_class(bLT_main.OP_PickLocation)
    bpy.utils.unregister_class(bLT_main.OP_DrawSplashScreen)
    
    
    bpy.utils.unregister_class(AddonPref_bLT)



if __name__ == "__main__":
    register()
    
    
    