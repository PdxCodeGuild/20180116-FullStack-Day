import random

eye_list = [":", ";", "=", '8']
nose_list = ["-", "o", "*"]
mouth_list = [")", "(", "}", "{", "D", "P"]

emotiocon = random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list)

print(emotiocon)

