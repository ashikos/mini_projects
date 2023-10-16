from PIL import ImageEnhance, Image, ImageFilter
import os


path = "./galery"
path_out = "./automated galary"

for filename in os.listdir(path):
    print(filename)
    img = Image.open(f"{path}/{filename}")

    edit = ImageEnhance.Color(img).enhance(1.5)
    edit = edit.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{path_out}/{clean_name}_edited.jpg")
    img.close()
