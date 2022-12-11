import os

file_dir = 'dist/news/world/'

file_list = os.listdir(file_dir)

print(file_list[:3])

with open('dist/all_world.txt', 'w', encoding="utf-8") as outfile:
    for fname in file_list:
        with open(f'{file_dir}{fname}', encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)


with open('dist/all_world.txt', encoding="utf-8") as f:
    doc = f.read()
    lines = doc.split('. ')
    print(len(lines))
    with open('dist/train.txt', mode="w", encoding="utf-8") as f:
            for line in lines:
                line = line.replace('Getty Images', '')
                f.write("".join(line) + "\n")