from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about
    the quote(quote content,
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.selec_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.selec_one(locator).string

    @property
    def tag(self):
        locator = QuoteLocators.TAGS
        return self.parent.select(locator)

