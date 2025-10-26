"""Modul yang menyediakan kelas dan fungsi GUI PySide6"""

from PySide6 import QtCore, QtWidgets

# fix docstring class GUI


class GuiApp:
    """Kelas GUI"""

    def __init__(self, riwayat, kategoriPendapatan, kategoriPengeluaran):
        self.riwayat = riwayat
        self.kategoriPendapatan = kategoriPendapatan
        self.kategoriPengeluaran = kategoriPengeluaran

    class Window(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()

            self.text = QtWidgets.QLabel("hello world", alignment=QtCore.Qt.AlignCenter)
            self.resize(300, 200)

            layout = QtWidgets.QVBoxLayout()

            layout.addWidget(self.text)
            self.setLayout(layout)

    def run(self):
        app = QtWidgets.QApplication([])

        window = self.Window()
        window.show()

        app.exec()
