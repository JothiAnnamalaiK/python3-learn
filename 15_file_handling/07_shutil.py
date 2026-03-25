import os
import shutil

move_dir_path = os.path.join(os.path.dirname(__file__), "move-dir")
source_file = os.path.join(os.path.dirname(__file__), "jothi.txt")
dest_file = os.path.join(os.path.dirname(__file__), "Annamalai.txt")
shutil.copy(source_file, dest_file)  # copy from source to dest

shutil.move(dest_file, move_dir_path)  # move to the dir

# try:
#     file_path = os.path.join(os.path.dirname(__file__), "sample-dir")
#     shutil.rmtree(file_path)  # permanently remove the dir even if it has files
#     print("Directory deleted successfully")
# except FileNotFoundError:
#     print("Directory not found")
