# Website Content Similarity Checker

This project compares the content similarity between two web pages using cosine similarity of document vectors derived from simhash values of n-grams in the content. The program accepts two URLs, retrieves and processes the HTML content, and calculates a similarity score.

## Table of Contents
- [Features](#features)
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features
- Extracts content from the `<body>` section of HTML from any two given URLs without external libraries.
- Processes and cleans HTML to extract meaningful text.
- Generates n-grams and hashes them using simhash to create a document vector.
- Compares document vectors using cosine similarity to determine content similarity.

## Project Overview
This project aims to calculate the similarity between two web pages based on their textual content. It:
1. Accepts two URLs.
2. Fetches and parses the HTML content of each URL to extract meaningful text from the `<body>`.
3. Processes text into n-grams and calculates simhash values for each n-gram.
4. Creates document vectors from simhash values.
5. Compares the vectors using cosine similarity to generate a similarity score.

## Methodology

### 1. **HTML Content Extraction**
   - Fetches raw HTML content from each URL.
   - Parses the HTML structure manually to extract only the `<body>` content without using external libraries.

### 2. **Content Processing and n-gram Generation**
   - The content is tokenized into words.
   - Generates n-grams (e.g., bigrams, trigrams) from the tokenized text for capturing contextual meaning.

### 3. **Simhash Vectorization**
   - Each n-gram is hashed using binary hashing to produce a unique simhash value.
   - These values are aggregated to form a document vector representing the entire content of the page.

### 4. **Cosine Similarity Calculation**
   - Computes the cosine similarity between the two document vectors to yield a similarity score between 0 (completely dissimilar) and 1 (identical).

## Example
```bash
python main.py https://example.com/page1 https://example.com/page2
```
Output:
```
Similarity score: 0.85
```
