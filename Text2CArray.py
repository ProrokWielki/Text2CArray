import numpy
import yaml
import logging
import argparse

from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description="Program converting providing text to C array.")

required_named = parser.add_argument_group("Required named arguments")
required_named.add_argument("--config",  dest="config_file", required=True,  help="Configuration file to be used.")

args = parser.parse_args()

def create_header(texts):

  with open("texts.h", "w") as header:

    TopDecortaor = "#ifndef TEXTS_H\n#define TEXTS_H\n\n#include <stdint.h>\n\n"
    BottomDecorator = "#endif /* TEXTS_H */"

    header.write(TopDecortaor)

    for text in texts:
      header.write("extern uint8_t " + text["id"] + "[];\n")

    header.write("\n" + BottomDecorator)



with open(args.config_file, 'r') as stream:
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

  font = ImageFont.truetype(font_name, font_size)

  text_size = font.getsize(text)

  image = Image.new("L", text_size, (0))
  image_draw = ImageDraw.Draw(image)
  image_draw.text((0, 0), text, font=font, fill=(255))

  array = numpy.asarray(image)

  TopDecortaor = "#include <stdint.h>\n\nuint8_t  "+ text_config["id"] +"[] = {"
  BottomDecorator = "};"

  with open(text_config["id"]+".cpp",'w') as file:
    file.write(TopDecortaor + "\n")

    line_length = 0

    for line in array:
        for pixel in line:
            line_length += 6
            file.write(f"0x{pixel:02x}" + ", ")
            if line_length + 6 > 160:
              file.write("\n")
              line_length = 0 
            
    file.write(BottomDecorator)

create_header(config["Texts"])

