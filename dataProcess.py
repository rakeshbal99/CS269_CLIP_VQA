import json
import os
annotations_path = "v2_mscoco_val2014_annotations.json"
questions_path = "v2_OpenEnded_mscoco_val2014_questions.json"

f = open(annotations_path)
anno = json.load(f)
f.close()

f = open(questions_path)
ques = json.load(f)
f.close()

split_len = 25000

new_anno = {}

for key in anno:
    if key == "annotations":
        new_anno[key] = anno[key][:split_len]
    else:
        new_anno[key] = anno[key]

new_ques = {}

for key in ques:
    if key == "questions":
        new_ques[key] = ques[key][:split_len]
    else:
        new_ques[key] = ques[key]

with open( "new_" + annotations_path, "w") as outfile:
    json.dump(new_anno, outfile)

with open( "new_" + questions_path, "w") as outfile:
    json.dump(new_ques, outfile)