# importing the computer vision libraries and the hand detection libraries
import cv2
import mediapipe as mp


# importing to get audio deices and mess with audio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

fingerCheck = 20
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # converting the image to bgr so that its easier to process
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # converting the image back to rgb
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        fingerCount = 0


        # Get default audio device using PyCAW
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # if there are hand landmarks (aka if hands are on screen or detected)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # getting the hand index, then using the index to check the label (left or right)
                hand_index = results.multi_hand_landmarks.index(hand_landmarks)
                hand_label = results.multi_handedness[hand_index].classification[0].label

                # creating an open array to hold the coordinates of the x and y positions
                handLandmarks = []

                # filling out that array with x and y positions
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                # checking thumb (refer to media pipe hands chart)
                if hand_label == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount += 1
                elif hand_label == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount += 1

                # checking for index finger being bent
                if handLandmarks[8][1] < handLandmarks[6][1]:
                    fingerCount += 1

                # checking for middle finger being bent
                if handLandmarks[12][1] < handLandmarks[10][1]:
                    fingerCount += 1

                # checking for ring finger being bent
                if handLandmarks[16][1] < handLandmarks[14][1]:
                    fingerCount += 1

                # checking for pinky being bent
                if handLandmarks[20][1] < handLandmarks[18][1]:
                    fingerCount += 1

                # drawing the hand landmarks and such
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            #  making sure we are not repeating the same volume change
            if fingerCheck != fingerCount:
                volume.SetMasterVolumeLevelScalar(fingerCount / 10, None)
                fingerCheck = fingerCount

        cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()