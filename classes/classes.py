from datetime import datetime


class Operation:

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.date = kwargs.get('date')
        self.state = kwargs.get('state')
        self.cash = kwargs.get('operationAmount').get('amount')
        self.code = kwargs.get('operationAmount').get('currency')['code']
        self.description = kwargs.get('description')
        self.from_: str = kwargs.get('from')
        self.to = kwargs.get('to')

    def format_date(self):
        """Переводит дату в нужный формат"""
        self.date = self.date[8:10] + '.' + self.date[5:7] + '.' + self.date[:4]

    @staticmethod
    def format_card(data):
        """"""
        if data and data.startswith('Счет'):
            return 'Счет ' + '**' + data[-4:]
        elif data is None:
            return None
        else:
            return data[:-12] + ' ' + data[-14:-12] + '** **** ' + data[-4:]

    def choice(self):
        self.from_ = self.format_card(self.from_)
        self.to = self.format_card(self.to)

    def beautiful_output(self):
        """ывод в требуемом формате"""
        print(f"""
            {self.date}  {self.description}
            {self.from_ if self.from_ else ""} -> {self.to}
            {self.cash} {self.code}
        """)

    def __str__(self):
        return (f'{self.id}, {self.date},{self.state}, '
                f'{self.description}'
                f'{self.from_}, {self.to}')
