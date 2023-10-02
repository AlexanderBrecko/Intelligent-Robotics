from controller import Robot

robot = Robot()
timestep = int(64)

motor_one = robot.getDevice('motor5')
motor_two = robot.getDevice('motor6')

motor_one.setVelocity(0)
motor_two.setVelocity(0)

motor_one.setPosition(0)
motor_two.setPosition(0)


while robot.step(timestep) != -1:
    motor_one.setPosition(1)
    motor_one.setVelocity(5)
    
    motor_two.setPosition(1)
    motor_two.setVelocity(5)
