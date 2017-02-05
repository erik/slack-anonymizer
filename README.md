# Slack Anonymizer

![](https://thumbs.gfycat.com/VigorousHastyChimpanzee-size_restricted.gif)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Ask questions or leave comments anonymously on slack.

# Deployment (with Heroku)

1. Create a [new Slack /slash command](https://my.slack.com/services/new/slash-commands)
   for your account.
2. Click the Deploy to Heroku button, paste in the Token from the Slack slash command and
   fill in the channel whitelist.
3. Deploy the Heroku app and wait for it to come online
4. Paste the https URL from heroku into the URL field of the slash command. Make sure 
   Method is set to POST and save your changes.
5. Done!
