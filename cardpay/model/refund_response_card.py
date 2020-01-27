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


class RefundResponseCard(object):
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
    swagger_types = {"issuing_country_code": "str", "masked_pan": "str"}

    attribute_map = {
        "issuing_country_code": "issuing_country_code",
        "masked_pan": "masked_pan",
    }

    def __init__(self, issuing_country_code=None, masked_pan=None):  # noqa: E501
        """RefundResponseCard - a model defined in Swagger"""  # noqa: E501

        self._issuing_country_code = None
        self._masked_pan = None
        self.discriminator = None

        if issuing_country_code is not None:
            self.issuing_country_code = issuing_country_code
        if masked_pan is not None:
            self.masked_pan = masked_pan

    @property
    def issuing_country_code(self):
        """Gets the issuing_country_code of this RefundResponseCard.  # noqa: E501

        Country code of issuing card country  # noqa: E501

        :return: The issuing_country_code of this RefundResponseCard.  # noqa: E501
        :rtype: str
        """
        return self._issuing_country_code

    @issuing_country_code.setter
    def issuing_country_code(self, issuing_country_code):
        """Sets the issuing_country_code of this RefundResponseCard.

        Country code of issuing card country  # noqa: E501

        :param issuing_country_code: The issuing_country_code of this RefundResponseCard.  # noqa: E501
        :type: str
        """

        self._issuing_country_code = issuing_country_code

    @property
    def masked_pan(self):
        """Gets the masked_pan of this RefundResponseCard.  # noqa: E501

        Masked PAN (shows first 6 digits and 4 last digits)  # noqa: E501

        :return: The masked_pan of this RefundResponseCard.  # noqa: E501
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this RefundResponseCard.

        Masked PAN (shows first 6 digits and 4 last digits)  # noqa: E501

        :param masked_pan: The masked_pan of this RefundResponseCard.  # noqa: E501
        :type: str
        """

        self._masked_pan = masked_pan

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
        if issubclass(RefundResponseCard, dict):
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
        if not isinstance(other, RefundResponseCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
