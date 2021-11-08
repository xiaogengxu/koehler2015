from otree.api import Currency as c, currency_range
from .models import Constants
from ._builtin import Page as oTreePage, WaitPage
import datetime
from .generic_pages import Page
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import random, time


class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['consent'] == 'yes'

    def quiz1_choices(player):
        choices = [['expenses', _('Expenses')], ['income', _('Income')], ['spending', _('Spending')]]
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['expense_zero', _('Expenses are zero.')], ['income_zero', _('Income is zero.')],
                   ['no_spending', _('Spending is not allowed or possible.')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = [['expense_deducted',
                    _('Expenses are deducted from my Income or Savings, limiting my maximum Spending')],
                   ['expense_increase', _('Expenses increase my Savings automatically')],
                   ['expense_added', _('Expenses are added to my Income and increase maximum Spending')]]
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['less_saving', _('During retirement when you have less Savings than Expenses')],
                   ['zero_expense', _('During employment when you have zero Expenses')],
                   ['spend_higher', _('During retirement when your Spending is higher than your Income')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['end_life', _('Savings points at the end of one life (as selected by a computer).')],
                   ['one_life', _('Spending points in one period of one life (as selected by a computer).')],
                   ['all_life', _('Average Expense points for all periods in all lives.')]]
        random.shuffle(choices)
        return choices

    def error_message(self, values):
        if not values['quiz1'] or not values['quiz2'] or not values['quiz3'] or not values['quiz4'] \
                or not values['quiz5']:
            return _('Please answer all questions.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {
            'lang': lang
        }

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60
        if self.player.quiz1 and self.player.quiz2 and self.player.quiz3 and self.player.quiz4 and self.player.quiz5:
            if self.player.quiz1 != 'spending':
                self.participant.vars['mis_q1'] = 1
                self.player.quiz1 = ''
            if self.player.quiz2 != 'income_zero':
                self.participant.vars['mis_q2'] = 1
                self.player.quiz2 = ''
            if self.player.quiz3 != 'expense_deducted':
                self.participant.vars['mis_q3'] = 1
                self.player.quiz3 = ''
            if self.player.quiz4 != 'less_saving':
                self.participant.vars['mis_q4'] = 1
                self.player.quiz4 = ''
            if self.player.quiz5 != 'one_life':
                self.participant.vars['mis_q5'] = 1
                self.player.quiz5 = ''


class End_attempt1(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']
        return sum_mistake > 2 and self.participant.vars['time_instruction'] >= 30 and self.participant.vars['consent'] == 'yes'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73953&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_retry(Page):
    form_model = 'player'

    def get_form_fields(self):
        formfield_list = []
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']
        if sum_mistake < 3:
            if self.participant.vars['mis_q1'] == 1:
                formfield_list.append('quiz1')
            if self.participant.vars['mis_q2'] == 1:
                formfield_list.append('quiz2')
            if self.participant.vars['mis_q3'] == 1:
                formfield_list.append('quiz3')
            if self.participant.vars['mis_q4'] == 1:
                formfield_list.append('quiz4')
            if self.participant.vars['mis_q5'] == 1:
                formfield_list.append('quiz5')
        return formfield_list

    def quiz1_choices(player):
        choices = [['expenses', _('Expenses')], ['income', _('Income')], ['spending', _('Spending')]]
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['expense_zero', _('Expenses are zero.')], ['income_zero', _('Income is zero.')],
                   ['no_spending', _('Spending is not allowed or possible.')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = [['expense_deducted',
                    _('Expenses are deducted from my Income or Savings, limiting my maximum Spending')],
                   ['expense_increase', _('Expenses increase my Savings automatically')],
                   ['expense_added', _('Expenses are added to my Income and increase maximum Spending')]]
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['less_saving', _('During retirement when you have less Savings than Expenses')],
                   ['zero_expense', _('During employment when you have zero Expenses')],
                   ['spend_higher', _('During retirement when your Spending is higher than your Income')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['end_life', _('Savings points at the end of one life (as selected by a computer).')],
                   ['one_life', _('Spending points in one period of one life (as selected by a computer).')],
                   ['all_life', _('Average Expense points for all periods in all lives.')]]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']
        return sum_mistake != 0 and sum_mistake < 3 and self.participant.vars['time_instruction'] >= 30 and self.participant.vars['consent'] == 'yes'

    def error_message(self, values):
        if (self.participant.vars['mis_q1'] == 1 and not values['quiz1']) or \
                (self.participant.vars['mis_q2'] == 1 and not values['quiz2']) or \
                (self.participant.vars['mis_q3'] == 1 and not values['quiz3']) or \
                (self.participant.vars['mis_q4'] == 1 and not values['quiz4']) or \
                (self.participant.vars['mis_q5'] == 1 and not values['quiz5']):
            return _('Please answer the question.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        if self.participant.vars['mis_q1'] == 1:
            show1 = 1
        else:
            show1 = 0

        if self.participant.vars['mis_q2'] == 1:
            show2 = 1
        else:
            show2 = 0

        if self.participant.vars['mis_q3'] == 1:
            show3 = 1
        else:
            show3 = 0

        if self.participant.vars['mis_q4'] == 1:
            show4 = 1
        else:
            show4 = 0

        if self.participant.vars['mis_q5'] == 1:
            show5 = 1
        else:
            show5 = 0

        return {
            'lang': lang,
            'show1': show1,
            'show2': show2,
            'show3': show3,
            'show4': show4,
            'show5': show5
        }

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60

        if self.participant.vars['mis_q1'] == 1:
            if self.player.quiz1 == 'spending':
                self.participant.vars['mis_q1'] = 0

        if self.participant.vars['mis_q2'] == 1:
            if self.player.quiz2 == 'income_zero':
                self.participant.vars['mis_q2'] = 0

        if self.participant.vars['mis_q3'] == 1:
            if self.player.quiz3 == 'expense_deducted':
                self.participant.vars['mis_q3'] = 0

        if self.participant.vars['mis_q4'] == 1:
            if self.player.quiz4 == 'less_saving':
                self.participant.vars['mis_q4'] = 0

        if self.participant.vars['mis_q5'] == 1:
            if self.player.quiz5 == 'one_life':
                self.participant.vars['mis_q5'] = 0


class End_attempt2(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']
        return sum_mistake != 0 and self.participant.vars['time_instruction'] >= 30 and self.participant.vars['consent'] == 'yes'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73953&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


page_sequence = [Quiz, End_attempt1, Quiz_retry, End_attempt2]
