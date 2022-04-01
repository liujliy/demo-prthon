import os
import time
import shutil

from PIL import Image


class Wallpaper:
    username = os.environ['USERNAME']

    file_urls = {
        "wall_src": "C:\\Users\\" + username
                    + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\"
                    + "LocalState\\Assets\\",
        "wall_dst": "C:\\Users\\" + username + "\\Desktop\\Wallpapers\\",
        "wall_mobile": "C:\\Users\\" + username + "\\Desktop\\Wallpapers\\mobile\\",
        "wall_desktop": "C:\\Users\\" + username + "\\Desktop\\Wallpapers\\desktop\\"
    }

    msg = '''
                DDDDD      OOOOO    NN      N  EEEEEEE
                D    D    O     O   N N     N  E
                D     D   O     O   N  N    N  E
                D     D   O     O   N   N   N  EEEE
                D     D   O     O   N    N  N  E
                D    D    O     O   N     N N  E
                DDDDD      OOOOO    N      NN  EEEEEEE
            '''

    @staticmethod
    def time_gap(string):
        print(string, end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(1)
        print(".")

    @staticmethod
    def copy_wallpapers():
        w = Wallpaper()
        w.time_gap("复制壁纸")

        for filename in os.listdir(w.file_urls["wall_src"]):
            shutil.copy(w.file_urls["wall_src"] +
                        filename, w.file_urls["wall_dst"])

    @staticmethod
    def change_ext():
        w = Wallpaper()
        w.time_gap("更改扩展名")
        for filename in os.listdir(w.file_urls["wall_dst"]):
            base_file, ext = os.path.splitext(filename)
            if ext == "":
                if not os.path.isdir(w.file_urls["wall_dst"] + filename):
                    os.rename(w.file_urls["wall_dst"] + filename,
                              w.file_urls["wall_dst"] + filename + ".jpg")

    @staticmethod
    def extract_wall():
        w = Wallpaper
        w.time_gap("提取壁纸")
        for filename in os.listdir(w.file_urls["wall_dst"]):
            base_file, ext = os.path.splitext(filename)
            if ext == ".jpg":
                try:
                    im = Image.open(w.file_urls["wall_dst"] + filename)
                except IOError:
                    print("This isn't a picture.", filename)
                if list(im.size)[0] != 1920 and list(im.size)[0] != 1080:
                    im.close()
                    os.remove(w.file_urls["wall_dst"] + filename)
                else:
                    im.close()

    @staticmethod
    def arr_desk_wallpapers():
        w = Wallpaper
        w.time_gap("整理桌面壁纸")
        for filename in os.listdir(w.file_urls["wall_dst"]):
            base_file, ext = os.path.splitext(filename)
            if ext == ".jpg":
                try:
                    im = Image.open(w.file_urls["wall_dst"] + filename)

                    if list(im.size)[0] == 1920:
                        im.close()
                        os.rename(w.file_urls["wall_dst"] + filename,
                                  w.file_urls["wall_desktop"] + filename)
                    elif list(im.size)[0] == 1080:
                        im.close()
                        os.rename(w.file_urls["wall_dst"] + filename,
                                  w.file_urls["wall_mobile"] + filename)
                    else:
                        im.close()
                except FileExistsError:
                    print("文件已存在!")
                    os.remove(w.file_urls["wall_dst"] + filename)

    @staticmethod
    def exec_all():
        w = Wallpaper
        w.copy_wallpapers()
        w.change_ext()
        w.extract_wall()
        w.arr_desk_wallpapers()
        print(w.msg)
        time.sleep(2)


wall = Wallpaper()
wall.exec_all()
