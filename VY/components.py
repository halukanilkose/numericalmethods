# components.py
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QComboBox, QDoubleSpinBox, QPushButton, QGraphicsDropShadowEffect, QTableWidget, QApplication
from PyQt5.QtGui import QColor, QKeySequence
from config import CARD, BORDER, FG, ENTRY_BG, ACCENT, ACCENT2

class RoundedCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("RoundedCard")
        self.setStyleSheet(f"""
        QFrame#RoundedCard {{
            background: {CARD};
            border-radius: 16px;
            border: 1px solid {BORDER};
        }}
        QLabel {{ color: {FG}; font: 10pt 'Calibri'; }}
        QLineEdit, QComboBox, QDoubleSpinBox {{
            background: {ENTRY_BG}; color: {FG}; border: 1px solid {BORDER};
            border-radius: 10px; padding: 8px 10px; selection-background-color: {ACCENT};
            font: 10pt 'Calibri';
        }}
        QPushButton {{
            background: {ACCENT}; color: white; border: none; border-radius: 12px;
            padding: 10px 16px; font: 10pt 'Calibri'; font-weight: 600;
        }}
        QPushButton#Success {{ background: {ACCENT2}; color: #0b1220; }}
        QPushButton:hover {{ background: #1d4ed8; }}
        QPushButton#Success:hover {{ background: #16a34a; }}
        """)
        shadow = QGraphicsDropShadowEffect(self, blurRadius=24, xOffset=0, yOffset=8)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)

class CopyableTableWidget(QTableWidget):
    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Copy):
            self.copy_selection()
        else:
            super().keyPressEvent(event)

    def copy_selection(self):
        selection = self.selectedIndexes()
        if not selection: return
        rows = sorted(index.row() for index in selection)
        columns = sorted(index.column() for index in selection)
        if not rows or not columns: return
        rowcount = rows[-1] - rows[0] + 1
        colcount = columns[-1] - columns[0] + 1
        table = [[''] * colcount for _ in range(rowcount)]
        for index in selection:
            table[index.row() - rows[0]][index.column() - columns[0]] = str(index.data())
        stream = "\n".join(["\t".join(row) for row in table])
        QApplication.clipboard().setText(stream)