import tkinter as tk
from tkinter import PhotoImage
import urllib.request
import base64

def ok():
    global password
    password = lol.get()
    rootl.destroy()
    launch_lock_screen()

def valider():
    entered_password = entry.get()

    if entered_password == password:
        root.destroy()
    else:
        label.config(text="Mot de passe incorrect")

def launch_lock_screen():
    global root, label, entry
    # Créer une fenêtre de verrouillage
    root = tk.Tk()
    root.title("Verrouillage d'écran")
    root.attributes("-fullscreen", True)

    # Télécharger et afficher l'image du cadenas depuis l'URL
    url = "https://cdn-icons-png.flaticon.com/512/456/456112.png"
    with urllib.request.urlopen(url) as u:
        data = u.read()
        image = tk.PhotoImage(data=base64.encodebytes(data).decode())
    image_label = tk.Label(root, image=image, bg="#333333")
    image_label.image = image
    image_label.pack()

    # Modifier la couleur du fond de la fenêtre et du texte
    root.configure(bg="#333333")
    label = tk.Label(root, text="Veuillez entrer le mot de passe :", bg="#333333", fg="white")
    label.pack()

    # Créer une zone de texte pour entrer le mot de passe
    entry = tk.Entry(root, show="*", bg="white")
    entry.pack()

    # Créer un bouton pour valider le mot de passe
    button = tk.Button(root, text="Valider", command=valider, bg="#666666", fg="white")
    button.pack()

    # Démarrer la boucle principale de l'interface utilisateur de verrouillage
    root.mainloop()

# Créer une fenêtre de saisie pour le mot de passe initial
rootl = tk.Tk()
rootl.title("Choisir")

lol = tk.Entry(rootl, show="*", bg="white")
lol.pack()

ok_button = tk.Button(rootl, text="Ok", command=ok, bg="#666666", fg="white")
ok_button.pack()

password = ""

# Démarrer la boucle principale de l'interface utilisateur de saisie
