# Resource_Allocator_Assignment
A minimal resource allocation program. The following program for each geolocation and the resources available in the particular geolocation based on the input number of units and hours generates a json containing the optimal combination of machines that serves the user requirements along with the cost.

## Usage
The following command to run the program

```
python3 main.py --units 1150 --hours 1
```

Output generated

```
{
    "Output": [
        {
            "region": "NY",
            "total_cost": 10150,
            "machines": {
                "8XLarge": 7,
                "XLarge": 1,
                "Large": 1
            }
        },
        {
            "region": "IND",
            "total_cost": 9520,
            "machines": {
                "8XLarge": 7,
                "Large": 3
            }
        },
        {
            "region": "CHN",
            "total_cost": 8570,
            "machines": {
                "8XLarge": 7,
                "XLarge": 1,
                "Large": 1
            }
        }
    ]
}
```
Tests are present in test directory and can be run against the methods using
```
python3 test_*.py
```
