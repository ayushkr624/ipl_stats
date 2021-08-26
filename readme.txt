1.) Create Virtual Enviornment and Activate it
2.) Install packages from requirement.txt Using command - pip install -r requirement.txt
3.) Create a database with name as ipl_stats
4.) Change the Mysql credentials in settings.py
5.) As makemigrations has already been done so we need to just migrate it using command -  python manage.py migrate
6.) If asked to load to static files then we have to run command - python manage.py collectstatic
7.) Lastly we can run our application in local using command - python manage.py runserver

Question and respective Tile in Application:-
Question                                                                                      Tile
•	Top 4 teams in terms of wins                                                              TOP 4 Winner
•	Which team won the most number of tosses in the season                                    TOP Toss Winner
•	Which player won the maximum number of Player of the Match awards in the whole season     Max Player of Match
•	Which team won max matches in the whole season                                            Top Winner Team
•	Which location has the most number of wins for the top team                               Location Top Winner Team
•	Which % of teams decided to bat when they won the toss                                    Percentage Toss Winner Batting Team
•	Which location hosted most number of matches                                              Top Hosted Location
•	Which team won by the highest margin of runs  for the season                              Highest margin team winner
•	Which team won by the highest number of wickets for the season                            Highest Wicket Taker Winner Team
•	How many times has a team won the toss and the match                                      Toss Winner Match Winner Team