studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):

    i = 0
    antw = []
    for student in studentencijfers:
        som = sum(studentencijfers[i])
        length = len(studentencijfers[i])
        average = int(som) / int(length)
        list.append(antw, int(average))
        i += 1

    return antw


def gemiddelde_van_alle_studenten(studentencijfers):

    gemiddelde = gemiddelde_per_student(studentencijfers)

    for cijfer in gemiddelde:
        som = sum(gemiddelde)
        length = len(gemiddelde)
        antw = int(som) / int(length)

    return int(antw)


print(gemiddelde_per_student([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]))
print(gemiddelde_van_alle_studenten([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]))
