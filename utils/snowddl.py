class Snowddl:
    """
    Snowddl class loads DDL files for various tables in a database.

    Attributes:
        ddl_dict (dict): dictionary of DDL files for various tables in a database.

    Methods:
        load_ddls: loads DDL files for various tables in a database.
    """

    def __init__(self):
        self.ddl_dict = self.load_ddls()

    @staticmethod
    def load_ddls():
        ddl_files = {
            "Account_Dim": "sql/ddl_account_dim.sql",
            "contract_and_renewal": "sql/ddl_contract_and_renewal.sql",
            "Bookings": "sql/ddl_Bookings.sql",
            "Guided_Selling_Greenfield": "sql/ddl_Guided_Selling_Greenfield.sql",
            "Quota_Target": "sql/ddl_Quota_Target.sql",
            "risk_reason": "sql/ddl_risk_reason.sql",
            "account_activity": "sql/ddl_account_activity.sql",
            "Cross_Sell_Scores": "sql/ddl_Cross_Sell_Scores.sql",

        }

        ddl_dict = {}
        for table_name, file_name in ddl_files.items():
            with open(file_name, "r") as f:
                ddl_dict[table_name] = f.read()
        return ddl_dict
