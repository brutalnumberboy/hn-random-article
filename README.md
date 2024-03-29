# hn-random-article
A python script, which returns a random Hacker News article based on the query and parameters.

Usage python main.py [options]
    
Options:
    -h, --help  Show this help message
    -q, --query=QUERY  Optional query for stories 
    -d, --date=DATE  Date range for stories: all, last24h, pastWeek, pastMonth, pastYear. Defaults to all
    -s, --sort=SORT  Sort stories: byDate, byPopularity. Defaults to byPopularity
