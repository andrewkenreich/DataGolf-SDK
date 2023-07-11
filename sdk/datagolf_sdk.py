import requests


class DataGolfSDK:
    def __init__(self, api_token):
        """
        Initialize the DataGolfSDK with the base URL and API token.

        Args:
            base_url (str): The base URL of the DataGolf API.
            api_token (str): Your DataGolf API token.
        """
        self.base_url = "https://feeds.datagolf.com"
        self.api_token = api_token

    def make_request(self, endpoint, params=None):
        """
        Make a request to the DataGolf API.

        Args:
            endpoint (str): The API endpoint.
            params (dict, optional): Query parameters. Defaults to None.

        Returns:
            dict or None: The JSON response from the API or None if an error occurred.
        """
        params = params or {}
        params["key"] = self.api_token

        url = f"{self.base_url}/{endpoint}"

        print(url)
        response = requests.get(url, params=params)

        if response.status_code == 200 and params["file_format"] == "json":
            return response.json()
        if response.status_code == 200 and params["file_format"] == "csv":
            return response.text
        else:
            # Handle error cases here
            print(
                "Something went wrong with the request : Error "
                + str(response.status_code)
                + " : "
                + response.text
            )
            return None

    def get_player_list(self, file_format="json"):
        """
        Get the list of players who have played on a major tour since 2018 or are playing this week.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The player list or None if an error occurred.
        """
        endpoint = f"get-player-list"
        params = {"file_format": file_format}
        return self.make_request(endpoint, params)

    def get_tour_schedules(self, tour, file_format="json"):
        """
        Get the current season schedules for primary tours.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The tour schedules or None if an error occurred.
        """
        endpoint = f"get-schedule"
        params = {"tour": tour, "file_format": file_format}
        return self.make_request(endpoint, params)

    def get_field_updates(self, tour, file_format="json"):
        """
        Get up-to-the-minute field updates for tour events.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"field-updates"
        params = {"tour": tour, "file_format": file_format}
        return self.make_request(endpoint, params)

    def get_dg_rankings(self, file_format="json"):
        """
        Returns the top 500 players in the current DG rankings, along with each player's skill estimate and respective OWGR rank.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/get-dg-rankings"
        params = {"file_format": file_format}
        return self.make_request(endpoint, params)

    def get_pre_tournament_predictions(
        self, tour, add_position, odds_format, file_format="json"
    ):
        """
        Returns full-field probabilistic forecasts for the upcoming tournament on PGA, European, and Korn Ferry Tours from both our baseline and baseline + course history & fit models. Probabilities provided for various finish positions (make cut, top 20, top 5, win, etc.).

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            add_position (str): Whether to add position to the output - yes (default), no.
            odds_format (str): The desired odds format - american (default), decimal, fractional.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/pre-tournament"
        params = {
            "tour": tour,
            "add_position": add_position,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_pre_tournament_predictions_archive(
        self, event_id, year, odds_format, file_format="json"
    ):
        """
        Historical archive of our PGA Tour pre-tournament predictions.

        Args:
            event_id (str): The desired event id.
            year (str): The desired year.
            odds_format (str): The desired odds format - american (default), decimal, fractional.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/pre-tournament-archive"
        params = {
            "event_id": event_id,
            "year": year,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_player_skill_decompositions(self, tour, file_format="json"):
        """
        Returns a detailed breakdown of every player's strokes-gained prediction for upcoming PGA and European Tour tournaments.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/player-decompositions"
        params = {"tour": tour, "file_format": file_format}
        return self.make_request(endpoint, params)

    def get_player_skill_ratings(self, display, file_format="json"):
        """
        Returns our estimate and rank for each skill for all players with sufficient Shotlink measured rounds (at least 30 rounds in the last year or 50 in the last 2 years).

        Args:
            display (str): The desired display - skill (default), rank.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/skill-ratings"
        params = {"display": display, "file_format": file_format}
        return self.make_request(endpoint, params)

    def get_detailed_approach_skill(self, period, file_format="json"):
        """
        Returns detailed player-level approach performance stats (strokes-gained per shot, proximity, GIR, good shot rate, poor shot avoidance rate) across various yardage/lie buckets.

        Args:
            period (str): The desired period - l24 (last 24 months) (default), l12 (last 12 months), ytd (year to date).
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/approach-skill"
        params = {"period": period, "file_format": file_format}
        return self.make_request(endpoint, params)

    def get_fanatasy_projection_defaults(self, tour, site, slate, file_format="json"):
        """
        Returns our default fantasy projections for main, showdown, late showdown, weekend, and captain mode contests at Draftkings, Fanduel, and Yahoo. Currently, Fanduel and Yahoo projections are only provided for main contests.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            site (str): The desired site - dk (default), fd, yh.
            slate (str): The desired slate - main (default), showdown, late, weekend, captain.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/fantasy-projection-defaults"
        params = {
            "tour": tour,
            "site": site,
            "slate": slate,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_live_model_predictions(
        self, tour, dead_heat, odds_format, file_format="json"
    ):
        """
        Returns live (updating at 5 minute intervals) finish probabilities for ongoing PGA and European Tour tournaments.

        Args:
            tour (str): The desired tour - pga (default), euro, opp (opposite field PGA TOUR event), kft, alt.
            dead_heat (str): Adjusts odds for dead-heat rules - no (default), yes.
            odds_format (str): The desired odds format - percent (default), american, decimal, fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/in-play"
        params = {
            "tour": tour,
            "dead_heat": dead_heat,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_live_tournament_stats(self, stats, round, display, file_format="json"):
        """
        Returns live strokes-gained and traditional stats for every player during PGA Tour tournaments.

        Args:
            stats (str): Comma-separated list of statistics to be returned.
            round (str): Specifies the round.
            display (str): Specifies how stats are displayed.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/live-tournament-stats"
        params = {
            "stats": stats,
            "round": round,
            "display": display,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_live_hole_scoring_distribution(self, tour, file_format="json"):
        """
        Returns live hole scoring averages and distrubutions (birdies, pars, bogeys, etc.) broken down by tee time wave.

        Args:
            tour (str): The desired tour - pga (default), euro, opp (opposite field PGA TOUR event), kft, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/live-hole-stats"
        params = {
            "tour": tour,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_outright_odds(self, tour, market, odds_format, file_format="json"):
        """
        Returns the most recent win, top 5, top 10, top 20, make/miss cut, and first round leader odds offered at 11 sportsbooks alongside the corresponding predictions from our model.

        Args:
            tour (str): Specifies the tour - pga (default), euro, kft, opp (opposite field PGA TOUR event), alt.
            market (str): Specifies the match-up market - win, top_5, top_10, top_20, mc, make_cut, frl.
            odds_format (str): Specifies the odds format - percent (default), american, decimal, fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"betting-tools/outrights"
        params = {
            "tour": tour,
            "market": market,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_matchup_odds(self, tour, market, odds_format, file_format="json"):
        """
        Returns the most recent tournament match-up, round match-up, and 3-ball odds offered at 8 sportsbooks alongside the corresponding prediction from our model.

        Args:
            tour (str): Specifies the tour - pga (default), euro, opp (opposite field PGA TOUR event), alt.
            market (str): Specifies the match-up market - tournament_matchups, round_matchups, 3_balls.
            odds_format (str): Specifies the odds format - percent (default), american, decimal, fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"betting-tools/matchups"
        params = {
            "tour": tour,
            "market": market,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_matchup_odds_all_pairings(
        self, tour, market, odds_format, file_format="json"
    ):
        """
        Returns the most recent tournament match-up, round match-up, and 3-ball odds offered at 8 sportsbooks alongside the corresponding prediction from our model.

        Args:
            tour (str): Specifies the tour - pga (default), euro, opp (opposite field PGA TOUR event), alt.
            market (str): Specifies the match-up market - tournament_matchups, round_matchups, 3_balls.
            odds_format (str): Specifies the odds format - percent (default), american, decimal, fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"betting-tools/matchups-all-pairings"
        params = {
            "tour": tour,
            "market": market,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_odds_data_event_ids(self, tour, file_format="json"):
        """
        Returns the list of tournaments (and corresponding IDs) that are available through the historical odds/predictions endpoints. Use this endpoint to fill the event_id and year query parameters in the Archived Predictions, Historical Outrights, and Historical Matchups & 3-Balls endpoints.

        Args:
            tour (str): Specifies the tour. pga (default), euro, alt
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-odds/event-list"
        params = {
            "tour": tour,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_outrights(
        self,
        tour,
        event_id,
        year,
        market,
        book,
        odds_format,
        file_format="json",
    ):
        """
        Returns opening and closing lines in various markets (win, top 5, make cut, etc.) at 11 sportsbooks. Bet outcomes also included.

        Args:
            tour (str): Specifies the tour. pga (default), euro, alt
            event_id (str): Specifies the event.
            year (str): Specifies the calendar year (not season) of the event. 2019, 2020, 2021, 2022, 2023 (default)
            market (str): Specifies the market/finish position.
            book (str): Specifies the bookmaker.
            odds_format (str): Specifies the odds format.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-odds/outrights"
        params = {
            "tour": tour,
            "event_id": event_id,
            "year": year,
            "market": market,
            "book": book,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_matchups_3balls(
        self,
        tour,
        event_id,
        year,
        book,
        odds_format,
        file_format="json",
    ):
        """
        Returns opening and closing lines for tournament match-ups, round match-ups, and 3-balls at 12 sportsbooks. Bet outcomes also included.

        Args:
            tour (str): Specifies the tour. pga (default), euro, alt
            event_id (str): Specifies the event.
            year (str): Specifies the calendar year (not season) of the event. 2019, 2020, 2021, 2022, 2023 (default)
            book (str): Specifies the bookmaker.
            odds_format (str): Specifies the odds format.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-odds/matchups"
        params = {
            "tour": tour,
            "event_id": event_id,
            "year": year,
            "book": book,
            "odds_format": odds_format,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_dfs_data_event_ids(self, file_format="json"):
        """
        Returns the list of tournaments (and corresponding IDs) that are available through the historical DFS data API endpoint. Use this endpoint to fill the event_id and year query parameters in the DFS Points endpoint.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-dfs-data/event-list"
        params = {
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)

    def get_dfs_points_salaries(
        self, tour, site, event_id, year, market, file_format="json"
    ):
        """
        Returns salaries and ownerships alongside event-level finish, hole, and bonus scoring for PGA and European Tour events.

        Args:
            tour (str): Specifies the tour. pga, euro
            site (str): Specifies the site. draftkings (default), fanduel
            event_id (str): Specifies the event.
            year (str): Specifies the calendar year (not season) of the event. 2019, 2020, 2021, 2022, 2023 (default)
            market (str): Specifies the market/finish position.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-dfs-data/points"
        params = {
            "tour": tour,
            "site": site,
            "event_id": event_id,
            "year": year,
            "market": market,
            "file_format": file_format,
        }
        return self.make_request(endpoint, params)
