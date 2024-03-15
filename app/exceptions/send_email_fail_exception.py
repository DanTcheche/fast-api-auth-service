class SendEmailFailException(Exception):
    def __init__(self, message="Failed to send email."):
        self.message = message
        super().__init__(self.message)
