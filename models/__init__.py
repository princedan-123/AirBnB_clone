#!/usr/bin/python3
"""it initialises the file storage for the application"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
