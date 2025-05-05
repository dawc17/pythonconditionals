yourWeight = float(input("Enter your weight in kg: "))
planet = int(input("Now enter a planet number from 1-7: "))

destWeight = 0

if planet == 1:
    destWeight = yourWeight * 0.38
elif planet == 2:
    destWeight = yourWeight * 0.91
elif planet == 3:
    destWeight = yourWeight * 0.38
elif planet == 4:
    destWeight = yourWeight * 2.53
elif planet == 5:
    destWeight = yourWeight * 1.07
elif planet == 6:
    destWeight = yourWeight * 0.89
elif planet == 7:
    destWeight = yourWeight * 1.14
else:
    print("Invalid planet number")

print(f"Your weight on this planet is {round(destWeight, 2)} kg.")