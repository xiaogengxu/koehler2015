from otree.api import Currency as c, currency_range
from .models import Constants
from ._builtin import Page as oTreePage, WaitPage
import datetime
from .generic_pages import Page
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Start(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60


class Period1(Page):
    form_model = 'player'
    form_fields = ['spend1', 'check_spend1']

    def error_message(self, values):
        if not values['check_spend1']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        period = 1
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(2, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        total_saving1 = self.participant.vars['total_saving1']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'total_saving1': total_saving1,
        }

    def before_next_page(self):
        self.participant.vars['spend1'] = self.player.spend1
        self.participant.vars['total_saving2'] = self.participant.vars['total_saving1'] + \
                                                      self.participant.vars['income1'] - \
                                                      self.player.expense1 - \
                                                      self.participant.vars['spend1']


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend2', 'check_spend2']

    def error_message(self, values):
        if not values['check_spend2']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 2
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving2 = self.participant.vars['total_saving2']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving2': total_saving2,
        }

    def before_next_page(self):
        self.participant.vars['spend2'] = self.player.spend2
        self.participant.vars['total_saving3'] = self.participant.vars['total_saving2'] + \
                                                      self.participant.vars['income2'] - \
                                                      self.player.expense2 - \
                                                      self.participant.vars['spend2']


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend3', 'check_spend3']

    def error_message(self, values):
        if not values['check_spend3']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 3
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving3 = self.participant.vars['total_saving3']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving3': total_saving3,
        }

    def before_next_page(self):
        self.participant.vars['spend3'] = self.player.spend3
        self.participant.vars['total_saving4'] = self.participant.vars['total_saving3'] + \
                                                      self.participant.vars['income3'] - \
                                                      self.player.expense3 - \
                                                      self.participant.vars['spend3']


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend4', 'check_spend4']

    def error_message(self, values):
        if not values['check_spend4']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 4
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving4 = self.participant.vars['total_saving4']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving4': total_saving4,
        }

    def before_next_page(self):
        self.participant.vars['spend4'] = self.player.spend4
        self.participant.vars['total_saving5'] = self.participant.vars['total_saving4'] + \
                                                      self.participant.vars['income4'] - \
                                                      self.player.expense4 - \
                                                      self.participant.vars['spend4']


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend5', 'check_spend5']

    def error_message(self, values):
        if not values['check_spend5']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 5
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving5 = self.participant.vars['total_saving5']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving5': total_saving5,
        }

    def before_next_page(self):
        self.participant.vars['spend5'] = self.player.spend5
        self.participant.vars['total_saving6'] = self.participant.vars['total_saving5'] + \
                                                      self.participant.vars['income5'] - \
                                                      self.player.expense5 - \
                                                      self.participant.vars['spend5']


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend6', 'check_spend6']

    def error_message(self, values):
        if not values['check_spend6']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 6
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving6 = self.participant.vars['total_saving6']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving6': total_saving6,
        }

    def before_next_page(self):
        self.participant.vars['spend6'] = self.player.spend6
        self.participant.vars['total_saving7'] = self.participant.vars['total_saving6'] + \
                                                      self.participant.vars['income6'] - \
                                                      self.player.expense6 - \
                                                      self.participant.vars['spend6']


class Period7(Page):
    form_model = 'player'
    form_fields = ['spend7', 'check_spend7']

    def error_message(self, values):
        if not values['check_spend7']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 7
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving7 = self.participant.vars['total_saving7']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving7': total_saving7,
        }

    def before_next_page(self):
        self.participant.vars['spend7'] = self.player.spend7
        self.participant.vars['total_saving8'] = self.participant.vars['total_saving7'] + \
                                                      self.participant.vars['income7'] - \
                                                      self.player.expense7 - \
                                                      self.participant.vars['spend7']


class Period8(Page):
    form_model = 'player'
    form_fields = ['spend8', 'check_spend8']

    def error_message(self, values):
        if not values['check_spend8']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 8
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving8 = self.participant.vars['total_saving8']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving8': total_saving8,
        }

    def before_next_page(self):
        self.participant.vars['spend8'] = self.player.spend8
        self.participant.vars['total_saving9'] = self.participant.vars['total_saving8'] + \
                                                      self.participant.vars['income8'] - \
                                                      self.player.expense8 - \
                                                      self.participant.vars['spend8']


class Period9(Page):
    form_model = 'player'
    form_fields = ['spend9', 'check_spend9']

    def error_message(self, values):
        if not values['check_spend9']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 9
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving9 = self.participant.vars['total_saving9']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving9': total_saving9,
        }

    def before_next_page(self):
        self.participant.vars['spend9'] = self.player.spend9
        self.participant.vars['total_saving10'] = self.participant.vars['total_saving9'] + \
                                                      self.participant.vars['income9'] - \
                                                      self.player.expense9 - \
                                                      self.participant.vars['spend9']


class Period10(Page):
    form_model = 'player'
    form_fields = ['spend10', 'check_spend10']

    def error_message(self, values):
        if not values['check_spend10']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 10
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving10 = self.participant.vars['total_saving10']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving10': total_saving10,
        }

    def before_next_page(self):
        self.participant.vars['spend10'] = self.player.spend10
        self.participant.vars['total_saving11'] = self.participant.vars['total_saving10'] + \
                                                      self.participant.vars['income10'] - \
                                                      self.player.expense10 - \
                                                      self.participant.vars['spend10']


class Period11(Page):
    form_model = 'player'
    form_fields = ['spend11', 'check_spend11']

    def error_message(self, values):
        if not values['check_spend11']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 11
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving11 = self.participant.vars['total_saving11']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving11': total_saving11,
        }

    def before_next_page(self):
        self.participant.vars['spend11'] = self.player.spend11
        self.participant.vars['total_saving12'] = self.participant.vars['total_saving11'] + \
                                                      self.participant.vars['income11'] - \
                                                      self.player.expense11 - \
                                                      self.participant.vars['spend11']


class Period12(Page):
    form_model = 'player'
    form_fields = ['spend12', 'check_spend12']

    def error_message(self, values):
        if not values['check_spend12']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 12
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving12 = self.participant.vars['total_saving12']
        return {
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving12': total_saving12,
        }

    def before_next_page(self):
        self.participant.vars['spend12'] = self.player.spend12
        self.participant.vars['total_saving13'] = self.participant.vars['total_saving12'] + \
                                                      self.participant.vars['income12'] - \
                                                      self.player.expense12 - \
                                                      self.participant.vars['spend12']


class Period13(Page):
    form_model = 'player'
    form_fields = ['spend13', 'check_spend13']

    def error_message(self, values):
        if not values['check_spend13']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        start_text_retire = self.participant.vars['start_text_retire']
        spend_text = self.participant.vars['spend_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 13
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving13 = self.participant.vars['total_saving13']
        return {
            'start_text': start_text,
            'start_text_retire': start_text_retire,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving13': total_saving13,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving13'] <= 0:
            self.participant.vars['spend13'] = 0
        else:
            self.participant.vars['spend13'] = self.player.spend13
        self.participant.vars['total_saving14'] = self.participant.vars['total_saving13'] + \
                                                      self.participant.vars['income13'] - \
                                                      self.player.expense13 - \
                                                      self.participant.vars['spend13']


class Period14(Page):
    form_model = 'player'
    form_fields = ['spend14', 'check_spend14']

    def error_message(self, values):
        if not values['check_spend14']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        spend_text = self.participant.vars['spend_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 14
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving14 = self.participant.vars['total_saving14']
        return {
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving14': total_saving14,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving14'] <= 0:
            self.participant.vars['spend14'] = 0
        else:
            self.participant.vars['spend14'] = self.player.spend14
        self.participant.vars['total_saving15'] = self.participant.vars['total_saving14'] + \
                                                      self.participant.vars['income14'] - \
                                                      self.player.expense14 - \
                                                      self.participant.vars['spend14']


class Period15(Page):
    form_model = 'player'
    form_fields = ['spend15', 'check_spend15']

    def error_message(self, values):
        if not values['check_spend15']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        spend_text = self.participant.vars['spend_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 15
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving15 = self.participant.vars['total_saving15']
        return {
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving15': total_saving15,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving15'] <= 0:
            self.participant.vars['spend15'] = 0
        else:
            self.participant.vars['spend15'] = self.player.spend15
        self.participant.vars['total_saving16'] = self.participant.vars['total_saving15'] + \
                                                      self.participant.vars['income15'] - \
                                                      self.player.expense15 - \
                                                      self.participant.vars['spend15']


class Period16(Page):
    form_model = 'player'
    form_fields = ['spend16', 'check_spend16']

    def error_message(self, values):
        if not values['check_spend16']:
            return 'Please decide the amount you would like to spend.'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        start_text = self.participant.vars['start_text']
        spend_text = self.participant.vars['spend_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 16
        for k in range(1, period+1):
            str_expense = 'expense%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving16 = self.participant.vars['total_saving16']
        return {
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving16': total_saving16,
        }


class End_trial(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60


page_sequence = [Start, Period1, Period2, Period3, Period4, Period5, Period6, Period7, Period8, Period9, Period10,
                 Period11, Period12, Period13, Period14, Period15, Period16, End_trial]
