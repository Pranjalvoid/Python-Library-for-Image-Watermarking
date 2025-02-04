<h1>**Watermark Image using OpenCV**</h1>
<p>This repository demonstrates how to add a watermark to an image using OpenCV in Python. The script reads an image and a watermark, resizes the watermark to fit the image, and then applies it using image blending.</p>
---
**Requirements**
To run this code, you'll need the following Python libraries:

OpenCV (cv2)
You can install the necessary library using pip:

pip install opencv-python
---
<h2>**Code Explanation**</h2>
The Python code provided in this repository performs the following tasks:

**1. Reading the Input Image**:
The script loads an image (image.jpg) using cv2.imread().

**2. Getting Image Dimensions:**
The dimensions (height, width, and number of color channels) of the image are extracted using .shape.

**3. Loading the Watermark:**
The watermark image (watermark.png) is loaded using cv2.imread().

**4. Resizing the Watermark:**
The watermark is resized to match the dimensions of the input image (height and width).

**5. Blending the Watermark with the Image:**
The cv2.addWeighted() function is used to blend the watermark and the image together. The function applies a weighted sum of the two images.

**6. Displaying the Result:**
The resulting image is displayed using cv2.imshow().

**7. Saving the Watermarked Image:**
The final image with the watermark is saved as watermarkedimage.jpg.

**8. Cleanup:**
The cv2.destroyAllWindows() function is called to close any OpenCV windows after the key press.

---
<p><h1><b>EXAMPLE </b></h1></p>
**Input image

![Image](https://github.com/user-attachments/assets/8d006d26-e312-4cad-9a7d-3b129793fcf9)
---

**Watermark image to add **
![Image](https://github.com/user-attachments/assets/350d9bfd-39ce-4b0c-b81a-dd1b555561dd)
---

**watermarked_image**
![Image](https://github.com/user-attachments/assets/f112f39d-7114-47f5-ab66-f5ff52a48bb4)
---

---

