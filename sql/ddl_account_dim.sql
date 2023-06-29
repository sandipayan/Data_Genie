	primary key (sfdc_account_id)
	fy_quarter VARCHAR(7) NOT NULL
	qtr_start TIMESTAMP WITHOUT TIME ZONE NOT NULL
	qtr_end TIMESTAMP WITHOUT TIME ZONE NOT NULL
	account_name VARCHAR(20) NOT NULL
	zm_contract_id VARCHAR(18) NOT NULL
	sfdc_account_id VARCHAR(18) NOT NULL
	rpt_account_id VARCHAR(22) NOT NULL
	zoom_account_number BIGINT NOT NULL
	zuora_billing_account_number VARCHAR(26) NOT NULL
	zm_contract_name VARCHAR(29) NOT NULL
	account_segment VARCHAR(6) NOT NULL
	industry VARCHAR(16) NOT NULL
	account_owner_division VARCHAR(9) NOT NULL
	ae_name VARCHAR(13) NOT NULL
	renewal_manager_name VARCHAR(8) NOT NULL
	csm_name VARCHAR(14) NOT NULL
	csm_email VARCHAR(22) NOT NULL
	renewal_manager_email VARCHAR(16) NOT NULL
	ae_email VARCHAR(20) NOT NULL
	level_1_account_name VARCHAR(55) NOT NULL
	level_2_account_name VARCHAR(44) NOT NULL
	split_billing BOOLEAN NOT NULL
	sales_channel VARCHAR(8) NOT NULL
	account_age VARCHAR(9) NOT NULL
	contract_source VARCHAR(34) NOT NULL
	billing_country_region VARCHAR(8) NOT NULL
	billing_country VARCHAR(14) NOT NULL
	currency_iso_code VARCHAR(3) NOT NULL
	auto_renewal BOOLEAN NOT NULL