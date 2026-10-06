# 🧠 Machine Learning Full Foundations

![Python](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Fundamentals-green)
![Notebooks](https://img.shields.io/badge/Notebooks-19-orange)
![Status](https://img.shields.io/badge/Status-Learning%20in%20Progress-blue)

This repository is my attempt to **build a strong foundation in Machine Learning from the ground up**.

Instead of jumping straight into advanced models or large frameworks, I wanted to slow down and understand **how the core algorithms actually work** — both mathematically and practically.

So this repo contains a collection of **19 notebooks covering essential Machine Learning concepts**, implemented step by step.

It is also part of my **100 Days of Machine Learning journey**, where I learn a concept, experiment with it, and document the process.

---

# 📚 What You'll Find Here

The notebooks walk through important Machine Learning topics starting from the basics and gradually moving toward more complex ideas.

### Foundations
- Introduction to Machine Learning  
- Supervised Learning  
- Linear Regression  
- Gradient Descent  
- Locally Weighted Linear Regression  

### Classification Algorithms
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Machines (SVM)  
- Naive Bayes  

### Tree-Based Models
- Decision Trees  
- Random Forest  

### Ensemble Methods
- Boosting Algorithms  

### Neural Network Basics
- Neural Networks / Perceptron  
- Activation Functions  
- Backpropagation  

### Optimization & Training
- Loss Functions  
- Optimization Algorithms  

### Unsupervised Learning
- K-Means Clustering  

### Dimensionality Reduction
- Principal Component Analysis (PCA)

---

# 📂 Repository Structure

```text
ML_fundamentals/
├── Notebooks/              # 19 learning notebooks; keep their existing filenames
├── scripts/check_notebooks.py
├── requirements.in         # Direct dependencies
├── requirements.txt        # Pinned notebook and JupyterLab environment
├── .github/workflows/daily-streak.yml  # Notebook checks, not streak commits
└── README.md
```

Each notebook focuses on **one concept at a time** and usually includes:

• Explanation of the idea  
• Some mathematical intuition  
• Code implementation  
• Small experiments or visualizations  

The goal is to make the learning **practical and intuitive**, not just theoretical.

---

# 🧭 How I'm Using This Repo

My approach while building this repository is simple:

1. Study the concept  
2. Understand the math behind it  
3. Implement it step by step  
4. Run small experiments to see how it behaves  

This helps avoid treating ML algorithms as **black boxes**.

---

# Setup and running

The pinned environment is tested with **Python 3.12.14**. Other Python versions
are not covered by this check.

```bash
git clone https://github.com/harshitgavita-07/ML_fundamentals.git
cd ML_fundamentals
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

Open the notebooks interactively:

```bash
python -m jupyterlab
```

Or execute all 19 notebooks in fresh kernels:

```bash
python scripts/check_notebooks.py
```

The checker prints a result for each notebook and exits with a nonzero status
if any notebook fails. It executes in memory and does not overwrite notebook
outputs or commit files. Execution checks catch runtime errors; they do not
prove that every explanation or model is correct.

The linear-regression notebook downloads the California housing dataset through
scikit-learn on first use. An internet connection is needed for that download;
later runs can use scikit-learn's local data cache. The other notebooks use
bundled scikit-learn datasets or generated examples.

## Automated checks

Pushes to main, pull requests and manual workflow runs execute the same checker
on Python 3.12.14. The former daily streak-commit workflow has been replaced:
checks no longer append to `STREAK_LOG.md` or make automated activity commits.
The old log remains as history. The separate snake-graphic workflow is unchanged.

`requirements.in` records the direct dependencies, and `requirements.txt` pins
the resolved environment. After a dependency update, regenerate the lock with
`uv pip compile requirements.in --python 3.12 --output-file requirements.txt`,
then execute all notebooks before committing it.

---

# ⭐ If This Helps You

If you find this repository useful or interesting, feel free to give it a **star ⭐**.

It motivates me to keep improving the project and sharing what I learn.
