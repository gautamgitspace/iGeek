# pseudo code for Employee Card Reader System

import random
#VALIDATES AN EXISTING EMPLOYEE
def validate_user(employee, request):
    existingChipCode = DB.get(request.data.uniqueChipCode)
    if existingChipCode:
        fp = DB.get(request.data.finger)
        if fp:
            DB.insert('EmployeeActivity', {userID : employee.userID, timestamp : system.getLocalTimeStamp(), area_code : system.getAreaCode(), direction : sensor.getDirection()})
            system.sendTrap('OPEN DOOR')
            sensor.flashLED('GREEN')
        if not fp:
            DB.insert('Log', {unauthorized_flag_fp : true, employee.userID : userID, timestamp.getLocalTimeStamp, area_code : system.getAreaCode()}, direction : sensor.getDirection()})
            sensor.flashLED('RED')
    if not existingChipCode:
        DB.insert('Log', {unauthorized_flag_chip : true, timestamp.getLocalTimeStamp, area_code : system.getAreaCode()}, direction : sensor.getDirection()})
        sensor.flashLED('RED')

#ADDS A NOOGLER TO THE SYSTEM
def add_noogler(employee):
    uniqueChipCode = randomSlug()
    DB.insert('EmployeeTable', {userID : employee.userID, userName: employee.userName, uniqueChipCode : uniqueChipCode})
    burnToCard(employee, uniqueChipCode)

#BURN CODE TO CARD - EMPLOYEE
def burnToCard(employee, uniqueChipCode):
    card.burn(uniqueChipCode)

#BURN CODE TO CARD - VISITOR
def burnToCard(visitor, randomTempCode):
    card.burn(randomTempCode)

#GENERATEES RANDOM SLUG OF 7 CHARS
def randomSlug():
    passphrase = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    slug = ''.join([random.choice(passphrase) for x in range(7)])
    slug_comparator = DB.get(slug)
    if not slug_comparator:
        return slug
    else:
        randomSlug()

#ADD A NEW VISITOR
def visitor(visitor):
    randomTempCode = randomSlug()
    DB.insert('VisitorTable', {timestamp : system.getLocalTimeStamp(), visitorRandomCode: randomTempCode})
    burnToCard(visitor, randomTempCode)




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
