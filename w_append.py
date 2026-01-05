text = input("Enter text to write to the file: ")
with open("output.txt", "w") as fh:
    fh.write(text + "\n")
print("Data successfully written to output.txt.")

extra = input("Enter additional text to append: ")
with open("output.txt", "a") as fh:
    fh.write(extra + "\n")
print("Data successfully appended.")

with open("output.txt", "r") as fh:
    print("\nFinal content of output.txt:")
    print(fh.read())

