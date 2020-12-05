def token_request():
     # Request an IAM token from IBM Cloud IAM API

    # IAM token request documentation:
    # https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    payload = "my-payload"
    req = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data=payload,
        headers=headers
    )
    res = req.json()

    return res['token']
