# components.py
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
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