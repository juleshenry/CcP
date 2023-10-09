import re

def add_one_to_numbers(text):
    pattern = r'\d+(?:\s+\d+)+'
    matches = re.findall(pattern, text)

    for match in matches:
        numbers = [int(num) + 1 for num in re.findall(r'\d+', match)]
        new_numbers = ' '.join(map(str, numbers))
        text = text.replace(match, new_numbers)

    return text

text = "123 45 678 9 12345"
modified_text = add_one_to_numbers(text)

print(modified_text)
