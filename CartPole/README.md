# CartPole Reinforcement Learning using PPO

## Overview

This project demonstrates how to solve the **CartPole-v1** environment from Gymnasium using the **Proximal Policy Optimization (PPO)** algorithm provided by Stable-Baselines3.

The agent is trained to balance a pole on a moving cart by learning the optimal actions through reinforcement learning. After training, the model is evaluated and tested in a rendered simulation.

---

## Features

* PPO-based Reinforcement Learning
* Training on CartPole-v1 environment
* Model evaluation over 100 episodes
* Learning curve visualization
* Human-rendered simulation
* Evaluation report generation

---

## Project Structure

```text
CartPole/
│── train.py                 # Train the PPO agent
│── evaluate.py              # Evaluate trained model
│── test.py                  # Run trained agent in simulation
│── ppo_model.zip            # Saved trained model
│── learning_curve.png       # Training reward graph
│── evaluation_report.txt    # Evaluation results
│── logs/                    # Training logs
│── README.md
```

---

## Requirements

* Python 3.12
* Gymnasium
* Stable-Baselines3
* PyTorch
* NumPy
* Matplotlib

Install dependencies using:

```bash
pip install stable-baselines3[extra]
pip install gymnasium
pip install matplotlib
```

---

## How to Run

### 1. Train the Agent

```bash
python train.py
```

This generates:

* `ppo_model.zip`
* `learning_curve.png`

---

### 2. Evaluate the Model

```bash
python evaluate.py
```

This generates:

* `evaluation_report.txt`

---

### 3. Test the Agent

```bash
python test.py
```

A simulation window will open showing the trained CartPole agent balancing the pole.

---

## Training Results

| Metric              | Value               |
| ------------------- | ------------------- |
| Environment         | CartPole-v1         |
| Algorithm           | PPO                 |
| Evaluation Episodes | 100                 |
| Mean Reward         | **500.00 / 500.00** |
| Standard Deviation  | **0.00**            |
| Status              | **Solved / Passed** |

---

## Technologies Used

* Python
* Gymnasium
* Stable-Baselines3
* PyTorch
* NumPy
* Matplotlib

---

## Author

**D V Shriram**
Student
VIT Bhopal University

---

## License

This project is developed for educational and learning purposes.
