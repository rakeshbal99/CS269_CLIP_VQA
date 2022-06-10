import torch
import clip
from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import pudb

path = 'updated_image_features_rn101_train/'
save_path = 'merged_image_features_rn101_train/'
path2 = 'datasets/coco_extract/train2014/'
images_files = [f for f in listdir(path) if isfile(join(path, f))]

if path in os.listdir("./"):
    os.system("rm -r " + save_path)
os.system("mkdir -p " + save_path)

for image_file in tqdm(images_files):
    
    bu_features = np.load(path2 + image_file)["x"]
    clip_features = np.load(path + image_file)["x"]
    image_features_np = np.concatenate((bu_features, clip_features), axis = 1)


    np.savez(save_path + image_file, x=image_features_np)