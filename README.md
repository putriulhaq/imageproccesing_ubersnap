# **Image Processing Backend Service**

This repository contains a Python backend service dedicated to image processing tasks including converting PNG to JPEG, resizing images, and compressing images to reduce file size while maintaining quality.

## **Functionality**

1. **Convert PNG to JPEG**: Allows users to convert PNG image files to JPEG format.
2. **Resize Images**: Users can resize images according to specified dimensions.
3. **Compress Images**: Images can be compressed to reduce file size while maintaining reasonable quality.

## **Installation and Usage**

1. _Clone the Repository_:

   ```
   git clone -b master  https://github.com/putriulhaq/imageproccesing_ubersnap.git
   ```

3. _Install Dependencies_:

   ```
   cd task_ubersnap
   pip install -r requirements.txt
   ```

4. _Run the Flask App_:

   ```
   python task.py
   ```
*The service will be accessible at http://localhost:5000*

### Convert PNG to JPEG

1. *Open Postman*.
2. *Create a POST request*.
3. *Set the request URL*: http://localhost:5000/convert_to_jpg.
4. *Select the body type as form-data*.
5. *Add a key-value pair*:
   - Key: image
   - Value: Path to your PNG image file.
6. *Send the request*.
7. Verify the response to ensure successful conversion.

### Resize Images

1. *Open Postman*.
2. *Create a POST request*.
3. *Set the request URL*: http://localhost:5000/resize_image.
4. *Select the body type as form-data*.
5. *Add key-value pairs*:
   - Key: image,  Value: Path to your image file.
   - Key: width,  Value: Desired width.
   - Key: height, Value: Desired height.
6. *Send the request*.
7. Verify the response to ensure successful resizing.

### Compress Images

1. *Open Postman*.
2. *Create a POST request*.
3. *Set the request URL*: http://localhost:5000/compress.
4. *Select the body type as form-data*.
5. *Add key-value pairs*:
   - Key: image,    Value: Path to your image file.
   - Key: quality,  Value: Compression quality (0-100).
6. *Send the request*.
7. Verify the response to ensure successful compression.


