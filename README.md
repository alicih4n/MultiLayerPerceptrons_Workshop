# Multi Layer Perceptrons Workshop

<div align="center">
  <h3>Group 2</h3>
  <p>
    <strong>Members:</strong> <br />
    Ali Cihan Ozdemir (9091405) <br />
    Lohith Reddy Danda (9054470)
  </p>
  <p>
    ⚠️ <strong>Contribution Note:</strong> Roshan did not attend the lab session and provided zero contribution to this project.
  </p>
</div>

---

## 📖 Project Overview

This repository contains the completion of the **Multi Layer Perceptrons Workshop** assignment. The overarching objective of the project is to build a profound understanding of deep learning workflows, frameworks, and low-level mathematics.

The workshop consists of two distinct parts:
1. **Framework Comparison & Application:** A detailed comparative analysis of the big three open-source deep learning frameworks (Keras, PyTorch, and TensorFlow). We evaluated these libraries focusing on execution speed, model accuracy, and overall useability while training on standard image classification tasks like MNIST.
2. **From-Scratch NumPy MLP Implementation:** A low-level, completely from-scratch implementation of a 3-layer Multi-Layer Perceptron using purely NumPy arrays.

---

## 🛠️ How it Works (Step-by-Step)

### 1. The NumPy XOR Problem (From Scratch)
The standout piece of this workshop is the manual NumPy network. Here's a breakdown of the math we built:
- **Initialization:** We initialize parameters (`W1, b1, W2, b2, W3, b3`) scaled by a crucial `0.5` factor. We realized if the scale was too high, gradients exploded; if too low (zeros), the network stalled due to symmetry.
- **Forward Propagation:** The input flows sequentially through the network via dot products.
  - *Hidden Layers 1 & 2* use the **ReLU** activation function `max(0, Z)`. We deliberately chose ReLU to eradicate vanishing gradients because its derivative is simply `1` or `0`.
  - *Output Layer* uses the **Sigmoid** activation function to output a clean probability map between `0` and `1`.
- **Loss Computation:** We compute the cost using the **Binary Cross-Entropy Loss** equation.
- **Backward Propagation (Chain Rule):** This is where the magic happens. We accurately backtrack the gradients from the output prediction all the way to the input by chaining derivatives (`dZ`, `dW`, `db`), using the exact derivatives of Sigmoid and ReLU.
- **Gradient Descent Update:** The manual weights are incrementally updated via our learning rate `alpha = 0.1` and pushed back through 10,000 iterations until convergence.

### 2. The Framework Comparison
We ran benchmark tests configuring similar Convolutional and Dense networks using APIs from `keras.models`, `torch.nn`, and raw `tensorflow`. By comparing the epochs, training time, and loss curves, we summarized the best enterprise use cases for each framework.

---

## 🚀 How to Run the Project

Follow these steps to deploy and experiment with the code locally.

### Prerequisites
Make sure you have `python 3.9+` installed on your machine. All required packages (including scientific Python equivalents for Keras, Torch, SciKit, TensorFlow, and Jupyter) are provided.

### Step 1: Clone the Repository
```bash
git clone https://github.com/alicih4n/MultiLayerPerceptrons_Workshop.git
cd MultiLayerPerceptrons_Workshop
```

### Step 2: Install the Dependencies
The project uses `requirements.txt` which has been thoroughly checked to include TensorFlow, PyTorch, Keras, NumPy, Matplotlib, and Jupyter configurations.
```bash
pip install -r requirements.txt
```

### Step 3: Launch Jupyter Notebook
```bash
jupyter notebook
```

### Step 4: Execute the Code
- Open `MultiLayerPerceptrons_Workshop.ipynb`.
- Click on **Run -> Run All Cells** to watch the Framework Comparisons build and execute.
- Scroll to the bottom to watch the NumPy MLP dynamically train itself to solve the XOR dataset using our explicitly coded gradient chain-rule!

---

*Project implemented for CSCN8010 Workshop Assignments.*
