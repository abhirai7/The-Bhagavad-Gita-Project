from PIL import Image, ImageDraw, ImageFont
from shlok import Shlok



def add_text_to_image(image_path, output_path):
    text_color = (237, 232, 220)
    shlok_ = Shlok()
    shlok_data = shlok_.get_shlok()
    translation = shlok_data['Translation']
    shlok = shlok_data['Shlok']
    image = Image.open(image_path)
    print(shlok_.exclude_shloks.__len__())

    draw = ImageDraw.Draw(image)
    sanskrit_font = ImageFont.truetype('NotoSansDevanagari-Regular.ttf', 80)
    # if font_path:
    #     font = ImageFont.truetype(font_path, font_size)
    # else:
    font = ImageFont.load_default(60)
    shlok_positon = (150, 700)
    translation_position = (50, 2000)
    draw.text(shlok_positon, shlok, font=sanskrit_font, fill=text_color)
    draw.text(translation_position, translation, font=font, fill=text_color)



    # draw.text(position, text, font=font, fill=text_color)

    image.save(output_path)

    print(f"Text added to image and saved as {output_path}")

