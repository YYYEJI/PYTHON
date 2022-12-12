from PIL import Image, ImageDraw, ImageFont

### YOUR CODE STARTS HERE
# This line opens the God.jpg background-picture.
img = Image.open('God.jpg')

# This line puts my favorite Bible verse in a text variable.
text="Come to me, all you who are weary and burdened, I will give you rest. (Matthew 11:28)"

# This is the line that i want to write text to the image.
draw=ImageDraw.Draw(img)
# A line that I want to write text to this location.
draw.text((30,10),text)

# This line stores the generated picture in my-bible-verse.png.
img.save('my-bible-verse.png')

# This line shows pictures that contain text.
img.show()
### YOUR CODE ENDS HERE