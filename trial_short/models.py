from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
from django.utils.translation import ugettext_lazy as _


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'trial0'
    players_per_group = None
    num_rounds = 1

    income = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 0, 0, 0, 0]
    expense = [20, 20, 30, 30, 30, 40, 40, 40, 50, 50, 50, 60, 60, 60, 70, 70]


class Subsession(BaseSubsession):
    def creating_session(self):
        income_seq = Constants.income.copy()
        expense_seq = Constants.expense.copy()
        for player in self.get_players():
            random.shuffle(expense_seq)
            player.participant.vars['expense_list'] = expense_seq
            player.participant.vars['start_text'] = _('Please tap and move on the slider below to indicate '
                                                      'how much you would like to spend in current Period')
            player.participant.vars['start_text_retire'] = _('You have just entered retirement in this period.')
            player.participant.vars['spend_text'] = _('You have less ')+'<b>'+_('Savings')+'</b>'+\
                                                    _(' than you need to cover your ')+'<b>'+_('Expenses')+'</b>'+\
                                                    _(' this turn. You are in debt and will not make any ')+'<b>'+\
                                                    _('Spending')+'</b>'+_(' decision.')
            player.participant.vars['total_saving1'] = 0

            for j in range(1, 17):
                str_income = 'income%s' % j
                str_expense = 'expense%s' % j
                player.participant.vars[str_income] = income_seq[j-1]
                setattr(player, str_income, income_seq[j-1])
                setattr(player, str_expense, expense_seq[j-1])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income1 = models.IntegerField(blank=True)
    income2 = models.IntegerField(blank=True)
    income3 = models.IntegerField(blank=True)
    income4 = models.IntegerField(blank=True)
    income5 = models.IntegerField(blank=True)
    income6 = models.IntegerField(blank=True)
    income7 = models.IntegerField(blank=True)
    income8 = models.IntegerField(blank=True)
    income9 = models.IntegerField(blank=True)
    income10 = models.IntegerField(blank=True)
    income11 = models.IntegerField(blank=True)
    income12 = models.IntegerField(blank=True)
    income13 = models.IntegerField(blank=True)
    income14 = models.IntegerField(blank=True)
    income15 = models.IntegerField(blank=True)
    income16 = models.IntegerField(blank=True)

    expense1 = models.IntegerField(blank=True)
    expense2 = models.IntegerField(blank=True)
    expense3 = models.IntegerField(blank=True)
    expense4 = models.IntegerField(blank=True)
    expense5 = models.IntegerField(blank=True)
    expense6 = models.IntegerField(blank=True)
    expense7 = models.IntegerField(blank=True)
    expense8 = models.IntegerField(blank=True)
    expense9 = models.IntegerField(blank=True)
    expense10 = models.IntegerField(blank=True)
    expense11 = models.IntegerField(blank=True)
    expense12 = models.IntegerField(blank=True)
    expense13 = models.IntegerField(blank=True)
    expense14 = models.IntegerField(blank=True)
    expense15 = models.IntegerField(blank=True)
    expense16 = models.IntegerField(blank=True)

    spend1 = models.IntegerField(blank=True)
    check_spend1 = models.IntegerField(blank=True)

    spend2 = models.IntegerField(blank=True)
    check_spend2 = models.IntegerField(blank=True)

    spend3 = models.IntegerField(blank=True)
    check_spend3 = models.IntegerField(blank=True)

    spend4 = models.IntegerField(blank=True)
    check_spend4 = models.IntegerField(blank=True)

    spend5 = models.IntegerField(blank=True)
    check_spend5 = models.IntegerField(blank=True)

    spend6 = models.IntegerField(blank=True)
    check_spend6 = models.IntegerField(blank=True)

    spend7 = models.IntegerField(blank=True)
    check_spend7 = models.IntegerField(blank=True)

    spend8 = models.IntegerField(blank=True)
    check_spend8 = models.IntegerField(blank=True)

    spend9 = models.IntegerField(blank=True)
    check_spend9 = models.IntegerField(blank=True)

    spend10 = models.IntegerField(blank=True)
    check_spend10 = models.IntegerField(blank=True)

    spend11 = models.IntegerField(blank=True)
    check_spend11 = models.IntegerField(blank=True)

    spend12 = models.IntegerField(blank=True)
    check_spend12 = models.IntegerField(blank=True)

    spend13 = models.IntegerField(blank=True)
    check_spend13 = models.IntegerField(blank=True)

    spend14 = models.IntegerField(blank=True)
    check_spend14 = models.IntegerField(blank=True)

    spend15 = models.IntegerField(blank=True)
    check_spend15 = models.IntegerField(blank=True)

    spend16 = models.IntegerField(blank=True)
    check_spend16 = models.IntegerField(blank=True)
