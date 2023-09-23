# Standard Library Imports
# ------------------------
import os
from pathlib import Path

# Related Third Party Imports
# ---------------------------
import pytest
from PyQt5 import QtGui, QtWidgets

# Local Imports
# -------------
os.environ['QT_API'] = 'PyQt5'
from tablerqicon import TablerQIcon


# Fixture Definition
# ------------------
@pytest.fixture(scope="class")
def qt_application():
    app = QtWidgets.QApplication([])
    yield app
    app.quit()


@pytest.fixture
def tabler_qicon_instance():
    return TablerQIcon()


# Test Cases
# ----------
class TestTablerQIcon(object):
    """Test case for the TablerQIcon class.
    """

    def test_icon_names(self, tabler_qicon_instance):
        """Test the get_icon_names method.
        """
        icon_names = tabler_qicon_instance.get_icon_names()
        assert isinstance(icon_names, list)
        assert len(icon_names) > 0

    def test_icon_path(self, tabler_qicon_instance):
        """Test the get_icon_path method.
        """
        # Put the name of one icon from your directory here.
        icon_path = tabler_qicon_instance.get_icon_path('users')
        assert isinstance(icon_path, Path)
        assert os.path.exists(icon_path)

    def test_icon_retrieval_instance(self, qt_application, tabler_qicon_instance):
        """Test the icon retrieval from an instance of TablerQIcon.
        """
        # Use the name of an icon from your directory here.
        icon = tabler_qicon_instance.users
        assert isinstance(icon, QtGui.QIcon)

    def test_icon_retrieval_class(self, qt_application):
        """Test the icon retrieval from the TablerQIcon class itself.
        """
        # Use the name of an icon from your directory here.
        icon = TablerQIcon.users
        assert isinstance(icon, QtGui.QIcon)

    def test_icon_name_read_only_instance(self, tabler_qicon_instance):
        """Test if icon names are read-only on an instance of TablerQIcon.
        """
        with pytest.raises(AttributeError):
            tabler_qicon_instance.users = QtGui.QIcon()

    def test_icon_name_read_only_class(self):
        """Test if icon names are read-only on the TablerQIcon class itself.
        """
        with pytest.raises(AttributeError):
            TablerQIcon.users = QtGui.QIcon()

    def test_flip_flop_transformations(self, qt_application, tabler_qicon_instance):
        """Test the flip and flop transformations on an icon.
        """
        # Test flip transformation.
        icon_flipped1 = tabler_qicon_instance.flip.users
        assert isinstance(icon_flipped1, QtGui.QIcon)
        
        # Test caching for flip transformation.
        icon_flipped2 = tabler_qicon_instance.flip.users
        assert icon_flipped1 is icon_flipped2

        # Test flop transformation.
        icon_flopped1 = tabler_qicon_instance.flop.users
        assert isinstance(icon_flopped1, QtGui.QIcon)

        # Test caching for flop transformation.
        icon_flopped2 = tabler_qicon_instance.flop.users
        assert icon_flopped1 is icon_flopped2

        # Test both flip and flop transformations.
        icon_flip_flop1 = tabler_qicon_instance.flip.flop.users
        assert isinstance(icon_flip_flop1, QtGui.QIcon)

        # Test caching for both flip and flop transformations.
        icon_flip_flop2 = tabler_qicon_instance.flip.flop.users
        assert icon_flip_flop1 is icon_flip_flop2

        # Test if transformations are reset after retrieving the icon.
        icon_reset = tabler_qicon_instance.users
        assert isinstance(icon_reset, QtGui.QIcon)

        # Ensure that the icon without transformations is not cached with transformations.
        assert icon_reset is not icon_flip_flop1
        assert icon_reset is not icon_flopped1
        assert icon_reset is not icon_flipped1
