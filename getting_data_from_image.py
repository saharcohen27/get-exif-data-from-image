# pip install PIL or
# pip install Pillow
from PIL import Image
from PIL.ExifTags import TAGS


# path to the image or video
imagename = r"C:\XXXXXXXX\XXXXXXXXX\XXXXXXXXX\imagename.imagefiletype"  # change it to your local file location

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)

    print(f"{tag:25}: {data}")


