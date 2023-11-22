# Text Preprocessing Library

## Overview
This Python library provides a range of functions for preprocessing text data. It includes functions to remove stopwords, emails, brackets, numbers, punctuations, extra spaces, and expand contractions. It utilizes regular expressions, NLTK, and SpaCy libraries to perform these operations.

## Features
- **Remove Stopwords**: Removes common stopwords using SpaCy's English language model.
- **Remove Email**: Extracts and removes email addresses from text.
- **Remove Brackets**: Deletes any kind of brackets and their contents.
- **Remove Numbers**: Strips out numerical characters.
- **Remove Punctuations**: Replaces all punctuation marks with spaces.
- **Remove Extra Space**: Eliminates excess whitespace, tabs, and newlines.
- **Expand Contractions**: Converts contractions to their expanded forms, including slang.
- **Text Preprocessing**: A comprehensive function that combines several of the above features for general text preprocessing.

## Dependencies
To use this library, you need to have the following Python packages installed:
- `re`
- `pandas`
- `contractions`
- `nltk`
- `spacy`

## Installation
Ensure you have the required packages:
```bash
pip install pandas contractions nltk spacy
