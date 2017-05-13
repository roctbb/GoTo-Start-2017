emotions = { "anger": 0.34, "happiness": 0.9, "surprise": 0.1}
emotions_list = list(emotions.items())
emotions_sorted = sorted(emotions_list, key=lambda x:x[1], reverse=True)
print(emotions_sorted[0][0])