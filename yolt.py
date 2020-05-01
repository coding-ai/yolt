import subprocess
import os

# Start 3D_Photo and generate videos
p_3d = subprocess.Popen(["python", "main.py", "--config", "argument.yml"], cwd='3d-photo-inpainting')
p_3d.wait()
print('Successfully completed the 3D_Photo generator!')
# Start YOLOv4 and generate output
p_make = subprocess.Popen(["make"], cwd='darknet')
p_make.wait()
for cout, video in enumerate(os.listdir('videos')):
    print('Processing video: '+ video)
    p_yolo = subprocess.Popen(["./darknet", "detector", "demo", "cfg/coco.data", "cfg/yolov4.cfg", "yolov4.weights", "../videos/"+video, "-out_filename", "../videos/res_"+video], cwd='darknet')
    p_yolo.wait()
    print('Video '+video+' successfully processed!')