from otree.api import Currency as c, currency_range
from .models import Constants
from ._builtin import Page as oTreePage, WaitPage
import datetime, time
from .generic_pages import Page
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


def get_timeout_seconds(player):
    return player.participant.vars['expiry'] - time.time()


class Start(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               self.participant.vars['treatment'] == 'long_first' and self.player.round_number == 1 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'


class Start_to_L(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               self.participant.vars['treatment'] == 'short_first' and self.player.round_number == 1 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'


class Period1(Page):
    form_model = 'player'
    form_fields = ['spend_long1', 'check_spend_long1']

    def error_message(self, values):
        if not values['check_spend_long1']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number
        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        period = 1
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(2, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        total_saving1 = self.participant.vars['total_saving_long1']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'total_saving1': total_saving1,
        }

    def before_next_page(self):
        self.participant.vars['spend_long1'] = self.player.spend_long1
        self.participant.vars['total_saving_long2'] = self.participant.vars['total_saving_long1'] + \
                                                      self.participant.vars['income_long1'] - \
                                                      self.player.expense_long1 - \
                                                      self.participant.vars['spend_long1']


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend_long2', 'check_spend_long2']

    def error_message(self, values):
        if not values['check_spend_long2']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 2
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving2 = self.participant.vars['total_saving_long2']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving2': total_saving2,
        }

    def before_next_page(self):
        self.participant.vars['spend_long2'] = self.player.spend_long2
        self.participant.vars['total_saving_long3'] = self.participant.vars['total_saving_long2'] + \
                                                      self.participant.vars['income_long2'] - \
                                                      self.player.expense_long2 - \
                                                      self.participant.vars['spend_long2']


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend_long3', 'check_spend_long3']

    def error_message(self, values):
        if not values['check_spend_long3']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 3
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving3 = self.participant.vars['total_saving_long3']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving3': total_saving3,
        }

    def before_next_page(self):
        self.participant.vars['spend_long3'] = self.player.spend_long3
        self.participant.vars['total_saving_long4'] = self.participant.vars['total_saving_long3'] + \
                                                      self.participant.vars['income_long3'] - \
                                                      self.player.expense_long3 - \
                                                      self.participant.vars['spend_long3']


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend_long4', 'check_spend_long4']

    def error_message(self, values):
        if not values['check_spend_long4']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 4
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving4 = self.participant.vars['total_saving_long4']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving4': total_saving4,
        }

    def before_next_page(self):
        self.participant.vars['spend_long4'] = self.player.spend_long4
        self.participant.vars['total_saving_long5'] = self.participant.vars['total_saving_long4'] + \
                                                      self.participant.vars['income_long4'] - \
                                                      self.player.expense_long4 - \
                                                      self.participant.vars['spend_long4']


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend_long5', 'check_spend_long5']

    def error_message(self, values):
        if not values['check_spend_long5']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 5
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving5 = self.participant.vars['total_saving_long5']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving5': total_saving5,
        }

    def before_next_page(self):
        self.participant.vars['spend_long5'] = self.player.spend_long5
        self.participant.vars['total_saving_long6'] = self.participant.vars['total_saving_long5'] + \
                                                      self.participant.vars['income_long5'] - \
                                                      self.player.expense_long5 - \
                                                      self.participant.vars['spend_long5']


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend_long6', 'check_spend_long6']

    def error_message(self, values):
        if not values['check_spend_long6']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 6
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving6 = self.participant.vars['total_saving_long6']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving6': total_saving6,
        }

    def before_next_page(self):
        self.participant.vars['spend_long6'] = self.player.spend_long6
        self.participant.vars['total_saving_long7'] = self.participant.vars['total_saving_long6'] + \
                                                      self.participant.vars['income_long6'] - \
                                                      self.player.expense_long6 - \
                                                      self.participant.vars['spend_long6']


class Period7(Page):
    form_model = 'player'
    form_fields = ['spend_long7', 'check_spend_long7']

    def error_message(self, values):
        if not values['check_spend_long7']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 7
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving7 = self.participant.vars['total_saving_long7']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving7': total_saving7,
        }

    def before_next_page(self):
        self.participant.vars['spend_long7'] = self.player.spend_long7
        self.participant.vars['total_saving_long8'] = self.participant.vars['total_saving_long7'] + \
                                                      self.participant.vars['income_long7'] - \
                                                      self.player.expense_long7 - \
                                                      self.participant.vars['spend_long7']


class Period8(Page):
    form_model = 'player'
    form_fields = ['spend_long8', 'check_spend_long8']

    def error_message(self, values):
        if not values['check_spend_long8']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 8
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving8 = self.participant.vars['total_saving_long8']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving8': total_saving8,
        }

    def before_next_page(self):
        self.participant.vars['spend_long8'] = self.player.spend_long8
        self.participant.vars['total_saving_long9'] = self.participant.vars['total_saving_long8'] + \
                                                      self.participant.vars['income_long8'] - \
                                                      self.player.expense_long8 - \
                                                      self.participant.vars['spend_long8']


class Period9(Page):
    form_model = 'player'
    form_fields = ['spend_long9', 'check_spend_long9']

    def error_message(self, values):
        if not values['check_spend_long9']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        start_title_retire = self.participant.vars['start_title_retire']
        start_text_retire = self.participant.vars['start_text_retire']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 9
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving9 = self.participant.vars['total_saving_long9']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'start_title_retire': start_title_retire,
            'start_text_retire': start_text_retire,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving9': total_saving9,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long9'] <= 0:
            self.participant.vars['spend_long9'] = 0
        else:
            self.participant.vars['spend_long9'] = self.player.spend_long9
        if self.participant.vars['total_saving_long9'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long10'] = self.participant.vars['total_saving_long9'] + \
                                                      self.participant.vars['income_long9'] - \
                                                      self.player.expense_long9 - \
                                                      self.participant.vars['spend_long9']


class Period10(Page):
    form_model = 'player'
    form_fields = ['spend_long10', 'check_spend_long10']

    def error_message(self, values):
        if not values['check_spend_long10']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 10
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving10 = self.participant.vars['total_saving_long10']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving10': total_saving10,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long10'] <= 0:
            self.participant.vars['spend_long10'] = 0
        else:
            self.participant.vars['spend_long10'] = self.player.spend_long10
        if self.participant.vars['total_saving_long10'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long11'] = self.participant.vars['total_saving_long10'] + \
                                                      self.participant.vars['income_long10'] - \
                                                      self.player.expense_long10 - \
                                                      self.participant.vars['spend_long10']


class Period11(Page):
    form_model = 'player'
    form_fields = ['spend_long11', 'check_spend_long11']

    def error_message(self, values):
        if not values['check_spend_long11']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 11
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving11 = self.participant.vars['total_saving_long11']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving11': total_saving11,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long11'] <= 0:
            self.participant.vars['spend_long11'] = 0
        else:
            self.participant.vars['spend_long11'] = self.player.spend_long11
        if self.participant.vars['total_saving_long11'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long12'] = self.participant.vars['total_saving_long11'] + \
                                                      self.participant.vars['income_long11'] - \
                                                      self.player.expense_long11 - \
                                                      self.participant.vars['spend_long11']


class Period12(Page):
    form_model = 'player'
    form_fields = ['spend_long12', 'check_spend_long12']

    def error_message(self, values):
        if not values['check_spend_long12']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 12
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving12 = self.participant.vars['total_saving_long12']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving12': total_saving12,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long12'] <= 0:
            self.participant.vars['spend_long12'] = 0
        else:
            self.participant.vars['spend_long12'] = self.player.spend_long12
        if self.participant.vars['total_saving_long12'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long13'] = self.participant.vars['total_saving_long12'] + \
                                                      self.participant.vars['income_long12'] - \
                                                      self.player.expense_long12 - \
                                                      self.participant.vars['spend_long12']


class Period13(Page):
    form_model = 'player'
    form_fields = ['spend_long13', 'check_spend_long13']

    def error_message(self, values):
        if not values['check_spend_long13']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 13
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving13 = self.participant.vars['total_saving_long13']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving13': total_saving13,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long13'] <= 0:
            self.participant.vars['spend_long13'] = 0
        else:
            self.participant.vars['spend_long13'] = self.player.spend_long13
        if self.participant.vars['total_saving_long13'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long14'] = self.participant.vars['total_saving_long13'] + \
                                                      self.participant.vars['income_long13'] - \
                                                      self.player.expense_long13 - \
                                                      self.participant.vars['spend_long13']


class Period14(Page):
    form_model = 'player'
    form_fields = ['spend_long14', 'check_spend_long14']

    def error_message(self, values):
        if not values['check_spend_long14']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 14
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving14 = self.participant.vars['total_saving_long14']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving14': total_saving14,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long14'] <= 0:
            self.participant.vars['spend_long14'] = 0
        else:
            self.participant.vars['spend_long14'] = self.player.spend_long14
        if self.participant.vars['total_saving_long14'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long15'] = self.participant.vars['total_saving_long14'] + \
                                                      self.participant.vars['income_long14'] - \
                                                      self.player.expense_long14 - \
                                                      self.participant.vars['spend_long14']


class Period15(Page):
    form_model = 'player'
    form_fields = ['spend_long15', 'check_spend_long15']

    def error_message(self, values):
        if not values['check_spend_long15']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 15
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving15 = self.participant.vars['total_saving_long15']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving15': total_saving15,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long15'] <= 0:
            self.participant.vars['spend_long15'] = 0
        else:
            self.participant.vars['spend_long15'] = self.player.spend_long15
        if self.participant.vars['total_saving_long15'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1
        self.participant.vars['total_saving_long16'] = self.participant.vars['total_saving_long15'] + \
                                                      self.participant.vars['income_long15'] - \
                                                      self.player.expense_long15 - \
                                                      self.participant.vars['spend_long15']


class Period16(Page):
    form_model = 'player'
    form_fields = ['spend_long16', 'check_spend_long16']

    def error_message(self, values):
        if not values['check_spend_long16']:
            return _('Please decide the amount you would like to spend.')

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        start_text = self.participant.vars['start_text']
        spend_text = str(self.participant.vars['spend_text'])
        expense_list1 = []
        expense_past = []
        spend_past = []
        period = 16
        for k in range(1, period+1):
            str_expense = 'expense_long%s' % k
            expense_past.append(getattr(self.player, str_expense))
        for j in range(period+1, 17):
            str_expense = 'expense_long%s' % j
            expense_list1.append(getattr(self.player, str_expense))
        for jj in range(1, period+1):
            expense_list1.append('?')
        for m in range(1, period):
            str_spend = 'spend_long%s' % m
            spend_past.append(self.participant.vars[str_spend])
        total_saving16 = self.participant.vars['total_saving_long16']
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
            'start_text': start_text,
            'spend_text': spend_text,
            'period': period,
            'expense_past': expense_past,
            'expense_list1': expense_list1,
            'spend_past': spend_past,
            'total_saving16': total_saving16,
        }

    def before_next_page(self):
        if self.participant.vars['total_saving_long16'] <= 0:
            self.participant.vars['spend_long16'] = 0
        else:
            self.participant.vars['spend_long16'] = self.player.spend_long16
        if self.participant.vars['total_saving_long16'] < 0:
            str_debt = 'debt_long_r%s' % self.round_number
            self.participant.vars[str_debt] = 1


class End_long(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 30 and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3 and self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        round_bar = self.player.round_number

        if self.participant.vars['treatment'] == 'long_first':
            round_num = self.player.round_number
        else:
            round_num = self.player.round_number + 2
        return {
            'lang': lang,
            'treatment': treatment,
            'round_bar': round_bar,
            'round_num': round_num,
        }

    def before_next_page(self):
        if self.participant.vars['reward_treat'] == 'long' and self.player.round_number == 2:
            reward_round = self.participant.vars['reward_round']
            str_debt = 'debt_long_r%s' % reward_round
            str_reward = 'spend_long%s' % self.participant.vars['reward_period']
            reward_num = getattr(self.player.in_round(reward_round), str_reward)
            self.participant.vars['reward_origin'] = reward_num
            if self.participant.vars[str_debt] == 1:
                self.participant.vars['reward'] = 0
                self.participant.vars['in_debt'] = 1
            else:
                self.participant.vars['reward'] = reward_num


page_sequence = [Start, Start_to_L, Period1, Period2, Period3, Period4, Period5, Period6, Period7, Period8, Period9,
                 Period10, Period11, Period12, Period13, Period14, Period15, Period16, End_long]
