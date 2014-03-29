from PIL import Image, ImageDraw
import ch09_input

def main():
    """http://www.pythonchallenge.com/pc/return/good.html"""
    for name in 'first', 'second':
        xy = getattr(ch09_input, name)
        im = Image.new('RGB', (420, 420))
        draw = ImageDraw.Draw(im)
        draw.line(xy)
        im.save(name + '.png', 'png')
        im.show()
        print 'http://www.pythonchallenge.com/pc/return/bull.html'


if __name__ == '__main__':
    main()

