from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice


class MotorController:

    # Motor controller board initialisation GPIO CONSTANTS
    MOTOR_BOARD_INIT = 0
    # Motor A, Left Side GPIO CONSTANTS
    PWM_DRIVE_LEFT = 21  # ENA - H-Bridge enable pin
    FORWARD_LEFT_PIN = 26  # IN1 - Forward Drive
    REVERSE_LEFT_PIN = 19  # IN2 - Reverse Drive
    # Motor B, Right Side GPIO CONSTANTS
    PWM_DRIVE_RIGHT = 5  # ENB - H-Bridge enable pin
    FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
    REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

    # Initialise objects for H-Bridge GPIO PWM pins
    # Set initial duty cycle to 0 and frequency to 1000
    driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
    driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

    # Initialise objects for H-Bridge digital GPIO pins
    boardInit = DigitalOutputDevice(MOTOR_BOARD_INIT)
    forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
    reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
    forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
    reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)

    def board_init(self):
        self.boardInit.value = 1

    def board_shutdown(self):
        self.boardInit.value = 0

    def all_stop(self, speed=1):
        self.forwardLeft.value = False
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = False
        self.driveLeft.value = 0 * speed
        self.driveRight.value = 0 * speed

    def forward(self, speed=1):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def reverse(self, speed=1):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def spin_left(self, speed=1):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def Spin_light(self, speed=1):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def forward_left(self, speed=1):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 0.2 * speed
        self.driveRight.value = 0.8 * speed

    def forward_right(self, speed=1):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 0.8 * speed
        self.driveRight.value = 0.2 * speed

    def reverse_left(self, speed=1):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 0.2 * speed
        self.driveRight.value = 0.8 * speed

    def reverse_right(self, speed=1):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 0.8 * speed
        self.driveRight.value = 0.2 * speed
