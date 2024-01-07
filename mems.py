from PIL import Image, ImageDraw, ImageFont


print ('Генератор мемов запущен!')
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
print(top_text, bottom_text)


print ("Список картинок")
print ("1. Кот в ресторане.")
print("2. Кот в очках")
png = int(input ("Введите номер картинки"))
if png == 1 :
    png_file = "Кот в ресторане.png"
if png == 2 :
    png_file = "Кот в очках.png"

image = Image.open(png_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70 )

#draw.tex(0,0)), top_tex, font=font, fill='black')
#tex_width = tex[2]

text = draw.textbbox((0,0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill='black')

text = draw.textbbox((0,0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill='black')
#draw.tex(0,100)), bottom_tex, font=font, fill='black')

image.save("new_meme.jpg")




