def switchDef(caseValue):
    def monday():
        print('i am from monday')
    def tuesday():
        print('i am from tuesday')
    def wednesday():
        print('i am from wednesday')
    def thursday():
        print('i am from thursday')
    def friday():
        print('i am from thursday')
    def saturday():
        print('i am from satudray')
    def sunday():
        print('i am form sunday')

    d1 = {
        1 : monday,
        2 : tuesday,
        3 : wednesday,
        4 : thursday,
        5 : friday,
        6 : saturday,
        7 : sunday
    }

    d1.get(caseValue)()

switchDef(3)

switchDef(1)

switchDef(7)

switchDef(2)