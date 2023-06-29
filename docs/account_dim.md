**Table 2: ACCOUNT_DIM** (Stores dimensional data for accounts)

This table contains Stores dimensional data for accounts.

- fy_quarter VARCHAR(7) NOT NULL The fiscal year quarter
- qtr_start TIMESTAMP WITHOUT TIME ZONE NOT NULL The fiscal year quarter start date
- qtr_end TIMESTAMP WITHOUT TIME ZONE NOT NULL The fiscal year quarter end date
- account_name VARCHAR(20) NOT NULL The account name
- zm_contract_id VARCHAR(18)  The salesforce contract id
- sfdc_account_id VARCHAR(18)  - [PRIMARY KEY NOT NULL] Primary Key for join .The salesforce account id
- rpt_account_id VARCHAR(22) NOT NULL The zoom account id
- zoom_account_number BIGINT NOT NULL The zoom account number
- zuora_billing_account_number VARCHAR(26) NOT NULL The zuora billing account number
- zm_contract_name VARCHAR(29) NOT NULL The salesforce contract name
- account_segment VARCHAR(6) NOT NULL The account segment
- industry VARCHAR(16) NOT NULL The account industry. Always use this column for Industry information.
- account_owner_division VARCHAR(9) NOT NULL The account executive owner division
- ae_name VARCHAR(13) NOT NULL The account executive name
- renewal_manager_name VARCHAR(8) NOT NULL The renewal manager name
- csm_name VARCHAR(14) NOT NULL The customer success manager CSM name
- csm_email VARCHAR(22) NOT NULL The customer success manager CSM email
- renewal_manager_email VARCHAR(16) NOT NULL THE renewal manager email
- ae_email VARCHAR(20) NOT NULL The account executive email
- level_1_account_name VARCHAR(55) NOT NULL The level 1 partner account name
- level_2_account_name VARCHAR(44) NOT NULL The level 2 partner account name
- split_billing BOOLEAN NOT NULL A boolean indicator if the contract has split billing
- sales_channel VARCHAR(8) NOT NULL The sales channel
- account_age VARCHAR(9) NOT NULL The account age
- contract_source VARCHAR(34) NOT NULL The contract source
- billing_country_region VARCHAR(8) NOT NULL The billing country region
- billing_country VARCHAR(14) NOT NULL The billing country
- currency_iso_code VARCHAR(3) NOT NULL The currency code
- auto_renewal BOOLEAN NOT NULL A boolean indicator if the contract is set for auto renewal