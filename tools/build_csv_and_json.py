2###############################################################################

# Load images or products in /media folder and run this program to generate the
# products database

# IMPORTED RESOURCES #

# EXTERNAL:
import os
import glob
import random


# INTERNAL:

###############################################################################


# Initialize counters for later print of QC messages
total_files = 0
file_paths_found = 0
file_names_found = 0
dem_files_found = 0
gravimetry_files_found = 0
resistivity_files_found = 0
magnetometry_files_found = 0
report_files_found = 0

model = 'products.product'


# First count total files to know which is last when writing the JSON file
for file in glob.glob("media/*.png"):
    total_files += 1


# Randomly generate the indexes to select 20 products that
# will be considered as "Last Arrivals"
is_last_arrival = []
is_last_arrival_index = 0
last_arrivals_items = 20
is_last_arrival = random.sample(range(total_files), last_arrivals_items)
is_last_arrival.sort()


# Open and write files in Python, continues below in ****
# https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python
# Accessed on March 2nd, 2022, at 00:57
# Create/Open CSV file
csv_file = open('tools/products.csv', 'w')
# Create/Open JSON file
json_file = open('products/fixtures/products.json', 'w')
json_file.write('[')


# Write first line (header)
csv_file.write('pk,model,category,sku,name,description,price,rating,' +
               'image_url,image_name\n')

# Read file path
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# Accessed on March 1st, 2022, at 23_35
for file in glob.glob("media/*.png"):
    png_file_path = file
    file_paths_found += 1

# Read file name
# https://stackoverflow.com/questions/7336096/python-glob-without-the-whole-path-only-the-filename
# Accessed on March 1st, 2022, at 23:45
    name = os.path.basename(file)
    png_file_name = name
    file_names_found += 1

    # If first character in file name is "d", then it is an image
    # for digital elevation model (DEM)
    if name[0] == 'd':
        # Category
        category = 'DEM'
        # Assign fk, check first if it should be a last arrival product
        if ((file_paths_found == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items - 1)):
            fk = 5
            is_last_arrival_index += 1
        else:
            fk = 1
        # Country
        country = name[28:-4]
        name_title = country + ' ' + category
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        year = str(random.randint(1970, 2022))
        sku = (year + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = ('This file contains ' + category.upper() +
                       ' data for ' + country)
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        dem_files_found += 1

    # If first character in file name is "g", then it is an image
    # for gravimetry
    if name[0] == 'g':
        # Category
        category = 'Gravimetry'
        # Assign fk, check first if it should be a last arrival product
        if ((file_paths_found == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items - 1)):
            fk = 5
            is_last_arrival_index += 1
        else:
            fk = 2
        # Country
        country = name[15:-4]
        name_title = country + ' ' + category
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        year = str(random.randint(1970, 2022))
        sku = (year + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = ('This file contains ' + category.lower() +
                       ' data for ' + country)
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        gravimetry_files_found += 1

    # If first character are file name is "res", then it is an image
    # for resitivity
    if name[0:3] == 'res':
        # Category
        category = 'Resistivity'
        # Assign fk, check first if it should be a last arrival product
        if ((file_paths_found == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items - 1)):
            fk = 5
            is_last_arrival_index += 1
        else:
            fk = 3
        # Country
        country = name[16:-4]
        name_title = country + ' ' + category
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        year = str(random.randint(1970, 2022))
        sku = (year + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = ('This file contains ' + category.lower() +
                       ' data for ' + country)
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        resistivity_files_found += 1

    # If first character in file name is "m", then it is an image
    # for magnetometry
    if name[0] == 'm':
        # Category
        category = 'Magnetometry'
        # Assign fk, check first if it should be a last arrival product
        if ((file_paths_found == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items - 1)):
            fk = 5
            is_last_arrival_index += 1
        else:
            fk = 4
        # Country
        country = name[17:-4]
        name_title = country + ' ' + category
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        year = str(random.randint(1970, 2022))
        sku = (year + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = ('This file contains ' + category.lower() +
                       ' data for ' + country)
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        magnetometry_files_found += 1


    # If first characters in file name are "rep", then it is an image
    # for a report
    if name[0:3] == 'rep':
        # Category, assigned later, based on fk
        # Assign fk, check first if it should be a last arrival product
        if ((file_paths_found == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items)):
            fk = 14
            is_last_arrival_index += 1
        else:
            # Randomly assigned a category for the type of report
            fk = random.randint(6, 8)
        if fk == 6:
            category = 'Environmental Impact Assessment'
        elif fk == 7:
            category = 'Weather Data'
        else:
            category = 'Geological Map'
        # Country
        country = name[11:-4]
        name_title = country + ' ' + category
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        year = str(random.randint(1970, 2022))
        sku = (year + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = ('This file contains a ' + category.lower() +
                       ' for ' + country)
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        report_files_found += 1


    # ****
    # Write several variables to file
    # https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file
    # Accessed on March 2nd, 2022, at 01:03
    # (Blank space, 6th element, is for rating)
    rating = ' '
    csv_file.write('%i,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
                   % (file_names_found,
                      model,
                      fk,
                      sku,
                      country,
                      description,
                      price,
                      rating,
                      png_file_path,
                      png_file_name)
                   )

    ## Last record, no comma
    #if file_paths_found == total_files:
    #    json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}}'
    #                    % (file_paths_found, model, sku, name_title,
    #                       description, price, fk,
    #                       png_file_path, png_file_name))
    # Include comma for all other records
    #else:
    json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}},'
                        % (file_paths_found, model, sku, name_title,
                           description, price, fk,
                           png_file_path, png_file_name))


# Add 10 books to products
total_books = 10
is_last_arrival = []
is_last_arrival_index = 0
last_arrivals_items = 3
for i in range(1, total_books):
    is_last_arrival.append(random.randint(file_paths_found + 1,
                                          file_paths_found + total_books + 1))

for i in range(file_paths_found + 1, file_paths_found + total_books + 1):
    serial_number = '000' + str(i)
    year = str(random.randint(1970, 2022))
    sku = (year + 'BKS' + serial_number[-4:] +
               country[0:3]).upper()
    name_title = 'Book Name'
    description = 'This book contains '
    price = format(random.uniform(20, 60), '.2f')
    if ((i == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items)):
            fk = 15
            is_last_arrival_index += 1
    else:
        fk = 9

    png_file_path = 'media/'
    png_file_name = 'file_name'

    json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}},'
                        % (i, model, sku, name_title,
                           description, price, fk,
                           png_file_path, png_file_name))

    country = 'N/A'
    rating = ' '
    csv_file.write('%i,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
                   % (i,
                      model,
                      fk,
                      sku,
                      country,
                      description,
                      price,
                      rating,
                      png_file_path,
                      png_file_name)
                   )



# Add 10 courses to products
total_courses = 10
is_last_arrival = []
is_last_arrival_index = 0
last_arrivals_items = 3
for i in range(1, last_arrivals_items):
    is_last_arrival.append(random.randint(file_paths_found + total_books + 1, 
                                          file_paths_found + total_books + 
                                          total_courses + 1))
for i in range(file_paths_found + total_books + 1, file_paths_found
               + total_books + total_courses + 1):
    serial_number = '000' + str(i)
    year = str(random.randint(1970, 2022))
    sku = (year + 'COU' + serial_number[-4:] +
               country[0:3]).upper()
    name_title = 'Course Name'
    description = 'This course is designated to train '
    price = format(random.uniform(100, 200), '.2f')
    if ((i == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items)):
            fk = 15
            is_last_arrival_index += 1
    else:
        fk = 10
    png_file_path = 'media/'
    png_file_name = 'file_name'

    json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}},'
                        % (i, model, sku, name_title,
                           description, price, fk,
                           png_file_path, png_file_name))

    country = 'N/A'
    rating = ' '
    csv_file.write('%i,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
                   % (i,
                      model,
                      fk,
                      sku,
                      country,
                      description,
                      price,
                      rating,
                      png_file_path,
                      png_file_name)
                   )


# Add 15 software to products
total_software = 15
is_last_arrival = []
is_last_arrival_index = 0
last_arrivals_items = 4
for i in range(1, last_arrivals_items):
    is_last_arrival.append(random.randint(file_paths_found + total_books +
                                          total_courses + 1, 
                                          file_paths_found + total_books + 
                                          total_courses + total_software + 1))
for i in range(file_paths_found + total_books + total_courses + 1, 
               file_paths_found + total_books + total_courses +
               total_software + 1):
    serial_number = '000' + str(i)
    year = str(random.randint(1970, 2022))
    sku = (year + 'COU' + serial_number[-4:] +
               country[0:3]).upper()
    name_title = 'Software Name'
    description = 'This software package is a fundamental tool for '
    price = format(random.uniform(500, 800), '.2f')
    if ((i == is_last_arrival[is_last_arrival_index]) and
                (is_last_arrival_index < last_arrivals_items)):
            fk = 16
            is_last_arrival_index += 1
    else:
        fk = random.randint(11, 13)
    png_file_path = 'media/'
    png_file_name = 'file_name'


    # No "comma" in last record
    if i == file_paths_found + total_books + total_courses + total_software:
        json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}}'
                        % (i, model, sku, name_title,
                           description, price, fk,
                           png_file_path, png_file_name))
    
    #Include comma for all other records, as before
    else:
        json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}},'
                        % (i, model, sku, name_title,
                           description, price, fk,
                           png_file_path, png_file_name))

    country = 'N/A'
    rating = ' '
    csv_file.write('%i,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
                   % (i,
                      model,
                      fk,
                      sku,
                      country,
                      description,
                      price,
                      rating,
                      png_file_path,
                      png_file_name)
                   )








# Close the CSV file
csv_file.close()

# Write last character of JSON file and close the file
json_file.write(']')
json_file.close()


# Print amount of files for QC
print()
print("Files paths found: " + str(file_paths_found))
print("Files names found: " + str(file_names_found))
print()
print("DEM images found: " + str(dem_files_found))
print("Gravimetry images found: " + str(gravimetry_files_found))
print("Resistivity images found: " + str(resistivity_files_found))
print("Magnetometry images found: " + str(magnetometry_files_found))
print("Report images found: " + str(report_files_found))
print()


# Values for the category model
cats_model = '"products.category"'
cats = ['dem', 'gravimetry', 'resistivity', 'magnetometry', 'data_offers',
        'eia', 'weather', 'geological_maps', 'books', 'courses',
        'simulators', 'data_processing', 'data_qc', 'report_offers',
        'training_offers', 'software_offers']
cats_friendly = ['DEM', 'Gravimetry', 'Resistivity', 'Magnetometry',
                 'Data Offers', 'EIA', 'Weather', 'Geological Maps',
                 'Books', 'Courses', 'Simulators', 'Data Processing',
                 'Data QC', 'Report Offers', 'Training Offers',
                 'Software Offers']


# Create/Open file and write categories of products in a CSV file
csv_file = csv_file = open('tools/categories.csv', 'w')
# Write first line (header)
csv_file.write('pk,model,category_name,friendly_name\n')
for i in range(0, len(cats)):
    csv_file.write('%i,%s,%s,%s\n'
                   % (i+1,
                      cats_model,
                      cats[i],
                      cats_friendly[i])
                   )
# Close the file
csv_file.close()


# Create/Open file and write five categories of products in a JSON file
json_file = open('products/fixtures/categories.json', 'w')
json_file.write('[')
for i in range(0, len(cats)):
    # If last record, do not include comma
    if i == len(cats)-1:
        json_file.write('{"pk":%s,"model":%s,"fields":{"name":"%s","friendly_name":"%s"}}'
                        % (i+1, cats_model, cats[i], cats_friendly[i]))
    # Include comma for all other records
    else:
        json_file.write('{"pk":%s,"model":%s,"fields":{"name":"%s","friendly_name":"%s"}},'
                        % (i+1, cats_model, cats[i], cats_friendly[i]))
# Write last character of JSON format
json_file.write(']')
# Close the file
json_file.close()
