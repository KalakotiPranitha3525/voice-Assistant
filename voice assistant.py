import sys
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class VoiceAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Assistant")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Press the button and speak", self)
        self.label.setGeometry(50, 50, 300, 30)

        self.button = QPushButton("Listen", self)
        self.button.setGeometry(150, 100, 100, 30)
        self.button.clicked.connect(self.listen_and_process)

    def listen_and_process(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            self.label.setText("Listening...")
            audio = recognizer.listen(source)

        try:
            self.label.setText("Processing...")
            command = recognizer.recognize_google(audio)
            self.label.setText(f"You said: {command}")
            # Here you can process the command and perform actions based on it
        except sr.UnknownValueError:
            self.label.setText("Sorry, I couldn't understand that.")
        except sr.RequestError:
            self.label.setText("Sorry, there was an error processing your request.")

def main():
    app = QApplication(sys.argv)
    window = VoiceAssistant()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
