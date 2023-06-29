**Table 4: contract_and_renewal** (Stores contract and renewal data for accounts)

This table contains Stores contract and renewal data for accounts.

- qtr_start TIMESTAMP WITHOUT TIME ZONE NOT NULL - this is the Quarter Start Date
- qtr_end TIMESTAMP WITHOUT TIME ZONE NOT NULL - this is the Quarter End Date
- account_name VARCHAR(20) NOT NULL - Account Name or Customer Name
- zm_contract_id VARCHAR(18) NOT NULL
- sfdc_account_id VARCHAR(18) NOT NULL - [Primary Key], Unique Account Identifier
- rpt_account_id VARCHAR(22) NOT NULL
- zoom_account_number BIGINT NOT NULL
- zuora_billing_account_number VARCHAR(26) NOT NULL
- zm_contract_name VARCHAR(29) NOT NULL - Contract Name
- contract_renewal_date_entry TIMESTAMP WITHOUT TIME ZONE NOT NULL - Contract Renewal Date at the Beginning of the Quarter
- contract_renewal_date_exit TIMESTAMP WITHOUT TIME ZONE NOT NULL - Contract Renewal Date at present
- contract_start_date TIMESTAMP WITHOUT TIME ZONE NOT NULL - Start date of the Contract
- renewal_quarter VARCHAR(7) NOT NULL - Quarter when is the renewal is due
- contract_status VARCHAR(9) NOT NULL - Current Status of the Contract
- renewal_term VARCHAR(10) NOT NULL - Renewal Term
- current_term VARCHAR(10) NOT NULL
- discounted_mrr_usd DECIMAL(7 2) NOT NULL - Discounted MRR value of the Contract
- last_payment_date VARCHAR(10) - Last Payment date by the customer
- non_payment_gt_61d VARCHAR(5) - Non Payment by the Customer
- product_list_exit VARCHAR(113) NOT NULL - List of Products on the Contract
- last_updated_date TIMESTAMP WITHOUT TIME ZONE NOT NULL
- days_until_renewal INTEGER NOT NULL - Number of days until Renewal
- src_date TIMESTAMP WITHOUT TIME ZONE NOT NULL
- mrr_account_channel VARCHAR(8) NOT NULL - MRR Channel or Type of MRR
- mrr_band VARCHAR(14) NOT NULL - MRR Band
- total_account_mrr_before_cancel DECIMAL(7 2) NOT NULL - Total MRR value of the Contract at the Beginning of the Quarter
- is_mrr_0 BOOLEAN NOT NULL - if the MRR for the account is 0
- mrr_cancel_date TIMESTAMP WITHOUT TIME ZONE NOT NULL - Date the Contract was cancelled
- total_current_contract_value DECIMAL(8 2) NOT NULL - Current MRR value of the Contract
- renewal_stage VARCHAR(16) NOT NULL - Renewal Stage
- opportunity_category VARCHAR(23) NOT NULL - Opportunity Category
- opportunity_name VARCHAR(28) NOT NULL - Name of the Opportunity
- renewal_amount_change DECIMAL(4 1) NOT NULL - Renewal Amount Change
- opps_is_closed VARCHAR(5) - Closed Opportunities
- mrr_qtd_fy_quarter VARCHAR(7) NOT NULL
- renewal_in_qtr BOOLEAN NOT NULL - Amount of Renewals happened within the Quarter
- subscription_end_date TIMESTAMP WITHOUT TIME ZONE NOT NULL
- mrr_entry_qtd DECIMAL(7 2) NOT NULL - Entry MRR
- mrr_upsell_qtd DECIMAL(9 6) NOT NULL - Upsell MRR
- mrr_downsell_qtd DECIMAL(4 2) NOT NULL - Downsell MRR
- mrr_cancel_qtd INTEGER NOT NULL - Cancel MRR
- mrr_churn_qtd DECIMAL(4 2) NOT NULL - Churn MRR
- mrr_exit_qtd DECIMAL(7 2) NOT NULL - Current MRR value
- renewal_status VARCHAR(18) NOT NULL - Renewal Status
- mrr_status VARCHAR(9) NOT NULL - MRR Status

