data = 1
for i in range(1, 4):
    file_name = 'file{}.txt'.format(i)
    with open(file_name, 'w') as f:
        f.write(str(data))
        data *= 12

