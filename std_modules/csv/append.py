import csv
csvfile = open('eggs.csv', 'a')
spamwriter = csv.writer(csvfile, delimiter=':',
                        escapechar='\\')
spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])