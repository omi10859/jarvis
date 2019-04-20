import cv2
import numpy as np
import face_recognition as fc
import os



def unlock():
    image = os.path.join('asset','img','login','')

    files = []
    for root,file,dirs in os.walk(image):
        for _dir in dirs:
            files.append(_dir)

    if len(files) > 1:
        """If there is more than one image in the folder asset/img/login then Groot Rejects to Login"""
        print("login must have a unique image")

    imageAsset = image+files[0]
    print(imageAsset)


    #Creates encoding of known face placed in Asset -> img -> login to be used against the video frames
    master_image = fc.load_image_file(imageAsset)
    master_face_encoding = fc.face_encodings(master_image)[0]
    known_face_encodings = [master_face_encoding]
    known_face_names = ["Master"]


    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    face_values_observed = []
    flag = False

    video_capture = cv2.VideoCapture(0)

    while True:
        ret,frame = video_capture.read()
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        if process_this_frame:
            #<---------------------------IMPORTANT-------------------------------------->#
            # Find all the faces and face encodings in the current frame of video
            face_locations = fc.face_locations(rgb_small_frame)
            face_encodings = fc.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = fc.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = fc.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame
        
        #<=================FACE MATCHING AUTOMATION PART==============================>
        face_values_observed.append(face_names)
        if face_values_observed[:-101:-1].count(["Master"]) == 50:
            flag = True
            break
        #<============================================================================>
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255,0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)


        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            flag = False
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
    return flag

