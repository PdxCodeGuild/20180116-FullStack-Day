import random

eye_list = [":", ";", "=", "8"]
nose_list = ["-", "o", "*"]
mouth_list = [")", "(", "}", "{", "D", "P"]


run_emotions = 0

while run_emotions < 5:
    emotiocon = random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(emotiocon)
    run_emotions = run_emotions + 1
