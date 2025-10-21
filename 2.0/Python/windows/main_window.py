from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QCheckBox
from PySide6.QtCore import Qt
from cores.Blattes_core import initialize_beads, draw_beads, remove_used, sort_beads, choose_bead, show_beads

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blattes 2.0")
        self.resize(750, 450)

        # Layout principal
        self.central = QWidget()
        self.layout = QVBoxLayout()
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)

        # Ajoute les widgets
        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(30)
        self.slider.setToolTip("Nombre de billes à tirer")
        self.slider.valueChanged.connect(self.update_button)

        # neg_box
        self.neg_box = QCheckBox("Tirer le pire résultat (après tirage, le programme donnera comme résultat la pire bille tirée)")

        # Label
        self.label = QLabel("Le résultat du tirage s'affichera ici.")
        self.neg_box.stateChanged.connect(self.update_button)

        #draw_btn
        self.draw_btn = QPushButton("Tirer 1 bille et garder la meilleure")
        self.draw_btn.clicked.connect(self.draw)

        # Ajouter les widgets au layout
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.neg_box)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.draw_btn)

        # Easter eggs
        self.easter_eggs = {
            "tooltip": False,
            "konami": False
        }
        self.total_easter_eggs = len(self.easter_eggs)
        self.easter_eggs_found = 0
        #self.setToolTip(f"Easter egg trouvé ! (trouvés : {self.easter_eggs_found}, total : {self.total_easter_eggs})")
        self.sequence = []
    
    def update_button(self):
        val = self.slider.value()
        self.draw_btn.setText(f"Tirer {val} bille{'s' if val > 1 else ''} et garder la {'pire' if self.neg_box.isChecked() else 'meilleure'}")
    
    def draw(self):
        n = self.slider.value()
        if self.neg_box.isChecked():
            n = -n

        beads = initialize_beads()
        used = draw_beads(n, beads)
        remove_used(used, beads)
        sort_beads(used)
        msg = choose_bead(used, n)
        used_msg = show_beads(used)

        self.label.setText(f"{msg}\n{used_msg}")

    def keyPressEvent(self, event):
        key = event.key()
        self.sequence.append(key)

        if len(self.sequence) > 10:
            self.sequence.pop(0)

        konami = [
            Qt.Key_Up, Qt.Key_Up,
            Qt.Key_Down, Qt.Key_Down,
            Qt.Key_Left, Qt.Key_Right,
            Qt.Key_Left, Qt.Key_Right,
            Qt.Key_B, Qt.Key_A
        ]

        if self.sequence == konami:
            if not self.easter_eggs["konami"]:
                self.easter_eggs_found += 1
                self.easter_eggs["konami"] = True
                message = "Easter egg trouvé !"
                self.setToolTip(f"Easter egg trouvé ! (trouvés : {self.easter_eggs_found}, total : {self.total_easter_eggs})")
            else:
                message = "Easter egg déjà trouvé"
            
            print(f"{message} (trouvés : {self.easter_eggs_found}, total : {self.total_easter_eggs})")
