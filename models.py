"""Models"""
from datetime import date

class Comment(object):

    def __init__(self, text, date):
        """Constructor."""
        self.text = text
        self.date = date
        
    def __repr__(self):
        return "text: {}, date: {}".format(self.text,self.date)

COMMENTS = [Comment('text','2005-11-05'), Comment('text2','2015-07-05'), Comment('text3','2018-01-03')]