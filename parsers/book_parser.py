import re

from locators.book_locators import BookLocators



class BookParser:

    RATING={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5,
        'Six':6,
        'Seven':7
    }

    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f' < Book  {self.name} {self.price},{self.rating} stars>'

    @property
    def name(self):
        locator=BookLocators.NAME_LOCATOR
        item_link=self.parent.select_one(locator)
        item_name=item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator=BookLocators.LINK_LOCATOR
        item_link=self.parent.select_one(locator)
        item_name=item_link.attrs['href']
        return item_name

    @property
    def price(self):
        locator=BookLocators.PRICE_LOCATOR
        item_link=self.parent.select_one(locator)
        item=item_link.string
        item_pattern='£([0-9,]+\.[0-9])'
        price=re.search(item_pattern,item)
        price=float(price.group(1))
        return price


    @property
    def rating(self):
        locator=BookLocators.RATING_LOCATOR
        item_link=self.parent.select_one(locator)
        classes=item_link.attrs['class']
        #rating_class=filter(lambda x:x != 'star-rating', classes)
        rating_class=[r for r in classes if r!='star-rating']
        rating_number=BookParser.RATING.get(rating_class[0])
        return rating_number