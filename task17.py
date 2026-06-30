class AnswerByCode:

    def __init__(self):
        self._answer_by_code = {}
        self._default_answer = {
            "status": "error",
            "client_message": "Произошла непредвиденная ситуация",
        }

    def set_default(self, answer):
        self._default_answer = answer

    def set(self, code, answer):
        self._answer_by_code[code] = answer

    def get(self, code):
        return self._answer_by_code.get(code, self._default_answer)
