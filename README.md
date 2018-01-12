# Salesforce Batch

Salesforce Batch is a basic Salesforce.com REST API client written almost entirely by [Nick Catalano and the rest of the team](https://github.com/simple-salesforce/simple-salesforce/graphs/contributors) over at [Simple Salesforce](https://github.com/simple-salesforce/simple-salesforce/). For example of how the Salesforce Batch client is used, look there.

At the time of this writing, while Simple Salesforce does interface with the Salesforce bulk API, it does not leverage multi-batch upload jobs, and as a result can only create/update/destroy up to 10,000 records at a time. Considering the cost of entry, for many Salesforce users this simply isn't good enough. Enter Salesforce Batch. Batch breaks your records out into batches (groups of 10,000) and leverages Python's multithreading library to complete a bulk requests as quickly and efficiently as possible. It's still early days for this package; but for me at least it's already paying off. We started using it at work and on day two, in a sort of trial by fire, it successuflly updated over a quarter million customer records in a single call. 

Getting Started...
---------------
...goes like this:

```shell
$ pip install salesforce_batch
```

What's Different in Salesforce Batch
------------------------------------

Batch does about what you'd expect, especially if you're familiar with Simple Salesforce. The only differences are in the bulk API, and even there things are pretty much the same. In terms of usage, there is one change.
When accessing the bulk API, instead of returning a list of results, one dictionary per row, Salesforce Batch returns a list of lists, with each outer list representing the results of you job. Each inner list is the results of a batch and - like Simple Salesforce - comprises dictionaries corresponding to the affected rows.
```python
from simple_salesforce import Salesforce
sf = Salesforce(username=your_name, password=your_pass,
                       sandbox=False, security_token=i_wish_id_bought_bitcoin,
                       client_id=your_id)
bulk_client = sf.bulk.Account
bulk_client.update(update_dict)
# => [[{key: row_from_batch_one}], [{key: row_from_batch_two}], [{key: etc}]]
```


For examples and documentation, check out [Simple Salesforce](https://github.com/simple-salesforce/simple-salesforce/)
