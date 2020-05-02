ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'
TELEMETRY_DELTA = 20 * 60 # seconds
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_TELEMETRY_LAST_SENT = 'telemetry_sent_time' # integer
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to Gavel.

**Please read this important message carefully before continuing.**

Have you read our training slides? It won't take long: [give it a read
here](https://tiny.cc/codevid19-judges-training).

Gavel is based on the model of pairwise comparison. You'll start off by
looking at a single submission, and then for every submission after that,
you'll decide whether it's better or worse than the one you looked at
**immediately beforehand**.

If at any point, you can't find a particular submission, you can click the
'Skip' button and you will be assigned a new project. **Please don't skip
unless absolutely necessary.**

Gavel makes it really simple for you to submit votes, but please think hard
before you vote. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to Gavel!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to Gavel, the online expo judging system. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
You've made it to the end!

Thank you for taking the time to judge CODEVID-19's Qualifying Round
submissions. We couldn't have done it without you.

For those who are being considered for Lead Judging positions, the organizers
will be in touch with you soon.

To all, we hope you stay tuned for details
on the Final Ceremonies happening Saturday, May 16 at 17:00 UTC!
'''.strip()
