# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    deliveries = data["innings"][0]["1st innings"]["deliveries"]

    for delivery in deliveries:
        for delivery_num, delivery_info in delivery.items():
            if delivery_info["batsman"] == "RT Ponting":
                count = count + 1

    print count

    return count
