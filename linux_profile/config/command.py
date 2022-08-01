from linux_profile.config.base import Config


class BaseCommand(Config):
    """Base Command class
    """
    PARAM = ['all']

    def start(self):
        """Start to basic settings
        """
        self.add_config()
        self.load_config()
        self.initial_commands()

    def initial_commands(self) -> None:
        """Initial Commands
        """
        if self.param:
            if self.param not in self.PARAM:
                raise Exception(
                    "Invalid parameter: " + self.param + " not exist!"
                    )

            getattr(self, 'param_'+self.param)()