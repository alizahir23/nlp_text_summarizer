# End-to-End Text Summarizer Project

This project implements a text summarization model using Hugging Face transformers. The goal is to provide an end-to-end solution that ingests data, validates it, transforms it, trains a model, and finally evaluates and serves the model. This project also includes AWS CICD deployment with GitHub Actions.

## Table of Contents

- [Overview](#overview)
- [Workflows](#workflows)
- [How to Run](#how-to-run)
- [AWS CICD Deployment with GitHub Actions](#aws-cicd-deployment-with-github-actions)
- [Improving the Model](#improving-the-model)
- [License](#license)

## Overview

The NLP Text Summarizer project aims to develop a robust text summarization pipeline. This includes data ingestion, validation, transformation, model training, and evaluation. The project uses the Hugging Face transformers library to leverage pre-trained models and fine-tune them for text summarization tasks.

## Workflows

1. **Update config.yaml:** Configure the necessary parameters and paths.
2. **Update params.yaml:** Define the training parameters.
3. **Update entity:** Update the entity classes as needed.
4. **Update the configuration manager in `src/config`:** Manage configurations efficiently.
5. **Update the components:** Implement and update the necessary components for the pipeline.
6. **Update the pipeline:** Ensure the pipeline stages are correctly defined and linked.
7. **Update `main.py`:** Define the execution flow of the pipeline.
8. **Update `app.py`:** Set up the FastAPI application for serving predictions.

## How to Run

### Steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/alizahir23/nlp_text_summarizer
   cd nlp_text_summarizer
   ```

2. Create a conda environment:

   ```bash
   conda create -n summary python=3.8 -y
   conda activate summary
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open up your local host and port in the browser to access the API documentation.

## AWS CICD Deployment with GitHub Actions

1. **Login to AWS Console:**

2. **Create IAM user for deployment** with the following access:

   - EC2: Virtual machine
   - ECR: Elastic Container Registry to save your Docker image in AWS

   **Policies:**

   - `AmazonEC2ContainerRegistryFullAccess`
   - `AmazonEC2FullAccess`

3. **Create ECR repo to store/save Docker image:**

   - Save the URI: `058264517556.dkr.ecr.us-east-1.amazonaws.com/nlp_text_summarizer`

4. **Create EC2 machine (Ubuntu):**

5. **Install Docker in EC2 Machine:**

   ```bash
   sudo apt-get update -y
   sudo apt-get upgrade
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

6. **Configure EC2 as self-hosted runner:**

   - Go to `Settings > Actions > Runner > New self-hosted runner`
   - Choose OS and run the provided commands.

7. **Setup GitHub secrets:**
   ```plaintext
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_REGION=us-east-1
   AWS_ECR_LOGIN_URI=058264517556.dkr.ecr.us-east-1.amazonaws.com
   ECR_REPOSITORY_NAME=nlp_text_summarizer
   ```

## Improving the Model

To improve the model, you can update the `TrainingArguments` in your configuration file. Adjusting these parameters can help enhance the model's performance.

```python
TrainingArguments:
  num_train_epochs: 1          # Increase the number of training epochs
  warmup_steps: 500            # Increase or decrease the warmup steps
  per_device_train_batch_size: 1  # Adjust batch size based on available resources
  weight_decay: 0.01           # Modify weight decay for regularization
  logging_steps: 10            # Change logging steps for more/less frequent logs
  evaluation_strategy: steps   # Use 'epoch' for evaluating at the end of each epoch
  eval_steps: 500              # Change evaluation steps frequency
  save_steps: 1e6              # Adjust model saving frequency
  gradient_accumulation_steps: 16  # Modify gradient accumulation steps
```

Experimenting with these parameters can help you find the optimal settings for your specific use case. Always monitor the training and evaluation metrics to ensure the changes are beneficial.
