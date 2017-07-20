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

        
class dbqpl10o(AddonPreferences):
    bl_idname = __name__

    d0oqpbl1 = StringProperty(name="GDAL",
        description="Path to GDAL",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='c:\Program Files\GDAL\\')
        
    d1qo0pbl = StringProperty(name="Output",
        description="Path to Output folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default='{}\\Documents\\'.format(os.environ['USERPROFILE']))
    
    def draw(self, context):
        layout = self.layout   
        box = layout.box()
        box.label('External Paths')
        box.prop(self, "d0oqpbl1")
        box.prop(self, "d1qo0pbl")

classes = (
    bLT_main.dob1p0ql,
    bLT_main.d1lb0opq,
    bLT_main.do1b0qlp,
    bLT_main.doq1pb0l,
    bLT_main.dq0lo1bp,
    bLT_main.db1lo0qp,
    bLT_main.d1qbo0lp,
    bLT_main.dq0bplo1,
    bLT_main.db1qlp0o,
    bLT_main.dbql10op,
    bLT_main.db0olq1p,
    bLT_main.doplq01b,
    bLT_main.dbpoq10l,
    bLT_main.d0qb1lop,
    bLT_main.dop1lb0q,
    bLT_main.dbpol1q0,
    bLT_main.dl1obp0q,
    bLT_main.dlpoq0b1,
    bLT_main.d0lpobq1,
    bLT_main.dbploq10,
    dbqpl10o
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.dlop10qb = CollectionProperty(type=bLT_main.dob1p0ql)
    bpy.types.Scene.dlop10qb_index = IntProperty(default=-1)

    bpy.context.user_preferences.filepaths.use_relative_paths = False
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.dlop10qb
    del bpy.types.Scene.dlop10qb_index

if __name__ == "__main__":
    register() 