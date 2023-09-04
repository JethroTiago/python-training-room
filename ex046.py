from time import sleep
print('\033[1;34mContagem Regressiva\033[m')
print('\033[1;32m-=-\033[m' * 20)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('\033[1;32m-\U0001F386-\033[m' * 14)
