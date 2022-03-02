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
file_to_write = open('tools/products.csv', 'w')


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
    file_to_write.write('%s, %s, %s, %s, %s, ' ', %s, %s\n' % (category,
                                                               sku,
                                                               name,
                                                               description,
                                                               price,
                                                               png_file_path,
                                                               png_file_name)
                        )


# Close file
file_to_write.close()


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
