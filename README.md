# File: README.md

# Grade Tracker

A students grade tracker for school examinations.
Asssigns the grade to each student by the use of a Python function and if/else loop.

## What It Does

- Accepts students score list
- Calculates each student's average score
- Prints the average grade notes
- Exports a weekly summary report as JSON

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
print(f"{row['name']:<20} {average:>5} {grade:>5}")
    results.append({"name": row["name"],
                     "scores": [row["score1"], row["score2"], row["score3"]],
                     "average": average,
                     "grade": grade
                     })

```

## Sample Output

```
Victor Kiptoo         88.3     B
Edwin Kibet           94.7     A

```

## Stack

Python, JSON