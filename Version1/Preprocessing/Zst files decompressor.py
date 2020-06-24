"""
* https://github.com/MI-K253/Python-Plays-Game
"""
import zstandard
import pathlib
import shutil
import numpy as np

path = r"C:\Users\Miaad\PycharmProjects\Python plays nfs\Version2\Test data hot encoded.npy.zst"
out = r"C:\Users\Miaad\PycharmProjects\Python plays nfs\Version2\a.npy"


def decompress_zstandard_to_folder():
    with open(path, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()

        with open(out, 'wb') as destination:
            decomp.copy_stream(compressed, destination)

decompress_zstandard_to_folder()

file = np.load(out, allow_pickle=True)
print(file)

# END