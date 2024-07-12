# Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative" or "zero".

def determine_sign(num: int) -> str:
    if num <= 0:
        if num < 0:
            return "negative"
        return "zero"
    return "positive"