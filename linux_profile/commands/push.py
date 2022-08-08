"""System Command"""

from linux_profile.config.command import BaseCommand
from linux_profile.utils.text import text_command


class Push(BaseCommand):
    """Start of settings
    """

    def param_all(self):
        """Param All
        """
        text_command(value='push ' + self.param)
