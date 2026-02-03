from cs50 import get_string

text = get_string("Text: ")

letters = 0
words = 0
sentences = 0

for i in range(len(text)):
    if text[i].isalpha():
        letters += 1

    if text[i] == ' ':
        words += 1

    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentences += 1

words += 1

L = (letters / words) * 100
S = (sentences / words) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
