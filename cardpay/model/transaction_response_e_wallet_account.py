# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TransactionResponseEWalletAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"holder": "str", "id": "str"}

    attribute_map = {"holder": "holder", "id": "id"}

    def __init__(self, holder=None, id=None):  # noqa: E501
        """TransactionResponseEWalletAccount - a model defined in Swagger"""  # noqa: E501

        self._holder = None
        self._id = None
        self.discriminator = None

        if holder is not None:
            self.holder = holder
        if id is not None:
            self.id = id

    @property
    def holder(self):
        """Gets the holder of this TransactionResponseEWalletAccount.  # noqa: E501

        Ewallet account holder name For DIRECTBANKINGEU - Account holder name (optional)  # noqa: E501

        :return: The holder of this TransactionResponseEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._holder

    @holder.setter
    def holder(self, holder):
        """Sets the holder of this TransactionResponseEWalletAccount.

        Ewallet account holder name For DIRECTBANKINGEU - Account holder name (optional)  # noqa: E501

        :param holder: The holder of this TransactionResponseEWalletAccount.  # noqa: E501
        :type: str
        """

        self._holder = holder

    @property
    def id(self):
        """Gets the id of this TransactionResponseEWalletAccount.  # noqa: E501

        For ALIPAY - 16 digits number For QIWI - Customer phone number (from 1 to 15 digits) For WEBMONEY - Customer account number For NETELLER - Email address of the customer For YANDEXMONEY - Customer wallet number, 11 to 16 digits, begins with 410 For DIRECTBANKINGNGA - Bank account number For AQRCODE - Customer account number For AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE, TIGO - Customer account number For 'Latin America' - Customer’s personal identification number For DIRECTBANKINGEU - Sender IBAN (optional)  # noqa: E501

        :return: The id of this TransactionResponseEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionResponseEWalletAccount.

        For ALIPAY - 16 digits number For QIWI - Customer phone number (from 1 to 15 digits) For WEBMONEY - Customer account number For NETELLER - Email address of the customer For YANDEXMONEY - Customer wallet number, 11 to 16 digits, begins with 410 For DIRECTBANKINGNGA - Bank account number For AQRCODE - Customer account number For AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE, TIGO - Customer account number For 'Latin America' - Customer’s personal identification number For DIRECTBANKINGEU - Sender IBAN (optional)  # noqa: E501

        :param id: The id of this TransactionResponseEWalletAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(TransactionResponseEWalletAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionResponseEWalletAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
