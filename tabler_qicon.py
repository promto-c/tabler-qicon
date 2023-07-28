# Standard library imports
# ------------------------
import logging
import os
import re
import sys
from typing import Dict, List, Optional
from xml.etree import ElementTree

# Related third party imports
# ---------------------------
# Declare the variables for the Qt libraries as None initially
QtCore = QtGui = QtWidgets = QtSvg = None

def use(lib_name: str = None):
    """Use the preferred Qt library specified by the user.
    
    This function tries to import QtCore, QtGui, QtWidgets and QtSvg from the specified library.

    Args:
        lib_name (str, optional): Preferred Qt library. Choices are ["PyQt6", "PySide6", "PyQt5", "PySide2"].
            If not provided, the function will try to load the libraries in the above order.
    """
    global QtCore, QtGui, QtWidgets, QtSvg

    # Try to import the modules from the specified Qt library
    QtCore = __import__(f'{lib_name}.QtCore', fromlist=[''])
    QtGui = __import__(f'{lib_name}.QtGui', fromlist=[''])
    QtWidgets = __import__(f'{lib_name}.QtWidgets', fromlist=[''])
    
    # Some libraries may not support QtSvg, handle it separately
    try:
        QtSvg = __import__(f'{lib_name}.QtSvg', fromlist=[''])
    except ModuleNotFoundError:
        # If QtSvg is not available, log a warning and set QtSvg as None
        QtSvg = None
        logging.warning(f"The QtSvg module could not be imported from {lib_name}. SVG icon functionality may not be available.")

# Loop through the list of Qt libraries in order of preference
for lib_name in ['PyQt6', 'PySide6', 'PyQt5', 'PySide2']:
    try:
        # Attempt to use the current library
        use(lib_name)
    except ModuleNotFoundError:
        # If the current library is not found, continue to the next one
        continue
    else:
        # If the current library is imported successfully, log this information and break the loop
        logging.info(f'Successfully imported {lib_name}')
        break
else:
    # If none of the libraries could be imported, raise an ImportError
    raise ImportError('No Qt libraries could be imported. Please ensure that at least one of PyQt6, PyQt5, PySide6, or PySide2 is installed.')

# Constants Definition
# --------------------
TABLER_ICONS_SVG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'icons')

# Classes Definition
# ------------------
class TablerQIcon:
    """A class that loads icons from the tabler-icons directory and makes them available as attributes.

    Attributes:
        _icon_name_to_path_dict (dict): A dictionary containing the icon name as key and the icon path as value.
        _color (QtGui.QColor): The color of the icon.
        _size (int): The size of the icon.
        _view_box_size (int): The size of the icon's view box.
        _stroke_width (int): The width of the icon's stroke.
        _opacity (float): The opacity of the icon.
    """
    # Class Variables
    # ---------------
    # Create an instance of QPalette
    _palette = QtGui.QPalette()
    # Get the default color (text color) of the palette and store it in the _default_color attribute
    _default_color = _palette.color(QtGui.QPalette.ColorRole.Text)

    # Initialization and Setup
    # ------------------------
    def __init__(self, color: QtGui.QColor=_default_color, size: int=24, view_box_size: int=24, stroke_width: int=2, opacity: float=1.0):
        """Initialize the widget and load the icons from the tabler-icons directory.

        Args:
            color (QtGui.QColor): color of the icon
            size (int): size of the icon 
            view_box_size (int): size of the view box of the icon
            stroke_width (int): width of the stroke of the icon
            opacity (float): opacity of the icon
        """
        # Save the properties
        self._color = color
        self._size = size
        self._view_box_size = view_box_size
        self._stroke_width = stroke_width
        self._opacity = opacity

        # Get the icon name to path dictionary  and store it in the _icon_name_to_path_dict attribute
        self._icon_name_to_path_dict = self.get_icon_name_to_path_dict()

    # Special Methods
    # ---------------
    def __call__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons using function call style.
        
        Args:
            name (str): The name of the icon to retrieve.
        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        return self.get_qicon(name)

    def __getattr__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons as attributes by returning a QIcon object for a given icon name.

        Args:
            name (str): The name of the icon to retrieve.
        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        return self.get_qicon(name)

    def __getitem__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons as index.
        
        Args:
            name (str): The name of the icon to retrieve.
        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        return self.get_qicon(name)

    # Extended Methods
    # ----------------
    def get_qicon(self, name: str) -> QtGui.QIcon:
        """Get the icon as a QIcon object using a method.

        Args:
            name (str): The name of the icon to retrieve.
        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        # Get the path of the icon from the dictionary using the name as the key
        svg_icon_path = self._icon_name_to_path_dict.get(name)

        # Return empty qicon if the icon doesn't exist in the dictionary
        if not svg_icon_path:
            # Print a message indicating that the icon is not available
            print(f'WARNING: Icon "{name}" is not available.')
            # Return an empty QIcon object
            return QtGui.QIcon()

        if QtSvg:
            # Load the original SVG file
            with open(svg_icon_path, 'r') as svg_file:
                svg_str = svg_file.read()

            # Parse the SVG file as XML
            svg = ElementTree.fromstring(svg_str)
            # Set the stroke width of the icon
            svg.set('stroke-width', str(self._stroke_width))
            svg_bytes = ElementTree.tostring(svg)

            # Create a renderer object to render the SVG file
            renderer = QtSvg.QSvgRenderer(svg_bytes)
            # Set the view box size
            renderer.setViewBox(QtCore.QRectF(0, 0, self._view_box_size, self._view_box_size))

            # Create a QPixmap object to hold the rendered image
            pixmap = QtGui.QPixmap(self._size, self._size)

            # Fill the pixmap with transparent color
            pixmap.fill(QtCore.Qt.GlobalColor.transparent)
            
            # Create a QPainter object to draw on the QPixmap
            painter = QtGui.QPainter(pixmap)

            # Render the SVG file to the pixmap
            renderer.render(painter)

        else:
            # Load the SVG file as a QPixmap
            pixmap = QtGui.QPixmap(svg_icon_path)

            # Set the size of the pixmap
            pixmap = pixmap.scaled(self._size, self._size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)

            # Create a QPainter object to draw on the QPixmap
            painter = QtGui.QPainter(pixmap)
        
        # Set the opacity of the icon
        painter.setOpacity(self._opacity)
        # Set the composition mode to "SourceIn" to composite the color on the icon
        painter.setCompositionMode(QtGui.QPainter.CompositionMode.CompositionMode_SourceIn)
        
        # Fill the pixmap with the specified color
        painter.fillRect(pixmap.rect(), self._color)
        
        # End the painter
        painter.end()

        # Create a QIcon object using the rendered image       
        icon = QtGui.QIcon(pixmap)

        # Return the icon
        return icon
    
    @staticmethod
    def get_icon_name_to_path_dict() -> Dict[str, str]:
        """Scans the predefined icon directory and constructs a dictionary mapping sanitized SVG file names to their respective file paths.
        
        Returns:
            Dict[str, str]: containing the icon name as key and the icon path as value

        Raises:
            FileNotFoundError: If the predefined directory does not exist.
        """
        # Ensure the specified directory exists before proceeding
        if not os.path.isdir(TABLER_ICONS_SVG_DIRECTORY):
            # If the directory does not exist, raise a FileNotFoundError with a descriptive message
            raise FileNotFoundError(f"Directory {TABLER_ICONS_SVG_DIRECTORY} does not exist")
        
        # Create an empty dictionary to store the icon name and path
        icon_name_to_path_dict = dict()

        # Get a list of all SVG files in the TABLER_ICONS_SVG_DIRECTORY
        svg_files = [ file for file in os.listdir(TABLER_ICONS_SVG_DIRECTORY) if file.endswith('.svg') ]

        # Compile the regex pattern once to avoid recompilation in each loop iteration
        pattern = re.compile(r'[^a-zA-Z0-9_]')
        
        for svg_file in svg_files:
            # Use regex to replace invalid characters with an underscore
            icon_name = pattern.sub('_', svg_file.split('.')[0])
            # Prepend an underscore to the icon name if it starts with a number
            if icon_name[0].isdigit():
                icon_name = "_" + icon_name
                
            # Add the icon name and path to the icon_name_to_path_dict
            icon_name_to_path_dict[icon_name] = os.path.join(TABLER_ICONS_SVG_DIRECTORY, svg_file)

        # return the dictionary containing the icon name and path
        return icon_name_to_path_dict
    
    @classmethod
    def get_icon_names(cls) -> List[str]:
        """Provides a list of all available icon names.
        
        Returns:
            List[str]: A list containing all the available icon names.
        """
        # Retrieve the dictionary mapping from icon names to their paths
        icon_name_to_path_dict = cls.get_icon_name_to_path_dict()

        # Return the list of icon names
        return list(icon_name_to_path_dict.keys())

    @classmethod
    def get_icon_path(cls, name: str = None) -> Optional[str]:
        """Provides the path of a specific icon or the icons directory.

        Args:
            name (str, optional): The name of the icon. If not provided, the method will return the icons directory.

        Returns:
            Optional[str]: Path of the icon if the name is provided and exists in the dictionary, else the icons directory.
                If the name is provided but doesn't match any in the dictionary, returns None.
        """
        # If no icon name is provided, return the directory of all icons
        if not name:
            return TABLER_ICONS_SVG_DIRECTORY

        # Retrieve the dictionary mapping from icon names to their paths
        icon_name_to_path_dict = cls.get_icon_name_to_path_dict()

        # Return the path corresponding to the provided icon name
        return icon_name_to_path_dict.get(name)

# Main Execution
# --------------
if __name__ == '__main__':
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create instance
    tabler_qicon = TablerQIcon()

    # Check attribute
    icon_users = tabler_qicon.users # output <PyQt5.QtGui.QIcon object at 0x...>
