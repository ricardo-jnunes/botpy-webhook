from chatterbot.logic import LogicAdapter
from bot.validations import dynatrace_monitor as dt
from chatterbot.conversation import Statement

class EnvironmentLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['ambiente', 'ambiente?', "Ambiente"]
        if any(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        data = dt.get_environment_data()

        # Let's base the confidence value on if the request was successful
        if isinstance(data, str):
            response_statement = Statement(text='O pico mais alto de thread é {}'.format(data))
            response_statement.confidence = 1
        else:
            response_statement = Statement(text='Ocorreu erro ao validar o ambiente.')
            response_statement.confidence = 0

        return response_statement
        