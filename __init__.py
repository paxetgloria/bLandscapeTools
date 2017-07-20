bl_info= {
    "name": "bLandscape Tools",
    "author": "Miroslav Horvath",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "View3D > Properties > Landscape Tools",
    "description": "Tools for virtual landscaping",
    "warning": "",
    "wiki_url": "https://github.com/paxetgloria/BlenderLandscapeTools/wiki",
    "tracker_url": "https://github.com/paxetgloria/BlenderLandscapeTools/issues",
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
from bpy.props import StringProperty,CollectionProperty,IntProperty,BoolProperty

        
class dlp0b1oq(AddonPreferences):
    bl_idname = __name__

    dp01lobq = StringProperty(name="GDAL",
        description="Path to GDAL",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='c:\Program Files\GDAL\\')
        
    dqlop1b0 = StringProperty(name="Output",
        description="Path to Output folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='{}\\Documents\\'.format(os.environ['USERPROFILE']))
    
    def draw(self, context):
        layout = self.layout   
        box = layout.box()
        box.label('External Paths')
        box.prop(self, "dp01lobq")
        box.prop(self, "dqlop1b0")

classes = (
    bLT_main.d0q1bolp,
    bLT_main.d1bp0qol,
    bLT_main.doq0blp1,
    bLT_main.d0qp1olb,
    bLT_main.dopblq10,
    bLT_main.d1bo0qpl,
    bLT_main.d1qpbo0l,
    bLT_main.d10qbolp,
    bLT_main.dql0pb1o,
    bLT_main.dlpb10oq,
    bLT_main.dl1p0obq,
    bLT_main.d01lqpob,
    bLT_main.dp0obq1l,
    bLT_main.d1qopbl0,
    bLT_main.d01poqlb,
    bLT_main.dqp0lob1,
    bLT_main.dpblo1q0,
    bLT_main.doq10lbp,
    bLT_main.db0op1lq,
    bLT_main.dlpo01qb,
    dlp0b1oq
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.dlp1qbo0 = CollectionProperty(type=bLT_main.d0q1bolp)
    bpy.types.Scene.d1ol0pbq = IntProperty(default=-1)

    bpy.context.user_preferences.filepaths.use_relative_paths = False
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.dlp1qbo0
    del bpy.types.Scene.d1ol0pbq

if __name__ == "__main__":
    register() 