# pseudo code for Employee Card Reader System
def validate_user(request):
    existingChipCode = DB.get(request.data.uniqueChipCode)
    if existingChipCode:
        fp = DB.get(request.data.finger)
        if fp:
            DB.insert('Employee', {userID : userID, timestamp : system.getLocalTimeStamp(), area_code : system.getAreaCode(), direction : sensor.getDirection()})
            system.sendTrap('OPEN DOOR')
            sensor.flashLED('GREEN')
        if not fp:
            DB.insert('Log', {unauthorized_flag_fp : true, userID : userID, timestamp.getLocalTimeStamp, area_code : system.getAreaCode()}, direction : sensor.getDirection()})
            sensor.flashLED('RED')
    if not existingChipCode:
        DB.insert('Log', {unauthorized_flag_chip : true, userID : userID, timestamp.getLocalTimeStamp, area_code : system.getAreaCode()}, direction : sensor.getDirection()})
        sensor.flashLED('RED')

#SCOPE
"""
Employee count = 2000 in New York Office
Scanners per floor = 200
Floor count = 5
Total scanners = 1000
Maximum scans at a time = all scanners busy = 1000
"""

#ABSTRACT DESIGN //TODO
"""
Scanner, dispatcher(load balancer), worker pool, DB
#Requirements:
1. Authentication for Employee
2. Add a new legitimite employee
3. Tokens for visitor
"""

#BOTTLENECKS
"""
All scanners busy, people move in and out all the time.
"""

#SCALABILITY
"""
Dispatcher balancing load for incoming requests to DB access
"""
