JPG to PNG Converter CLI
A Python-based command-line utility that automates the process of converting images from JPG format to PNG format. 
This tool is designed for bulk processing, allowing users to transform entire directories of images with a single command.

Features
1. Bulk Conversion: Processes all images within a specified source folder.
2. Auto-Directory Creation: Automatically creates the output folder if it doesn't already exist.
3. Dynamic Path Handling: Uses os.path to ensure compatibility across Windows, Mac, and Linux.
4. Clean Output: Strips old extensions to prevent "double extensions" (e.g., image.jpg.png).

How to Use
This tool is run entirely through the Terminal. 
You must provide the source folder (where your JPGs are) and the destination folder (where you want the PNGs to go).
Example: python JPGtoPNGconverter.py <source_directory> <destination_directory>

What I Learned
During the development of this project, I mastered several core Backend Engineering concepts:
System Manipulation (sys): Using sys.argv to create flexible, non-hardcoded tools.
OS Integration (os): Automating folder creation and navigating file systems safely.
Image Processing (PIL): Opening, manipulating, and saving different image formats programmatically.
Error Handling: Implementing "guard rails" to prevent crashes when incorrect inputs are provided.
