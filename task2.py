text_to_write = input("Enter text to write to the file: ")
try:
    with open("output.txt", "w") as file:
        file.write(text_to_write + "\n")
    print("Data successfully written to output.txt.")
except Exception as e:
    print(f"Error writing to file: {e}")

text_to_append = input("\nEnter additional text to append: ")
try:
    with open("output.txt", "a") as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.")
except Exception as e:
    print(f"Error appending to file: {e}")

print("\nFinal content of output.txt:")
try:
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"Error reading the file: {e}")
