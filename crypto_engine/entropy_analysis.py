import math

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1

    entropy = 0
    length = len(data)
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy

def analyze_file_entropy(file_path: str, threshold: float = 7.5) -> dict:
    with open(file_path, "rb") as f:
        data = f.read()

    entropy = calculate_entropy(data)
    result = {
        "entropy": entropy,
        "is_suspicious": entropy >= threshold
    }
    return result
