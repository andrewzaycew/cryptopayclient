import requests

class CryptoBotClient:
    def __init__(self, api_token: str, use_testnet: bool = False):
        self.api_token = api_token
        self.use_testnet = use_testnet
        self.base_url = "https://testnet-pay.crypt.bot/api/" if use_testnet else "https://pay.crypt.bot/api/"
        self.headers = {
            "Crypto-Pay-API-Token": self.api_token,
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, params: dict = None):
        url = self.base_url + endpoint
        response = requests.request(method, url, headers=self.headers, json=params)
        response_data = response.json()
        if response_data.get("ok"):
            return response_data.get("result")
        else:
            raise Exception(f"Error: {response_data.get('error')}")

    def get_me(self):
        return self._request("GET", "getMe")

    def create_invoice(self, amount: str, currency_type: str = "crypto", asset: str = None, fiat: str = None,
                       accepted_assets: str = None, description: str = None, hidden_message: str = None,
                       paid_btn_name: str = None, paid_btn_url: str = None, payload: str = None,
                       allow_comments: bool = True, allow_anonymous: bool = True, expires_in: int = None):
        params = {
            "amount": amount,
            "currency_type": currency_type,
            "asset": asset,
            "fiat": fiat,
            "accepted_assets": accepted_assets,
            "description": description,
            "hidden_message": hidden_message,
            "paid_btn_name": paid_btn_name,
            "paid_btn_url": paid_btn_url,
            "payload": payload,
            "allow_comments": allow_comments,
            "allow_anonymous": allow_anonymous,
            "expires_in": expires_in
        }
        # Убираем ключи с значением None
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("POST", "createInvoice", params)

    def delete_invoice(self, invoice_id: int):
        params = {"invoice_id": invoice_id}
        return self._request("POST", "deleteInvoice", params)

    def create_check(self, asset: str, amount: str, pin_to_user_id: int = None, pin_to_username: str = None):
        params = {
            "asset": asset,
            "amount": amount,
            "pin_to_user_id": pin_to_user_id,
            "pin_to_username": pin_to_username
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("POST", "createCheck", params)

    def delete_check(self, check_id: int):
        params = {"check_id": check_id}
        return self._request("POST", "deleteCheck", params)

    def transfer(self, user_id: int, asset: str, amount: str, spend_id: str, comment: str = None,
                 disable_send_notification: bool = False):
        params = {
            "user_id": user_id,
            "asset": asset,
            "amount": amount,
            "spend_id": spend_id,
            "comment": comment,
            "disable_send_notification": disable_send_notification
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("POST", "transfer", params)

    def get_invoices(self, asset: str = None, fiat: str = None, invoice_ids: str = None, status: str = None,
                     offset: int = 0, count: int = 100):
        params = {
            "asset": asset,
            "fiat": fiat,
            "invoice_ids": invoice_ids,
            "status": status,
            "offset": offset,
            "count": count
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("GET", "getInvoices", params)

    def get_checks(self, asset: str = None, check_ids: str = None, status: str = None, offset: int = 0,
                   count: int = 100):
        params = {
            "asset": asset,
            "check_ids": check_ids,
            "status": status,
            "offset": offset,
            "count": count
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("GET", "getChecks", params)

    def get_transfers(self, asset: str = None, transfer_ids: str = None, offset: int = 0, count: int = 100):
        params = {
            "asset": asset,
            "transfer_ids": transfer_ids,
            "offset": offset,
            "count": count
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("GET", "getTransfers", params)

    def get_balance(self):
        return self._request("GET", "getBalance")

    def get_exchange_rates(self):
        return self._request("GET", "getExchangeRates")

    def get_currencies(self):
        return self._request("GET", "getCurrencies")

    def get_stats(self, start_at: str = None, end_at: str = None):
        params = {
            "start_at": start_at,
            "end_at": end_at
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("GET", "getStats", params)

