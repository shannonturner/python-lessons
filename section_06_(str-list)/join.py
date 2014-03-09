states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "PALAU", "Pennsylvania", "PUERTO RICO", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# .join() is a string method (a function that works only on strings) that glues together a list back into a string.

# .join() has two main parts to it: the glue and the list

# The glue is the string that you'd like to glue in between each piece of the list as you're putting it back together as a string.
# The glue is the string that goes just before the dot.

# The list is the list you'd like to glue back together.

# So if we ran the following command:
print "glue".join(states)

# We'd get:
#AlabamaglueAlaskaglueArizonaglueArkansasglueCaliforniaglueColoradoglueConnecticutglueDelawareglueDistrict Of ColumbiaglueFloridaglueGeorgiaglueHawaiiglueIdahoglueIllinoisglueIndianaglueIowaglueKansasglueKentuckyglueLouisianaglueMaineglueMarylandglueMassachusettsglueMichiganglueMinnesotaglueMississippiglueMissouriglueMontanaglueNebraskaglueNevadaglueNew HampshireglueNew JerseyglueNew MexicoglueNew YorkglueNorth CarolinaglueNorth DakotaglueOhioglueOklahomaglueOregongluePALAUgluePennsylvaniagluePUERTO RICOglueRhode IslandglueSouth CarolinaglueSouth DakotaglueTennesseeglueTexasglueUtahglueVermontglueVirginiaglueWashingtonglueWest VirginiaglueWisconsinglueWyoming

# Funny (and helpful for remembering), but that doesn't look very good.

# Instead, let's use a useful piece of glue.  Let's glue it back together with a newline between each state.
print "\n".join(states)

# Now we get:
# Alabama
# Alaska
# Arizona
# Arkansas
# California
# Colorado
# Connecticut
# Delaware
# District Of Columbia
# Florida
# Georgia
# Hawaii
# Idaho
# Illinois
# Indiana
# Iowa
# Kansas
# Kentucky
# Louisiana
# Maine
# Maryland
# Massachusetts
# Michigan
# Minnesota
# Mississippi
# Missouri
# Montana
# Nebraska
# Nevada
# New Hampshire
# New Jersey
# New Mexico
# New York
# North Carolina
# North Dakota
# Ohio
# Oklahoma
# Oregon
# PALAU
# Pennsylvania
# PUERTO RICO
# Rhode Island
# South Carolina
# South Dakota
# Tennessee
# Texas
# Utah
# Vermont
# Virginia
# Washington
# West Virginia
# Wisconsin
# Wyoming