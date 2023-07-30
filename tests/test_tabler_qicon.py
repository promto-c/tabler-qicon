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
tabler_qicon.set_backend('PyQt5')
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

    def test_icon_retrieval_instance(self):
        """Test the icon retrieval from an instance of TablerQIcon.
        """
        # Use the name of an icon from your directory here.
        icon = self.tabler_qicon.users
        # Check if the returned object is QIcon.
        self.assertTrue(isinstance(icon, QtGui.QIcon))

    def test_icon_retrieval_class(self):
        """Test the icon retrieval from the TablerQIcon class itself.
        """
        # Use the name of an icon from your directory here.
        icon = TablerQIcon.users
        # Check if the returned object is QIcon.
        self.assertTrue(isinstance(icon, QtGui.QIcon))

    def test_icon_name_read_only_instance(self):
        """Test if icon names are read-only on an instance of TablerQIcon.
        """
        with self.assertRaises(AttributeError):
            self.tabler_qicon.users = QtGui.QIcon()

    def test_icon_name_read_only_class(self):
        """Test if icon names are read-only on the TablerQIcon class itself.
        """
        with self.assertRaises(AttributeError):
            TablerQIcon.users = QtGui.QIcon()

# Main Execution
# --------------
if __name__ == '__main__':
    # Run unit tests if script is executed directly.
    unittest.main()
