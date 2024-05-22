subjects = []
notes = []
reprobed = []

while True:
    subject = input("Type subject: ")
    if subject == "":
        break
    else:
        subjects.append(subject)

i = 0
while i < len(subjects):
    nota = input(f"What was your note in {subjects[i]}: ")
    i += 1
    notes.append(nota)

for i in range(len(subjects)):
    
        if int(notes[i]) < 3:
            reprobed.append(subjects[i])
            print(f"{subjects[i]}: {notes[i]} reprueba")
        else:
            print(f"{subjects[i]}: {notes[i]} aprueba")
            
subjects.clear()
subjects.append(reprobed)

print("Reprobed:")
for subject in range(len(subjects)):
    print(f"{subjects[subject]} toca repetirla")