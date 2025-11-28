import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QMenu, QMenuBar, QFileDialog, QSizePolicy
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GW NOTEPAD")
        self.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

        # 1. Create the central text editor widget
        self.text_editor = QTextEdit()
        self.setCentralWidget(self.text_editor)

        # 2. Create the Menu Bar
        self._create_menu_bar()

    def _create_menu_bar(self):
        # Initialize the Menu Bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # Create Menus
        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("&Edit")
        help_menu = menu_bar.addMenu("&Help")
        
        # --- File Menu Actions ---
        
        # New Action
        new_action = QAction("&New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.setStatusTip("Create a new document")
        # In a full app, you'd connect this to a 'clear_text' method
        file_menu.addAction(new_action) 

        # Open Action
        open_action = QAction("&Open...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open an existing document")
        open_action.triggered.connect(self.open_file) 
        file_menu.addAction(open_action)

        # Save Action
        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.setStatusTip("Save the current document")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Separator
        file_menu.addSeparator()

        # Exit Action
        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Close the application")
        exit_action.triggered.connect(self.close) # Built-in method to close QMainWindow
        file_menu.addAction(exit_action)
        
        # --- Edit Menu Actions (Basic placeholders) ---
        edit_menu.addAction(QAction("&Cut", self))
        edit_menu.addAction(QAction("C&opy", self))
        edit_menu.addAction(QAction("&Paste", self))


    def open_file(self):
        """Opens a file and loads its content into the QTextEdit widget."""
        # QFileDialog.getOpenFileName returns a tuple: (filename, filter)
        filename, _ = QFileDialog.getOpenFileName(self, 
            "Open File", 
            "", 
            "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)"
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                    self.text_editor.setText(content)
                self.setWindowTitle(f"GW NOTEPAD - {filename}")
            except Exception as e:
                # Basic error handling
                print(f"Could not open file: {e}")

    def save_file(self):
        """Saves the content of the QTextEdit widget to a file."""
        # QFileDialog.getSaveFileName returns a tuple: (filename, filter)
        filename, _ = QFileDialog.getSaveFileName(self, 
            "Save File", 
            "", 
            "Text Files (*.txt);;All Files (*.*)"
        )

        if filename:
            try:
                # Ensure the file has a .txt extension if not provided
                if not filename.endswith('.txt') and '.' not in filename:
                    filename += '.txt'
                    
                content = self.text_editor.toPlainText()
                with open(filename, 'w') as f:
                    f.write(content)
                self.setWindowTitle(f"GW NOTEPAD - {filename}")
            except Exception as e:
                # Basic error handling
                print(f"Could not save file: {e}")

# --- Main Execution Block ---
if __name__ == '__main__':
    # You must create a QApplication object
    app = QApplication(sys.argv)
    
    # Create the Notepad instance
    window = Notepad()
    window.show() # Display the window
    
    # Start the event loop
    sys.exit(app.exec())
