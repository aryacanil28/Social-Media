import os
from django.conf import settings
from django.contrib.auth.models import User

from django.shortcuts import render,HttpResponse
from django.views import View
from accounts.models import Userdetails
from posts.models import BluredPost, Posts
from .models import FaceShieldDetails, BluredImages

import os
import face_recognition

import cv2 as cv


# Create your views here.


class faceAuthentification(View):

    def __init__(self,request,type):
        self.user = Userdetails.objects.get(user=request.user)
        self.blur_areas=[]
        self.usersnames = []
        if type == 'profile_pic':
            self.img = (str(self.user.profile_pic).split('/'))[1]
            # getting the path of uploaded profile img
            self.load_image = os.path.join(settings.MEDIA_ROOT, 'profile-pic\{}'.format(self.img))
        else:
            self.latest_post = Posts.objects.filter(post_owner = request.user)
            print((self.latest_post[len(self.latest_post)-1]).post_id)
            self.post_id = (self.latest_post[len(self.latest_post)-1]).post_id
            print(self.latest_post[len(self.latest_post)-1].post_image,'***')
            self.img = (str(self.latest_post[len(self.latest_post)-1].post_image).split('/'))[1]
            #getting the path of uploaded post img
            self.load_image = os.path.join(settings.MEDIA_ROOT, 'post_images\{}'.format(self.img))

    def fds(self):
        # user = Userdetails.objects.get(user = request.user)
        # print(str(user.profile_pic).split('/'))
        # img = (str(user.profile_pic).split('/'))[1]
        # print(img)
        # load_image = os.path.join(settings.MEDIA_ROOT,'profile-pic\{}'.format(img))
        # print(load_image)
        # print(os.path.join(settings.MEDIA_ROOT,'face_training\\'))

        self.target_image = face_recognition.load_image_file(self.load_image)
        self.target_encoding = face_recognition.face_encodings(self.target_image)

        result = self.find_target_face(self.target_image, self.target_encoding)
        return result

    def encode_facess(self,folder):
        list_people_encoding = []

        for filename in os.listdir(folder):
            known_image = face_recognition.load_image_file(f'{folder}{filename}')
            known_encoding = face_recognition.face_encodings(known_image)[0]
            list_people_encoding.append((known_encoding, filename))

        return list_people_encoding

    def find_target_face(self,target_image, target_encoding):
        face_location = face_recognition.face_locations(target_image)
        x = self.encode_facess(os.path.join(settings.MEDIA_ROOT, 'face_training\\'))
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
                        self.blur_areas.append(location)
                        # create_frame(location,label)
                        print(location, label)
                        found_labels.append(label)
                    face_number += 1

        print(not_found)

        if not True in not_found:
            print("no person found")
            return False
        else:
            for p in found_labels:
                x = p.split('.')
                self.usersnames.append(x[0])
            print("persons found", self.usersnames)
        return self.usersnames

    def save_blured_image(self, request, folder_name, photo, type):

        img_blur_path = os.path.join(settings.MEDIA_ROOT, '{0}\\'.format(folder_name))
        img_blur_path2 = '/{1}/{0}-{2}.jpg'.format(request.user.username, folder_name, self.post_id)
        print(img_blur_path)

        if type == 'profile_pic':
            cv.imwrite(os.path.join(img_blur_path, '{}.jpg'.format(request.user.username)), photo)
        else:
            cv.imwrite(os.path.join(img_blur_path, '{0}-{1}.jpg'.format(request.user.username, self.post_id)), photo)

        cv.waitKey(0)
        print(img_blur_path)
        user = User.objects.get(username=request.user)
        if type == 'profile_pic':
            BI = BluredImages.objects.create(user=user, blur_image=img_blur_path2)
            BI.save()
        elif type == 'post_image':
            print(img_blur_path2,type)
            BP = BluredPost.objects.create(user=user, blur_post=img_blur_path2)
            BP.save()
        else:
            pass

    def bluring_faces(self,request,type):
        face_location = face_recognition.face_locations(self.target_image)
        # Blur all face
        self.photo = cv.imread(self.load_image)

        for top, right, bottom, left in self.blur_areas:
            # Scale back up face locations since the frame we detected in was scaled to 1/zoom_in size

            # Extract the region of the image that contains the face
            face_image = self.photo[top:bottom, left:right]

            # Blur the face image
            face_image = cv.GaussianBlur(face_image, (61, 61), 0)

            # Put the blurred face region back into the frame image
            self.photo[top:bottom, left:right] = face_image


        # Save image to file
        if type == 'profile_pic':
            self.save_blured_image(request, 'blured', self.photo, type)
            # img_blur_path = os.path.join(settings.MEDIA_ROOT,'blured\\')
            # img_blur_path2 = '/blured/{}.jpg'.format(request.user.username)
            # print(img_blur_path)
            # cv.imwrite(os.path.join(img_blur_path,'{}.jpg'.format(request.user.username)), self.photo)
            # cv.waitKey(0)
            # print(img_blur_path)
            # user = User.objects.get(username=request.user)
            # BI = BluredImages.objects.create(user=user,blur_image=img_blur_path2)
            # BI.save()

        elif type == 'post_image':
            self.save_blured_image(request, 'blured-post', self.photo, type)
        else:
            pass







