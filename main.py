import requests

post = "https://www.facebook.com/100090346516171/posts/pfbid038EkQkP2nTe5K135tiSLPst7tdfiEA1uKCzRderNDBC5Y6tE3rFQHh5CZTt1DHTx1l/?app=fbl"
token = "EAAGNO4a7r2wBO96hjN3RvlkwwyMUwE1yB6o8j1kRhUVRvQmRAtkIHPkAlZCjZCPkHmKkR0IJjcxXYJ4uaA06Ev0VMxUWCl24hg5iZAMpM2zOmpCC8ZAtgKe8lD9KhHKYLItYtV2AlVsNlZB1ZBtUjgVzZBfUeMCKk16xQcM7O2lt43fkOdvMsZCWGbfJdygZBIGlJAwZDZD"

res = requests.post(f'https://graph.facebook.com/v20.0/{post}/comments?message=Hwllo&access_token={token}')
print(res.json())
