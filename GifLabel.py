# from https://pythonprogramming.altervista.org/animate-gif-in-tkinter/
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle


class GifLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    def __init__(self, root):
        """
        init GifLabel
        :param root: root window
        """
        super().__init__(root)
        self.is_show = True

    def load(self, im):
        """
        loads image
        :param im: image path
        """
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        """
        unload image
        """
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        """
        show next frame
        """
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
