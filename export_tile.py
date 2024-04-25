import os
import sys
import bpy
import math 


def find_obj(objname):

    objects_list = []
    
    for obj in bpy.context.scene.objects:          
        
        if obj.type == 'MESH' and objname in obj.name:               
            objects_list.append(obj)             

    return objects_list


def arg_parser(args, value):
    '''this function check for arg in the command use to launch the script'''

    matching = [x for x in args if x.startswith(value)]

    if matching:
        return matching[0].split(value)[-1]
    else:
        return ""
    

if __name__ == "__main__":

    args = sys.argv
    output = arg_parser(args, "output=")
    print(output)

    #select all obj with _tile at the end 
    objs_to_export = find_obj('__tile')
    print(len(objs_to_export))

    for obj in objs_to_export :

        obj_name = obj.name
        #save their initial position 
        initial_position = bpy.data.objects[obj_name].location
        #print(initial_position, "begin")

        #move them to 0, 0,0 
        bpy.data.objects[obj_name].location[0] = 0
        bpy.data.objects[obj_name].location[1] = 0
        bpy.data.objects[obj_name].location[2] = 0

        rotation_angle = math.radians(270)
        bpy.data.objects[obj_name].rotation_euler[2] += rotation_angle

        #print(bpy.data.objects[obj_name].location, "middle")

        full_output = os.path.join(output, f"{obj_name}.fbx")

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[obj_name].select_set(True)

        #export them as fbx in the content folder 
        bpy.ops.export_scene.fbx(filepath=full_output, use_selection=True)





