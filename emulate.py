bl_info = {
    "name": "Toggle 'Emulate 3 Button Mouse'",
    "author": "Robert Guetzkow",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Edit > Operator Search",
    "description": "Operator for toggeling the 'Emulate 3 Button Mouse' option.",
    "warning": "",
    "wiki_url": "",
    "category": "Preferences"}

import bpy


class PREFERENCES_OT_toggle_emulate_3_button_mouse(bpy.types.Operator):
    bl_idname = "preferences.toggle_emulate_3_button_mouse"
    bl_label = "Toggle 'Emulate 3 Button Mouse'"

    def execute(self, context):
        context.preferences.inputs.use_mouse_emulate_3_button = not context.preferences.inputs.use_mouse_emulate_3_button
        return {"FINISHED"}


classes = (PREFERENCES_OT_toggle_emulate_3_button_mouse,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
