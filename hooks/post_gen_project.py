import os
import glob

if __name__ == "__main__":
    for filename in glob.glob("./**/.gitkeep", recursive=True):
        os.remove(filename)
