# Cmse802_project


# Project Title: "What factors distinguish retaliatory/reprisal acts from indsiscriminate violence"


## Project Description
This project explores detecting selective and indiscriminate violence by the government on civilians. I term selective violence as retaliatory acts or reprisals by the govenrmnet following actions either by rebel groups or the communities. To do this I plan to use semi-supervised machine learning to train a model on news data to be able to distinguish between these two acts. The project will particularly focus on government-led reprisals. 


## Project Objectives
1. First, there is a debate in the conflict literature on whether govenrmnet violence has a reducing effect on insurgent activities. I plan on developing a model that can distinguish between selective and indiscriminate violence to see whether both or either have a reducing effect on insurgent activities
2. This project will train model that would be able to label news articles to identify retaliatory acts and differentiate them from non-reprisal acts.
3. The project will analyze model performance using metrics such as accuracy, precision, recall, and F1-score.


## Folder Structure

The following is an overview of the project’s folder structure, detailing the purpose and contents of each folder:

### 1. `Newspaper`
- **Description**: This folder contains the downloaded Nigerian news sources from LexisNexis.
- **Contents**:
  - The folder is split into five subfolders (`1`, `2`, `3`, `4`, and `5`).
  - Each subfolder contains approximately 10,000 news stories in JSON format.

### 2. `Converted News`
- **Description**: This folder mirrors the structure of the `Newspaper` folder, but with JSONL files.
- **Contents**:
  - The same news stories from the `Newspaper` folder are converted to JSONL format for easier annotation.
  - The folder has five subfolders (`1`, `2`, `3`, `4`, and `5`) containing the converted news articles.

### 3. `JSONL Output`
- **Description**: This folder contains compressed JSONL news into a single JSONL file for use with the annotation tool Prodigy.
- **Contents**:
  - All the news files in the `Converted News` folder are merged and compressed into six large JSONL files, allowing for efficient annotation during the machine learning process.

### 4. `Annotate`
- **Description**: This folder contains the annotations.
- **Contents**:
  - These files have been labeled and annotated, and they are used as the training data for the machine learning model.

### 5. `Scripts`
- **Description**: This folder contains Python scripts used for data conversion and model training.
- **Contents**:
  - **Conversion Script**: Converts the JSON news files to JSONL format for annotation.
  - **Preprocessing and Training Script**: Preprocesses the annotated files and trains the machine learning model based on the annotated data.
