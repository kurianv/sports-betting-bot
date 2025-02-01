# Sport Betting Bot

This Python script designed to fetch and analyze sports betting odds from the [The Odds API](https://the-odds-api.com/). The script focuses on NFL and provides recommendations on whether to place bets based on arbitrage opportunities.

## Features

- **Fetching Odds**: The script fetches live odds for NFL from multiple sportsbooks.
- **Arbitrage Calculation**: It calculates arbitrage opportunities to determine if a profitable bet is possible.
- **Bet Recommendations**: Provides recommendations on whether to bet and which sportsbook to use for each team.
- **Email Notifications**: Sends an email with the betting recommendations.

## Requirements

To run this script, you need the following Python packages:

- `requests`
- `datetime`
- `secure-smtplib`

You can install these packages using pip:

```bash
pip install requests datetime secure-smtplib
```

## Usage

1. **API Key**: Replace the `API_KEY` variable with your own API key from [The Odds API](https://the-odds-api.com/).

2. **Running the Script**:
   - The script will fetch the latest odds for NFL games.
   - It will analyze the odds to find arbitrage opportunities.
   - If an arbitrage opportunity is found, it will recommend bets and send an email with the recommendations.

3. **Email Configuration**:
   - Replace the `sender`, `receiver`, and `password` variables with your email credentials.
   - Ensure that you have enabled "Allow less secure apps" in your Gmail settings if using a Gmail account.

## Functions

- **game_odds()**: Prints the details of each game, including the teams and the odds offered by different sportsbooks.
- **feasibleBets()**: Analyzes the odds to find arbitrage opportunities and generates a recommendation message.
- **toDecimals(num)**: Converts American odds to decimal odds.
- **toAmerican(num)**: Converts decimal odds to American odds.
- **arbi(out1, out2)**: Calculates the arbitrage value for two outcomes.
- **betValue(odds, total)**: Calculates the bet value based on the odds and total arbitrage value.

## Example Output

The script will output the betting recommendations to the console and send an email with the same information. Here is an example of the console output:

```
For the Indiana Pacers v. Atlanta Hawks game, WE DON'T RECOMMEND TO BET. NO sportbook offers odds to earn profit.

For the Utah Jazz v. Orlando Magic game, WE DON'T RECOMMEND TO BET. NO sportbook offers odds to earn profit.

...

Programmed by Kurian Vadakara. 
SharperBets
```

## Email Notification

The script will send an email with the betting recommendations to the specified recipients. The email will look like this:

```
From: sender@gmail.com
To: reciever4@gmail.com
Subject: IMPORTANT: Bets to Make for NFL

For the Indiana Pacers v. Atlanta Hawks game, WE DON'T RECOMMEND TO BET. NO sportbook offers odds to earn profit.

For the Utah Jazz v. Orlando Magic game, WE DON'T RECOMMEND TO BET. NO sportbook offers odds to earn profit.

...

Programmed by Kurian Vadakara. 
SharperBets
```

## Notes

- The script is designed for educational purposes and should be used with caution.
- Betting involves risk, and it is important to gamble responsibly.
- The script assumes that the user has access to The Odds API with a valid API key, and Google App Password to access Gmail.

## Author

- **Kurian Vadakara**
