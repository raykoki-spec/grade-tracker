# File: README.md

# Grade Tracker

A students grade tracker for school examinations.
It reads the students' raw data logged by the teacher, cleans it, computes the results then outputs the report.

## What It Does

- Reads students score from a structured CSV data
- Handles missing and invalid input without crashing
- Applies logic to compute results  and assign each student's average score and grade
- Formats a clear report
- Exports the summary to JSON

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

Python

Built-in Modules: `io`, `csv`, `JSON`
