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
        self.file_format = "json"

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

    def get_player_list(self, file_format=None):
        """
        Get the list of players who have played on a major tour since 2018 or are playing this week.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The player list or None if an error occurred.
        """
        endpoint = f"get-player-list"
        params = {"file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_tour_schedules(self, tour, file_format=None):
        """
        Get the current season schedules for primary tours.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The tour schedules or None if an error occurred.
        """
        endpoint = f"get-schedule"
        params = {"tour": tour, "file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_field_updates(self, tour: str, file_format=None):
        """
        Get up-to-the-minute field updates for tour events.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"field-updates"
        params = {"tour": tour, "file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_dg_rankings(self, file_format=None):
        """
        Returns the top 500 players in the current DG rankings, along with each player's skill estimate and respective OWGR rank.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/get-dg-rankings"
        params = {"file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_pre_tournament_predictions(
        self,
        tour: str = None,
        add_position: str = None,
        dead_heat: str = None,
        odds_format: str = None,
        file_format=None,
    ):
        """
        Returns full-field probabilistic forecasts for the upcoming tournament on PGA, European, and Korn Ferry Tours from both our baseline and baseline + course history & fit models. Probabilities provided for various finish positions (make cut, top 20, top 5, win, etc.).

        Args:
            tour (str, optional): The desired tour - pga (default), euro, kft, opp (opposite field PGA TOUR event), alt.
            add_position (str, optional): Comma-separated list of additional positions to include in output. Defaults are win, top 5, top 10, top 20, make cut. Options : 1, 2, 3 .... 48, 49, 50
            dead_heat (str, optional): Adjusts odds for dead-heat rules - yes (default), no.
            odds_format (str, optional): The desired odds format - percent (default), american, decimal, fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/pre-tournament"
        params = {
            "file_format": file_format or self.file_format,
        }
        if tour:
            params["tour"] = tour
        if add_position:
            params["add_position"] = add_position
        if dead_heat:
            params["dead_heat"] = dead_heat
        if odds_format:
            params["odds_format"] = odds_format
        return self.make_request(endpoint, params)

    def get_pre_tournament_predictions_archive(
        self, event_id: str, year: int, odds_format: str = None, file_format=None
    ):
        """
        Historical archive of our PGA Tour pre-tournament predictions.

        Args:
            event_id (str): The desired event id.
            year (int): The desired year (format - YYYY)
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_player_skill_decompositions(self, tour: str, file_format=None):
        """
        Returns a detailed breakdown of every player's strokes-gained prediction for upcoming PGA and European Tour tournaments.

        Args:
            tour (str): The desired tour - pga (default), euro, kft, opp, alt.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/player-decompositions"
        params = {"tour": tour, "file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_player_skill_ratings(self, display: str, file_format=None):
        """
        Returns our estimate and rank for each skill for all players with sufficient Shotlink measured rounds (at least 30 rounds in the last year or 50 in the last 2 years).

        Args:
            display (str): The desired display - skill (default), rank.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/skill-ratings"
        params = {"display": display, "file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_detailed_approach_skill(self, period: str, file_format=None):
        """
        Returns detailed player-level approach performance stats (strokes-gained per shot, proximity, GIR, good shot rate, poor shot avoidance rate) across various yardage/lie buckets.

        Args:
            period (str): The desired period - l24 (last 24 months) (default), l12 (last 12 months), ytd (year to date).
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/approach-skill"
        params = {"period": period, "file_format": file_format or self.file_format}
        return self.make_request(endpoint, params)

    def get_fantasy_projection_defaults(
        self, tour: str = None, site: str = None, slate: str = None, file_format=None
    ):
        """
        Returns our default fantasy projections for main, showdown, late showdown, weekend, and captain mode contests at Draftkings, Fanduel, and Yahoo. Currently, Fanduel and Yahoo projections are only provided for main contests.

        Args:
            tour (str, optional): The desired tour - pga (default), euro, opp (opposite field PGA TOUR event), alt.
            site (str, optional): The desired site - draftkings (default), fanduel, yahoo.
            slate (str, optional): The desired slate - main (default), showdown, showdown_late, weekend, captain.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"preds/fantasy-projection-defaults"
        params = {
            "file_format": file_format or self.file_format,
        }
        if tour:
            params["tour"] = tour
        if site:
            params["site"] = site
        if slate:
            params["slate"] = slate
        return self.make_request(endpoint, params)

    def get_live_model_predictions(
        self, tour: str, dead_heat: str, odds_format: str = None, file_format=None
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_live_strokes_gained(self, sg: str = None, file_format=None):
        """
        Returns a live strokes-gained breakdown for every player during PGA Tour tournaments.
        Note: This endpoint is marked as DEPRECATED - use Live Tournament Stats going forward.

        Args:
            sg (str, optional): Specifies the strokes-gained "view" - raw (default), relative (returns strokes-gained values relative to our prediction).
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The live strokes-gained data or None if an error occurred.
        """
        endpoint = f"preds/live-strokes-gained"
        params = {
            "file_format": file_format or self.file_format,
        }
        if sg:
            params["sg"] = sg
        return self.make_request(endpoint, params)

    def get_live_tournament_stats(
        self, stats: list, round: int, display: str, file_format=None
    ):
        """
        Returns live strokes-gained and traditional stats for every player during PGA Tour tournaments.

        Args:
            stats (list): Comma-separated list of statistics to be returned. (sg_putt, sg_arg, sg_app, sg_ott, sg_t2g, sg_bs, sg_total, distance, accuracy, gir, prox_fw, prox_rgh, scrambling)
            round (int): Specifies the round.
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_live_hole_scoring_distribution(self, tour: str, file_format=None):
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_outright_odds(
        self, tour: str, market: str, odds_format: str = None, file_format=None
    ):
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_matchup_odds(
        self, tour: str, market: str, odds_format: str = None, file_format=None
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
        endpoint = f"betting-tools/matchups"
        params = {
            "tour": tour,
            "market": market,
            "odds_format": odds_format,
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_matchup_odds_all_pairings(
        self, tour: str = None, odds_format: str = None, file_format=None
    ):
        """
        Returns Data Golf matchup / 3-ball odds for every pairing in the next round of current PGA Tour and European Tour events.

        Args:
            tour (str, optional): Specifies the tour - pga (default), euro, opp, alt.
            odds_format (str, optional): Specifies the odds format - percent, american, decimal (default), fraction.
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"betting-tools/matchups-all-pairings"
        params = {
            "file_format": file_format or self.file_format,
        }
        if tour:
            params["tour"] = tour
        if odds_format:
            params["odds_format"] = odds_format
        return self.make_request(endpoint, params)

    def get_historical_raw_data_event_ids(self, file_format=None):
        """
        Returns the list of tournaments (and corresponding IDs) that are available through the historical raw data API endpoint. Use this endpoint to fill the event_id and year query parameters in the Round Scoring & Strokes Gained endpoint.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The event IDs or None if an error occurred.
        """
        endpoint = f"historical-raw-data/event-list"
        params = {
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_round_scoring_stats_strokes_gained(
        self,
        tour: str,
        event_id: str,
        year: int,
        file_format=None,
    ):
        """
        Returns round-level scoring, traditional stats, strokes-gained, and tee time data across 22 global tours.

        Args:
            tour (str): Specifies the tour. Hover over tour codes in table here to see full tour names. Options: pga, euro, kft, cha, jpn, anz, alp, champ, kor, ngl, bet, chn, afr, pgt, pgti, atvt, atgt, sam, ept, can, liv, mex
            event_id (str): Specifies the event. Use "all" to return every event for the given year and tour.
            year (int): Specifies the calendar year (not season) of the event. 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The round scoring data or None if an error occurred.
        """
        endpoint = f"historical-raw-data/rounds"
        params = {
            "tour": tour,
            "event_id": event_id,
            "year": year,
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_odds_data_event_ids(self, tour: str, file_format=None):
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_outrights(
        self: str,
        tour: str,
        event_id: str,
        year: int,
        market: str,
        book: str,
        odds_format: str = None,
        file_format=None,
    ):
        """
        Returns opening and closing lines in various markets (win, top 5, make cut, etc.) at 11 sportsbooks. Bet outcomes also included.

        Args:
            tour (str): Specifies the tour. pga (default), euro, alt
            event_id (str): Specifies the event.
            year (int): Specifies the calendar year (not season) of the event. 2019, 2020, 2021, 2022, 2023 (default)
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_matchups_3balls(
        self,
        tour: str,
        event_id: str,
        year: int,
        book: str,
        odds_format: str = None,
        file_format=None,
    ):
        """
        Returns opening and closing lines for tournament match-ups, round match-ups, and 3-balls at 12 sportsbooks. Bet outcomes also included.

        Args:
            tour (str): Specifies the tour. pga (default), euro, alt
            event_id (str): Specifies the event.
            year (int): Specifies the calendar year (not season) of the event. 2019, 2020, 2021, 2022, 2023 (default)
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
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_historical_dfs_data_event_ids(self, file_format=None):
        """
        Returns the list of tournaments (and corresponding IDs) that are available through the historical DFS data API endpoint. Use this endpoint to fill the event_id and year query parameters in the DFS Points endpoint.

        Args:
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-dfs-data/event-list"
        params = {
            "file_format": file_format or self.file_format,
        }
        return self.make_request(endpoint, params)

    def get_dfs_points_salaries(
        self,
        tour: str,
        event_id: str,
        year: int,
        site: str = None,
        file_format=None,
    ):
        """
        Returns salaries and ownerships alongside event-level finish, hole, and bonus scoring for PGA and European Tour events.

        Args:
            tour (str): Specifies the tour. pga, euro
            event_id (str): Specifies the event.
            year (int): Specifies the calendar year (not season) of the event. 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
            site (str, optional): Specifies the site. draftkings (default), fanduel
            file_format (str, optional): The desired file format of the response. Defaults to 'json' , csv.

        Returns:
            dict or None: The field updates or None if an error occurred.
        """
        endpoint = f"historical-dfs-data/points"
        params = {
            "tour": tour,
            "event_id": event_id,
            "year": year,
            "file_format": file_format or self.file_format,
        }
        if site:
            params["site"] = site
        return self.make_request(endpoint, params)
