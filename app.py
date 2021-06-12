from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import cv2
import numpy
import os
port = int(os.environ.get('PORT', 5000))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
app = Flask(__name__)
api = Api(app)
CORS(app)
class FotoRecognize(Resource):
    def get(self):
        response = {"msg":"Halloo"}
        return response
    def post(self):
        foto = request.files['file']
        if not foto:
            response = {"data":"no foto"}
            return response, 400
        else:            
            foto  = request.files['file'].read()
            npimg = numpy.fromstring(foto, numpy.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=4,
                minSize=(30, 30)
            )
            
            # print("[INFO] Found {0} Faces!".format(len(faces)))
            if len(faces)!=1 :
                response = {"data":"not ok"}
                return response  
            response = {"data":"ok"}
            return response   
                 
class Nidzam(Resource):
    def get(self):
        response = {"msg":"welcome"}
        return response
    
             

api.add_resource(FotoRecognize, "/fotoRecognize" , methods=["GET","POST"])
api.add_resource(Nidzam, "/" , methods=["GET"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)




