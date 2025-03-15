from Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    account_creation_message_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)
