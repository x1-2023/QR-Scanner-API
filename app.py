from flask import Flask, request, Response
from PIL import Image
from io import BytesIO
import base64
from pyzbar import pyzbar

app = Flask(__name__)

@app.route("/")
def hyworld():
    return "API Or Node 2037 Digital"
@app.route('/decode_qr', methods=['POST'])
def decode_qr():
    try:
        # Lấy dữ liệu ảnh base64 từ request
        image_base64 = request.json['image']

        # Giải mã ảnh mã QR từ chuỗi base64
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))

        # Giải mã mã QR
        qr_codes = pyzbar.decode(image)

        # Trích xuất dữ liệu từ mã QR
        qr_data = []
        for qr_code in qr_codes:
            data = qr_code.data.decode('utf-8')
            qr_data.append(data)

        # Trả về kết quả dưới dạng text/plain
        return Response('\n'.join(qr_data), mimetype='text/plain')
    except Exception as e:
        return Response(str(e), status=400, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
