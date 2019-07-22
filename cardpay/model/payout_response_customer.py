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


class PayoutResponseCustomer(object):
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
    swagger_types = {
        'email': 'str',
        'id': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'phone': 'phone'
    }

    def __init__(self, email=None, id=None, phone=None):  # noqa: E501
        """PayoutResponseCustomer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        self.id = id
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this PayoutResponseCustomer.  # noqa: E501

        Customer's e-mail address, here can be value returned from payment method - in case then in Merchant request `customer.email` wasn't presented  # noqa: E501

        :return: The email of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayoutResponseCustomer.

        Customer's e-mail address, here can be value returned from payment method - in case then in Merchant request `customer.email` wasn't presented  # noqa: E501

        :param email: The email of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this PayoutResponseCustomer.  # noqa: E501

        Customer's ID in Merchant's system  # noqa: E501

        :return: The id of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayoutResponseCustomer.

        Customer's ID in Merchant's system  # noqa: E501

        :param id: The id of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def phone(self):
        """Gets the phone of this PayoutResponseCustomer.  # noqa: E501

        Customer's phone  # noqa: E501

        :return: The phone of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PayoutResponseCustomer.

        Customer's phone  # noqa: E501

        :param phone: The phone of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(PayoutResponseCustomer, dict):
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
        if not isinstance(other, PayoutResponseCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
