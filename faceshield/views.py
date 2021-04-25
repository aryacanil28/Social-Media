import os
from django.conf import settings

from django.shortcuts import render,HttpResponse
from django.views import View
from accounts.models import Userdetails
from .models import FaceShieldDetails

import os
import face_recognition


# Create your views here.
def encode_facess(folder):
    list_people_encoding = []

    for filename in os.listdir(folder):
        known_image = face_recognition.load_image_file(f'{folder}{filename}')
        known_encoding = face_recognition.face_encodings(known_image)[0]
        list_people_encoding.append((known_encoding, filename))

    return list_people_encoding


def find_target_face(target_image,target_encoding):
    face_location = face_recognition.face_locations(target_image)
    x = encode_facess(os.path.join(settings.MEDIA_ROOT,'face_training\\'))
    found_labels = []
    not_found = []
    for person in x:
        encode_faces = person[0]
        filename = person[1]

        is_target_face = face_recognition.compare_faces(encode_faces, target_encoding, tolerance=0.51)
        # print(is_target_face)
        if not True in is_target_face:
            not_found.append(False)
        else:
            not_found.append(True)

        if face_location:
            face_number = 0
            for location in face_location:
                if is_target_face[face_number]:
                    label = filename
                    # create_frame(location,label)
                    print(location, label)
                    found_labels.append(label)
                face_number += 1

    print(not_found)
    usersnames = []
    if not True in not_found:
        print("no person found")
        return False
    else:
        for p in found_labels:
            x = p.split('.')
            usersnames.append(x[0])
        print("persons found", usersnames)
    return usersnames

class faceAuthentification(View):
    def fds(self,request):
        user = Userdetails.objects.get(user = request.user)
        print(str(user.profile_pic).split('/'))
        img = (str(user.profile_pic).split('/'))[1]
        print(img)
        load_image = os.path.join(settings.MEDIA_ROOT,'profile-pic\{}'.format(img))
        print(load_image)
        print(os.path.join(settings.MEDIA_ROOT,'face_training\\'))

        target_image = face_recognition.load_image_file(load_image)
        target_encoding = face_recognition.face_encodings(target_image)

        result = find_target_face(target_image, target_encoding)
        return result



