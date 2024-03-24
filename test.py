import unittest
from tkinter import Tk, Button

class TestCalculator(unittest.TestCase):

    def test_button_click(self):
        root = Tk()
        root.withdraw()  # Supprimer la fenêtre principale pour les tests

        button = Button(root, text="7")
        button.invoke()  # Simuler un clic sur le bouton
        self.assertEqual(button.cget("text"), "7")

        button = Button(root, text="C")
        button.invoke()
        self.assertEqual(button.cget("text"), "C")

        button = Button(root, text="=")
        button.invoke()
        self.assertEqual(button.cget("text"), "=")

        button = Button(root, text="*", padx=20, pady=10)
        button.invoke()
        self.assertEqual(button.cget("text"), "*")

if __name__ == '__main__':
    unittest.main()