# Twitch Sub Tier Lister

A simple Python script that fetches and displays all Twitch subscribers for a channel — grouped by their subscription tier (Tier 1, Tier 2, Tier 3), including whether each sub is gifted or not.

---

## Features
- Lists **all active subscribers** for a Twitch channel  
- Groups subscribers by **Tier 1 / Tier 2 / Tier 3**  
- Indicates whether each subscription was **gifted**  
- Prints summary counts by tier  
- Saves the full subscriber data as a `subscribers.json` file for later use  

---

## Requirements
- **Python 3.8+**  
- **Twitch Developer App** with the scope:
  ```
  channel:read:subscriptions
  ```
- A **User OAuth Access Token** for the broadcaster (or a bot with the correct permissions)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/twitch-sub-tier-lister.git
   cd twitch-sub-tier-lister
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Open the script and update your credentials:
   ```python
   CLIENT_ID = 'your_twitch_client_id'
   ACCESS_TOKEN = 'your_oauth_access_token'
   BROADCASTER_ID = 'your_twitch_user_id'
   ```

---

## Usage
Run the script from your terminal:

```bash
python Twitch-Sub-Tier-Lister.py
```

Example output:
```
Fetching subscribers from Twitch API...

Total Subscribers: 15

Username                  Tier       Gift?
--------------------------------------------------
user_one                  Tier 1     No
user_two                  Tier 2     Yes
user_three                Tier 3     No

==================================================
Summary by Tier:
  Tier 1: 10
  Tier 2: 3
  Tier 3: 2

Data saved to subscribers.json
```

---

## Output
The script will generate a file named `subscribers.json` containing all subscriber data in the format returned by Twitch’s [Helix Subscriptions API](https://dev.twitch.tv/docs/api/reference#get-broadcaster-subscriptions).

Example snippet:
```json
[
  {
    "user_name": "coolviewer",
    "tier": "1000",
    "is_gift": false
  },
  {
    "user_name": "superfan",
    "tier": "3000",
    "is_gift": true
  }
]
```

---

## How It Works
1. Uses the [Twitch Helix API](https://dev.twitch.tv/docs/api) endpoint `/helix/subscriptions`.  
2. Fetches up to 100 subs per request and automatically paginates through results.  
3. Displays formatted subscriber information and a tier summary.  
4. Optionally exports raw data to JSON for analytics or dashboards.  

---

## Notes
- You can retrieve your **Broadcaster ID** via:
  ```bash
  curl -H "Client-ID: YOUR_CLIENT_ID"        -H "Authorization: Bearer YOUR_ACCESS_TOKEN"        https://api.twitch.tv/helix/users
  ```
- Your `ACCESS_TOKEN` must include `channel:read:subscriptions` scope.  
- Tokens expire, so if you get a 401 error, re-authenticate.  

---

## Future Ideas
- Export to CSV  
- Filter by gifted subs  
- Discord or web dashboard integration  
- Add CLI arguments for credentials  

---

## License
MIT License © 2025 — rrittenhouse

---

