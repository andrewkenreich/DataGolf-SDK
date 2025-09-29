# DataGolf SDK

This is a comprehensive Python SDK implementation for the [DataGolf API](https://datagolf.com/api-access). This SDK provides complete coverage of all DataGolf API endpoints across six main categories.

## API Coverage

✅ **Complete Coverage of All DataGolf API Endpoints:**

### General Use (3/3)
- Player List & IDs
- Tour Schedules  
- Field Updates

### Model Predictions (7/7)
- Data Golf Rankings
- Pre-Tournament Predictions
- Pre-Tournament Predictions Archive
- Player Skill Decompositions
- Player Skill Ratings
- Detailed Approach Skill
- Fantasy Projection Defaults

### Live Model Endpoints (3/3)
- Live Model Predictions
- Live Strokes-Gained (deprecated but available)
- Live Tournament Stats
- Live Hole Scoring Distributions

### Betting Tools (3/3)
- Outright (Finish Position) Odds
- Match-Up & 3-Ball Odds
- Match-Up & 3-Ball Data Golf Odds — All Pairings

### Historical Raw Data (2/2)
- Historical Raw Data Event IDs
- Round Scoring, Stats & Strokes Gained

### Historical Betting Odds (2/2)
- Historical Odds Data Event IDs
- Historical Outrights
- Historical Match-Ups & 3-Balls

### Historical DFS Data (2/2)
- Historical DFS Data Event IDs
- DFS Points & Salaries

## Prerequisites

- Python 3 (version >= 3.7)
- A DataGolf Scratch PLUS membership
- `requests` library

## Installation and Setup

Clone the repo and install dependencies:

```bash
pip install requests
```

Create a .env file with your API key in the root:
```
apikey = "your_api_key_here"
```

## Usage and Examples

The main.py file has a basic usage example for the SDK. All endpoints support both JSON and CSV output formats.

### Basic Usage
```python
from sdk.datagolf_sdk import DataGolfSDK

# Initialize with your API key
dg = DataGolfSDK("your_api_key_here")

# Get player list
players = dg.get_player_list()

# Get pre-tournament predictions for PGA Tour
predictions = dg.get_pre_tournament_predictions(tour="pga")

# Get live tournament stats
live_stats = dg.get_live_tournament_stats(
    stats=["sg_total", "sg_putt"], 
    round="event_cumulative", 
    display="value"
)
```

# License

MIT

