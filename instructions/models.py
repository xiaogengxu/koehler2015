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


def seq_to_dict(s):
    r = {}
    l = len(s) - 1
    for i, j in enumerate(s):
        if i < l:
            r[j] = s[i + 1]
        else:
            r[j] = None
    return r


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

    seq_treat = ['short_first', 'long_first']
    treat_seq = ['short', 'long']
    round_seq = [1, 2]
    period = range(1, 17)


class Subsession(BaseSubsession):
    def creating_session(self):
        app_seq = self.session.config.get('app_sequence')
        treat = Constants.treat_seq.copy()
        round = Constants.round_seq.copy()

        for p in self.get_players():
            seq_treatment = Constants.seq_treat.copy()
            p.treatment = random.choice(seq_treatment)
            p.participant.vars['treatment'] = p.treatment
            p.participant.vars['finished'] = ''
            app_instruction, app_trial1, app_trial2, app_quiz, app_decision1, app_decision2, app_post, app_result \
                = app_seq
            if p.treatment == 'long_first':
                new_app_seq = [app_instruction] + [app_trial1] + [app_quiz] + [app_decision1] + [app_decision2] \
                              + [app_post] + [app_result]
            else:
                new_app_seq = [app_instruction] + [app_trial2] + [app_quiz] + [app_decision2] + [app_decision1] \
                              + [app_post] + [app_result]
            p.participant.vars['_updated_seq_apps'] = seq_to_dict(new_app_seq)

            reward_treat = random.choice(treat)
            p.reward_treat = reward_treat
            p.participant.vars['reward_treat'] = reward_treat
            reward_round = random.choice(round)
            p.reward_round = reward_round
            p.participant.vars['reward_round'] = reward_round
            reward_period = random.choice(Constants.period)
            p.reward_period = reward_period
            p.participant.vars['reward_period'] = reward_period
            if reward_treat == 'short':
                if p.participant.vars['treatment'] == 'short_first':
                    if reward_round == 1:
                        p.participant.vars['reward_life'] = 1
                    else:
                        p.participant.vars['reward_life'] = 2
                else:
                    if reward_round == 1:
                        p.participant.vars['reward_life'] = 3
                    else:
                        p.participant.vars['reward_life'] = 4
            else:
                if p.participant.vars['treatment'] == 'short_first':
                    if reward_round == 1:
                        p.participant.vars['reward_life'] = 3
                    else:
                        p.participant.vars['reward_life'] = 4
                else:
                    if reward_round == 1:
                        p.participant.vars['reward_life'] = 1
                    else:
                        p.participant.vars['reward_life'] = 2


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    time_instruction = models.IntegerField()
    reward_treat = models.StringField(blank=True)
    reward_round = models.IntegerField(blank=True)
    reward_period = models.IntegerField(blank=True)
    consent = models.StringField(blank=True)
    lang = models.StringField(
        label='Bitte wählen Sie Ihre Sprache. / Please, select your language.',
        choices=[('de', 'Deutsch'), ('en', 'English')],
        widget=widgets.RadioSelect,
        initial='de',
        blank=True
    )
    username = models.StringField(blank=True)
