import numpy as np
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import pudb, json
import pandas as pd
from copy import copy

with open("datasets/vqa/v2_mscoco_val2014_annotations.json") as f:
    val_annot = json.load(f)

with open("datasets/vqa/v2_OpenEnded_mscoco_val2014_questions.json") as f:
    val_quest = json.load(f)

val_annot_copy = copy(val_annot)
val_quest_copy = copy(val_quest)

val_questions = []
val_annotations = []

m_val_file = pd.read_csv("../multilingual-vqa/val_file_trans.tsv", sep='\t')

with open("../multilingual-vqa/answer_reverse_mapping.json") as f:
    answers_reverse_dict = json.load(f)

question_ids = {}

for index, row in m_val_file.iterrows():
    image_file = row['image_file']
    question = row['question']
    answer_label = row['answer_label']
    question_type = row['question_type']

    img_id = image_file.replace('val2014/COCO_val2014_', '').replace('.jpg', '')
    img_id = str(int(img_id))
    img_id_int = int(img_id) 
    ques_id_start = img_id_int * 1000

    if ques_id_start in question_ids:
        question_ids[ques_id_start] += 1
        ques_id_start = ques_id_start + question_ids[ques_id_start]
    else:
        question_ids[ques_id_start] = 0
        ques_id_start = ques_id_start + question_ids[ques_id_start]

    question_dict_here = {'image_id': img_id_int, 'question_id': ques_id_start, 'question': question}
    val_questions.append(question_dict_here)

    annotation_dict_here = {'question_type': question_type, 'multiple_choice_answer': answers_reverse_dict[str(answer_label)],
                            'image_id': img_id_int, 'question_id': ques_id_start, 'answer_type': 'other'}
    val_annotations.append(annotation_dict_here)

val_annot_copy["annotations"] = val_annotations
val_quest_copy["questions"] = val_questions

with open("multilingual_v2_mscoco_val2014_annotations.json", "w") as outfile:
    json.dump(val_annot_copy, outfile)

with open("multilingual_v2_OpenEnded_mscoco_val2014_questions.json", "w") as outfile:
    json.dump(val_quest_copy, outfile)


#### Train Files ####

with open("datasets/vqa/v2_mscoco_train2014_annotations.json") as f:
    train_annot = json.load(f)

with open("datasets/vqa/v2_OpenEnded_mscoco_train2014_questions.json") as f:
    train_quest = json.load(f)

m_train_file = pd.read_csv("../multilingual-vqa/train_file_trans.tsv", sep='\t')

train_annot_copy = copy(train_annot)
train_quest_copy = copy(train_quest)

train_questions = []
train_annotations = []

with open("../multilingual-vqa/answer_reverse_mapping.json") as f:
    answers_reverse_dict = json.load(f)

question_ids = {}

for index, row in m_train_file.iterrows():
    image_file = row['image_file']
    question = row['question']
    answer_label = row['answer_label']
    question_type = row['question_type']

    img_id = image_file.replace('train2014/COCO_train2014_', '').replace('.jpg', '')
    img_id = str(int(img_id))
    img_id_int = int(img_id) 
    ques_id_start = img_id_int * 1000

    if ques_id_start in question_ids:
        question_ids[ques_id_start] += 1
        ques_id_start = ques_id_start + question_ids[ques_id_start]
    else:
        question_ids[ques_id_start] = 0
        ques_id_start = ques_id_start + question_ids[ques_id_start]

    question_dict_here = {'image_id': img_id_int, 'question_id': ques_id_start, 'question': question}
    train_questions.append(question_dict_here)

    annotation_dict_here = {'question_type': question_type, 'multiple_choice_answer': answers_reverse_dict[str(answer_label)],
                            'image_id': img_id_int, 'question_id': ques_id_start, 'answer_type': 'other'}
    train_annotations.append(annotation_dict_here)

train_annot_copy["annotations"] = train_annotations
train_quest_copy["questions"] = train_questions

with open("multilingual_v2_mscoco_train2014_annotations.json", "w") as outfile:
    json.dump(train_annot_copy, outfile)

with open("multilingual_v2_OpenEnded_mscoco_train2014_questions.json", "w") as outfile:
    json.dump(train_quest_copy, outfile)