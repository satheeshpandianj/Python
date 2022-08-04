# bids = {
#     34: "Raja",
#     "Sats": 45,
# }

# print(bids[34])

# travel_log = {
#     "cities": ["PVP","SVL","BLR"],
#     "Countries": ["India", "UK","USA"],
# }

# print(travel_log["cities"][1])

travel_log = {
    "cities": {
        "PVP":19,
        "SVL": 20,
        "BLR":5,
    },
    "Countries": {
        "India":1982, 
        "UK": 2019,
        "USA": 2011,
    },
}

print(travel_log["cities"]["SVL"])