from otree.api import Currency as c, currency_range
from .models import Constants
from ._builtin import Page as oTreePage, WaitPage
import datetime
from .generic_pages import Page
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Lang(oTreePage):
    form_model = 'player'
    form_fields = ['lang']

    def before_next_page(self):
        lang_chosen = self.player.lang
        self.request.session[settings.LANGUAGE_SESSION_KEY] = lang_chosen
        self.participant.vars['lang_chosen'] = lang_chosen
        self.player.username = self.participant.label


class Intro(Page):
    form_model = 'player'
    form_fields = ['consent']

    def error_message(self, values):
        if not values['consent']:
            return _('Please answer the question.')

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/screenout?p=73953&m='+username_value)

    def before_next_page(self):
        if self.player.consent == 'no':
            self.participant.vars['consent'] = 'no'
            self.participant.vars['time_instruction'] = 0
        else:
            self.participant.vars['consent'] = 'yes'


class Instruct0(Page):
    form_model = 'player'

    def before_next_page(self):
        start_datetime = datetime.datetime.now()
        self.participant.vars['start_time'] = start_datetime

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'


class Instruct1(Page):
    form_model = 'player'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'


class Instruct2(Page):
    form_model = 'player'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'


class Instruct3(Page):
    form_model = 'player'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'


class Instruct4(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'


class Instruct5(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['consent'] == 'yes'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {
            'lang': lang
        }

    def before_next_page(self):
        end_datetime = datetime.datetime.now()
        start_time = self.participant.vars['start_time']
        self.player.time_instruction = round((end_datetime - start_time).total_seconds())
        self.participant.vars['time_instruction'] = round((end_datetime - start_time).total_seconds())


class End_instruct(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] < 30 and self.participant.vars['consent'] == 'yes'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/screenout?p=73953&m='+username_value)


page_sequence = [Lang, Intro, Instruct0, Instruct1, Instruct2, Instruct3, Instruct4, Instruct5, End_instruct]
