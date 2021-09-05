# Dictionaries and lists, together

# Loading from https://raw.githubusercontent.com/shannonturner/education-compliance-reports/master/investigations.json

investigations = {
  "type": "FeatureCollection",
  "features": [

  {
   "type": "Feature",
   "geometry": {
      "type": "Point",
      "coordinates": [
     -112.073032,
     33.453527
        ]
    },
    "properties": {
      "marker-symbol": "marker",
      "marker-color": "#D4500F",
      "address": " AZ ",
      "name": "Arizona State University"
      }
  },

  {
   "type": "Feature",
   "geometry": {
      "type": "Point",
      "coordinates": [
     -121.645734,
     39.648248
        ]
    },
    "properties": {
      "marker-symbol": "marker",
      "marker-color": "#D4500F",
      "address": " CA ",
      "name": "Butte-Glen Community College District"
      }
  },
  ]
}

# The first level is a dictionary with two keys: type and features
# type's value is a string: FeatureCollection
# features' value is a list of dictionaries

# We're going to focus on the features list.

# Each item in the features list is a dictionary that has three keys: type, geometry, and properties

# If we wanted to access all of the properties for the first map point, here's how:
print investigations['features'][0]['properties']
#   list of dictionaries ^       ^        ^
#                first map point |        | properties

# {
#   "marker-symbol": "marker",
#   "marker-color": "#D4500F",
#   "address": " AZ ",
#   "name": "Arizona State University"
# }

# As we see above, properties is itself a dictionary

# To get the name of that map point:
print investigations['features'][0]['properties']['name']

# Arizona State University

# Generally speaking, if what's between the square brackets is a number, you're accessing a list.
# If it's a string, you're accessing a dictionary.
# If you get stuck or are getting errors, try printing out the item and the key or index.