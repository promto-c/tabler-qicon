# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
-

## [0.2.3] - 2023-12-21
### Added
- Support for `QT_PREFERRED_BINDING` environment variable as an alternative to `QT_API`. The module now checks `QT_API` first and falls back to `QT_PREFERRED_BINDING` if `QT_API` is not set or is empty, enhancing flexibility in configuring the preferred Qt binding.

## [0.2.2] - 2023-09-24
### Added
- Flip and flop transformations can be applied to icons easily.

## [0.1.0] - 2023-09-11
### Added
- Adjust color, size, view box size, stroke width, and opacity.
- Python stubs enhance code autocompletion and type-checking in your IDE.
- Supports PyQt5, PyQt6, PySide2, and PySide6.
