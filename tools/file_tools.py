def read_file(path: str):
    try:
        with open(path, "r") as f:
            content = f.read()

        return content
    except Exception as e:
        return str(e)