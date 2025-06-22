filename1 = "output.txt"
user_input = input("Enter text to write to the file:")
with open(filename1,"w")as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt.")

append_input = input("Enter additional text to append:")
with open(filename1,"a")as file:
    file.write(append_input + "\n")
    print("Data successfully appended.")

print ("\nFinal content of output.txt:")
with open(filename1,"r") as file:
    content = file.read()
    print(content)