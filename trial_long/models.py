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
    name_in_url = 'trial1'
    players_per_group = None
    num_rounds = 1

    income = [80, 115, 150, 185, 220, 255, 290, 325, 0, 0, 0, 0, 0, 0, 0, 0]
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
            player.participant.vars['total_saving_long1'] = 0

            for j in range(1, 17):
                str_income = 'income_long%s' % j
                str_expense = 'expense_long%s' % j
                player.participant.vars[str_income] = income_seq[j-1]
                setattr(player, str_income, income_seq[j-1])
                setattr(player, str_expense, expense_seq[j-1])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income_long1 = models.IntegerField(blank=True)
    income_long2 = models.IntegerField(blank=True)
    income_long3 = models.IntegerField(blank=True)
    income_long4 = models.IntegerField(blank=True)
    income_long5 = models.IntegerField(blank=True)
    income_long6 = models.IntegerField(blank=True)
    income_long7 = models.IntegerField(blank=True)
    income_long8 = models.IntegerField(blank=True)
    income_long9 = models.IntegerField(blank=True)
    income_long10 = models.IntegerField(blank=True)
    income_long11 = models.IntegerField(blank=True)
    income_long12 = models.IntegerField(blank=True)
    income_long13 = models.IntegerField(blank=True)
    income_long14 = models.IntegerField(blank=True)
    income_long15 = models.IntegerField(blank=True)
    income_long16 = models.IntegerField(blank=True)

    expense_long1 = models.IntegerField(blank=True)
    expense_long2 = models.IntegerField(blank=True)
    expense_long3 = models.IntegerField(blank=True)
    expense_long4 = models.IntegerField(blank=True)
    expense_long5 = models.IntegerField(blank=True)
    expense_long6 = models.IntegerField(blank=True)
    expense_long7 = models.IntegerField(blank=True)
    expense_long8 = models.IntegerField(blank=True)
    expense_long9 = models.IntegerField(blank=True)
    expense_long10 = models.IntegerField(blank=True)
    expense_long11 = models.IntegerField(blank=True)
    expense_long12 = models.IntegerField(blank=True)
    expense_long13 = models.IntegerField(blank=True)
    expense_long14 = models.IntegerField(blank=True)
    expense_long15 = models.IntegerField(blank=True)
    expense_long16 = models.IntegerField(blank=True)

    spend_long1 = models.IntegerField(blank=True)
    check_spend_long1 = models.IntegerField(blank=True)

    spend_long2 = models.IntegerField(blank=True)
    check_spend_long2 = models.IntegerField(blank=True)

    spend_long3 = models.IntegerField(blank=True)
    check_spend_long3 = models.IntegerField(blank=True)

    spend_long4 = models.IntegerField(blank=True)
    check_spend_long4 = models.IntegerField(blank=True)

    spend_long5 = models.IntegerField(blank=True)
    check_spend_long5 = models.IntegerField(blank=True)

    spend_long6 = models.IntegerField(blank=True)
    check_spend_long6 = models.IntegerField(blank=True)

    spend_long7 = models.IntegerField(blank=True)
    check_spend_long7 = models.IntegerField(blank=True)

    spend_long8 = models.IntegerField(blank=True)
    check_spend_long8 = models.IntegerField(blank=True)

    spend_long9 = models.IntegerField(blank=True)
    check_spend_long9 = models.IntegerField(blank=True)

    spend_long10 = models.IntegerField(blank=True)
    check_spend_long10 = models.IntegerField(blank=True)

    spend_long11 = models.IntegerField(blank=True)
    check_spend_long11 = models.IntegerField(blank=True)

    spend_long12 = models.IntegerField(blank=True)
    check_spend_long12 = models.IntegerField(blank=True)

    spend_long13 = models.IntegerField(blank=True)
    check_spend_long13 = models.IntegerField(blank=True)

    spend_long14 = models.IntegerField(blank=True)
    check_spend_long14 = models.IntegerField(blank=True)

    spend_long15 = models.IntegerField(blank=True)
    check_spend_long15 = models.IntegerField(blank=True)

    spend_long16 = models.IntegerField(blank=True)
    check_spend_long16 = models.IntegerField(blank=True)
