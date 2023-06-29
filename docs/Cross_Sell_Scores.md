**Table 5: cross_sell_scores ** (predicted cross selling scores)

This table contains predicted cross selling scores for accounts.

- SFDC_ACCOUNT_ID	VARCHAR(18)   – Primary Key, Unique identifier for accounts
- PRODUCT_OPPORTUNITY	VARCHAR(19) - New Product Offering for Existing Customers.
- CROSS_SELL_SCORE	NUMBER(38,0) - Score to sell more products to our current customers. Higher the score better the chances to score the deal.
- EXPLANATION	VARCHAR(522) - Explanation or reason for why the new product is good for the customer
- FY_QUARTER	VARCHAR(7) - Offering is applicable this Quarter
- SCORE_CURRENT	BOOLEAN - Score Value is current