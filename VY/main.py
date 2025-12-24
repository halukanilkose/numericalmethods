import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import config
from tabs.isa_tab import ISATab
from tabs.p2p_tab import PixelToPointTab
from tabs.pao_tab import PAOTab 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MEOS Engineering Toolbox-1")
        self.setGeometry(100, 100, 1200, 800)

        self.setStyleSheet(f"""
            QMainWindow {{ background-color: #f5f6fa; }}
            QTabWidget::pane {{ border: 1px solid #dcdde1; background: white; border-radius: 8px; top: -1px; }}
            QTabBar::tab {{
                background: #e1e1e1; padding: 10px 25px; margin-right: 2px;
                border-top-left-radius: 6px; border-top-right-radius: 6px;
                font-family: '{config.FONT_FAMILY}'; font-size: 13px;
            }}
            QTabBar::tab:selected {{ background: {config.ACCENT}; color: white; }}
        """)
        
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 10)

        self.tabs = QTabWidget()

        self.tab_isa = ISATab()
        self.tab_p2p = PixelToPointTab()
        self.tab_pao = PAOTab()
        
    
        self.tabs.addTab(self.tab_p2p, "Pixel to Point")
        self.tabs.addTab(self.tab_isa, "ISA Atmosfer")
        self.tabs.addTab(self.tab_pao, "PAO Özellikler")
        
        layout.addWidget(self.tabs)
       
        footer = QLabel("© 2025 MEOS - Isıl Tasarım Ekibi")
        footer.setStyleSheet(f"color: {config.MUTED}; font-size: 12px;")
        layout.addWidget(footer)

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    app.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
    
    window = MainApp()
    window.show()
    
    sys.exit(app.exec_())