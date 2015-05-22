import sys
from cx_Freeze import setup, Executable
import hashlib

buildOptions = dict(
        compressed = True,
        path = sys.path)
setup(
    name = "md2pdf",
    version = "0.1",
    description = "Convert Markdown to PDF",
    executables = [Executable("md2pdf.py")])