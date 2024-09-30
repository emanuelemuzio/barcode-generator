import json

from barcode import Code128
from barcode.writer import ImageWriter

json_data = []  

with open('list.json') as json_file:
   json_data = json.load(json_file)

for cf in json_data:
   with open(f"barcodes/{cf}.png", "wb") as f:
      Code128(cf, writer=ImageWriter()).write(f)