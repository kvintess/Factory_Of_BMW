class Bmw:

    def __init__(self):
        self.color = 'черный'
        self.price = '3000000 руб.'
        self.engine_rpm = 0
        self.current_velocity = 0
        self.max_velocity = 300

    def start(self):
        print('мотор запущен')
        self.engine_rpm = 900

    def go(self):
        print('поехали!')
        self.engine_rpm = 2000
        self.current_velocity = 20
