# cryptopayclient

`cryptopayclient` is a Python library for interacting with the CryptoBot API.

## Installation

To install the library, use pip:

```bash
pip install requests
git clone https://github.com/andrewzaycew/cryptopayclient
cd cryptopayclient
pip install ./
```
or

```bash
pip install cryptopayclient
```

## Usage

### Initializing the Client

```python
from cryptopayclient import CryptoBotClient

api_token = "YOUR_API_TOKEN"
client = CryptoBotClient(api_token=api_token, use_testnet=True)
```

### Methods

#### `get_me`

Tests the authentication token of your app.

```python
result = client.get_me()
print(result)
```

#### `create_invoice`

Creates a new invoice.

**Parameters:**

- `amount` (str): The amount of the invoice.
- `currency_type` (str, optional): The type of currency, can be "crypto" or "fiat". Defaults to "crypto".
- `asset` (str, optional): The cryptocurrency code, required if `currency_type` is "crypto".
- `fiat` (str, optional): The fiat currency code, required if `currency_type` is "fiat".
- `accepted_assets` (str, optional): List of cryptocurrency codes separated by commas that can be used to pay the invoice.
- `description` (str, optional): Description of the invoice.
- `hidden_message` (str, optional): Text of the message presented to the user after the invoice is paid.
- `paid_btn_name` (str, optional): Label of the button presented to the user after the invoice is paid.
- `paid_btn_url` (str, optional): URL opened by the button presented to the user.
- `payload` (str, optional): Any data you want to attach to the invoice.
- `allow_comments` (bool, optional): Allow the user to add a comment to the payment. Defaults to `True`.
- `allow_anonymous` (bool, optional): Allow the user to pay the invoice anonymously. Defaults to `True`.
- `expires_in` (int, optional): Payment time limit for the invoice in seconds.

**Example:**

```python
invoice = client.create_invoice(amount="100.00", asset="BTC", description="Test Invoice")
print(invoice)
```

#### `delete_invoice`

Deletes an invoice by ID.

**Parameters:**

- `invoice_id` (int): The ID of the invoice.

**Example:**

```python
result = client.delete_invoice(invoice_id=123456)
print(result)
```

#### `create_check`

Creates a new check.

**Parameters:**

- `asset` (str): The cryptocurrency code.
- `amount` (str): The amount of the check.
- `pin_to_user_id` (int, optional): The ID of the user who will be able to activate the check.
- `pin_to_username` (str, optional): The username of the user who will be able to activate the check.

**Example:**

```python
check = client.create_check(asset="BTC", amount="100.00")
print(check)
```

#### `delete_check`

Deletes a check by ID.

**Parameters:**

- `check_id` (int): The ID of the check.

**Example:**

```python
result = client.delete_check(check_id=123456)
print(result)
```

#### `transfer`

Sends coins from your app's balance to a user.

**Parameters:**

- `user_id` (int): The ID of the user in Telegram.
- `asset` (str): The cryptocurrency code.
- `amount` (str): The amount of the transfer.
- `spend_id` (str): A unique UTF-8 string for idempotent requests.
- `comment` (str, optional): Comment for the transfer.
- `disable_send_notification` (bool, optional): Pass `True` to not send a notification to the user about the transfer. Defaults to `False`.

**Example:**

```python
transfer = client.transfer(user_id=123456789, asset="BTC", amount="50.00", spend_id="unique_id_123")
print(transfer)
```

#### `get_invoices`

Gets a list of invoices created by your app.

**Parameters:**

- `asset` (str, optional): The cryptocurrency code.
- `fiat` (str, optional): The fiat currency code.
- `invoice_ids` (str, optional): List of invoice IDs separated by commas.
- `status` (str, optional): Status of invoices to be returned. Available statuses: "active", "paid". Defaults to all statuses.
- `offset` (int, optional): Offset for returning a specific subset of invoices. Defaults to `0`.
- `count` (int, optional): Number of invoices to be returned. Values between 1-1000. Defaults to `100`.

**Example:**

```python
invoices = client.get_invoices()
print(invoices)
```

#### `get_checks`

Gets a list of checks created by your app.

**Parameters:**

- `asset` (str, optional): The cryptocurrency code.
- `check_ids` (str, optional): List of check IDs separated by commas.
- `status` (str, optional): Status of checks to be returned. Available statuses: "active", "activated". Defaults to all statuses.
- `offset` (int, optional): Offset for returning a specific subset of checks. Defaults to `0`.
- `count` (int, optional): Number of checks to be returned. Values between 1-1000. Defaults to `100`.

**Example:**

```python
checks = client.get_checks()
print(checks)
```

#### `get_transfers`

Gets a list of transfers created by your app.

**Parameters:**

- `asset` (str, optional): The cryptocurrency code.
- `transfer_ids` (str, optional): List of transfer IDs separated by commas.
- `offset` (int, optional): Offset for returning a specific subset of transfers. Defaults to `0`.
- `count` (int, optional): Number of transfers to be returned. Values between 1-1000. Defaults to `100`.

**Example:**

```python
transfers = client.get_transfers()
print(transfers)
```

#### `get_balance`

Gets the balances of your app.

**Example:**

```python
balance = client.get_balance()
print(balance)
```

#### `get_exchange_rates`

Gets the exchange rates of supported currencies.

**Example:**

```python
exchange_rates = client.get_exchange_rates()
print(exchange_rates)
```

#### `get_currencies`

Gets a list of supported currencies.

**Example:**

```python
currencies = client.get_currencies()
print(currencies)
```

#### `get_stats`

Gets app statistics.

**Parameters:**

- `start_at` (str, optional): The date from which to start calculating statistics in ISO 8601 format.
- `end_at` (str, optional): The date on which to finish calculating statistics in ISO 8601 format.

**Example:**

```python
stats = client.get_stats(start_at="2023-01-01T00:00:00Z", end_at="2023-01-31T23:59:59Z")
print(stats)
```

