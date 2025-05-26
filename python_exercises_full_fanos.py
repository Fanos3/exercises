
# Άσκηση 1 - Υπολογιστής Βαθμολογίας
print("\nΆσκηση 1")
grades = []
for i in range(5):
    grade = int(input(f"Εισάγε τον {i+1}o βαθμό (0-100): "))
    grades.append(grade)

print(f"\nΜέσος Όρος: {sum(grades)/len(grades):.2f}")
print(f"Μεγιστός Βαθμός: {max(grades)}")
print(f"Ελάχιστος Βαθμός: {min(grades)}")

# Άσκηση 2 - Τυχαίος Κωδικός
import random
import string

print("\nΆσκηση 2")
length = int(input("Εισάγε το μήκος του κωδικού: "))
specials = input("Να περιέχει ειδικούς χαρακτήρες; (Ναι/Όχι): ").lower() == 'ναι'
characters = string.ascii_letters + string.digits + (string.punctuation if specials else '')
password = ''.join(random.choice(characters) for _ in range(length))
print("Τυχαίος κωδικός:", password)

# Άσκηση 3 - Task List App
print("\nΆσκηση 3")
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()
while True:
    print("\n1. Προσθήκη")
    print("2. Διαγραφή")
    print("3. Εμφάνιση")
    print("4. Έξοδος")
    choice = input("-> ")
    if choice == '1':
        task = input("Task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == '2':
        task = input("Task to delete: ")
        if task in tasks:
            tasks.remove(task)
            save_tasks(tasks)
    elif choice == '3':
        print("\nTasks:")
        for t in tasks:
            print("-", t)
    elif choice == '4':
        break

# Άσκηση 4 - Ανάλυση Excel με Pandas
import pandas as pd

print("\nΆσκηση 4")
df = pd.read_excel("users.xlsx")
filtered = df[(df['Ηλικία'] > 30) & (df['Ενεργός'] == 'Ναι')]
print(filtered)
print("\nΜέσος Όρος Ηλικίας:", df['Ηλικία'].mean())
print("Μέσος Μισθός Ενεργών:", df[df['Ενεργός'] == 'Ναι']['Μισθός (€)'].mean())
filtered.to_excel("active_users_over30.xlsx", index=False)

# Άσκηση 5 - Έλεγχος Email
print("\nΆσκηση 5")
emails = [input(f"Email {i+1}: ") for i in range(5)]
valid_emails = []
for email in emails:
    if "@" in email and email.endswith(('.com', '.cy', '.gr')):
        valid_emails.append(email)
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")

with open("valid_emails.txt", "w") as file:
    for email in valid_emails:
        file.write(email + "\n")
