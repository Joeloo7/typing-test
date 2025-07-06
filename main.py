import time
import random

sentences = [
    "Python is an amazing programming language.",
    "Typing speed can be measured with simple code.",
    "Practice typing to improve your accuracy and speed."
]

sentence = random.choice(sentences)

print("Type the following sentence:")
print(f"{sentence}")

input("Press Enter when you're ready to start typing...")

start_time = time.time()
typed_sentence = input("Start typing here:\n")
end_time = time.time()

time_taken = round(end_time - start_time, 2)
print("Time Taken:", time_taken, "seconds")

word_count=len(typed_sentence.split())

if time_taken==0:
    wpm=0
else:
    wpm = round((word_count/time_taken)*60)

print("Typing Speed:",wpm,"words per minute")

correct_chars = 0
for i in range(min(len(sentence),len(typed_sentence))):
    if sentence[i]==typed_sentence[i]:
        correct_chars += 1

accuracy=(correct_chars/len(sentence))*100
accuracy=round(accuracy, 2)

print("Accuracy:",accuracy,"%")
