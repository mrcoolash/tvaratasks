# TVARA Tasks

This repository contains solutions for three tasks:

- Task A — DSA: LeetCode 142 Linked List Cycle II
- Task B — Gemini API Integration using Flask
- Task C — Vectorization with Hugging Face Embeddings

---

# Task A — LeetCode 142: Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins.

If there is no cycle, return `NULL`.

## Approach
I used Floyd’s Cycle Detection Algorithm, also known as the Tortoise and Hare Algorithm.

### Steps
1. Use two pointers:
   - `slow` moves one step at a time
   - `fast` moves two steps at a time
2. If the linked list contains a cycle, both pointers will eventually meet.
3. Once they meet:
   - Move one pointer back to the head
   - Keep the other pointer at the meeting point
4. Move both pointers one step at a time.
5. The node where they meet again is the starting point of the cycle.

## Time Complexity
- O(n)

## Space Complexity
- O(1)

## Why This Approach?
- No extra memory is used
- Faster and more optimal than using hash sets
- Works in linear time

## Example

Input:

```text
3 -> 2 -> 0 -> -4
     ^         |
     |_________|
```

Output:

```text
Node with value 2
```

---

# Task B — Gemini API Integration

## Objective
Build a simple Flask API that accepts a prompt and forwards it to Gemini 2.5 Flash.

## Tech Stack
- Python
- Flask
- Requests
- python-dotenv

## Files

```text
taskB/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Approach
1. Create a Flask app
2. Add a `/generate` POST endpoint
3. Read prompt from request body
4. Send request to Gemini API
5. Extract generated response text
6. Return formatted JSON response
7. Support optional debug mode

## Features
- Handles missing prompt errors
- Handles missing API key errors
- Handles timeout and connection errors
- Supports `.env` for secure API key storage
- Supports optional raw Gemini response through `debug=true`

## Example Request

```json
{
  "prompt": "Explain machine learning in simple words"
}
```

## Example Response

```json
{
  "prompt": "Explain machine learning in simple words",
  "response": "Machine learning is a method where computers learn patterns from data and make predictions without being explicitly programmed."
}
```

## Debug Example

```json
{
  "prompt": "What is deep learning?",
  "debug": true
}
```

## PowerShell Testing Command

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate" `
-Method Post `
-Headers @{"Content-Type"="application/json"} `
-Body '{"prompt":"Explain artificial intelligence in simple words"}'
```

## Requirements Installation

```bash
pip install flask requests python-dotenv
```

## Security
- API key is stored inside `.env`
- `.env` is added to `.gitignore`
- Sensitive credentials are not pushed to GitHub

---

# Task C — Vectorization with Hugging Face

## Objective
Use a lightweight embedding model from Hugging Face and perform similarity search.

## Model Used
`intfloat/e5-small-v2`

## Why This Model?
- Lightweight
- Fast inference
- Good semantic similarity performance
- Suitable for local systems with limited resources

## Tech Stack
- sentence-transformers
- torch
- scikit-learn
- numpy

## Approach
1. Load embedding model
2. Create example sentences
3. Add required `query:` and `passage:` prefixes
4. Generate embeddings
5. Use cosine similarity to compare embeddings
6. Find the most relevant sentence

## Example Query

```text
What is deep learning?
```

## Example Sentences

```text
1. Machine learning helps computers learn patterns from data.
2. Deep learning is a subset of machine learning that uses neural networks.
3. Natural language processing allows computers to understand human language.
```

## Example Output

```text
Sentence 1 Score: 0.81
Sentence 2 Score: 0.94
Sentence 3 Score: 0.42

Best Match:
Deep learning is a subset of machine lear