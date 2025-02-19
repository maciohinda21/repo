from huggingface_hub import HfApi
from transformers import (DistilBertForSequenceClassification, DistilBertTokenizer, Trainer, TrainingArguments, DataCollatorWithPadding)
from datasets import load_dataset
import numpy as np

# Load the dataset
dataset = load_dataset("imdb")

# Load the pre-trained model and tokenizer
model_name = "distilbert-base-uncased"
model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = DistilBertTokenizer.from_pretrained(model_name)

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)  # Dynamic padding

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Split the dataset into training and evaluation sets
train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))  # Subset for quick training
eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2,
    save_steps=500,
    logging_dir="./logs",
    logging_steps=10,
    fp16=True,  # Mixed precision training
)

# Define the Trainer
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=data_collator
)

# Train the model
trainer.train()

# Evaluate the model
trainer.evaluate()

# Save the model locally
save_path = "[Placeholder]"  # Replace with your desired path
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

print(f"Model and tokenizer saved to {save_path}")