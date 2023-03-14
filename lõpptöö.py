from tkinter import *
from tkinter import simpledialog
import random

# Loeme failist küsimused ja vastused sõnastikku
kus_vas = {}
with open('kusimused_vastused.txt') as file:
    for line in file:
        question, answer = line.strip().split(':')
        kus_vas[question] = answer

# Vormistame vastuvõetud ja tagasilükatud taotlejate tühjad nimekirjad
vastuvoetud = []
eisoobi = []

def küsimused_vastused():
    """
    Määrame küsimuste esitamise ja vastuste kontrollimise funktsioon
    """
    name = name_entry.get()
    if not name:
        print('Hoiatus', 'Palun sisestage oma nimi.')
        return

    num_correct = 0
    for question in random.sample(list(kus_vas.keys()), 5):
        answer = kus_vas[question]
        response = simpledialog.askstring(question, f'{question}\n\nAnswer:')
        if response.lower() == answer.lower():
            num_correct += 1

    if num_correct >= 3:
        vastuvoetud.append((name, num_correct))
        print('Palju õnne', f'Palju õnne, {name}! Läbisite testi {num_correct}/5 õigete vastustega.')
    else:
        eisoobi.append(name)
        print('Vabandust', f'Vabandust, {name}. Sa ei läbinud testi, ainult {num_correct}/5 õigete vastustega.')

    name_entry.delete(0, END)

def salvesta_tulemused_ja_kuva_loendid():
    """
    Määratleme funktsioon tulemuste salvestamiseks faili ja kuvamisloenditesse
    """
    vastuvoetud.sort(key=lambda x: x[1], reverse=True)
    with open('vastuvoetud.txt', 'w') as file:
        for name, num_correct in vastuvoetud:
            file.write(f'{name}: {num_correct}/5\n')

    eisoobi.sort()
    with open('eisoobi.txt', 'w') as file:
        for name in eisoobi:
            file.write(f'{name}\n')

    print('Vastu võetud taotlejad:')
    for name, num_correct in vastuvoetud:
        print(f'{name}: {num_correct}/5')
    print('Tagasilükatud taotlejad:')
    for name in eisoobi:
        print(name)

root = Tk()
root.geometry("600x200")
root.title('Tarkvaraarendaja töötaotlus')

name_label = Label(root, text='Nimi:')
name_entry = Entry(root, width=30)
question_button = Button(root, text='Esita küsimusi', command=küsimused_vastused)
save_button = Button(root, text='Salvestage tulemused ja kuvage loendid', command=salvesta_tulemused_ja_kuva_loendid)

name_label.pack(side=LEFT, padx=5, pady=5)
name_entry.pack(side=LEFT, padx=5, pady=5)
question_button.pack(side=LEFT, padx=5, pady=5)
save_button.pack(side=LEFT, padx=5, pady=5)

root.mainloop()
