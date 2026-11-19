import base64

png_file = r"C:\Users\KNT23265\Downloads\image.png"
txt_file = r"C:\Users\KNT23265\Downloads\image.txt"

with open(png_file, "rb") as f:
    data = f.read()

encoded = base64.b64encode(data).decode("ascii")

with open(txt_file, "w", encoding="utf-8") as f:
    f.write(encoded)

print("Done:", txt_file)
