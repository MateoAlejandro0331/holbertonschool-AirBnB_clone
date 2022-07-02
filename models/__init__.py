#!/usr/bin/python3
"""Create a unique FileStorage instance"""

from models.engine import FileStorage


storage = FileStorage()
storage.reload()
