Nepali = ['Daal', 'Bhat', 'Gundruk']
Chinese = ['EggRoll', 'Fried Rice', 'Pot Sticker']
Italian = ['Pizza', 'Pasta' ,'Risotto']
dish = input("Enter the name of the dish:")
if dish in Nepali:
    print("This is a nepali dish.")
elif dish in Chinese:
    print("Chinese dish.")
elif dish in Italian:
    print("Italian dish.")
else:
    print("Sorry , I don't know which cuisine is", dish)

