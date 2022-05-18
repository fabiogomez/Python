import sys
from decimal import *

class OrderAct():
    """
    Enum class for order type
    """
    BID = "B"
    ASK = "A"

class OrderType():
    """
    Enum class for order type
    """
    MARKET = "M"
    LIMIT = "L"


class Order():

    def __init__(self,  order_id: str, order_user_id: str,  order_act: str, order_price: float, order_size: float, order_peak_size: float, order_type: str):
        self.id = order_id
        self.__user_id = order_user_id
        self.__act = order_act
        self.__price = order_price
        self.__size = order_size
        self.__next_order = None
        self.__prev_order = None
        self.__trade_size = 0

    @property
    def is_ask(self) -> bool:
        """
        Returns if the Order is a sell or not
        Returns:
            Boolean: True if sell, False if buy
        """

        return self.act == OrderAct.ASK

    def match(self, other_order: object) -> bool:
        """
        Return True if other match all current size
        :param other_order:
        :return boolean:
        """
        if self.__size <= other_order.__size:
            trade_size = self.__size
            self.make_trade(trade_size)
            other_order.make_trade(trade_size)
            return True
        else:
            trade_size = other_order.__size
            self.make_trade(trade_size)
            other_order.make_trade(trade_size)
            return False

    def make_trade(self, trade_size: float):
        """
        Close a deal of a specific size and update remaining order sizes accordingly
        :param trade_size:
        """
        if(self.trade_size > 0):
            raise Exception('Peak size of order id {}  is negative'.format(self.id))
      
        self.__size -= trade_size
        self.trade_size += trade_size

    
