
# copy an image using binary mode
with open('pic.jpg', 'rb') as src, open('pic_copy.jpg', 'wb') as dst:
    while True:
        block= src.read(8192)
        if not block:
            break
        dst.write(block)


# Binary mode returns/accepts bytes (b"..."), not str.
# No encoding/decoding is done.