print("Swallow Speed Analysis : Version 1.0\n")

data_in_mph = [] #list to store data in miles per hour.
data_in_kmph = [] #list to store data in kilometre per hour.

while True: #Starting infinite loop
    reading = input("Enter the next reading : ")

    if reading == "":# checking if the input is empty.
        break 

    if (reading[0].lower() not in ["u", "e"]) or any(char.isalpha()  for char in reading[1:]): #checking the format of input.
        print("Invalid Input!")
        continue

    if reading[0].lower() == "u": #checking if the data is in british.
        reading = float(reading[1:])
        data_in_mph.append(reading)
        data_in_kmph.append(reading*1.60934)
        print("Reading Saved.")
    else:
        reading = float(reading[1:])
        data_in_kmph.append(reading)
        data_in_mph.append(reading/1.60934)
        print("Reading Saved.")


if data_in_mph == []: # checking if data is empty.
    print("\nNo Readings entered. Nothing to do.")

else :
    print(f"\n {len(data_in_kmph)} Readings Analysed.\n") #printing the number of data entered.
    max_in_mph = max(data_in_mph)
    max_in_kmph = max(data_in_kmph)
    min_in_mph = min(data_in_mph)
    min_in_kmph = min(data_in_kmph)
    avg_in_mph = sum(data_in_mph)/len(data_in_mph)
    avg_in_kmph = sum(data_in_kmph)/len(data_in_kmph)

    print(f"\nMax : {max_in_mph:.1f} mph, {max_in_kmph:.1f} kmph")
    print(f"Min : {min_in_mph:.1f} mph, {min_in_kmph:.1f} kmph")
    print(f"Avg : {avg_in_mph:.1f} mph, {avg_in_kmph:.1f} kmph")