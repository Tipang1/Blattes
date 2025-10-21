import random

def initialize_beads():
    beads = []

    # Types de billes et quantité
    bead_types = [
        {"color": "rouge", "success": "succès critique", "quantité": 3},
        {"color": "vert", "success": "succès amélioré", "quantité": 6},
        {"color": "bleu", "success": "succès", "quantité": 6},
        {"color": "blanc", "success": "échec", "quantité": 12},
        {"color": "noir", "success": "échec critique", "quantité": 3}
    ]

    # Génération de la liste
    for bead_type in bead_types:
        for _ in range(bead_type["quantité"]):
            beads.append({"color": bead_type["color"], "success": bead_type["success"]})

    return beads

def draw_beads(n, beads):
    used = random.sample(beads, abs(n))

    return used

def remove_used(used, beads):
    for bille in used:
        beads.remove(bille)

def sort_beads(used):
    success_order = {
        "échec critique": 0,
        "échec": 1,
        "succès": 2,
        "succès amélioré": 3,
        "succès critique": 4,
    }

    used.sort(key=lambda b: success_order[b["success"]])

def choose_bead(used, n):
    chosen = used[-1] if n > 0 else used[0]
    msg = f"Bille choisie : {chosen['color'].capitalize()}, {chosen['success']}"
    print(msg)

    return msg

def show_beads(used):
    print("Billes tirées :")
    msg = "Billes tirées :\n"
    for i, result in enumerate(used, start=1):
        b = f"{i}. {result['color'].capitalize()}, {result['success']}\n"
        msg += b
        print(b)
    
    return msg
