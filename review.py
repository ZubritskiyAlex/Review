import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # TODO: self.date = ... можно разместить таким образом
        self.date = (
            dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        )
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # TODO: Стоит заменить Record -> record
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # TODO: здесь ты можешь упростить сравнение таким образом  7 > (today - record.date).days >= 0
            # или до условия, в теле цикла, создать переменную
            # day_number = (today - record.date).days и использовать для сравнения ее
            # 7 > day_number >= 0:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # TODO: комментарии к методам стоит удалить и заменить на docstrings,
    #  там где это необходимо как я сделал в get_today_cash_remained,
    #  также подумай над тем чтобы переименовать метод в get_today_calories_remained

    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:

            # TODO: Пожалуйста не используй бэкслеши для переносов
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # TODO: Здесь следует удалить else и сдвинуть return('Хватит есть!') на один уровень с if x > 0:
        #  так как ты используешь return
        else:
            # TODO: Здесь следует удалить скобки  return 'Хватит есть!'
            return('Хватит есть!')


class CashCalculator(Calculator):

    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # TODO: название аргументов следует писать маленькими буквами: usd_rate=USD_RATE, euro_rate=EURO_RATE
    def get_today_cash_remained(self, currency: str, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE) -> str:
        """
        Вычисляет остаток на балансе.
        :param currency: str
        :param USD_RATE: float
        :param EURO_RATE: float
        :return: str
        """
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # TODO: Обрати внимание на строку ниже здесь ты устанавливаешь cash_remained равным единице если валюта руб
            #  вместо того чтобы делить на единицу так как не нужно переводить это необходимо исправить
            #  можешь добавить RUB_RATE как поле класса, как ты делал с EURO_RATE и USD_RATE или изменить так
            #  cash_remained /= 1 или cash_remained = cash_remained в этом действии нет смысла поэтому лучше всего
            #  просто удалить эту строку  cash_remained == 1.00 так как перевод из рублей в рубли не нужен
            #  также почитай когда используется == а когда, =
            #  cash_remained == 1.00 будет возвращать только True or False
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # TODO: Пожалуйста не используй бэкслеши для переносов
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        super().get_week_stats()
# TODO: пожалуйста добавь пустую строку после последней строки с кодом в файле :)
# TODO: Пожалуйста разделяй блоки логики пустыми строками например в методе get_today_cash_remained
#  стоит добавить пустую строку после объявления cash_remained и также отделать блоки условий,
#  чтобы это все не сливалось и твоим коллегам было удобнее читать код :)
# TODO: Подумай над тем, чтобы добавить аннотацию типов
#  как в get_today_cash_remained(self, currency: str, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE) -> str:
#  также будет полезно почитать о модуле Typing

# TODO: Советы:
#   в выражениях типа for iter in some_collection слудует использовать маленькую букву
#   если ты используешь одно и тоже для сравнения в нескольких местах, стоит создать для этого отдельную переменную
#   и использовать ее вместо того чтобы вычислять одно и то же несколько раз как здесь if (
#                 (today - record.date).days < 7 and
#                 (today - record.date).days >= 0
#             ):
#   вместо комментариев к функциям используй docstrings, также следует использовать аннотацию типов и познакомиться
#   с модулем Typing
#   Не используй бэкслеши для переноса
#   Нет используй лишних else там, где они не нужны (если в if происходит return/raise); используется Guard Block.
#   Повтори в чем разница между = и ==, также полезно будет почитать про разницу между is и ==
#   Успехов!
#
#

print("Hello world!")

