[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# 🎨 Exploring the Relationship Between Economic Periods, Social Movements, and Art Themes in America
1. How do economic periods, as measured by GDP, affect art themes in America?
2. How do social movements, like Black Lives Matter, influence art themes in America?

## 🎨 Short term to dos:
 - [ ] Make a projects board
 - [ ] Decide on alternative to Reddit
 - [ ] As we collect data make a note of any requirements 
 - [ ] Collect and clean FRED
 - [ ] Collect and clean Smithsonian
 - [ ] Colect and clean alternative to Reddit

## 🎨 Longer term to dos:
 - [ ] Combine data into an SQLite Data Base
 - [ ] Think about website design - what sort of headings/pages do we want?
 - [ ] Decide on data visualisations
 - [ ] Do data visualisations
 - [ ] Analysis of data visualisations, what did we find?

## Brief decription of this repository:
1. **What this repository is about:**

2. **What we initially wanted to discover:**

3. **What we did:**

4. **Our findings:**

5. **How we used AI**


## Using the Virtual Environment in a New System

To set up the virtual environment on a new system using **Pyenv** or **Conda**, follow these instructions.


### **Option 1: Using Pyenv + Virtualenv**

1. **Install `pyenv` and `pyenv-virtualenv`** (if not already installed):
   - **macOS/Linux:**  
     ```bash
     curl https://pyenv.run | bash
     ```
     Add the following to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):
     ```bash
     export PATH="$HOME/.pyenv/bin:$PATH"
     eval "$(pyenv init --path)"
     eval "$(pyenv init -)"
     eval "$(pyenv virtualenv-init -)"
     ```
     Restart your terminal or run:
     ```bash
     exec $SHELL
     ```

2. **Clone the project repository:** -> need to change this to be my actual repository
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

3. **Create and activate a Python virtual environment using Pyenv:**
    ```bash
    pyenv install <python_version>  # Example: pyenv install 3.11.5
    pyenv virtualenv <python_version> <env_name>  # Example: pyenv virtualenv 3.11.5 myenv
    pyenv activate <env_name>
    ```
4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **To deactivate the virtual environment:**
    ```bash
    pyenv deactivate
    ```


### **Option 2: Using Conda**

1. **Prerequisites**

Make sure you have Conda installed on your system. You can install it using either **Miniconda** (lightweight) or **Anaconda** (full distribution with data science libraries).

- **Download and Install Miniconda (Recommended):**  
  [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html)

- **Download and Install Anaconda:**  
  [Anaconda Installation](https://www.anaconda.com/products/distribution)


2. **Clone the project repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

3. **Create a new Conda environment with the same name or any name you prefer:**
    ```bash
    conda create --name <env_name> python=<python_version>
    # Example: conda create --name myenv python=3.11
    ```

4. **Activate the Conda environment:**
    ```bash
    conda activate <env_name>
    ```

5. **Install the required dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```
6. **To deactivate the Conda environment:**
    ```bash
    conda deactivate
    ```

---

## All API Credentials Setup

This explains how to obtain all API credentials and securely set them up for use.

### 1. Smithsonian:





### 2. Fred


---

## Replicating the Results from the Repository

To replicate the results from this repository, follow the steps below.

### Prerequisites

1. **Python version:** Ensure that you are using Python 3.7 or later.

2. **Required tools:** 
   - [Git](https://git-scm.com/) (for cloning the repository)
   - [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/) (for installing dependencies)
   - [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) (optional, for managing virtual environments)

### Step 1: Clone the Repository

First, clone the repository to your local system using the following command in terminal:

```bash
git clone git@github.com:lse-ds105/ds105a-2024-project-data_dazzlers.git
```

### Running the code:

After setting up the environment and creating the .env file, cd to code folder in terminal, then run the code by executing the following:

```bash
python helper_functions.py
```
**the above is just an example - we need to replace this with our actual python files**

This will run the functions stored.

If you're working with Jupyter notebooks, you can start the notebook server with:

```bash
jupyter notebook
```

Then, navigate to the relevant notebook file and run the cells to replicate the analysis interactively.



