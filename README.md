# Cross-Modal Emotion Recognition with Causality Inference in Human Conversations

<img src="https://i.imgur.com/waxVImv.png" alt="Emotion Chat Inference" style="max-width: 100%;">

## 🧠 Overview

Emotion recognition plays a vital role in many real-world applications, from affective computing to empathetic conversational agents. However, many existing methods fall short in inferring the **underlying causes** of emotions, particularly in multimodal conversations.

We propose a **Cross-Modal Emotion Recognition** framework that:

- Integrates **visual**, **audio**, and **textual** inputs in a unified architecture.
- Employs an **adaptive cross-modal attention module** to weigh modalities based on contextual relevance.
- Uses a **trainable LLaMA2-Chat (7B)** model to infer emotion **causality** from vision-language cues.
- Delivers **real-time emotional feedback** to support dynamic interactions.

Our framework outperforms existing methods on multiple benchmarks including **SEMAINE**, **AESI**, **ECF**, and **MER-2024**.

---

## 🏗️ Architecture

The core pipeline consists of:

1. **Multimodal Inputs** — Visual frames, audio, and text.
2. **Adaptive Cross-Modal Attention** — Captures inter-modal dependencies dynamically.
3. **Emotion Causality Inference** — Uses LLaMA2-Chat to reason over visual and textual cues.
4. **Real-Time Feedback Module** — Provides on-the-fly emotional summaries.

<img style="max-width: 100%;" src="https://github.com/swerizwan/DT3DPE/blob/main/resources/overview.png" alt="Framework Overview">

---

## 📦 Installation

Create and activate the `mmec` conda environment:

```bash
conda create -n mmec python=3.9
conda activate mmec
```

Install required dependencies:

```yaml
name: mmec
channels:
  - pytorch
  - defaults
  - anaconda
dependencies:
  - python=3.9
  - cudatoolkit
  - pip
  - pip:
    - torch==2.0.0
    - torchaudio
    - torchvision
    - huggingface-hub==0.18.0
    - matplotlib==3.7.0
    - psutil==5.9.4
    - iopath
    - pyyaml==6.0
    - regex==2022.10.31
    - tokenizers==0.13.2
    - tqdm==4.64.1
    - transformers==4.30.0
    - timm==0.6.13
    - webdataset==0.2.48
    - omegaconf==2.3.0
    - opencv-python==4.7.0.72
    - decord==0.6.0
    - peft==0.2.0
    - sentence-transformers
    - gradio==3.47.1
    - accelerate==0.20.3
    - bitsandbytes==0.37.0
    - scikit-image
    - visual-genome
    - wandb
```

Alternatively, save this list in `environment.yaml` and run:

```bash
conda env create -f environment.yaml
```

---

## 🚀 Demo

### Single Input Inference
```bash
python demo.py --text "I'm feeling anxious about tomorrow." \
               --image_path ./assets/frame1.jpg \
               --audio_path ./assets/audio1.wav
```

### Batch Input (JSON)
```bash
python demo_batch.py --input_file ./assets/conversations.json
```

### Launch Gradio App
```bash
python gradio_app.py
```

---

## 📊 Datasets

Our model has been evaluated on the following:

- **SEMAINE**: Emotion-rich conversational dataset.
- **AESI**: Multimodal dataset of affective interactions.
- **ECF**: Emotion-Cause-Factor annotated corpus.
- **MER-2024**: Multi-domain dataset for robust emotion recognition.

---

## 🏋️ Train & Evaluate

### Train the Model

```bash
python train.py --config configs/train.yaml
```

### Evaluate the Model

```bash
python evaluate.py --checkpoint checkpoints/best_model.pth \
                   --config configs/eval.yaml
```

