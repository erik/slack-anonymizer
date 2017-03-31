# Slack Anonymizer

![](https://thumbs.gfycat.com/VigorousHastyChimpanzee-size_restricted.gif)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Ask questions or leave comments anonymously on slack.

# Deployment (with Heroku)

1. Create a [new Slack /slash command](https://my.slack.com/services/new/slash-commands)
   for your account.
2. Create a [new Slack incoming webhook](https://my.slack.com/services/new/incoming-webhook/)
   which posts to the desired recipient (direct message, public / private channel, etc.)
3. Click the Deploy to Heroku button, paste in the Token from the Slack slash command and
   fill in the webhook url.
4. Deploy the Heroku app and wait for it to come online
5. Paste the https URL from heroku into the URL field of the slash command. Make sure
   Method is set to POST and save your changes.
6. Done!
