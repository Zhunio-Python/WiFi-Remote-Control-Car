import RPi.GPIO as GPIO
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


class Motor:
  """
  An instance of this class represents a DC Motor controlled by
  the Raspberry Pi 3 and a L293D Motor Drive IC (Integrated Circuit).

  A DC Motor is useful for rotating the motor in clockwise and counter-clockwise
  direction as well as controlling the speed of the rotation. The rotation of the
  motor is driven by the GPIO Pins, so there is no magic in there.... However, to
  control the speed of the rotation, we use a technique called PWM (Pulse Modular
  Width).

  To create an instance of this class, simply import this module and type:
    GPIO_PIN_ENABLE = 17
    GPIO_PIN_A = 22
    GPIO_PIN_B = 5
    MODE = MOTOR.BCM # For BCM mode OR (i.e. you use the GPIO numbering system)
    #MOTOR_MODE = MOTOR.BOARD # For Board mode (i.e. you use the physical pin numbering)
    myMotor = Motor(GPIO_PIN_ENABLE, GPIO_PIN_A, GPIO_PIN_B, MODE)

  It is not necessary that we know how this class work behind the scenes. But, if you
  are curious, the GPIO_PIN_A and GPIO_PIN_B are the ones that rotate the motor by
  having opposite polarities. The GPIO_PIN_ENABLE enables the circuit once it begins
  to supply voltage.
  """

  # Class Variables
  BCM = GPIO.BCM
  BOARD = GPIO.BOARD

  def __init__(self, GPIO_PIN_ENABLE, PIN_A, PIN_B, MODE):
    """
    Creates a new motor.
    :param GPIO_PIN_ENABLE: Any BCM or GPIO Pin
    :param PIN_A: Any BCM or GPIO Pin
    :param PIN_B: Any BCM or GPIO Pin
    :param MODE: The mode to use when referring to the Pins
    """
    self.ENABLE_PIN = GPIO_PIN_ENABLE
    self.PIN_A = PIN_A
    self.PIN_B = PIN_B
    self.MODE = MODE
    self.__setup()

  def rotateForward(self):
    forward = 'f'
    self.__rotate(forward)

  def rotateBackward(self):
    backward = 'b'
    self.__rotate(backward)

  def stop(self):
    try:
      GPIO.output(self.ENABLE_PIN, False)
    except:
      raise

  def cleanup(self):
    try:
      GPIO.cleanup([self.ENABLE_PIN, self.PIN_A, self.PIN_B])
    except:
      raise

  def __rotate(self, direction):
    try:
      forwards = 'f'
      backwards = 'b'
      # Rotate forwards
      if direction[0] == forwards:
        GPIO.output(self.PIN_A, False)
        GPIO.output(self.PIN_B, True)
      # Rotate Backwards
      elif direction[0] == backwards:
        GPIO.output(self.PIN_A, True)
        GPIO.output(self.PIN_B, False)
      # Enable rotation for n seconds
      GPIO.output(self.ENABLE_PIN, True)
    except:
      self.cleanup()
      raise

  def __setup(self):
      self.__setMode()
      self.__setupPins()

  def __setMode(self):
    try:
      GPIO.setmode(self.MODE)
    except:
      raise

  def __setupPins(self):
    try:
      GPIO.setup(self.ENABLE_PIN, GPIO.OUT)
      GPIO.setup(self.PIN_A, GPIO.OUT)
      GPIO.setup(self.PIN_B, GPIO.OUT)
    except:
      raise
