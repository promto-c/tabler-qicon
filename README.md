# Tabler QIcon

<!-- Badges -->
[![GitHub](https://img.shields.io/github/license/promto-c/tabler-qicon)](https://github.com/promto-c/tabler-qicon/blob/main/LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue.svg)](https://github.com/promto-c/tabler-qicon)
[![PyPI Version](https://img.shields.io/pypi/v/tabler-qicon)](https://pypi.org/project/tabler-qicon/)

`Tabler QIcon` is a Python package that provides easy access to [Tabler Icons](https://tabler-icons.io/) [[Preview]](https://tabler-icons.io/) [[GitHub]](https://github.com/tabler/tabler-icons) for PyQt and PySide applications. It uses SVGs from Tabler Icons and converts them into QIcon objects, which can be used in PyQt and PySide applications.

This package also supports icon customization such as changing color, size, view box size, stroke width, opacity, and applying transformations like flip and flop.

`Tabler QIcon v0.2.3` is currently synced with [tabler-icons](https://github.com/tabler/tabler-icons) version 2.44.0. Please refer to the [update.log](./tablerqicon/icons/update.log) file for more details on the last sync.
<details>
  <summary><b>Preview icons</b></summary>

  ![Tabler Icons](https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/icons.png)

</details>

## 🚀 Features

- **Customizable Icons**: Adjust color, size, view box size, stroke width, opacity, and apply transformations like flip and flop.
- **Developer-Friendly**: Python stubs enhance code autocompletion and type-checking in your IDE.
  Code Autocompletion
    ![Code Autocompletion](https://raw.githubusercontent.com/promto-c/tabler-qicon/main/screenshots/autocompletion_screenshot.png)
- **Broad Compatibility**: Supports PyQt5, PyQt6, PySide2, and PySide6.
- **Transformation Features**: Flip and flop transformations can be applied to icons easily. (introduced in v0.2.2)

## 📋 Prerequisites

- Python 3.7 or later
- One of the following: PyQt5, PyQt6, PySide2, or PySide6

## 💻 Installation

You can install `tabler-qicon` from PyPI using pip:

```bash
pip install tabler-qicon
```

Alternatively, you can install it directly from the GitHub repository:

```bash
pip install git+https://github.com/promto-c/tabler-qicon.git
```

Using PyQt5? Install it separately:

```bash
pip install PyQt5
```

## 🖌️ Usage

### Setting the Backend

#### Using Environment Variables (with `qtpy`)

If you're using `qtpy` to maintain compatibility across different PyQt/PySide backends, you'll need to specify the backend before importing other modules:

```python
import os
os.environ['QT_API'] = 'PyQt5'  # Change 'PyQt5' to your desired backend

from tablerqicon import TablerQIcon

# ... Additional code ...
```

#### Using the `use_backend` method

Alternatively, you can also set the backend directly using the `use_backend` method:

```python
import tablerqicon
tablerqicon.use_backend('PyQt5')

from tablerqicon import TablerQIcon

# ... Additional code ...
```

### Default Usage

Directly access icons with default properties:

```python
from PyQt5 import QtWidgets
from tablerqicon import TablerQIcon

# ... Additional code ...

refresh_button = QtWidgets.QPushButton("Refresh")

# Set the QIcon for the refresh_button using the 'refresh' icon name as an attribute
refresh_button.setIcon(TablerQIcon.refresh)
```

### Customized Icons

1. Instantiate `TablerQIcon` with your desired properties.
2. Access icons using icon names.
3. Utilize `flip` and `flop` transformations for versatile usage of icons.

```python
from PyQt5 import QtWidgets
from tablerqicon import TablerQIcon

# ... Additional code ...

# Example: Using a custom opacity
tabler_icon = TablerQIcon(opacity=0.6)

refresh_button = QtWidgets.QPushButton('Refresh')
word_wrap_button = QtWidgets.QPushButton('Word Wrap')
play_backward_button = QtWidgets.QPushButton('Play Backward')

# Set the QIcon for the refresh_button using the 'refresh' icon name as an attribute
refresh_button.setIcon(tabler_icon.refresh)
# Set the QIcon for the word_wrap_button using the 'text_wrap' icon name as an attribute
word_wrap_button.setIcon(tabler_icon.text_wrap)
# Applying flip and flop transformations before setting the icon
play_backward_button.setIcon(tabler_icon.flip.flop.player_play)
```

### Retrieve All Icon Names

```python
print(TablerQIcon.get_icon_names())
```

## 🛠️ Development

### Syncing Icons
To sync icons, we use a shell script that clones the icons from the `tabler-icons` repository and generates a `.pyi` file to facilitate type hints and autocompletion in IDEs.

If you are a contributor or a developer working on this project and need to sync icons, follow the steps below:

1. **Run the Sync Script:**
   ```bash
   ./sync_tabler_icons.sh
   ```
   This script will:
   - Clone the latest icons from the `tabler-icons` repository.
   - Copy the icons to the target directory.
   - Generate a `.pyi` file to facilitate type hints and autocompletion.

2. **Check the Update Log:**
   After running the script, check the `update.log` file in the `icons` directory to ensure that the sync was successful and to view details of the sync.

3. **Commit Changes:**
   After successfully syncing the icons and generating the `.pyi` file, commit these changes to the version control system.

### Note to Contributors
- Please do not edit the generated `.pyi` file directly. It is auto-generated by the sync script.
- Ensure that you have run the sync script and tested the changes locally before submitting a pull request.

### Running Tests
Run the tests to ensure that your changes do not break existing functionality.
```bash
pytest tests
```

## 🖋️ Coding Style

Adhering to PEP 8 with [flake8](https://flake8.pycqa.org/en/latest/) oversight. Auto-formatting via [yapf](https://github.com/google/yapf). Our docstrings embrace the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for clarity and consistency.

## 📜 License

`Tabler QIcon` is licensed under the [MIT License](LICENSE).

> **Note:** This `README.md` file was generated by ChatGPT.
