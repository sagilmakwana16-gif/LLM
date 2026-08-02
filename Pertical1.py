data={
    "NLP":{
    "Domain_name":" NPL ",
    "Description":"Natural Language Processing (NLP) is a branch of artificial intelligence that helps computers read, understand, and generate human language",
    "Two_real-word_application":"1. Chatbots,2.Voice Assistants  ",
    "Popular_python_libraries used":"1.spaCy,2.NLTK  "
    },

     "Computer_Vision":{
    "Domain_name":"Computer_Vision",
    "Description":"Computer vision is a field of artificial intelligence that trains computers to see, process, and understand visual data from images and videos. It turns digital pixels into meaningful numbers and labels ",
    "Two_real-word_application":"1. Healthcare,2.Military   ",
    "Popular_python_libraries used":"1.Mediapipe,2.OpenCV  "
    },

    "Speech_ Processing":{
    "Domain_name":"Speech_ Processing",
    "Description":"Speech processing is the study and digital manipulation of human speech signals ",
    "Two_real-word_application":"1. Voice Assistants,2.utomatic Speech Recognition (ASR) for Transcription   ",
    "Popular_python_libraries used":"1.Librosa,2.PyAudio  "
    },

    "Robotics":{
    "Domain_name":" Robotics ",
    "Description":"Robotics is the branch of technology that deals with designing, building, programming, and operating robots.",
    "Two_real-word_application":"1. Manufacturing,2.Healthcare  ",
    "Popular_python_libraries used":"1.ROSPy,2.PyRobot  "}



}




print("Please select option")
print("1.NLP")
print("2.Computer_Vision")
print("3.Speech_ Processing")
print("4.Robotics")

choice=int(input("Please enter choice"))
print("User Choice",choice)

if choice==1:
 print(data['NLP'])
elif choice==2:
 print(data['Computer_Vision'])
elif choice==3:
 print(data['Speech_ Processing'])
elif choice==4:
    print(data['Robotics'])
else:
 print("Error")
