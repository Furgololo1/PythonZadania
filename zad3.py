

year = 2021

for i in range(year, year+20):
    if i%4 == 0 and i%100 != 0 or i%400 == 0:
        print(i)