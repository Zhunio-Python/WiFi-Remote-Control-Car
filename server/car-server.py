from flask import Flask
from lib.utils import Car


app = Flask(__name__)
car = None
isInitialized = False


@app.route("/")
def welcome():
    return "Welcome to the Car App :)"


@app.route("/init")
def init():
    global car
    global isInitialized

    if isInitialized:
        answer = "Car is already initialized."
        answer += "\nContinuing... anyway"
    else:
        leftMotor = [17, 27, 22]
        rightMotor = [18, 23, 24]
        duration = 1
        car = Car(leftMotor, rightMotor, duration)
        isInitialized = True
        answer = "Car successfully created."
    print(answer)
    return answer


@app.route("/moveForward")
def moveForward():
    if isInitialized:
        forward = 'f'
        __move(forward)
        answer = "Moving forward..."
    else:
        answer = "Car is not initialized."
    print(answer)
    return answer


@app.route("/moveBackward")
def moveBackward():
    if isInitialized:
        backward = 'b'
        __move(backward)
        answer = "Moving backward..."
    else:
        answer = "Car is not initialized."
    print(answer)
    return answer


@app.route("/moveRight")
def moveRight():
    if isInitialized:
        right = 'r'
        __move(right)
        answer = "Moving right..."
    else:
        answer = "Car is not initialized."
    print(answer)
    return answer


@app.route("/moveLeft")
def moveLeft():
    if isInitialized:
        left = 'l'
        __move(left)
        answer = "Moving left..."
    else:
        answer = "Car is not initialized."
    print(answer)
    return answer


@app.route("/cleanup")
def cleanup():
    global car
    global isInitialized

    if isInitialized:
        answer = "Cleaning car..."
        car.cleanup()
        isInitialized = False
        answer += "\nCar cleaned up."
    else:
        answer = "Car is not initialized."
        answer += "\nNot cleaning up..."
    print(answer)
    return answer


def __move(direction):
    if direction == 'f':
        car.moveForward()
    elif direction == 'b':
        car.moveBackward()
    elif direction == 'r':
        car.moveRight()
    elif direction == 'l':
        car.moveLeft()


if __name__ == "__main__":
    app.run(host='192.168.0.19', port=3000)
