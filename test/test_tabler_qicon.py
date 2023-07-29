# Standard library imports
# ------------------------
import os
import unittest

# Related third party imports
# ---------------------------
from PyQt5 import QtGui, QtWidgets

# Local imports
# -------------
import tabler_qicon
tabler_qicon.use('PyQt5')
from tabler_qicon import TablerQIcon

# Classes Definition
# ------------------
class TestTablerQIcon(unittest.TestCase):
    """Test case for the TablerQIcon class.
    """
    @classmethod
    def setUpClass(cls):
        """Set up method to be run once for the entire class.
        """
        cls.app = QtWidgets.QApplication([])

    def setUp(self):
        """Set up method to be run before each test.
        """
        self.tabler_qicon = TablerQIcon()

    def tearDown(self):
        """Teardown method to be run after each test.
        """
        self.tabler_qicon = None

    def test_icon_names(self):
        """Test the get_icon_names method.
        """
        icon_names = self.tabler_qicon.get_icon_names()
        # Check if the returned object is a list and if the list is not empty.
        self.assertTrue(isinstance(icon_names, list))
        self.assertTrue(len(icon_names) > 0)

    def test_icon_path(self):
        """Test the get_icon_path method.
        """
        # Put the name of one icon from your directory here.
        icon_path = self.tabler_qicon.get_icon_path('users')
        # Check if the returned object is a string and if the file actually exists.
        self.assertTrue(isinstance(icon_path, str))
        self.assertTrue(os.path.exists(icon_path))

    def test_icon_retrieval(self):
        """Test the icon retrieval from TablerQIcon.
        """
        # Put the name of one icon from your directory here.
        icon = self.tabler_qicon.users
        # Check if the returned object is QIcon.
        self.assertTrue(isinstance(icon, QtGui.QIcon))

# Main Execution
# --------------
if __name__ == '__main__':
    # Run unit tests if script is executed directly.
    unittest.main()
