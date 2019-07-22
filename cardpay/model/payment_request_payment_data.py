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


class PaymentRequestPaymentData(object):
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
        'amount': 'float',
        'authentication_request': 'bool',
        'currency': 'str',
        'dynamic_descriptor': 'str',
        'generate_token': 'bool',
        'note': 'str',
        'preauth': 'bool'
    }

    attribute_map = {
        'amount': 'amount',
        'authentication_request': 'authentication_request',
        'currency': 'currency',
        'dynamic_descriptor': 'dynamic_descriptor',
        'generate_token': 'generate_token',
        'note': 'note',
        'preauth': 'preauth'
    }

    def __init__(self, amount=None, authentication_request=None, currency=None, dynamic_descriptor=None, generate_token=None, note=None, preauth=None):  # noqa: E501
        """PaymentRequestPaymentData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._authentication_request = None
        self._currency = None
        self._dynamic_descriptor = None
        self._generate_token = None
        self._note = None
        self._preauth = None
        self.discriminator = None

        self.amount = amount
        if authentication_request is not None:
            self.authentication_request = authentication_request
        self.currency = currency
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor
        if generate_token is not None:
            self.generate_token = generate_token
        if note is not None:
            self.note = note
        if preauth is not None:
            self.preauth = preauth

    @property
    def amount(self):
        """Gets the amount of this PaymentRequestPaymentData.  # noqa: E501

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 100 millions If 'payment_method' = `BITCOIN` then minimum order amount is approximately 0.003 bitcoins or its equivalent. The exact value should be provided by the account manager.  # noqa: E501

        :return: The amount of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequestPaymentData.

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 100 millions If 'payment_method' = `BITCOIN` then minimum order amount is approximately 0.003 bitcoins or its equivalent. The exact value should be provided by the account manager.  # noqa: E501

        :param amount: The amount of this PaymentRequestPaymentData.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def authentication_request(self):
        """Gets the authentication_request of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, amount must not be presented in request, no payment will be made, only cardholder authentication will be performed. Also can be used to generate token. *(for BANKCARD payment method only)*  # noqa: E501

        :return: The authentication_request of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._authentication_request

    @authentication_request.setter
    def authentication_request(self, authentication_request):
        """Sets the authentication_request of this PaymentRequestPaymentData.

        If set to `true`, amount must not be presented in request, no payment will be made, only cardholder authentication will be performed. Also can be used to generate token. *(for BANKCARD payment method only)*  # noqa: E501

        :param authentication_request: The authentication_request of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._authentication_request = authentication_request

    @property
    def currency(self):
        """Gets the currency of this PaymentRequestPaymentData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :return: The currency of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentRequestPaymentData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :param currency: The currency of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def dynamic_descriptor(self):
        """Gets the dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501

        Short description of the service or product, must be enabled by CardPay manager to be used *(for BANKCARD payment method only)*  # noqa: E501

        :return: The dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        """Sets the dynamic_descriptor of this PaymentRequestPaymentData.

        Short description of the service or product, must be enabled by CardPay manager to be used *(for BANKCARD payment method only)*  # noqa: E501

        :param dynamic_descriptor: The dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """
        if dynamic_descriptor is not None and len(dynamic_descriptor) > 25:
            raise ValueError("Invalid value for `dynamic_descriptor`, length must be less than or equal to `25`")  # noqa: E501
        if dynamic_descriptor is not None and len(dynamic_descriptor) < 0:
            raise ValueError("Invalid value for `dynamic_descriptor`, length must be greater than or equal to `0`")  # noqa: E501

        self._dynamic_descriptor = dynamic_descriptor

    @property
    def generate_token(self):
        """Gets the generate_token of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, token will be generated and returned in the response. Token can be generated only for successful transactions (not for declined transactions) *(for BANKCARD payment method only)*  # noqa: E501

        :return: The generate_token of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._generate_token

    @generate_token.setter
    def generate_token(self, generate_token):
        """Sets the generate_token of this PaymentRequestPaymentData.

        If set to `true`, token will be generated and returned in the response. Token can be generated only for successful transactions (not for declined transactions) *(for BANKCARD payment method only)*  # noqa: E501

        :param generate_token: The generate_token of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._generate_token = generate_token

    @property
    def note(self):
        """Gets the note of this PaymentRequestPaymentData.  # noqa: E501

        Note about the transaction that will not be displayed to Customer  # noqa: E501

        :return: The note of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PaymentRequestPaymentData.

        Note about the transaction that will not be displayed to Customer  # noqa: E501

        :param note: The note of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 100:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `100`")  # noqa: E501
        if note is not None and len(note) < 0:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `0`")  # noqa: E501

        self._note = note

    @property
    def preauth(self):
        """Gets the preauth of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, the amount will not be captured but only blocked. Payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. *(for BANKCARD payment method only)*.  # noqa: E501

        :return: The preauth of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._preauth

    @preauth.setter
    def preauth(self, preauth):
        """Sets the preauth of this PaymentRequestPaymentData.

        If set to `true`, the amount will not be captured but only blocked. Payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. *(for BANKCARD payment method only)*.  # noqa: E501

        :param preauth: The preauth of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._preauth = preauth

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
        if issubclass(PaymentRequestPaymentData, dict):
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
        if not isinstance(other, PaymentRequestPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
