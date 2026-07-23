# 🚀 Autonomous Lunar Landing using Proximal Policy Optimization (PPO)

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Gymnasium](https://img.shields.io/badge/Gymnasium-LunarLander-orange)
![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-PPO-success)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)
![License](https://img.shields.io/badge/License-Educational-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

</p>

---

## 📌 Overview

This project implements an **Autonomous Lunar Landing Agent** using **Proximal Policy Optimization (PPO)**, a state-of-the-art Reinforcement Learning algorithm from Stable-Baselines3.

The objective is to train an intelligent agent capable of safely landing a spacecraft in the **Gymnasium LunarLander-v3** environment by maximizing cumulative rewards through continuous interaction with the environment.

---

## 🎯 Objectives

* Train a reinforcement learning agent using PPO.
* Learn an optimal landing policy.
* Evaluate trained model performance.
* Visualize learning progress.
* Demonstrate autonomous landing through simulation.

---

## 🛠️ Technologies Used

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python            | Programming Language               |
| Gymnasium         | Reinforcement Learning Environment |
| Stable-Baselines3 | PPO Algorithm                      |
| PyTorch           | Deep Learning Backend              |
| NumPy             | Numerical Computation              |
| Matplotlib        | Training Visualization             |

---

## 📂 Project Structure

```text
Autonomous-Lunar-Landing-using-PPO/
│
├── train.py
├── evaluate.py
├── test.py
├── ppo_model.zip
├── learning_curve.png
├── evaluation_report.txt
├── requirements.txt
├── README.md
├── logs/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dvshriram-dvs/Autonomous-Lunar-Landing-using-PPO.git
```

Navigate to the project

```bash
cd Autonomous-Lunar-Landing-using-PPO
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Training the Agent

Run

```bash
python train.py
```

This will generate:

* ✅ Trained PPO Model
* ✅ Training Logs
* ✅ Learning Curve

---

## 📊 Evaluate the Model

```bash
python evaluate.py
```

This creates

* evaluation_report.txt

---

## 🎮 Test the Agent

```bash
python test.py
```

A simulation window will open showing the trained Lunar Lander performing an autonomous landing.

---

## 📈 Results

After training, the project generates:

* 📊 Learning Curve
* 🤖 Trained PPO Model
* 📄 Evaluation Report

---

## 🧠 PPO Algorithm

The project uses **Proximal Policy Optimization (PPO)**.

### Key Features

* Policy Gradient Method
* Clipped Objective Function
* Stable Training
* High Sample Efficiency
* Continuous Policy Improvement

---

## 📚 Reinforcement Learning Workflow

```text
Environment
      │
      ▼
Observe State
      │
      ▼
 PPO Agent
      │
      ▼
Choose Action
      │
      ▼
Environment
      │
      ▼
Receive Reward
      │
      ▼
Update Policy
```

---

## 🌟 Future Improvements

* TensorBoard Integration
* Hyperparameter Optimization
* Video Recording of Agent
* Multiple RL Algorithms (A2C, SAC, DQN)
* Reward Comparison Graphs
* Interactive Dashboard

---

## 👨‍💻 Author

**D V Shriram**
Student
VIT Bhopal University

GitHub: https://github.com/dvshriram-dvs

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is intended for educational and learning purposes.
