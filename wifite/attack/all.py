#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from .wpa import AttackWPA
from ..config import Configuration
from ..util.color import Color

class Answer(Enum):
    Skip = 1
    ExitOrReturn = 2
    Continue = 3
    Ignore = 4

class AttackAll(object):
    @classmethod
    def attack_multiple(cls, targets):
        """
        Attacks all given `targets` (list[wifite.model.target]) until user interruption.
        Returns: Number of targets that were attacked (int)
        """

        attacked_targets = 0
        targets_remaining = len(targets)
        for index, target in enumerate(targets, start=1):
            if Configuration.attack_max != 0 and index > Configuration.attack_max:
                print(("Attacked %d targets, stopping because of the --first flag" % Configuration.attack_max))
                break
            attacked_targets += 1
            targets_remaining -= 1

            bssid = target.bssid
            essid = target.essid if target.essid_known else '{O}ESSID unknown{W}'

            Color.pl('\n{+} ({G}%d{W}/{G}%d{W})'
                     % (index, len(targets)) + ' Starting WPA attack against {C}%s{W} ({C}%s{W})' % (bssid, essid))

            should_continue = cls.attack_single(target, targets_remaining)
            if not should_continue:
                break

        return attacked_targets

    @classmethod
    def attack_single(cls, target, targets_remaining):
        """
        Attacks a single `target` (wifite.model.target) with WPA attack only.
        Returns: True if attacks should continue, False otherwise.
        """
        # Only attack WPA/WPA2/WPA3 networks
        if target.primary_encryption.startswith('WPA'):
            attack = AttackWPA(target)
            should_continue = attack.run()
            if not should_continue:
                return False
        else:
            Color.pl("{!} {O}Target {C}%s{O} is not WPA-encrypted. Only WPA attacks are supported.{W}" % target.essid)
            return True
        return True
