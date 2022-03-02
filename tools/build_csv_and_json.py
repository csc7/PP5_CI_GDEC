###############################################################################

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
file_paths_found = 0
file_names_found = 0
dem_files_found = 0
gravimetry_files_found = 0
resistivity_files_found = 0
magnetometry_files_found = 0


# Open and write files in Python, continues below in ****
# https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python
# Accessed on March 2nd, 2022, at 00:57
csv_file = open('tools/products.csv', 'w')

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

    # If first character in file name is "r", then it is an image
    # for digital elevation model (DEM)
    if name[0] == 'd':
        # Category
        category = 'DEM'
        fk = 1
        # Country
        country = name[28:-4]
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        sku = ('2022' + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = 'This file contains ' + category + ' data for ' + country
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        dem_files_found += 1

    # If first character in file name is "r", then it is an image
    # for gravimetry
    if name[0] == 'g':
        # Category
        category = 'Gravimetry'
        fk = 2
        # Country
        country = name[15:-4]
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        sku = ('2022' + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = 'This file contains ' + category + ' data for ' + country
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        gravimetry_files_found += 1

    # If first character in file name is "r", then it is an image
    # for resitivity
    if name[0] == 'r':
        # Category
        category = 'Resistivity'
        fk = 3
        # Country
        country = name[16:-4]
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        sku = ('2022' + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = 'This file contains ' + category + ' data for ' + country
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        resistivity_files_found += 1

    # If first character in file name is "r", then it is an image
    # for magnetometry
    if name[0] == 'm':
        # Category
        category = 'Magnetometry'
        fk = 4
        # Country
        country = name[17:-4]
        # Generate SKU
        serial_number = '000' + str(file_names_found)
        sku = ('2022' + category[0:3] + serial_number[-4:] +
               country[0:3]).upper()
        # Generate Description
        description = 'This file contains ' + category + ' data for ' + country
        # Price
        # Random numbers from
        # https://www.w3schools.com/python/ref_random_uniform.asp, accessed
        # on March 2nd, 2022, at 01:42.
        price = format(random.uniform(10, 110), '.2f')
        # Count files in this category
        magnetometry_files_found += 1

    # ****
    # Write several variables to file
    # https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file
    # Accessed on March 2nd, 2022, at 01:03
    # (Blank space, 6th element, is for rating)
    model = 'products.product'
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

# Close the file
csv_file.close()


# Print amount of files for QC
print()
print("Files paths found: " + str(file_paths_found))
print("Files names found: " + str(file_names_found))
print()
print("DEM images found: " + str(dem_files_found))
print("Gravimetry images found: " + str(gravimetry_files_found))
print("Resistivity images found: " + str(resistivity_files_found))
print("Magnetometry images found: " + str(magnetometry_files_found))
print()


# Open JSON file and write according to its structure
json_file = open('tools/products.json', 'w')
json_file.write('[')
for i in range(1, file_paths_found+1):
    # If last record, do not include comma
    if i == file_paths_found:
        json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}}'
                        % (i, model, sku, name, description, price, fk,
                           png_file_path, png_file_name))
    # Include comma for all other records
    else:
        json_file.write('{"pk":%s,"model":"%s","fields":{"sku":"%s","name":"%s","description":"%s","price":%s,"category":%s,"rating":5,"image_url":"%s","image_name":"%s"}},'
                        % (i, model, sku, name, description, price, fk,
                           png_file_path, png_file_name))
# Write last character of JSON format
json_file.write(']')
# Close the file
json_file.close()


# Values for the category model
cats_model = '"products.category"'
cats = ['dem', 'gravimetry', 'resistivity', 'magnetometry', 'last_arrivals']
cats_friendly = ['DEM', 'Gravimetry', 'Resistivity', 'Magnetometry',
                 'Last Arrivals']


# Write five categories of products in a CSV file
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

# Write five categories of products in a JSON file
json_file = open('tools/categories.json', 'w')
json_file.write('[')
for i in range(1, len(cats)):
    # If last record, do not include comma
    if i == len(cats)-1:
        json_file.write('{"pk":%s,"model":%s,"fields":{"name":"%s","friendly_name":"%s"}}'
                        % (i, cats_model, cats[i], cats_friendly[i]))
    # Include comma for all other records
    else:
        json_file.write('{"pk":%s,"model":%s,"fields":{"name":"%s","friendly_name":"%s"}},'
                        % (i, cats_model, cats[i], cats_friendly[i]))
# Write last character of JSON format
json_file.write(']')
# Close the file
json_file.close()
