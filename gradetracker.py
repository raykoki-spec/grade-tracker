import csv, io, json

csv_data = """name,score1,score2,score3
Amina Agnes,85,90,78
Ben Koki,92,88,95
Chris Kamket,76,84,80
Victor Kiptoo,89,91,85
Edwin Kibet,95,97,92
"""
#Function to calculate average score
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def calculate_average(scores):
    valid_scores = [score for score in scores if score is not None]
    if not valid_scores:
        return None
    return round(sum(valid_scores) / len(valid_scores),1)
def letters_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#Process the CSV data


reader = csv.DictReader(io.StringIO(csv_data))
results = []
print("=" * 50)
print(f"{'NAME':<20} {'AVERAGE':>5} {'GRADE':>5} NOTES")
print("=" * 50)

for row in reader:
    scores = [parse_score(row["score1"]), parse_score(row["score2"]), parse_score(row["score3"])]
    invalid_scores = [score for score in scores if score is None]
    average = calculate_average(scores)
    grade = letters_grade(average)
    notes = "Invalid score(s)" if invalid_scores else ""
    print(f"{row['name']:<20} {average:>5} {grade:>5}")
    results.append({"name": row["name"],
                     "scores": [row["score1"], row["score2"], row["score3"]],
                     "average": average,
                     "grade": grade
                     })
print("=" * 50)

#Class summary
valid_averages = [result["average"] for result in results if result["average"] is not None]
class_average = round(sum(valid_averages) / len(valid_averages), 1) if valid_averages else None
print(f"Class Average: {class_average}")
print(f"Total Students: {len(results)}")

#Export results to JSON
print("\nJSON Export:")
print(json.dumps(results, indent=1))
