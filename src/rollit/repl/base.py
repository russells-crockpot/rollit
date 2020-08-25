"""
"""
try:
    import readline  # pylint: disable=unused-import
except ImportError:
    pass

__all__ = []


class Repl:
    """
    """

    prompt_text = '|> '

    def __init__(self, execution_env):
        self.execution_env = execution_env

    def print(self, value):
        """
        """
        print(value)

    def prompt(self):
        """
        """
        return input(self.prompt_text)  # nosec

    def run(self):
        """
        """
        try:
            while True:
                command = self.prompt()
                result = self.execution_env.evaluate(command)
                self.print(result)
        except KeyboardInterrupt:
            return
