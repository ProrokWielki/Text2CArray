import numpy
import yaml

from PIL import Image, ImageDraw, ImageFont

with open("texts.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

defaults = config["Defaults"]

for text_config in config["Texts"]:
  try:
  	font_size = text_config["size"]
  except:
  	font_size = defaults["size"]

  try:
  	font_name = text_config["font"]
  except:
  	font_name = defaults["font"]

  text = str(text_config["text"])

  print(font_name)
  print(font_size)

  font = ImageFont.truetype(font_name, font_size)

  text_size = font.getsize(text)

  image = Image.new("L", text_size, (0))
  image_draw = ImageDraw.Draw(image)
  image_draw.text((0, 0), text, font=font, fill=(255))

  array = numpy.asarray(image)

  TopDecortaor = "#include <stdint.h>\nuint8_t  "+ text_config["id"] +"[] = {"
  BottomDecorator = "};"

  with open(text_config["id"]+".cpp",'w') as file:
    file.write(TopDecortaor)

    for line in array:
        for pixel in line:
            file.write(str(pixel) + ", ")
            
    file.write(BottomDecorator)

