from dataclasses import dataclass


@dataclass
class Status:

    NEW = 'NEW'          # Активное. требует изменения на INPR
    IN_PROCESS = 'INPR'  # Активное. требует изменения на: FAIL или SCS
    SUCCESS = 'SCS'      # Активное. блокирует создание нового события
    FAILURE = 'FAIL'     # Активное. блокирует создание нового события
    ERROR = 'ERROR'      # Активное. Последнее событие завершилось ситемной ошибкой, бизнес-результат не известен
    CANCEL = 'CANCEL'    # Не активно. Отменяет предыдущий статус. В comment пишется предыдущий статус

    status: str
    comment: any

    def __init__(self, status, comment=None):
        assert status in [
            self.NEW,
            self.IN_PROCESS,
            self.SUCCESS,
            self.FAILURE,
            self.ERROR,
            self.CANCEL
        ], 'Wrong status'
        self.status = status
        self.comment = comment
