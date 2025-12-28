
# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import config
import os

# --- GÜNCEL SEKMELERİN IMPORTLARI ---
from tabs.fin_tab import FinTab
from tabs.temp_tab import TempTab
from tabs.absorptivity_tab import AbsorptivityTab 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MEOS Engineering Toolbox-1")
        self.setGeometry(100, 100, 1200, 800)

        # İkon Ayarı (Varsa yükler)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "app_icon.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.setStyleSheet(f"""
            QMainWindow {{ background-color: #f5f6fa; }}
            QTabWidget::pane {{ border: 1px solid #dcdde1; background: white; border-radius: 8px; top: -1px; }}
            QTabBar::tab {{
                background: #e1e1e1; padding: 10px 25px; margin-right: 2px;
                border-top-left-radius: 6px; border-top-right-radius: 6px;
                font-family: '{config.FONT_FAMILY}'; font-size: 13px;
                min-width: 140px; /* Sekme genişliğini sabitledik, titremeyi önler */
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

        # --- SEKMELERİ OLUŞTUR ---
        self.tab_fin = FinTab()
        self.tab_temp = TempTab()
        self.tab_absorp = AbsorptivityTab()
        
        # --- SEKMELERİ EKLE VE BAŞLIKLARI DÜZENLE ---
        self.tabs.addTab(self.tab_fin, "Optimum Fin Boşluk")
        self.tabs.addTab(self.tab_temp, "Çıkış Sıcaklık")
        self.tabs.addTab(self.tab_absorp, "Absorptivity")
        
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