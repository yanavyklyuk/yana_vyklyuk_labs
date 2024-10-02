class Status:
    valid_status_names = ['scheduled', 'cancelled', 'happend']
    def __init__(self, status_name):
        if not self.is_valid_status_name(status_name):
            raise ValueError(f'Invalid status name: {status_name}')
        self.__status_name = status_name.lower()

    @property
    def status_name(self):
        return self.__status_name

    @status_name.setter
    def status_name(self, status_name):
        if self.is_valid_status_name(status_name):
            self.__status_name = status_name.lower()
        else:
            raise ValueError(f'Invalid status name: {status_name}')

    def is_valid_status_name(self, status_name):
        return status_name.lower() in self.valid_status_names
