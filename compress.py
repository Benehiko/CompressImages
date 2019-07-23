import pathlib

from PIL import Image as im


def compress_image(f, directory, size=(1280, 960), quality=85):
    image = im.open("images/" + directory + "/" + f)
    image.thumbnail(size)
    image.save("compressed/" + directory + "/" + f, optimize=True, quality=quality)


def main():
    if not pathlib.Path("compressed").exists():
        pathlib.Path("compressed").mkdir(parents=True)

    pathlib.Path("images").mkdir(parents=True, exist_ok=True)
    path = pathlib.Path("images")

    counter = 0
    total = len(list(pathlib.Path('images/').rglob('*.*')))

    print(total)
    for f in path.rglob('*.*'):
        pathlib.Path("compressed/" + str(f.parent).split('/')[1] + "/").mkdir(parents=True, exist_ok=True)
        compress_image(f.name, str(f.parent).split('/')[1])
        percentage = float(counter * 100 / float(total))
        print("Progress: %f%%" % percentage)
        counter += 1


if __name__ == "__main__":
    main()
