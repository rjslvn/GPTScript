yt-ui-ellipsis-2">(.*?)</div>', html)

# Write the data to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Description'])
    for title, description in zip(titles, descriptions):
        writer.writerow([title, description])