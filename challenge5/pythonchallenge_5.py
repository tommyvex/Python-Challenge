import pickle

save = ""
file = open("pickle.p", "rb")
pickle_loaded = pickle.load(file)

file.close()

for line in pickle_loaded:
    save += "\n"
    for tup in line:
        char = tup[0]
        amount = tup[1]

        for loop in range(amount):
            save += char

print(save)
