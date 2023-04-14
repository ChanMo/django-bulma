import glob, os
import click
from PIL import Image


width = 960

@click.command()
@click.option('--img', required=True)
@click.option('--width', type=int, default=960)
def cli(img, width):
    # for infile in glob.glob("*.png"):
    #     file, _ = os.path.splitext(infile)
    #     with Image.open(infile) as im:
    #         im = im.convert('RGB')
    #         im.thumbnail((width,width / im.size[0] * im.size[1]))
    #         im.save(file + ".jpeg", "JPEG")
    filename, _ = os.path.splitext(img)
    with Image.open(img) as im:
        im = im.convert('RGB')
        im.thumbnail((width,width / im.size[0] * im.size[1]))
        im.save(filename + ".jpeg", "JPEG")
            
            


if __name__ == '__main__':
    cli()
