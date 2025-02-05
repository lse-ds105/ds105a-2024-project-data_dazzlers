[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# 🎨 Exploring the Relationship Between Economic Periods, Social Movements, and Art Themes in America

1.  How do economic periods, as measured by GDP, affect art themes in America?
2.  Is there a relationship between social movements, like Black Lives Matter and GDP?

## 🎨 Description of this repository:

1.  **What you will find here:**

    -   A `code` folder that contains there's four folders. The `FRED_Data`, `GDELT_Data` and `Smithsonian_Data` folders contain notebooks on gathering and processing the respective data. While the `Visualisations` folder contains notebooks that demonstrate how we creeated all our visualisations.
    -   A `data` folder that contains raw and processed data. The database that we created with all our data is in the processed folder under social_movements.db
    -   The `website` and `docs` folder contain the markdown, html and images used to produce our website
    -   Within the `docs` folder, there's a `figures` folder that contains all the visualisations we used in the website
    -   A `reflections` folder showing how we have individually contributed and developed throughout this project

2.  **What we initially wanted to discover:**

-   We wanted to explore how changes in GDP might influence art and social movements. Drawing from historical examples like the Dutch Golden Age and the Renaissance, we hypothesized that economic booms would drive art that celebrates prosperity, while downturns would lead to darker, more sombre themes. Focusing on the U.S., we aimed to see if the economic boom after WWI and the Great Depression had a similar effect on art.

-   We also wondered how GDP impacted social movements. Would movements like MeToo or Black Lives Matter have positive associations during prosperous times and more negative tones during economic hardship.

3.  **How we used AI:**
      -   AI was used to gain an understanding of how to properly use GitHub branches, such as fixing merging issues
    - It was used to edit pulling functions to be specific to the data we wanted to pull
    - It was mainly used to explain errors in the code and provide suggestions throughout the project, such as explaining why visualisations didn't achieve their desired look and asking for suggestions to improve the code
    - It was also used to generate ideas for visualisations
    - As for the website, AI was used to explain how to change the default background for dark mode on the website
   
------------------------------------------------------------------------

## 🎨 All API Credentials Setup

This explains how to obtain all API credentials and securely set them up for use.

### 1. Smithsonian:

-   To obtain a Smithsonian API key, you must create an account with [Smithsonian API Website](https://api.data.gov/signup/)

-   The API key will then be emailed to you

### 2. FRED:

-   FRED API credentials can be obtained by creating an account with the [FRED API website](https://fredaccount.stlouisfed.org/login/secure/).

-   You then create an application and are given an API key

### 3. GDELT:

-   GDELT data is accessible to the public and does not require an API key

------------------------------------------------------------------------

## 🎨 How to run the code

### Step 1 - Clone the project repository

```              
git clone <git@github.com:lse-ds105/ds105a-2024-project-data_dazzlers.git>
```

```         
cd <ds105a-2024-project-data_dazzlers>
```

### Step 2 - Creating a virtual environment

**1. If you already have conda installed:**

You can create a new environment with the following command:

```         
conda create -n .venv
```

Then, activate the environment:

``` 
conda activate .venv
```

Install `pip` inside conda:

``` 
conda install pip
```

**2. If you don't have conda installed**

Then on the command line run these commands

```         
cd /path/to/ds105a-2024-project-data_dazzlers
python -m venv .venv
```

If on Windows, run:

```         
.venv\Scripts\activate
```

If on MacOS or Linux, run:

```         
source .venv/bin/activate
```

**3.  Install the required dependencies:**

    ```              
    pip install -r requirements.txt
    ```

**To deactivate the virtual environment:** type `deactivate` into your terminal

### Step 3 - Order to run code in

``` 
python helper_functions.py
```

This will run the functions stored.

If you're working with Jupyter Notebooks, you can start the notebook server with:

``` 
jupyter notebook
```

Then, navigate to the relevant notebook file and run the cells to replicate the analysis interactively.

We recommend running the code in this order:

1.  Run NB01 for the FRED and Smithsonian data, then run NB01 and NB02 for the GDELT data to collect and process the data
2.  Run all the notebooks in the [Visualisations](code/Visualisations/) folder in any order for data visualisations

## 🎨 Work Contribution

| Contributors (%) | Data Collections (%) | Data Cleaning (%) | Visualisations (%) | Website Production (%) | Documentation (%) |
|----|----|----|----|----|----|
| Gbemi Banjo | 5% | 15% | --- | 100% | 33% |
| Amelia Dunn | 95%| 85% | --- | --- | 33% |
| Chiara Franzin | --- | --- | 100% | --- | 33% |
