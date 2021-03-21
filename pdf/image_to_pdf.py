import img2pdf as i2p 

img_path="boat.JPG"

with open(f"{img_path}.pdf",'wb') as f:
    f.write(i2p.convert(img_path))

print("Done")