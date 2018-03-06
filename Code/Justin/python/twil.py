from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC89d0fd5dff581ec57fe20430868376b5"
auth_token = "b15cccb7a26aa86b42a5f14ebccf23cf"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+14135193798",
    from_="+15005550006",
    body="Hello there!")

# +15005550006