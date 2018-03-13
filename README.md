# IRIM
Interesting Rule Induction Module with Handling Missing Attributes Values

In the current era of big data, huge amount of data can be easily collected, but the unprocessed data is not useful on its own. It can be useful only when we are able to find interesting patterns or hidden knowledge. The algorithm to find interesting patterns is known as Rule Induction Algorithm. Rule induction is a special area of data mining and machine learning in which formal rules are extracted from a dataset. The extracted rules may represent some general or local (isolated) patterns related to the data.

In this report, we will focus on the IRIM (Interesting Rule Inducing Module) which induces strong interesting rules that covers most of the concept. Usually, the rules induced by IRIM provides interesting and surprising insight to the expert in the domain area.

The IRIM algorithm was implemented using Python and pySpark library, which is specially customize for data mining. Further, the IRIM algorithm was extended to handle the different types of missing data. Then at the end the performance of the IRIM algorithm with and without missing data feature was analyzed. As an example, interesting rules induced from IRIS dataset are shown.
