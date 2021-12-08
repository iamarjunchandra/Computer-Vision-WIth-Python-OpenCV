# Computer-Vision-WIth-Python-OpenCV

The repositiorycontains an algorithm that takes feed from a camera and detects sticky notes in the screen as well as caluculate how far the sticky note is from the camera.

Let's try to apply the Triangle Similiarity principle in our problem to calculate the distance of the stickynote from camera. The triangle similarity goes something like this: Let’s say we have a marker or object with a known width W. We then place this marker some distance D from our camera. We take a picture of our object using our camera and then measure the apparent width in pixels P. This allows us to derive the perceived focal length F of our camera:

F = (P x D) / W

For example, let’s say I place a standard piece of 8.5 x 11in piece of paper (horizontally; W = 11) D = 24 inches in front of my camera and take a photo. When I measure the width of the piece of paper in the image, I notice that the perceived width of the paper is P = 248 pixels.

My focal length F is then:

F = (248px x 24in) / 11in = 543.45
