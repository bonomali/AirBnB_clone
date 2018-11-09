from models.engine.file_storage import FileStorage

""" Creates a unique FileStorage instance for the application """
storage = FileStorage()
storage.reload()
