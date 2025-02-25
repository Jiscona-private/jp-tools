import random

with open("term-generator_input.txt", mode="r") as file:
    content = file.readlines()

    lengths = content[0].split(":")[1].strip()
    minLength = int(lengths.split("-")[0])
    maxLength = int(lengths.split("-")[1])

    repetitions = int(content[1].split(":")[1].strip())

    characters = []
    probabilities = []
    for i in range(2,len(content)):
        characters.append(content[i].split(":")[0])
        probabilities.append(int(content[i].split(":")[1].strip()))
total = sum(probabilities)

# The probability is equal to the space between the density of two possible characters
density = [probabilities[0]]
for probIndex in range(1, len(probabilities)):
    density.append(probabilities[probIndex] + sum(probabilities[:(probIndex)])) 

with open("term-generator_output.txt", mode="w") as file:
    for length in range(minLength,maxLength+1):
        for repetition in range(repetitions):
            term = ""
            for charIndex in range(length):
                rand = random.randint(0,total)
                densityIndex = 0
                while rand > density[densityIndex]:
                    densityIndex += 1
                term += characters[densityIndex]
            file.write(term+"\n")
        