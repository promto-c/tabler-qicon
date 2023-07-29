#!/bin/bash
set -e  # Exit the script if any command fails

# Define the URL of the repository to be cloned
REPO_URL="https://github.com/tabler/tabler-icons.git"

# Use the mktemp command to create a temporary directory
TEMP_DIR=$(mktemp -d -t tabler-icons-XXXXXXXXXX)

# Ensure that the temporary directory is removed when the script ends
trap "rm -rf $TEMP_DIR" EXIT

# Define the target directory where the icons should be stored
# This directory is relative to the location of this script
TARGET_DIR="$(dirname "${BASH_SOURCE[0]}")/tabler_qicon/"

# Initialize a new git repository in the temporary directory
git init $TEMP_DIR

# Add a new remote pointing to the repository to be cloned
git -C $TEMP_DIR remote add origin $REPO_URL

# Fetch only the latest commit and the tree information without the blobs (file contents)
git -C $TEMP_DIR fetch --depth 1 --filter=blob:none origin master

# Enable sparse-checkout mode in the local repository
git -C $TEMP_DIR config core.sparseCheckout true

# Add 'icons' directory to the sparse-checkout configuration
echo "icons/*" > $TEMP_DIR/.git/info/sparse-checkout

# Checkout only the 'icons' directory from the 'master' branch
git -C $TEMP_DIR checkout master

# Check if rsync is available on the system, if not use cp
if command -v rsync &> /dev/null; then
    # Use rsync to copy the "icons" directory to the target location
    # -r: recursive copy, includes directories
    # --info=progress2: show progress during transfer
    rsync -r --info=progress2 $TEMP_DIR/icons/ $TARGET_DIR/
else
    # Use cp to copy the "icons" directory to the target location
    echo -n "Copying icons.."
    cp -rf $TEMP_DIR/icons/ $TARGET_DIR/
    echo -e "\rIcons copied successfully."
fi

generate_pyi_file() {
    # Generate the .pyi file
    {
        # Define a string with Python keywords, separated by spaces
        python_keywords="False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield"

        echo "class QIcon: ..."
        echo ""
        echo "class TablerQIcon:"
        for file in $TARGET_DIR/icons/*.svg; do
            icon_name=$(basename "$file" .svg)

            # Replace all non-alphanumeric characters with an underscore
            icon_name=$(echo "$icon_name" | sed 's/\W/_/g')

            # If the icon name starts with a digit or is a Python keyword, prepend an underscore
            if [[ $icon_name =~ ^[0-9] ]] || [[ " ${python_keywords[@]} " =~ " ${icon_name} " ]]; then
                icon_name="_$icon_name"
            fi

            echo "    def $icon_name(self) -> QIcon: ..."
        done
    } > $TARGET_DIR/tabler_qicon.pyi
}

# Call the function to generate the .pyi file
echo -n "Generating tabler_qicon.pyi file..."
generate_pyi_file
echo -e "\rtabler_qicon.pyi file generation completed."
