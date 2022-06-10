# Leveraging CLIP for Visual Question Answering

## UCLA CS 269 Seminar 5 S22 Course Project (Group 11)

| Name       | UID |
|---------------|----------|
| Rakesh Bal |   605526216  |
| Sri Keerthi Bolli |   505525868   |

This repository is a PyTorch and Python implementation of the course project for UCLA CS 269 Sem 5 (Human Centred Artificial Intelligence) S22 Course.

We use different exisitng works for our project and we recommend installing them from their respective repositories.

1. [MCAN-VQA](https://github.com/MILVLG/mcan-vqa) 
2. [LSeg](https://github.com/isl-org/lang-seg)
3. [Multilingual VQA](https://github.com/gchhablani/multilingual-vqa/)
4. [Multingual CLIP](https://github.com/FreddeFrallan/Multilingual-CLIP)

## Usage
The scripts are provided in this repository for running our experiments are changes we made to various files in the existing projects mentioned above. For example for MCAN-VQA, we recommend cloining the original repo `git clone https://github.com/MILVLG/mcan-vqa.git` and then replacing the original files with the files provided in the repository under `mcan-vqa` folder. Similarly, LSeg we provide the changes we made to the `lseg_demo.ipynb` in the original repository. For multilingual vqa, the scipt provided converts the multilingual files provided in the dataset ([here](https://huggingface.co/datasets/flax-community/multilingual-vqa)) to the corresponding jsons to be used by MCAN model.

## References
```
@inProceedings{yu2019mcan,
  author = {Yu, Zhou and Yu, Jun and Cui, Yuhao and Tao, Dacheng and Tian, Qi},
  title = {Deep Modular Co-Attention Networks for Visual Question Answering},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {6281--6290},
  year = {2019}
}
```

```
@inproceedings{
li2022languagedriven,
title={Language-driven Semantic Segmentation},
author={Boyi Li and Kilian Q Weinberger and Serge Belongie and Vladlen Koltun and Rene Ranftl},
booktitle={International Conference on Learning Representations},
year={2022},
url={https://openreview.net/forum?id=RriDjddCLN}
}
```

```
@inProceedings{yu2019mcan,
  author = {Yu, Zhou and Yu, Jun and Cui, Yuhao and Tao, Dacheng and Tian, Qi},
  title = {Deep Modular Co-Attention Networks for Visual Question Answering},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {6281--6290},
  year = {2019}
}
```