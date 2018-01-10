*****************
Salesforce Batch
*****************

Salesforce Batch is a basic Salesforce.com REST API client written almost entirely by Nick Catalano
and `the rest of the crew <https://github.com/simple-salesforce/simple-salesforce/graphs/contributors>`_ over at`Simple Salesforce <https://github.com/simple-salesforce/simple-salesforce/>`_
. For example of how the Salesforce Batch client
is used, look there. 

At the time of this writing, Simple Salesforce does interface with the Salesforce bulk API, but does not
leverage the multi-batch upload jobs, and so can only create/update/destroy up to 10,000 records at a time.
With the cost of entry as high as it is, for most paying Salesforce users, this is simply not enough. Enter
Salesforce Batch. 

Getting Started
---------------
Works like this:

.. code: bash
  $ pip install salesforce_batch
  
What's Different in Salesforce Batch
------------------------------------

Batch does about what you'd expect, especially if you're familiar with Simple Salesforce. The only differences
are in the bulk API, and even there things are pretty much the same. In terms of usage, there is one change.
When accessing the bulk API, instead of retruning a list of results, one dictionary per row, Salesforce Batch
returns a list of lists, representing the results of the job. Each inner list represents a batch, and
like Simple Salesforce, comprises dictionaries corresponding to the affected rows. 

For examples and documentation, check out the `Simple Salesforce`_ repo.
.. _Simple Salesforce https://github.com/simple-salesforce/simple-salesforce
