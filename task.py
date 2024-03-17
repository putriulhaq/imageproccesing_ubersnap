from flask import Flask, request, jsonify
import cv2
import os

app = Flask(__name__)

def convertImage(image):
    img = cv2.imread(image)
    if cv2.imwrite('converted.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100]):
        print(f"your image succesfully converted with name converted.jpg")
    else:
        print('failed to convert image')

def resize_image(image, width, height):
    img = cv2.imread(image)
    resized_img = cv2.resize(img, (int(width), int(height)))
    cv2.imwrite('resized.jpg', resized_img)

def compress_image(image_path, quality):
    img = cv2.imread(image_path)
    cv2.imwrite('compressed.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality)])

def validation_check(image_path): #if path is valid
    if os.path.exists(image_path):
        return True
    else:
        return False

@app.route('/convert_to_jpg', methods=['POST'])
def convert_to_jpg():
    image_file = request.args.get("image")
    validation = validation_check(image_file)
    if validation is True:
        convertImage(image_file)
        return jsonify({"message": "Image converted to JPEG"}), 200
    else:
        print('no valid')
        return jsonify({"message": "No Valid"}), 400
    
@app.route('/resize_image', methods=['POST'])
def resize_img():
    image_file = request.form.get("image")
    width = request.form.get('width')
    height = request.form.get('height')
    validation = validation_check(image_file)
    if validation is True:
        resize_image(image_file, width, height)
        return jsonify({"message": "Image resized"}), 200
    else:
        print('no valid')
        return jsonify({"message": "No Valid"}), 400
    
@app.route('/compress', methods=['POST'])
def compres():
    image_file = request.form.get("image")
    quality = request.form.get('quality')
    validation = validation_check(image_file)
    if validation is True:
        compress_image(image_file, quality)
        return jsonify({"message": "Image resized"}), 200
    else:
        print('no valid')
        return jsonify({"message": "No Valid"}), 400



# get versi OpenCV
print("Installed OpenCV version:", cv2.__version__)


if __name__ == '__main__':
    app.run(debug=True)