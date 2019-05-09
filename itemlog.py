#!usr/bin/python
import psycopg2

query_ThreePopularArticles = '''select articles.title, count(log.id) as total
    from articles
    left join log on
    log.path = ('/article/' || articles.slug)
    group by articles.title
    order by total desc
    limit 3'''

query_MostPopularAuthors = ''' select authors.name, count(log.id)
    from authors
    left join articles on
    articles.author = authors.id
    left join log on log.path = ('/article/' || articles.slug)
    group by authors.name
    order by count desc'''

query_RequestLeadingToErrors = '''select date, percent from err_rate
    where percent > 1;
    '''


def get_result(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    row_count = len((result))
    i = 0
    while i < row_count:
        print result[i][0], '\t', result[i][1]
        i = i+1


print("3 most popular articles are:")
get_result(query_ThreePopularArticles)

print("\nMost popular authors are:")
get_result(query_MostPopularAuthors)

print("\nThe days that which more than 1% of requests led to errors:")
get_result(query_RequestLeadingToErrors)
