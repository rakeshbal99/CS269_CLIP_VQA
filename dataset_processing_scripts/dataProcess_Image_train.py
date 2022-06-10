import json
import os
images_path = "../train2014/"

questions_path = "new_v2_OpenEnded_mscoco_train2014_questions.json"

f = open(questions_path)
ques = json.load(f)
f.close()

image_ids = set([ q["image_id"] for q in ques["questions"]])

new_images_path = "../new_train2014/" 

if os.path.isdir(new_images_path):
    os.system("rm -r " + new_images_path)

os.system("mkdir -p " + new_images_path)

for imageId in image_ids:
    zeros_len = 12 - len(str(imageId))
    i_old_path = images_path + "COCO_train2014_" + str(imageId).zfill(12) + ".jpg.npz"
    i_new_path = new_images_path + "COCO_train2014_" + str(imageId).zfill(12) + ".jpg.npz"
    os.system("cp " + i_old_path  + " " + i_new_path)

print("Length of Images Ids = "  + str(len(image_ids)))