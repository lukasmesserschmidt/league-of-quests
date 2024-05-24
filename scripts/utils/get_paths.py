import os


def get_path(relativ_path: str, top_moves: int = 0):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "..\\" * top_moves, relativ_path
    )
    file_path = os.path.normpath(file_path)

    return file_path
