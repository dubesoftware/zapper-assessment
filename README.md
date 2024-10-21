# zapper-assessment
Solutions to Zapper.com's interview assessment.

### 1. The relational database schema (SQL)

The Schema contained in the Data Definition Language SQL herein is designed to track transactions between customers and merchants. Therefore, we have three tables mapping to the thrtee entities/ objects that we have identified. These are Customers, Merchants and Transactions.

We define the relationship between customers and merchants via the Transactions table.

### 2. User settings management functions (Python)
#### To check that a feature is enabled, we use bitwise operations.

We define a `is_feature_enabled` function which checks the bit at the `setting_index` argument and either returns True for '1', or False.


