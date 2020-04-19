from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice


class MotorController:

    # Motor controller board initialisation GPIO CONSTANTS
    MOTOR_BOARD_INIT = 12
    # Motor A, Left Side GPIO CONSTANTS
    PWM_DRIVE_LEFT = 16  # ENA - H-Bridge enable pin
    FORWARD_LEFT_PIN = 20  # IN1 - Forward Drive
    REVERSE_LEFT_PIN = 21  # IN2 - Reverse Drive
    # Motor B, Right Side GPIO CONSTANTS
    PWM_DRIVE_RIGHT = 13  # ENB - H-Bridge enable pin
    FORWARD_RIGHT_PIN = 19  # IN1 - Forward Drive
    REVERSE_RIGHT_PIN = 26  # IN2 - Reverse Drive

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
        print("motor.board_init triggered")
        self.boardInit.value = 1

    def board_shutdown(self):
        print("motor.board_shutdown triggered")
        self.boardInit.value = 0

    def all_stop(self):
        print("Motor.all_stop triggered")
        self.forwardLeft.value = False
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = False
        self.driveLeft.value = 0
        self.driveRight.value = 0

    def forward(self, speed=1):
        print("Motor.forward triggered with speed = " + str(speed))
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def reverse(self, speed=1):
        print("Motor.reverse triggered with speed = " + str(speed))
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def spin_left(self, speed=1):
        print("Motor.spin_left triggered with speed = " + str(speed))
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def spin_right(self, speed=1):
        print("Motor.Spin_right triggered with speed = " + str(speed))
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1.0 * speed
        self.driveRight.value = 1.0 * speed

    def forward_left(self, speed=1):
        print("Motor.forward_left triggered with speed = " + str(speed))
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 0.2 * speed
        self.driveRight.value = 0.8 * speed

    def forward_right(self, speed=1):
        print("Motor.forward_right triggered with speed = " + str(speed))
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 0.8 * speed
        self.driveRight.value = 0.2 * speed

    def reverse_left(self, speed=1):
        print("Motor.reverse_left triggered with speed = " + str(speed))
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 0.2 * speed
        self.driveRight.value = 0.8 * speed

    def reverse_right(self, speed=1):
        print("Motor.reverse_right triggered with speed = " + str(speed))
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 0.8 * speed
        self.driveRight.value = 0.2 * speed
