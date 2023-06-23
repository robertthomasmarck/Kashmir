from alpaca.trading import TradingClient
import attr

from login.key_chain import key_chain


@attr.define
class TClient:

    acct_type: str = attr.ib(default="paper")
    keys: str = attr.ib()
    client = attr.ib()
    account: dict = attr.ib()

    @keys.default
    def get_keys(self):
        return key_chain()[self.acct_type]

    @client.default
    def get_tc(self):
        return TradingClient(**self.keys["teeth"])

    @account.default
    def look_at_account(self):
        account = self.client.get_account()
        print(account)
        return account






