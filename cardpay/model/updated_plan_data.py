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


class UpdatedPlanData(object):
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
        'id': 'str',
        'details': 'str',
        'updated': 'datetime',
        'is_executed': 'bool',
        'name_to': 'str',
        'name': 'str',
        'status_to': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'details': 'details',
        'updated': 'updated',
        'is_executed': 'is_executed',
        'name_to': 'name_to',
        'name': 'name',
        'status_to': 'status_to',
        'status': 'status'
    }

    def __init__(self, id=None, details=None, updated=None, is_executed=None, name_to=None, name=None, status_to=None, status=None):  # noqa: E501
        """UpdatedPlanData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._details = None
        self._updated = None
        self._is_executed = None
        self._name_to = None
        self._name = None
        self._status_to = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if details is not None:
            self.details = details
        if updated is not None:
            self.updated = updated
        if is_executed is not None:
            self.is_executed = is_executed
        if name_to is not None:
            self.name_to = name_to
        if name is not None:
            self.name = name
        if status_to is not None:
            self.status_to = status_to
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this UpdatedPlanData.  # noqa: E501

        Represents the ID of the modified plan  # noqa: E501

        :return: The id of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatedPlanData.

        Represents the ID of the modified plan  # noqa: E501

        :param id: The id of this UpdatedPlanData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def details(self):
        """Gets the details of this UpdatedPlanData.  # noqa: E501

        The reason why request was unsuccessful  # noqa: E501

        :return: The details of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UpdatedPlanData.

        The reason why request was unsuccessful  # noqa: E501

        :param details: The details of this UpdatedPlanData.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def updated(self):
        """Gets the updated of this UpdatedPlanData.  # noqa: E501

        Plan update date  # noqa: E501

        :return: The updated of this UpdatedPlanData.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UpdatedPlanData.

        Plan update date  # noqa: E501

        :param updated: The updated of this UpdatedPlanData.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def is_executed(self):
        """Gets the is_executed of this UpdatedPlanData.  # noqa: E501

        Indicates was the request successful or not  # noqa: E501

        :return: The is_executed of this UpdatedPlanData.  # noqa: E501
        :rtype: bool
        """
        return self._is_executed

    @is_executed.setter
    def is_executed(self, is_executed):
        """Sets the is_executed of this UpdatedPlanData.

        Indicates was the request successful or not  # noqa: E501

        :param is_executed: The is_executed of this UpdatedPlanData.  # noqa: E501
        :type: bool
        """

        self._is_executed = is_executed

    @property
    def name_to(self):
        """Gets the name_to of this UpdatedPlanData.  # noqa: E501

        New plan name -  for RENAME operation only  # noqa: E501

        :return: The name_to of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._name_to

    @name_to.setter
    def name_to(self, name_to):
        """Sets the name_to of this UpdatedPlanData.

        New plan name -  for RENAME operation only  # noqa: E501

        :param name_to: The name_to of this UpdatedPlanData.  # noqa: E501
        :type: str
        """

        self._name_to = name_to

    @property
    def name(self):
        """Gets the name of this UpdatedPlanData.  # noqa: E501

        Name of modified plan. Will be returned for `RENAME` operation  # noqa: E501

        :return: The name of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatedPlanData.

        Name of modified plan. Will be returned for `RENAME` operation  # noqa: E501

        :param name: The name of this UpdatedPlanData.  # noqa: E501
        :type: str
        """

        self._name = name

    class StatusTo(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        

    @property
    def status_to(self):
        """Gets the status_to of this UpdatedPlanData.  # noqa: E501

        New state of plan (active or hold) -  for CHANGE_STATUS operation only  # noqa: E501

        :return: The status_to of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this UpdatedPlanData.

        New state of plan (active or hold) -  for CHANGE_STATUS operation only  # noqa: E501

        :param status_to: The status_to of this UpdatedPlanData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}"  # noqa: E501
                .format(status_to, allowed_values)
            )

        self._status_to = status_to

    class Status(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        

    @property
    def status(self):
        """Gets the status of this UpdatedPlanData.  # noqa: E501

        Status of modified plan ('ACTIVE' or 'HOLD'). Will be returned for `CHANGE_STATUS` operation  # noqa: E501

        :return: The status of this UpdatedPlanData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatedPlanData.

        Status of modified plan ('ACTIVE' or 'HOLD'). Will be returned for `CHANGE_STATUS` operation  # noqa: E501

        :param status: The status of this UpdatedPlanData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(UpdatedPlanData, dict):
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
        if not isinstance(other, UpdatedPlanData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
