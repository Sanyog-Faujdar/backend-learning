# Data Processing
def analyze_numbers(numbers: list[int]) -> dict[str, int | float | None]:
    if not numbers:
        return {
        "count": 0,
        "unique_count": 0,
        "sum": 0,
        "average": 0,
        "minimum": None,
        "maximum": None,
        }
    count: int = 0
    total: int = 0
    minimum: float = float('inf')
    maximum: float = float('-inf')
    seen: set = set()
    for no in  numbers:
        count += 1
        if no in seen:
            seen.add(no)
        total += no
        if minimum > no:
            minimum = no
        if maximum < no:
            maximum = no
    average: float = total/count
    unique_count: int = len(seen)
    return {
        "count": count,
        "unique_count": unique_count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
    }
    

numbers: list = [10, 20, 20, 30, 40, 40, 40, 50]
print(analyze_numbers(numbers))
numbers: list = []
print(analyze_numbers(numbers))