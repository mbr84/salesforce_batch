"""Simple-Salesforce Package"""
# flake8: noqa

from simple_salesforce_batchsalesforce.api import (
    Salesforce,
    SalesforceAPI,
    SFType
)

from salesforce_batch.bulk import (
    SFBulkHandler
)

from salesforce_batch.login import (
    SalesforceLogin
)

from salesforce_batch.exceptions import (
    SalesforceError,
    SalesforceMoreThanOneRecord,
    SalesforceExpiredSession,
    SalesforceRefusedRequest,
    SalesforceResourceNotFound,
    SalesforceGeneralError,
    SalesforceMalformedRequest,
    SalesforceAuthenticationFailed
)
