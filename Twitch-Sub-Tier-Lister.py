import requests
import json

# Configuration
CLIENT_ID = ''
ACCESS_TOKEN = ''
BROADCASTER_ID = ''

def get_subscribers(broadcaster_id, client_id, access_token):
    """
    Fetch all subscribers for a broadcaster from the Twitch API.
    
    Args:
        broadcaster_id: The broadcaster's user ID
        client_id: Your Twitch application client ID
        access_token: OAuth access token with channel:read:subscriptions scope
    
    Returns:
        List of subscriber dictionaries
    """
    url = 'https://api.twitch.tv/helix/subscriptions'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'broadcaster_id': broadcaster_id,
        'first': 100  # Max results per page
    }
    
    all_subscribers = []
    
    while True:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        subscribers = data.get('data', [])
        all_subscribers.extend(subscribers)
        
        # Check if there are more pages
        pagination = data.get('pagination', {})
        cursor = pagination.get('cursor')
        
        if not cursor:
            break
        
        params['after'] = cursor
    
    return all_subscribers

def display_subscribers(subscribers):
    """Display subscriber information in a readable format."""
    tier_names = {
        '1000': 'Tier 1',
        '2000': 'Tier 2',
        '3000': 'Tier 3'
    }
    
    print(f"\nTotal Subscribers: {len(subscribers)}\n")
    print(f"{'Username':<25} {'Tier':<10} {'Gift?'}")
    print("-" * 50)
    
    for sub in subscribers:
        username = sub['user_name']
        tier = tier_names.get(sub['tier'], sub['tier'])
        is_gift = "Yes" if sub['is_gift'] else "No"
        
        print(f"{username:<25} {tier:<10} {is_gift}")
    
    # Summary by tier
    print("\n" + "="*50)
    print("Summary by Tier:")
    tier_counts = {}
    for sub in subscribers:
        tier = tier_names.get(sub['tier'], sub['tier'])
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
    
    for tier, count in sorted(tier_counts.items()):
        print(f"  {tier}: {count}")

def main():
    print("Fetching subscribers from Twitch API...")
    
    subscribers = get_subscribers(BROADCASTER_ID, CLIENT_ID, ACCESS_TOKEN)
    
    if subscribers:
        display_subscribers(subscribers)
        
        # Optionally save to JSON file
        with open('subscribers.json', 'w') as f:
            json.dump(subscribers, f, indent=2)
        print("\nData saved to subscribers.json")
    else:
        print("No subscribers found or error occurred.")

if __name__ == '__main__':
    main()
