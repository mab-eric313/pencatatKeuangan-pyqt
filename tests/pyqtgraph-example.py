import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPalette, QColor
import pyqtgraph as pg
import numpy as np


class BalanceGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Balance Graph - PyQtGraph Demo")
        self.resize(600, 400)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Widget grafik
        self.plot_widget = pg.PlotWidget(title="Pendapatan vs Pengeluaran")
        layout.addWidget(self.plot_widget)

        # Data contoh
        bulan = np.arange(1, 13)
        pendapatan = np.array([4.2, 4.8, 5.0, 4.6, 5.4, 5.8, 6.2, 6.5, 6.0, 6.8, 7.0, 7.5])
        pengeluaran = np.array([3.5, 3.8, 4.0, 4.2, 4.5, 4.7, 5.0, 5.3, 5.2, 5.5, 5.6, 6.0])
        balance = pendapatan - pengeluaran

        # Plot pendapatan dan pengeluaran
        self.plot_widget.plot(bulan, pendapatan, pen=pg.mkPen(color='g', width=2), name="Pendapatan")
        self.plot_widget.plot(bulan, pengeluaran, pen=pg.mkPen(color='r', width=2), name="Pengeluaran")

        # Plot balance sebagai bar chart
        bg = pg.BarGraphItem(x=bulan, height=balance, width=0.3, brush='b')
        self.plot_widget.addItem(bg)

        # Label sumbu
        self.plot_widget.setLabel('left', 'Jumlah (juta)')
        self.plot_widget.setLabel('bottom', 'Bulan')
        self.plot_widget.showGrid(x=True, y=True)


if __name__ == "__main__":

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(35, 35, 35))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))

    app = QApplication(sys.argv)
    window = BalanceGraph()
    window.show()

    app.setPalette(palette)
    sys.exit(app.exec())

