import psycopg2



## ok so far things are going great, I was able to get speaker data uploaded to the pdf and 
## now pretty much everything that the PDF example used is ready to go, besides the contact 
# information. Now I am working on 2 things
#1. getting pictures to work with posgres
#2. Making sure contact information works
#3. Testing out doc templates
#4. testing out template creation for other PDFs or Docs

#now figure this out and the stack overflow page # https://stackoverflow.com/questions/22288898/insert-an-image-in-postgresql-database

conn = psycopg2.connect(
    dbname="poc", user="postgres", password="xFl201X20FabSN2024Nov", host="localhost", port="5432"
)
cursor = conn.cursor()


with open("/Users/ericdahlberg/Desktop/superniche/picture/image2.png", "rb") as file:
    binary_data = file.read()
    
# use this #
# sql = "INSERT INTO event (event_logo) VALUES (%s) "
sql = "UPDATE event SET event_logo = %s WHERE id = %s"
print(binary_data)
cursor.execute(sql, (psycopg2.Binary(binary_data), 1))

# Fetch image data
cursor.execute("SELECT event_logo FROM event WHERE id = 2")
image_data = cursor.fetchone()[0]

# Save the image to a file
with open("output_image.png", "wb") as file:
    file.write(image_data)

conn.commit()
cursor.close()
conn.close()




#ex: '/Users/ericdahlberg/desktop/supernich/picture/download.png'
# def get_binary_array(path):
#     with open(path, "rb") as image:
#         f = image.read()
#         b = bytes(f).hex()
#         return b

# def send_files_to_postgresql(cursor, file_names):
#     query = "INSERT INTO event(event_logo) VALUES (decode(%s, 'hex'))"
#     mylist = []
#     for file_name in file_names:
#         mylist.append(get_binary_array(file_name))

#     try:
#         cursor.executemany(query, mylist)
       
#         connection.commit()  # commit the changes to the database is advised for big files, see documentation
#         count = cursor.rowcount # check that the images were all successfully added
#         print (count, "Records inserted successfully into table")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

# def get_connection_cursor_tuple():
#     connection = None
#     try:
#         params = config()
#         print('Connecting to the PostgreSQL database...')
#         connection = psycopg2.connect(**params)
#         cursor = connection.cursor()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

#     return connection, cursor



# conn = psycopg2.connect(
#     dbname="poc", user="postgres", password="xFl201X20FabSN2024Nov", host="localhost", port="5432"
# )
# cursor = conn.cursor()


# connection, cursor = conn.get_connection_cursor_tuple()
# img_names = ['.picture/image1.png', '.picture/image2.jpg']
# send_files_to_postgresql(connection, cursor, img_names)

# print(get_binary_array(img_names[0],img_names[1]))

# cursor.close()
# conn.close()