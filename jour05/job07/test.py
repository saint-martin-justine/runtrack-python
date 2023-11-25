def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40 or note % 5 < 3:
            notes_arrondies.append(note)
        else:
            notes_arrondies.append((note // 5 + 1) * 5)

    return notes_arrondies

liste_notes = [37, 82, 69, 95, 60]
notes_arrondies = arrondir_notes(liste_notes)

print("Notes originales :", liste_notes)
print("Notes arrondies  :", notes_arrondies)