class LogMixin:
    @staticmethod
    def write(msg):
        with open('heranca_multipla/logs/log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
