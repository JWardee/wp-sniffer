def import_file(name, methods=None):
    if methods is None:
        methods = []

    return __import__(name, globals(), locals(), methods)
