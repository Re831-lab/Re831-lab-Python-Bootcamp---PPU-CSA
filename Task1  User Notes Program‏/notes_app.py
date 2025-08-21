
name = input("Enter your name: ")

notes = input("Write your notes: ")

filename = "user_notes.txt"
with open(filename, "a", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Notes: {notes}\n")
    file.write("-" * 30 + "\n")  

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("\n--- All Saved Notes ---")
print(content)
