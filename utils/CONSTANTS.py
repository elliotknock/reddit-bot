# Supported Background. Can add/remove background video here....
# <key>-<value> : key -> used as keyword for TOML file. value -> background configuration
# Format (value):
# 1. Youtube URI
# 2. filename
# 3. Citation (owner of the video)
# 4. Position of image clips in the background.

background_options = {
    "subway-surfers": ( #Subway Surfers
        "https://youtu.be/hs7Z0JUgDeA",
        "subway-parkour.mp4",
        "foolish gamer",
        lambda t: ("center", 480 + t),
    )
}