import os
import subprocess

blender_dir = r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe"
blend_path = r"C:\Users\A.azoulay\Desktop\wfc folder\wfc\rock.blend"
python_script = r"C:\Users\A.azoulay\Desktop\wfc folder\wfc\export_tile.py"
output_folder = r"output=C:\Users\A.azoulay\Desktop\wfc folder\wfc\Content\wfc\TEST"


command = [
    blender_dir,
    blend_path,
    "--background",
    "--python",
    python_script,
    "--",
    output_folder
]

subprocess.run(command)