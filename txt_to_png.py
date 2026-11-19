import base64

txt_file = r"C:\Users\KNT23265\Downloads\anh.txt"
png_file = r"C:\Users\KNT23265\Downloads\anh_khoi_phuc.png"

with open(txt_file, "r", encoding="utf-8") as f:
    encoded = f.read()

data = base64.b64decode(encoded)

with open(png_file, "wb") as f:
    f.write(data)

print("Done:", png_file)
