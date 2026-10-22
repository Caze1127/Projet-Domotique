from tkinter import *

fenetre = Tk()
fenetre.title("Application Domotique")
fenetre.state("zoomed")
fenetre.configure(bg="#f4f1f1")

etats = {
    "Cuisine": {"lumiere": "OFF", "temperature": 20},
    "Salon": {"lumiere": "OFF", "temperature": 20},
    "Chambre": {"lumiere": "OFF", "temperature": 20}
}

piece_selectionnee = StringVar()
piece_selectionnee.set("Cuisine")

etat_lumiere = StringVar()
temperature_affichee = StringVar()

def mettre_a_jour_affichage():
    piece = piece_selectionnee.get()
    etat_lumiere.set(etats[piece]["lumiere"])
    temperature_affichee.set(str(etats[piece]["temperature"]) + "°C")

def reset_boutons_pieces():
    for b in boutons_pieces:
        b.config(bg="black")

def choisir_piece(piece, bouton):
    piece_selectionnee.set(piece)
    reset_boutons_pieces()
    bouton.config(bg="gray")
    mettre_a_jour_affichage()

def allumer():
    piece = piece_selectionnee.get()
    etats[piece]["lumiere"] = "ON"
    bouton_allumer.config(bg="gray")
    bouton_eteindre.config(bg="black")
    mettre_a_jour_affichage()

def eteindre():
    piece = piece_selectionnee.get()
    etats[piece]["lumiere"] = "OFF"
    bouton_eteindre.config(bg="gray")
    bouton_allumer.config(bg="black")
    mettre_a_jour_affichage()

def augmenter_temperature():
    piece = piece_selectionnee.get()
    if etats[piece]["temperature"] < 30:
        etats[piece]["temperature"] += 1
    mettre_a_jour_affichage()

def diminuer_temperature():
    piece = piece_selectionnee.get()
    if etats[piece]["temperature"] > 16:
        etats[piece]["temperature"] -= 1
    mettre_a_jour_affichage()

cadre = Frame(fenetre, bg="#f4f1f1")
cadre.place(relx=0.5, rely=0.5, anchor="center")

Label(
    cadre,
    text="Choix de la pièce",
    font=("Arial", 28, "bold"),
    bg="#f4f1f1"
).grid(row=0, column=0, columnspan=3, pady=20)

boutons_pieces = []

def creer_bouton_piece(nom, col):
    b = Button(
        cadre,
        text=nom,
        bg="black",
        fg="white",
        font=("Arial", 14),
        width=10,
        command=lambda: choisir_piece(nom, b)
    )
    b.grid(row=1, column=col, padx=15, pady=10)
    boutons_pieces.append(b)
    return b

btn_cuisine = creer_bouton_piece("Cuisine", 0)
btn_salon = creer_bouton_piece("Salon", 1)
btn_chambre = creer_bouton_piece("Chambre", 2)
btn_cuisine.config(bg="gray")

Label(
    cadre,
    text="Eclairage",
    font=("Arial", 26, "bold"),
    bg="#f4f1f1"
).grid(row=2, column=0, columnspan=3, pady=40)

bouton_allumer = Button(
    cadre,
    text="Allumer",
    bg="black",
    fg="white",
    font=("Arial", 14),
    width=10,
    command=allumer
)
bouton_allumer.grid(row=3, column=0, padx=20)

bouton_eteindre = Button(
    cadre,
    text="Eteindre",
    bg="black",
    fg="white",
    font=("Arial", 14),
    width=10,
    command=eteindre
)
bouton_eteindre.grid(row=3, column=2, padx=20)

Label(
    cadre,
    textvariable=etat_lumiere,
    font=("Arial", 34),
    fg="blue",
    bg="#f4f1f1"
).grid(row=4, column=0, columnspan=3, pady=20)

Label(
    cadre,
    text="Température",
    font=("Arial", 26, "bold"),
    bg="#f4f1f1"
).grid(row=5, column=0, columnspan=3, pady=20)

Label(
    cadre,
    textvariable=temperature_affichee,
    font=("Arial", 30),
    fg="blue",
    bg="#f4f1f1"
).grid(row=6, column=0, columnspan=3, pady=10)

Button(
    cadre,
    text="+",
    bg="black",
    fg="white",
    font=("Arial", 18),
    width=5,
    command=augmenter_temperature
).grid(row=7, column=0, pady=10)

Button(
    cadre,
    text="-",
    bg="black",
    fg="white",
    font=("Arial", 18),
    width=5,
    command=diminuer_temperature
).grid(row=7, column=2, pady=10)

mettre_a_jour_affichage()

fenetre.mainloop()