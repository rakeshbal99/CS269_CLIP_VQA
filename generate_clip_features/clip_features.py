import torch
import clip
from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import pudb

save_path = 'updated_image_features_rn101/'
clip_model = "RN101"

device = 'cuda:2'# "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load(clip_model, device=device)

path = '/home/shivam/My_Projects/Test/CLIP-ViL/CLIP-ViL-Direct/vqa/datasets/coco_2014/images/val2014/'
images_files = [f for f in listdir(path) if isfile(join(path, f))]

print("CLIP Model = " + str(clip_model) + ", train/val = val")

if save_path in os.listdir("./"):
    os.system("rm -r " + save_path)
os.system("mkdir -p " + save_path)
for image_file in tqdm(images_files):
    image = preprocess(Image.open(path + image_file)).unsqueeze(0).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)
    image_features_copied = []

    for i in np.array(image_features.cpu())[0]:
        image_features_copied.append(i)
    size = len(image_features_copied)
    for i in range(size, 2048):
        image_features_copied.append(0)
    image_features_np = np.reshape(np.array(image_features_copied), (-1, 1))


    np.savez(save_path + image_file + ".npz", x=image_features_np)