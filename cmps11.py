##cmps11 Lib by jensum, 30.11.16
import smbus

##Register	 Function
##0			    Command register (write) / Software version (read)
##1			    Compass Bearing 8 bit, i.e. 0-255 for a full circle
##2,3		    Compass Bearing 16 bit, i.e. 0-3599, representing 0-359.9 degrees. register 2 being the high byte
##4			    Pitch angle - signed byte giving angle in degrees from the horizontal plane, Kalman filtered with Gyro
##5			    Roll angle - signed byte giving angle in degrees from the horizontal plane, Kalman filtered with Gyro
##6,7		    Magnetometer X axis raw output, 16 bit signed integer with register 6 being the upper 8 bits
##8,9		    Magnetometer Y axis raw output, 16 bit signed integer with register 8 being the upper 8 bits
##10,11		Magnetometer Z axis raw output, 16 bit signed integer with register 10 being the upper 8 bits
##12,13		Accelerometer  X axis raw output, 16 bit signed integer with register 12 being the upper 8 bits
##14,15		Accelerometer  Y axis raw output, 16 bit signed integer with register 14 being the upper 8 bits
##16,17		Accelerometer  Z axis raw output, 16 bit signed integer with register 16 being the upper 8 bits
##18,19		Gyro X axis raw output, 16 bit signed integer with register 18 being the upper 8 bits
##20,21		Gyro  Y axis raw output, 16 bit signed integer with register 20 being the upper 8 bits
##22,23		Gyro Z axis raw output, 16 bit signed integer with register 22 being the upper 8 bits
##24,25		Temperature raw output, 16 bit signed integer with register 24 being the upper 8 bits
##26		    Pitch angle - signed byte giving angle in degrees from the horizontal plane (no Kalman filter)
##27		    Roll angle - signed byte giving angle in degrees from the horizontal plane (no Kalman filter)


### Vars / Init Bereich
bus = smbus.SMBus(1)
address = 0x60
table_String= '<table style="width:100%"> '\
    '<tr>'\
    '<th>ID</th>'\
    '<th>CompassHeading</th>'\
    '<th>GyroX</th> '\
    '<th>GyroY</th>'\
    '<th>GyroZ</th>'\
    '<th>Roll</th>'\
    '<th>Pitch</th>'\
    '<th>Temp</th>'\
    '</tr>'

id = 1

def bearing():
        bear1 = bus.read_byte_data(address, 2)
        bear2 = bus.read_byte_data(address, 3)
        bear = (bear1 << 8) + bear2
        bear = bear/10.0
        return bear

def getGyroX():
        x1 = bus.read_byte_data(address, 18) #higher bits
        x2 = bus.read_byte_data(address, 19)
        x = (x1 << 8) + x2
        return x
        
def getGyroY():
        y1 = bus.read_byte_data(address, 20) #higher bits
        y2 = bus.read_byte_data(address, 21)
        y = (y1 << 8) + y2
        return y
        
def getGyroZ():
        z1 = bus.read_byte_data(address, 22) #higher bits
        z2 = bus.read_byte_data(address, 23)
        z= (z1 << 8) + z2
        return z
        
def getTemp():
        t1 = bus.read_byte_data(address, 24) #higher bits
        t2 = bus.read_byte_data(address, 25)
        t= (t1 << 8) + t2
        return t

def getPitch():
    pit = bus.read_byte_data(address, 26)
    return pit
    
def getRoll():
    roll = bus.read_byte_data(address, 27)
    return roll


def getSensorData():
    global table_String
    global id
    s ="<tr>"
    s += "<td>" + str(id) +"</td> "
    s += "<td>" + str(bearing()) +"</td> "
    s += "<td>" +str(getGyroX()) +"</td> "
    s += "<td>" +str(getGyroY()) +"</td> "
    s +=  "<td>" +str(getGyroZ()) +"</td> "
    s += "<td>" + str(getPitch()) +"</td> "
    s += "<td>" + str(getRoll()) +"</td> "
    s += "<td>" + str(getTemp()) +"</td> "
    s += "</tr>"
    id +=1
    table_String += s
    return table_String 
