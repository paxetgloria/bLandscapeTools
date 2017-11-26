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
from bpy.props import StringProperty,CollectionProperty,IntProperty,BoolProperty


class d0obqp1l(AddonPreferences):
    bl_idname = __name__

    dboqpl01 = StringProperty(name="GDAL",
        description="Path to GDAL",
        maxlen= 1024,
        subtype='DIR_PATH',
        default="/usr/bin/" if os.name == "posix" else "c:\\Program Files\\GDAL\\"
        )
    # Actually, this option makes little sense on Linux/Mac Systems, as the executables of GDAL are
    # usually available in the path environment anyway.
    
    d0p1olqb = StringProperty(name="Output",
        description="Path to Output folder",
        maxlen= 1024,
        subtype='DIR_PATH',
        default="{}".format(os.environ["HOME"]) if os.name == "posix" else os.path.join(os.environ['USERPROFILE'], "Documents")
        )
    
    def draw(self, context):
        layout = self.layout   
        box = layout.box()
        box.label('External Paths')
        box.prop(self, "dboqpl01")
        box.prop(self, "d0p1olqb")

classes = (
    bLT_main.dplq01bo,
    bLT_main.dpq0bl1o,
    bLT_main.dbq10plo,
    bLT_main.d1qoplb0,
    bLT_main.dblqo0p1,
    bLT_main.d0bpqol1,
    bLT_main.dbolpq10,
    bLT_main.d0ob1lpq,
    bLT_main.dpqol01b,
    bLT_main.dobqlp01,
    bLT_main.d0qobl1p,
    bLT_main.dlob0p1q,
    bLT_main.d0o1plqb,
    bLT_main.dp0qbl1o,
    bLT_main.dpbo10ql,
    bLT_main.dp10bqol,
    bLT_main.dol1pbq0,
    bLT_main.dp1oqb0l,
    bLT_main.d0qo1lbp,
    bLT_main.dq0po1bl,
    d0obqp1l
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.d0obpql1 = CollectionProperty(type=bLT_main.dplq01bo)
    bpy.types.Scene.dq0p1bol = IntProperty(default=-1)

    bpy.context.user_preferences.filepaths.use_relative_paths = False

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.d0obpql1
    del bpy.types.Scene.dq0p1bol

if __name__ == "__main__":
    register() 
