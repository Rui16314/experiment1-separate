SESSION_CONFIGS = [
    dict(
        name='first_price_auction',
        display_name="Session 1: First-Price Sealed Bid Auction",
        num_demo_participants=2,
        app_sequence=['first_price_auction'],
    ),
    dict(
        name='repeated_first_price_fixed',
        display_name="Session 2: Repeated First-Price Auction (Fixed Pair)",
        num_demo_participants=2,
        app_sequence=['repeated_first_price_fixed'],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01,
    participation_fee=0.00,
    doc="",
)

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'  # Change this before deploying!
DEMO_PAGE_INTRO_HTML = """<h1>ECON 3310 Auction Game</h1>"""
SECRET_KEY = 'your-secret-key'
INSTALLED_APPS = ['otree']
