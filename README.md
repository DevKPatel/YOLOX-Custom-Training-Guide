# 🧠 YOLOX Custom Training - Abandoned Object Detection

This project demonstrates how to train a **YOLOX (You Only Look Once X)** object detection model on a custom dataset, specifically tailored for object detection in surveillance footage or real-world environments.

*(NOTE :- before starting to implement things using the docs, I would recommed to first go through it in depth and check the titles and important things that have been marked in the docx file)*

---

## 🔁 Files to Replace and Modify
- your yolox/tools/demo.py with my yolox/tools/demo.py file : Made changes in this file and added a "class_json" argument to read class names of json file during testing. Also scroll down and search for "DEFAULT_LVIS_JSON". Change the path to your annotations .json file. ( I trained my model on LVIS Dataset )
- replace yolox/yolox/data/dataset/coco.py with my file: not much changes but still safer side.
- ( if its gotten confusing at this point then copy and replace these entire folders , 1. yolox/exps, 2. yolox/yolox/data/datasets, 3. yolox/tools.
- Most important files to make changes - base_exp.py ( currently its modified version for yolox_m, take weights for different model versions as required ), coco.py, demo.py, train.py

---

## 📌 Project Summary

This repository provides a detailed pipeline for:

- Preparing custom datasets.
- Setting up a GPU-accelerated environment for training with YOLOX.
- Configuring experiment files for model customization.
- Training and evaluating the model.
- Running inference on images and videos.
- Exporting models for deployment (ONNX/TensorRT).

---

## 👤 Who is this for?

This project is ideal for:

- **Computer Vision researchers and engineers** building real-time object detection systems.
- **Security and surveillance teams** interested in detecting abandoned or unusual items in public spaces.
- **AI/ML students or enthusiasts** learning how to train models using YOLOX on custom datasets.
- **Developers** deploying object detection solutions on edge devices (NVIDIA Jetson, etc.).

---

## 🛠️ Technologies Used

- YOLOX (by Megvii - open source)
- PyTorch (with CUDA support)
- Python 3.10
- COCO/PASCAL VOC dataset standards
- TensorBoard for visualization

---

## 🚀 Setup & Installation

1. Clone YOLOX repo:
   ```bash
   git clone https://github.com/Megvii-BaseDetection/YOLOX
   cd YOLOX
