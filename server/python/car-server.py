from flask import Flask
from car.v1.Car import Car

app = Flask(__name__)
car = None


@app.route("/")
def welcome():
    return "Welcome to the Car App :)"


@app.route("/init")
def init():
    left = [17, 27, 22]
    right = [18, 23, 24]
    duration = 1
    global car
    car = Car(left, right, duration)
    print("Car successfully created.")


@app.route("/moveForward")
def moveForward():
    global car
    if car is None:
        print("Car not initialized")
    else:
        car.moveBackward()
        print("Mowing car forward.")


@app.route("/moveBackward")
def moveBackward():
    global car
    if car is None:
        print("Car not initialized")
    else:
        car.moveBackward()
        print("Mowing car backwards")

if __name__ == "__main__":
    app.run()
