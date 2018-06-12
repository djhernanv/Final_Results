from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# The app will be shown only after ALL participants have finished to avoid them leaving early etc.


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    ResultsWaitPage,
    Results
]
