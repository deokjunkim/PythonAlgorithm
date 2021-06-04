from flask import Flask, request, jsonify
from flask_restx import Resource, Api
import pdfFileMerge
import downloadFile

app = Flask(__name__)
api = Api(app)

# A welcome message to test our server
@api.route('/merge')
class merge(Resource):
    def post(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        print(request.json)
        result = pdfFileMerge.main(request.json)
        return result

@api.route('/download')
class merge(Resource):
    def post(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        print(request.json)
        result = downloadFile.main(request.json)
        return result


# @api.route('/download')
# class download(Resource):
#     def post(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
#         print(request.json)
#         result = pdfFileMerge.main(request.json,"download")
#         return result

# @api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
# class HelloWorld(Resource):
#     def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
#
#         return request.form
#     def post(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
#         print(request)
#         print(request.get_json)
#         print(request.get_data)
#         print(request.form)
#         print(request.json)
#         return request.form


# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)