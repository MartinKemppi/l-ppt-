from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random

# Loeme failist küsimused ja vastused sõnastikku
kus_vas = {}
with open('kusimused_vastused.txt',encoding="utf-8-sig") as file:
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
        messagebox.showerror('NB!', 'Palun sisestage oma nimi.')
        return

    num_correct = 0
    for question in random.sample(list(kus_vas.keys()), 5):
        answer = kus_vas[question]
        response = simpledialog.askstring(question, f'\t{question}\t\n\nVastus:')
        if response.lower() == answer.lower():
            num_correct += 1

    if num_correct >= 3:
        vastuvoetud.append((name, num_correct))
        messagebox.showinfo('Palju õnne', f'Palju õnne, {name}! Läbisite testi {num_correct}/5 õigete vastustega.')       
    else:
        eisoobi.append(name)
        messagebox.showinfo('Vabandust', f'Vabandust, {name}. Sa ei läbinud testi, ainult {num_correct}/5 õigete vastustega.')

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

def dark():
    root.configure(bg='black')
    name_label.config(fg='white',bg='black')
    name_entry.config(fg='white',bg='black')
    question_button.config(fg='white',bg='black')
    save_button.config(fg='white',bg='black')
    Tulemused.config(fg='white',bg='black')
    eesti_keeles.config(fg='white',bg='black')
    vene_keeles.config(fg='white',bg='black')
    Hele_foon.config(fg='white',bg='black')
    Tume_foon.config(fg='white',bg='black')

def light():
    root.configure(bg='white')
    name_label.config(bg='white',fg='black')
    name_entry.config(bg='white',fg='black')
    question_button.config(bg='white',fg='black')
    save_button.config(bg='white',fg='black')
    Tulemused.config(bg='white',fg='black')
    eesti_keeles.config(bg='white',fg='black')
    vene_keeles.config(bg='white',fg='black')
    Hele_foon.config(bg='white',fg='black')
    Tume_foon.config(bg='white',fg='black')  

def set_language_estonian():
    name_label.config(text='Nimi ja perekonnanimi')
    question_button.config(text='Esita küsimusi')
    save_button.config(text='Salvesta tulemused')
    Tulemused.config(text="Tulemused")
    eesti_keeles.config(text="Eesti keeles")
    vene_keeles.config(text="Vene keeles")
    Hele_foon.config(text="Hele foon")
    Tume_foon.config(text="Tume foon") 

def set_language_russian():
    name_label.config(text="Имя и фамилия")
    question_button.config(text="Задай вопросы")
    save_button.config(text="Сохрани результаты")
    Tulemused.config(text="Результаты")
    eesti_keeles.config(text="На эстонском языке")
    vene_keeles.config(text="На русском языке")
    Hele_foon.config(text="Светлый фон")
    Tume_foon.config(text="Тёмный фон") 

def kuva_tulemused():
    """
    Määratleme funktsioon tulemuste kuvamiseks uuel aknal
    """
    tulemuste_window = Toplevel(root)
    tulemuste_window.title('Tulemused')
    tulemuste_window.iconbitmap("note_icon.ico")
    
    vastuvoetud_label = Label(tulemuste_window, text='Läbinud taotlejad:', font='bold')
    vastuvoetud_label.pack(pady=10)
    vastuvoetud_text = Text(tulemuste_window, width=40, height=10)
    vastuvoetud_text.pack()
    
    eisoobi_label = Label(tulemuste_window, text='Tagasilükatud taotlejad:', font='bold')
    eisoobi_label.pack(pady=10)
    eisoobi_text = Text(tulemuste_window, width=40, height=10)
    eisoobi_text.pack()
    
    for name, num_correct in vastuvoetud:
        vastuvoetud_text.insert(END, f'{name}: {num_correct}/5\n')
    for name in eisoobi:
        eisoobi_text.insert(END, f'{name}\n')

    img_lbl2 = Label(tulemuste_window, image = img2)
    img_lbl3 = Label(tulemuste_window, image = img3)

    img_lbl2.place(x=25,y=0)
    img_lbl3.place(x=25,y=208)

root = Tk()
root.geometry("700x200")
root.title('Tarkvaraarendaja töötaotlus')
root.iconbitmap("note_icon.ico")

img=PhotoImage(file="tietoevry.png")
img2=PhotoImage(file="accept.png").subsample(13)
img3=PhotoImage(file="decline.png").subsample(13)

name_label = Label(root, text='Nimi ja perekonnanimi:')
img_lbl = Label(root, image = img)
name_entry = Entry(root, width=35)
question_button = Button(root, text='Esita küsimusi',width=20, command=küsimused_vastused)
save_button = Button(root, text='Salvesta tulemused',width=20, command=salvesta_tulemused_ja_kuva_loendid)
Tulemused=Button(root,text="Tulemused",width=20,command=kuva_tulemused)
eesti_keeles=Button(root,text="Eesti keeles",width=20,command=set_language_estonian)
vene_keeles=Button(root,text="Vene keeles",width=20,command=set_language_russian)
Hele_foon=Button(root,text="Hele foon",width=20,command=light)
Tume_foon=Button(root,text="Tume foon",width=20,command=dark)

name_label.place(x=8,y=85)
name_entry.place(x=145,y=85)
question_button.place(x=525,y=50)
save_button.place(x=525,y=80)
img_lbl.place(x=8,y=0)
Tulemused.place(x=525,y=110)
eesti_keeles.place(x=8,y=110)
vene_keeles.place(x=8,y=140)
Hele_foon.place(x=160,y=110)
Tume_foon.place(x=160,y=140)

root.mainloop()
