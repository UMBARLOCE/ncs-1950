from PIL import Image
from database.sq_db import select_ncs_html
import os


os.mkdir('colors')

ncs_html = select_ncs_html()

for color in ncs_html:
    img = Image.new('RGB', (5, 5), f'{color[1]}')
    img.save(os.path.join('colors', f'{color[0]}.jpg'))
