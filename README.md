# Salesforce Batch

Salesforce Batch is a basic Salesforce.com REST API client written on top of [Simple Salesforce](https://github.com/simple-salesforce/simple-salesforce/). For examples of how the Salesforce Batch client is used, look [there](https://github.com/simple-salesforce/simple-salesforce/tree/master/docs).

At the time of this writing, Simple Salesforce does interface with the Salesforce bulk API, but does not run multi-batch jobs. As a result it can only create/update/destroy up to 10,000 records at a time. Considering the cost of entry, we expect many businesses using Salesforce to operate on a much larger scale. 

Batch works by breaking the input list into batches of 10,000, and leverages Python's multithreading library to complete bulk requests as quickly and efficiently as possible. This is not only a boon for developers, who are spared the work of parceling out requests into digestible chunks; it's great for users as well. After all, jobs exist for a reason. They're categorized and cataloged for review in the Service Cloud UI. The interface would quickly lose all value without multi-batch jobs. For example, we recently ran a nightly job to update more than 750,000 records - an operation that would otherwise have ended in a prolific excess of "jobs" cluttering up the UI, that was instead concisely summarized under one line using Salesforce Batch.  

Getting Started...
---------------
...goes like this:

```shell
$ pip install salesforce_batch
```

What's Different in Salesforce Batch
------------------------------------

Batch does about what you'd expect, especially if you're familiar with Simple Salesforce. The only difference is in the bulk API, and even there things are pretty much the same. In terms of usage, there is one change.
When accessing the bulk API, instead of returning a list of results, one dictionary for each updated row, Salesforce Batch returns a list of lists - the outer list representing the entire job; the inner lists representing the results of each batch. and. As with Simple Salesforce, the inner lists hold dictionaries corresponding to affected rows.
```python
from salesforce_batch import Salesforce
sf = Salesforce(username=your_name, password=your_pass,
                       sandbox=False, security_token=im_rather_long,
                       client_id=your_id)
bulk_client = sf.bulk.Account
bulk_client.update(update_dict)
# => [[{key: row_from_batch_one}], [{key: row_from_batch_two}], [{key: etc}]]
```

Thanks and credit to [Nick Catalano and the rest of the team](https://github.com/simple-salesforce/simple-salesforce/graphs/contributors) over at [Simple Salesforce](https://github.com/simple-salesforce/simple-salesforce/)

For examples and documentation, check out [Simple Salesforce](https://github.com/simple-salesforce/simple-salesforce/tree/master/docs)

[Salesforce Batch on PyPI](https://pypi.python.org/pypi/salesforce_batch/0.1.2)
