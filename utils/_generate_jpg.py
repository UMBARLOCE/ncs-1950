# создание папки colors и генерация картинок.jpg по коду цвета NCS.
# необходимо сгененрировать картинки единожды перед стартом бота.

from PIL import Image
from database import select_all_ncs_and_html
import os


os.mkdir('colors')

ncs_html = select_all_ncs_and_html()

for ncs, html in ncs_html:
    img = Image.new('RGB', (5, 5), f'{html}')
    img.save(os.path.join('colors', f'{ncs}.jpg'))
