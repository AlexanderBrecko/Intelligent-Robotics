
from controller import Robot
from controller import DistanceSensor, Camera

if __name__ == "__main__":

    robot = Robot()
    
    timestep = int(64)
    max_speed = 6.28
    
    motor_1 = robot.getDevice('motor1')
    motor_2 = robot.getDevice('motor2')
    motor_3 = robot.getDevice('motor3')
    motor_4 = robot.getDevice('motor4')
    
    motor_1.setPosition(float('inf'))
    motor_1.setVelocity(0.0)
    
    motor_2.setPosition(float('inf'))
    motor_2.setVelocity(0.0)
    
    motor_3.setPosition(float('inf'))
    motor_3.setVelocity(0.0)
    
    motor_4.setPosition(float('inf'))
    motor_4.setVelocity(0.0)
    
    ds_1 = robot.getDevice('ds1')
    ds_1.enable(timestep)
    
    ds_2 = robot.getDevice('ds2')
    ds_2.enable(timestep)
    
    ds_3 = robot.getDevice('ds3')
    ds_3.enable(timestep)
    
    ds_4 = robot.getDevice('ds4')
    ds_4.enable(timestep)
    
    camera = robot.getDevice('camera')
    camera.enable(timestep)
    
    
    ds_value = [0,0,0,0]
    image = []
    
    led = robot.getDevice('led')
    
    
    while robot.step(timestep) != -1:
        
        left_speed = 0.3 * max_speed
        right_speed = max_speed
        
        motor_1.setVelocity(left_speed)
        motor_2.setVelocity(left_speed)
        motor_3.setVelocity(left_speed)
        motor_4.setVelocity(left_speed)
        
        ds_value[0] = ds_1.getValue()
        ds_value[1] = ds_2.getValue()
        ds_value[2] = ds_3.getValue()
        ds_value[3] = ds_4.getValue()

        print("---------------------")
        print("Distance senzor values:{} {} {} {}".format(ds_value[0],ds_value[1], ds_value[2], ds_value[3])) 
        
        
        image = camera.getImageArray()
        camera.getImage()
        if image:
            for x in range(0, camera.getWidth()):
                for y in range(0, camera.getHeight()):
                    red = image[x][y][0]
                    green = image[x][y][1]
                    blue = image[x][y][2]
                    print('r='+ str(red) + ' g=' + str(green) + ' b= ' + str(blue))   
    
        led.set(1)
       
    
    
