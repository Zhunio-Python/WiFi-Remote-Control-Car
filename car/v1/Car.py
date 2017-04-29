from motor.v2.Motor import Motor
import time


class Car:
  def __init__(self, leftMotor, rightMotor, duration):
    self.leftMotor = Motor(leftMotor[0], leftMotor[1],
                           leftMotor[2], Motor.BCM)
    self.rightMotor = Motor(rightMotor[0], rightMotor[1],
                            rightMotor[2], Motor.BCM)
    self.duration = duration

  def moveForward(self):
    self.leftMotor.rotateForward()
    self.rightMotor.rotateForward()
    time.sleep(self.duration)
    self.leftMotor.stop()
    self.rightMotor.stop()

  def moveBackward(self):
    self.leftMotor.rotateBackward()
    self.rightMotor.rotateBackward()
    time.sleep(self.duration)
    self.leftMotor.stop()
    self.rightMotor.stop()

  def moveLeft(self):
    self.rightMotor.rotateForward()
    time.sleep(self.duration)
    self.rightMotor.stop()

  def moveRight(self):
    self.leftMotor.rotateForward()
    time.sleep(self.duration)
    self.leftMotor.stop()

  def cleanup(self):
    self.leftMotor.cleanup()
    self.rightMotor.cleanup()
