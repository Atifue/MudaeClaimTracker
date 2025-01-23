# MudaeClaimTracker

A simple Discord bot that tracks all Mudae claim messages and forwards them to a separate channel. It also includes a `$qotd` command to display a random quote.

## Features

- **Claim Tracking**: Stores and forwards all Mudae claim messages to a specified channel.
- **Quote of the Day (`$qotd`) Command**: Returns a random quote from an array of pre-defined quotes (easily customizable).

## How to Set Up

1. **AWS Hosting (Optional):**
   - This bot can be hosted on an AWS EC2 instance for continuous operation.
   - If you're new to AWS, you can use a free `t2.micro` instance included with the AWS Free Tier.
   - Follow AWS setup documentation, or feel free to email me for specific questions.

2. **Edits Required in the Code:**
   - **Line 49**: Replace `channel_id` with the actual **18-digit channel ID** of the Discord channel where claim messages should be sent.
   - **Line 64**: Replace the `TOKEN` variable with your bot's **token**.
     - Ensure you store this token securely using environment variables (e.g., `.env` file) for production.

3. **Create and Configure Your Discord Bot:**
   - Create a developer account on Discord and create a new bot application.
   - Invite the bot to your server and grant it the following permissions:
     - **Read Messages**
     - **Send Messages**
   - Refer to [Discord's Developer Documentation](https://discord.com/developers/docs/intro) for detailed instructions.

4. **Customizing the Bot:**
   - **Quotes for `$qotd`**: You can modify the `quotes` array in the code to include your own quotes, fetch them from an API, or even sync them with a database for more dynamic content.

## Notes on Hosting

- To ensure the bot runs continuously, use a process monitor like `pm2` or configure a systemd service on your EC2 instance.
- Secure your bot's token by using environment variables and never hardcoding sensitive information.
  
## Additional Information

For more advanced functionality (like fetching quotes from an API or storing claims in a database), feel free to modify the code. The bot is designed to be simple yet flexible.

If you encounter any issues or have questions, feel free to contact me.

Thanks for checking out this project!

Happy coding,
Atif
