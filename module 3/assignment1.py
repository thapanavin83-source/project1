length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42
if length < size_limit:
    missing = size_limit - length
    print("The zander does not meet the size limit. ")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit. ")